from tilelist import tilelist
from Board import Board
import random

class Server:

	def __init__(self):
		self.hasDragonTile = False

	 #Runs through the game
	def playGame(self):

		playersOut = []
		drawPile = tilelist
		board = Board()
	 	#Dummy players for now- will have a function for this later
	 	player1 = sPlayer("blue", 28)
	 	player2 = sPlayer("red", 14)
	 	playersIn = [player1, player2]

	 	board.placePlayer(playersIn[0], 0, 0, 0)
	 	board.placePlayer(playersIn[1], 0, 2, 0)

		while True: #while tile choice is invalid, keep getting different choice
			player = playersIn[0]
			newTile = player.getTileChoice() 
			if (is_play_legal(newTile, player, board)):
				player.removeTile(tile)
				turn = play_a_turn(drawPile, playersIn, playersOut, board, newTile)
				playersIn = turn[1]
				#If turn returns true, it's over
				if (turn[4]):
					break
				else:
					drawPile = turn[0]
					playersOut = turn[2]
					gameBoard = turn[3]

			return "Player(s) "+playersIn+" have won!"


	 #Returns true if player move is legal, false otherwise
	 def is_play_legal(tile, player, board):

	 	okMovesList = board.findLegalMoves(player)
	 	if (tile.paths in okMovesList):
	 		return True
	 	else:
	 		return False

	 #Allows you to draw a tile. Returns tuple with chosen tile and updated list 
	 def drawTile(tilePile):
	 	index = random.randint(0, len(tilePile-1))
	 	tile = tilePile[index]
	 	tilePile.remove(tile)
	 	return [tile, tilePile]


	 def play_a_turn(self, tilePile, inList, outList, board, tile):
	 	player = inList[0]
	 	#place tile on board
	 	board.addTileToBoard(tile, player.location[0], player.location[1])
	 	#move first player to end
	 	inList = inList[1:]+inList[0]
	 	#move player and mark the dead ones
	 	out = board.moveAllPlayers(inList)
	 	#removes dead players from in list
	 	for j in out:
	 		if (j == self.hasDragonTile):
	 			self.hasDragonTile = False
	 		#Returns dead player's cards 
	 		for t in j.hand:
	 			tilePile.append(t)
	 		#Remove from inList and add to outList
	 		inList.remove(j)
	 		outList.append(j)
	 	#If everyone is out, add the last players who died back and kill the function
	 	if not inList:
	 		inList = out
	 		results = [tilePile, inList, outList, board, True]
	 		return results
	 	#If it's down to one player, they win
	 	elif (len(inList) == 1):
	 		results = [tilePile, inList, outList, board, True]
	 		return results

	 	#if there's tiles to give
	 	if (len(tilePile) > 0):
	 		#If someone has the dragon tile
	 		if (self.hasDragonTile):
	 			#Create a list ordered by who will get dealt to
	 			dealList = []
	 			for p in range(len(inList)):
	 				if (inList[p] == hasDragonTile):
	 					dealList = inList[p:] + inList[:p]
	 					self.hasDragonTile = False
	 					break
	 			#For each player in dealing order
	 			for d in dealList:
	 				#If player has fewer than 3 cards
	 				if (len(d.hand) < 3):
	 					#If there's cards left in the pile, give them one
	 					if (len(tilePile) > 0):
	 						newTile = drawTile(tilePile)
	 						d.addTileToHand(newTile[0])
	 						tilePile = newTile[1]
	 					#Otherwise, they get the dragon tile
	 					else:
	 						self.hasDragonTile = d
	 						break
	 				#If they have enough cards everyone else does too, so break
	 				else:
	 					break
	 		#If no one has the dragon tile and the player who just went is still in, they get to draw
		 	elif ((player == inList[-1]) and (len(player.hand) < 3)):
		 		getTile = drawTile(tilePile)
		 		player.addTileToHand(getTile[0])
		 		tilePile = getTile[1]

		 #If there's no tiles to give and no one has the dragon tile, give it to the current player
		 else:
		 	if not self.hasDragonTile:
		 		self.hasDragonTile = player

	 	#returns tuple with all the info
	 	results = [tilePile, inList, outList, board, False]
	 	return results