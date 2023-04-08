"""
Notation:
   <number>. [Piece (default pawn)][<file>][<rank>][action {x=take}] <file><rank>[{+=check,#=mate}][evaluation tag {!,!!,!?,?!,???}] Skip to <integer>

   * initial file and rank are each optional as disambiguation. ie, in the case of pawns always because a pawn can be in any square
     exd5 because a pawn can only take form a specific rank, so the rank is not specified.
   """

import re

def parse_moves( pgnblock="" ):
    """
    reads in the pgn data and generates a list of Move objects
    """
delim=re.compile(' \d\.')
move_expr='\s*(\d{1,3})\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?'
move_expr='\s*(\d{1,3})'
white_expr='\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)'
black_expr='(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?'

def parsemoves(pgndata):
    mover=re.compile(move_expr + white_expr + black_expr)
    for i, move in enumerate( mover.findall( pgndata )):
        if i+1 != int(move[0]):
            raise Exception( f"Move({i}) not equal to {move[0]} - Out of order!!!" )
        
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