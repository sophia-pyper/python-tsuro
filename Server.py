from tilelist import tilelist
from Board import Board
import random

class Server:

	 #Runs through the game
	 def playGame():

	 	drawPile = tilelist
	 	playersOut = []
	 	gameBoard = Board()

	 	#Dummy players for now- will have a function for this later
	 	
	 	player1 = sPlayer("blue", 28)
	 	player2 = sPlayer("red", 14)
	 	playersIn = [player1, player2]


	 	placePlayer(player1, 0, 0, 0)
	 	placePlayer(player2, 0, 2, 0)

	 	# if (playersIn.length == 1):
	 	# 	return "Player ",playersIn[0]," has won!"
	
		while True: #while tile choice is invalid, keep getting different choice
 			newTile = player.getTileChoice() #need to implement
 			if (is_play_legal(newTile, player)):
 				turn = play_a_turn(drawPile, playersIn, playersOut, gameBoard, newTile)
 				playersIn = turn[1]
 				if (turn[4]):
 					break
 				else:
 					drawPile = turn[0]
 					playersOut = turn[2]
 					gameBoard = turn[3]

 		return "Player(s) "+playersIn+" have won!"


	 #Returns true if player move is legal, false otherwise
	 def is_play_legal(tile, player, board):

	 	badMovesList = board.findIllegalMoves(player)
	 	if (tile.paths in badMovesList):
	 		return False
	 	else if (tile not in player.hand):
	 		return False
	 	else:
	 		return True

	 #Allows you to draw a tile. Returns tuple with chosen tile and updated list 
	 def drawTile(tilePile):
	 	index = random.randint(0, len(tilePile-1))
	 	tile = tilePile[index]
	 	del tilePile[index]
	 	return [tile, tilePile]


	 def play_a_turn(tilePile, inList, outList, board, tile):
	 	player = inList[0]
	 	#place tile on board
	 	board.addTileToBoard(tile, player.location[0], player.location[1])
	 	#move first player to end
	 	inList = inList[1:]+inList[0]
	 	#move player and mark the dead ones
	 	for p in inList:
	 		board.movePlayer(p)
	 		if (p.dead):
	 			outList.append(p)

	 	#removes dead players from in list
	 	newInList = []
	 	for j in inList:
	 		if (j not in outList):
	 			newInList.append(j)
	 	if (len(newInList) > 0):
	 		inList = newInList

	 	#adds tile to hand of player that just went if they're still alive and there's tiles to give 
	 	if ((player == inList[-1]) and (len(player.hand) < 3) and (len(tilePile) > 0)):
	 		getTile = drawTile(tilePile)
	 		player.addTileToHand(getTile[0])
	 		tilePile = getTile[1]

	 	#returns tuple with all the info
	 	results = [tilePile, inList, outList, board]
	 	if (len(inList) <= 1):
	 		results.append(True)
	 	else:
	 		results.append(False)

	 	return results


newServ = Server()

newServ.startGame()


