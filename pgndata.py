import pandas as pd
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
    return pd.DataFrame.from_records(columns=('Move','W_castle','W_Piece','W_Origin_R_F','W_Takes','W_File','W_Takes1','W_Rank','W_PTake','W_PDestination','W_PPiece','B_castle','B_Piece','B_Origin_R_F','B_Takes','B_File','B_Takes1','B_Rank','B_PTake','B_PDestination','B_PPiece'), data=[m.groupdict() for m in mover.finditer(pgndata)], index="Move")
        
movedata="""
1. e4 e5 2. Nc3 Nf6 3. Nge2 d5 4. f4 exf4 5. Nxf4 dxe4 6. d3 exd3 7. Bxd3 Bd6 8.
Bb5+ c6 9. Ba4 O-O 10. O-O Bg4 11. Nce2 Bxf4 12. Bxf4 Qxd1 13. Raxd1 Bxe2 14.
Bd6 Rd8 15. Rd3 Bxd3 16. cxd3 Rxd6 17. Bd1 Rxd3 18. h3 Nbd7 19. b4 Rd2 20. a4
Rb2 21. Rf4 Rb1 22. Rd4 Re8 23. Kf1 Re4 24. Rxe4 Nxe4 25. a5 Rxd1+ 26. Ke2 Rb1
27. Ke3 Rxb4 28. g4 Nec5 29. Kf3 b6 30. h4 Ne5+ 31. Kg3 Rxg4+ 32. Kh3 Nb3 33. h5
Nxa5 34. h6 g6 35. Kh2 c5 36. Kh3 c4 37. Kh2 c3 38. Kh3 c2 39. Kh2 c1=Q 40. Kh3
Qh1# 0-1
"""
print(parsemoves(movedata))