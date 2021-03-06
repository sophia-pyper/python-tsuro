The board will be initialized with 36 spaces, each with eight ticks (two on each side):

	    0  1
	  ________
	7 |       | 2
	  |       |
	6 |_______| 3
	    5  4

 Each tick will contain a tuple (x,y), where x is 1 if the tick falls on an edge and 0 otherwise, and y is the number of the tick within the space that the current tick connects to, and "X" if there is no connection, and "P" if it is an edge space containing a player during player placement. 
 Thus, the format of the board matrix is [row][column][tick_number][tuple_choice]

A player moving to a new tick will first check if the tick is an edge. If it is, the player is eliminated. If it is not an edge, the player will check the adjacent tick (i.e. tick 3 of one tile is adjacent to tick 6 of the tile on its right). If the adjacent tick is connected to a path, it will follow that path to its connected tick and repeat the edge check/path check. If the adjacent tick is not connected to a path, it will store the coordinates of the adjacent space for tile placement next round (if it's moved by another player's turn, these coordinates will have to be updated). 

During a given turn, the server will keep track of every tick each player visits. If two players visited the same tick within a turn, a collision has occurred and both are removed from the game. 

The tick checks/collision checks will be run on every rotation of every tile of the player's hand before their turn. Any tile/rotation choice that results in the player's elimination will be added to a list on the server, and the server will not permit the player to select that move. If all moves result in edge or player collisions, the player can do whatever they want (ultimately maybe we can force them to make the move which doesn't suicide-murder another player).

Possible future implementation: when running all of the tile rotation checks, store the outcomes of the turn (who dies, where the players end up) and just use that rather than resimulating the movement