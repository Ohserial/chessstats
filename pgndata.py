import pandas as pd
import sys
import numpy as np

move_dtypes={'Move':int,
             'W_castle':int,
             'W_Piece':char,
             'W_Origin_R_F':char,
             'W_Takes':bool,
             'W_File':char,
             'W_Takes1':bool,
             'W_Rank':char{1-8},
             'W_PTake':bool,
             'W_PDestination':char,
             'W_PPiece':char,
             'B_castle':int,
             'B_Piece':char,
             'B_Origin_R_F':char,
             'B_Takes':bool,
             'B_File':char{a-h},
             'B_Takes1':bool,
             'B_Rank':char,
             'B_PTake':bool,
             'B_PDestination':char,
             'B_PPiece':char}

"""
Notation:
   <number>. [Piece (default pawn)][<file>][<rank>][action {x=take}] <file><rank>[{+=check,#=mate}][evaluation tag {!,!!,!?,?!,???}] Skip to <integer>

   * initial file and rank are each optional as disambiguation. ie, in the case of pawns always because a pawn can be in any square
     exd5 because a pawn can only take form a specific rank, so the rank is not specified.
   """

import re

move_expr='\s*(?P<Move>\d{1,3})'
white_expr='\.?\s*(((?P<W_castle>O-O(:?-O)?)|(?P<W_Piece>[KQNBR](?P<W_Origin_R_F>[1-8a-h]?)(?P<W_Takes>x?)(?P<W_File>[a-h])(?P<W_Takes1>x?)(?P<W_Rank>[1-8]))|((?P<W_PTake>[a-h]x?)(?P<W_PDestination>[a-h]?[1-8]\=?)(?P<W_PPiece>[QRNB]?)))\+?)'
black_expr='\.?\s*(((?P<B_castle>O-O(:?-O)?)|(?P<B_Piece>[KQNBR](?P<B_Origin_R_F>[1-8a-h]?)(?P<B_Takes>x?)(?P<B_File>[a-h])(?P<B_Takes1>x?)(?P<B_Rank>[1-8]))|((?P<B_PTake>[a-h]x?)(?P<B_PDestination>[a-h]?[1-8]\=?)(?P<B_PPiece>[QRNB]?)))\+?)'
# black_expr='(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?'

def parsemoves(pgndata):
    mover=re.compile(move_expr + white_expr + black_expr)
    data = mover.finditer(pgndata)
    tf=pd.DataFrame.from_records(columns=('Move','W_castle','W_Piece','W_Origin_R_F','W_Takes','W_File','W_Takes1','W_Rank','W_PTake','W_PDestination','W_PPiece','B_castle','B_Piece','B_Origin_R_F','B_Takes','B_File','B_Takes1','B_Rank','B_PTake','B_PDestination','B_PPiece'), data=[m.groupdict() for m in mover.finditer(pgndata)], index="Move")
    print(tf)
    return(tf)

def parsepgn(gamedata):
    tag_expr='\[(?P<name>[^\s]+)\s+(?P<value>[^\]]+)\]'
    tagger=re.compile(tag_expr)
    retval=dict()
    for line in gamedata:
        mo=tagger.match(line)
        if mo:
            d=mo.groupdict()
            retval[d.get('name')]=d.get('value')
        else:
            break
    retval['moves']=parsemoves(gamedata.read())
    return retval

df=pd.DataFrame.from_records(index=sys.argv[1:],
                             data=[parsepgn(open(fname)) for fname in sys.argv[1:]])
print(df.shape)