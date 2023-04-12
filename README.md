I want to analyze the master game database to exctract features of particular chess openings
My goal is to extract features about individual pieces to understand which pieces are most active in which types of games. games could be classified by length, complexity, score, etc.
Games are recorded in PGN (Portable Game Notation) a plaintext file format. (more at https://en.wikipedia.org/wiki/Portable_Game_Notation).
Simple features of a game for classification:
* ECO
* Game outcome
* Length(moves)
* Score at end
* Piece count (Black/White)

## links

* https://cornerstone.lib.mnsu.edu/etds/1119/
* https://chess.stackexchange.com/questions/30124/is-there-a-standard-system-of-classification-of-games#:~:text=a%20whole%20chess%20game%20is%20quite%20long.%20Some%20parts%20of%20it%20can%20be%20categorized%2C%20others%20defy%20such%20attempts%20completely.%20So%20in%20chess%20it%20is%20positions%20that%20can%20sometimes%20be%20classified%2C%20not%20entire%20games.

## KPI (Key Per formance Indicator)

* 

## Visualization

histogram:
x-axis: move # or game % complete
y-axis: popularity
z-axis: move outcome (game outcome, affect on score)


## Implementation

Read in a set of game data add any tags then parse the moves into a vector whcih can be serialized as a table of  