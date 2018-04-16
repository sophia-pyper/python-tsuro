from tilelist import tilelist
from Board import Board

class Server:

	 def __init__(self, numPlayers = 2):
	 	#dummy code for now. we'll figure out player choice later
	 	player1 = SPlayer("blue", 28, 0, 0, 0)
	 	player2 = SPlayer("red", 14, 2, 0, 1)
	 	self.playersIn = [player1, player2]
	 	self.tileList = tilelist
	 	self.playersOut = []
	 	self.board = Board()
	 	self.ticksVisited = []

	 #Runs through the game
	 def playGame():

	 	gameBoard = Board()

	 	if (playersIn.length == 1):
	 		return "Player ",playersIn[0]," has won!"
	
		while True: #while tile choice is invalid, keep getting different choice
 		newTile = player.getTileChoice() #need to implement
 		
 		#if play is legal, commence turn
 		if (is_play_legal(newTile, player)):
 			gameBoard.addTileToBoard(newTile, player.location[0], player.location[1])
 			#remove tile from hand function
 			
 			#Move all tiles and check for collisions
 			for pl in playersIn:
 				movePlayer(pl)
 			collisionCheck()
 			
 			break

		#Find out who died and remove them from the game
		deadIndex = []
		for i in range(len(playersIn)):
			if (playersIn[i].dead):
				playersOut.append(playersIn[i])
				deadIndex.append(i)
		for j in deadIndex:
			del playersIn[j]


	 #Returns true if player move is legal, false otherwise
	 def is_play_legal(tile, player, board):
	 	badMovesList = findIllegalMoves(player, board)
	 	if (tile.paths in badMovesList):
	 		return False
	 	else if (tile not in player.hand):
	 		return False
	 	else:
	 		return True



newServ = Server()

newServ.startGame()


