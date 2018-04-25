from sPlayer import sPlayer
from Tile import Tile
from Board import Board
from Server import Server
from tilelist import tilelist
import copy



#game class instances to be used in testing below
player1 = sPlayer("blue", 20)
player2 = sPlayer("red", 30)
testtile = Tile([[0,1],[2,3],[4,5],[6,7]])  
testboard = Board()



#TILE TESTS

#test that constructor works
if(testtile.paths != [[0,1],[2,3],[4,5],[6,7]]):
	print "Tile constructor test failed!"

#test that rotating once works
testtile.rotate()
#Rotating once should change paths to [[2,3],[4,5],[6,7],[0,1]], test
if(testtile.paths != [[2,3],[4,5],[6,7],[0,1]]):
	print "Expected [[2,3],[4,5],[6,7],[0,1]] but received " + str(testtile.paths)
	print "Tile rotation test failed!"

#test that multi-rotation works (3 more rotations should result in original tile)
testtile.rotate()
testtile.rotate()
testtile.rotate()
if(testtile.paths != [[0,1],[2,3],[4,5],[6,7]]):
	print "Expected [[0,1],[2,3],[4,5],[6,7]] but received " + str(testtile.paths)
	print "Tile multi-rotation test failed!"



#sPlayer TESTS

#test for adding tile to hand
player1.addTileToHand(testtile)
if(len(player1.hand)==0):
	print "Add tile to hand test failed!"

#test for removing tile from hand
player1.removeTile(testtile)
if(len(player1.hand)!=0):
	print "Remove tile from hand test failed!"



#Board TESTS

#test for adding player1 to board
t1 = testboard.placePlayer(player1,0,0,0) #place player1 on the upper left most tick
if(not t1):
	print "Player1 not placed!"
	print "Only player placing test failed!"
if(testboard.spaces[0][0][0][1] != "P"): #check that "X" has been changed to "P"
	print "Player1 occupation indicator not present!"
	print "Only player placing test failed!"

#test checkcurrtick on player1
t2 = testboard.checkCurrTick(player1)
if(not t2):
	print "checkCurrTick test failed!"

#test for attempting to add player 2 to player 1's position
t3 = testboard.placePlayer(player2,0,0,0)
if(t3):
	print "Player placement overlap test failed!"

#test for adding tile to board
testboard.addTileToBoard(testtile,0,0)
expected = [[1,1],[1,0],[0,3],[0,2],[0,5],[0,4],[1,7],[1,6]]
if(testboard.spaces[0][0] != expected):
	print "Adding tile to board test failed!"

#test for impossible situation if player1 is only given testtile (which always leads to edge)
player1.addTileToHand(testtile)
legalmoves = testboard.findLegalMoves(player1)
if(len(legalmoves) == 0): #there are no bad moves since the testtile always leads to suicide
	print "Impossible bad moves test failed!"

#test for checkadjacenttick by forcing player2 position
player2.updateLocation(0,0,3)
t4 = testboard.checkAdjacentTick(player2)
if(t4 != [0,1,6]):
	print "checkAdjacentTick test failed!"

#test moveplayer on player1 (who should be eliminated) and player2 (who ends up on 0,0,2)
testboard.movePlayer(player1)
testboard.movePlayer(player2)
if(player2.location != [0,1,7]):
	print "movePlayer on Player2 test failed!"
if(not player1.dead):
	print "movePlayer on Player1 test failed!"

###MOVEMENT TESTS###

#Tests whether player can successfully move from the edge
def moveFromEdge():
	player1 = sPlayer("blue", 20)
	testBoard = Board()
	tile = Tile([[0,2],[1,4],[3,7],[5,6]])
	testBoard.placePlayer(player1, 0, 0, 0)
	testBoard.addTileToBoard(tile,0,0)
	testBoard.movePlayer(player1)
	if (player1.location == [0,1,7]):
		print "moveFromEdge test passed"
	else:
		print "moveFromEdge test failed with player location at ", player1.location, " rather than [0,1,7]."
	return

#Tests whether player successfully traverses multiple tiles
def multiTileMove():
	player1 = sPlayer("blue", 20)
	testBoard = Board()
	#player would move from 0 to 2
	tile1 = Tile([[0,2],[1,7],[3,4],[5,6]])
	#player would continue to 7 and move to 4
	tile2 = Tile([[0,3],[1,6],[2,5],[4,7]])
	#player would continue to 1 and move to 5
	tile3 = Tile([[0,6],[1,5],[2,4],[3,7]])
	#player would continue to tick 5 (tick 0 on next tile) then stop

	testBoard.placePlayer(player1, 0, 0, 0)
	testBoard.addTileToBoard(tile1,0,0)
	testBoard.addTileToBoard(tile2,0,1)
	testBoard.addTileToBoard(tile3,1,1)
	testBoard.movePlayer(player1)

	if (player1.location == [2,1,0]):
		print "multiTileMove test passed"
	else:
		print "multiTileMove test failed with player location at ", player1.location, " rather than [2,1,0]."

#Tests whether two players moving on same turn works
def multiPlayerMove():
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	playerList = [player1, player2]

	testBoard = Board()
	tile = Tile([[0,4],[1,5],[2,6],[3,7]])

	testBoard.placePlayer(player1, 5, 5, 4)
	testBoard.placePlayer(player2, 5, 5, 3)

	testBoard.addTileToBoard(tile, 5, 5)

	for p in playerList:
		testBoard.movePlayer(p)

	if ((player1.location == [4,5,5]) and (player2.location == [5,4,2])):
		print "multiPlayerMove passed"
	elif(player1.location != [4,5,5]):
		print "multiPlayerMove test failed, player1 location expected [4,5,5], got " + player1.location
	elif(player2.location != [5,4,2]):
		print "multiPlayerMove test failed, player2 location expected [5,4,2], got " + player2.location

#Tests when multiple players are eliminated at once
def multiElimMove():
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	testBoard = Board()
	tile = Tile([[0,1],[2,3],[4,5],[6,7]])

	testBoard.placePlayer(player1,0,0,0)
	testBoard.placePlayer(player2,0,0,7)
	testBoard.addTileToBoard(tile,0,0)

	testBoard.movePlayer(player1)
	testBoard.movePlayer(player2)

	if (player1.dead and player2.dead):
		print "multiElimMove passed"
	elif(not player1.dead):
		print "multiElimMove test failed, player1 not dead as expected"
	elif(not player2.dead):
		print "multiElimMove test failed, player2 not dead as expected"

#Tests adding a rotated tile to the board
def addRotatedTile():
	tile = Tile([[0,6],[1,3],[2,5],[4,7]])
	testBoard = Board()

	tile.rotate() #output should be [[0,2],[3,5],[4,7],[1,6]]
	testBoard.addTileToBoard(tile,0,0)

	expected = [[1,2],[1,6],[0,0],[0,5],[0,7],[0,3],[1,1],[1,4]]
	if(testBoard.spaces[0][0] != expected):
		print "addRotatedTile test failed."
		print "expected [[1,2],[1,6],[0,0],[0,5],[0,7],[0,3],[1,1],[1,4]], got " + testBoard.spaces[0][0]
	else:
		print "addRotatedTile passed"

#Tests that an illegal move is not approved when there is a legal move available
def blockIllegal():
	legal = Tile([[0,2],[1,3],[4,6],[5,7]])
	illegal = Tile([[0,1],[2,3],[4,5],[6,7]])
	testBoard = Board()
	player = sPlayer("blue", 30)

	testBoard.placePlayer(player,0,0,0)
	player.addTileToHand(legal)
	player.addTileToHand(illegal)
	legalmoves = testBoard.findLegalMoves(player)

	if(illegal.paths in legalmoves):
		print "blockIllegal test failed, illegal move is marked as legal"
	elif(legal.paths not in legalmoves):
		print "blockIllegal test failed, legal move did not appear in list" , legalmoves
	else:
		print "blockIllegal passed"

##HAND/DRAGON TILE TESTS
#Ensures no dragon tile is issued when it is unnecessary
def noDragonTile():
	#Create server instance and set up turn
	serv = Server()
	board = Board()
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	playersIn = [player1, player2]
	playersOut = []
	tile = False
	drawPile = copy.deepcopy(tilelist)
	board.placePlayer(playersIn[0], 0, 0, 0)
 	board.placePlayer(playersIn[1], 0, 2, 0)
 	drawPile = serv.dealTiles(playersIn, drawPile)
	while not tile:
		newT = player1.getTileChoice()
		if (serv.is_play_legal(newT, player1, board)):
			tile = newT
			player1.removeTile(tile)
 	serv.play_a_turn(drawPile, playersIn, playersOut, board, tile)
 	if serv.hasDragonTile:
 		print "noDragonTile test failed: player ", serv.hasDragonTile, " has a dragon tile."
 	else:
 		print "noDragonTile passed"

#Tests whether dragon tile switches to another player
def dragonTileOwner():
	serv = Server()
	board = Board()
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	playersIn = [player1, player2]
	playersOut = []
	tile = False
	drawPile = copy.deepcopy(tilelist)
	board.placePlayer(playersIn[0], 0, 0, 0)
 	board.placePlayer(playersIn[1], 0, 2, 0)
 	drawPile = serv.dealTiles(playersIn, drawPile)
 	#Ensure both players have only two tiles, which would qualify both for dragon tile
 	while not tile:
		newT = player1.getTileChoice()
		if (serv.is_play_legal(newT, player1, board)):
			tile = newT
			player1.removeTile(tile)
 	player2.hand = player2.hand[1:]
 	#Let player 2 have received it on the previous turn
 	serv.hasDragonTile = player2
 	#Make draw pile empty
 	drawPile = []
 	serv.play_a_turn(drawPile, playersIn, playersOut, board, tile)
 	if not (serv.hasDragonTile == player2):
 		print "dragonTileOwner failed: hasDragonTile value is ", serv.hasDragonTile, " instead of player2"
 	else:
 		print "dragonTileOwner passed"

#Tests whether dragon tile owner changes when they eliminate another player (should change since the dead player's tiles return to the hand)
def dragonTileElim1():
	serv = Server()
	board = Board()
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	player3 = sPlayer("green", 30)
	playersIn = [player1, player2, player3]
	playersOut = []
	tile = Tile([[0,4],[1,7],[2,3],[5,6]])
	drawPile = copy.deepcopy(tilelist)
	board.placePlayer(playersIn[0], 0, 0, 0)
 	board.placePlayer(playersIn[1], 0, 0, 1)
 	board.placePlayer(playersIn[2], 0, 2, 0)
 	drawPile = serv.dealTiles(playersIn, drawPile)
 	#Give everyone 2 tiles instead of 3
 	for p in playersIn:
 		p.hand = p.hand[1:]
 	drawPile = []
 	serv.hasDragonTile = player1
 	serv.play_a_turn(drawPile, playersIn, playersOut, board, tile)
 	if serv.hasDragonTile:
 		print "dragonTileElim1 failed: hasDragonTile value is ", serv.hasDragonTile, " instead of False"
 	else:
 		print "dragonTileElim1 passed"

#Tests whether dragon tile ownership rotates after an elimination when draw pile is refilled and then emptied
def dragonTileElim2():
	serv = Server()
	board = Board()
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	player3 = sPlayer("green", 30)
	playersIn = [player1, player2, player3]
	playersOut = []
	tile = Tile([[0,4],[1,7],[2,3],[5,6]])
	drawPile = copy.deepcopy(tilelist)
	board.placePlayer(playersIn[0], 0, 0, 0)
 	board.placePlayer(playersIn[1], 0, 0, 1)
 	board.placePlayer(playersIn[2], 0, 2, 0)
 	drawPile = serv.dealTiles(playersIn, drawPile)
 	#Give everyone 1 tiles instead of 3
 	for p in playersIn:
 		p.hand = p.hand[2:]
 	drawPile = []
 	serv.hasDragonTile = player1
 	serv.play_a_turn(drawPile, playersIn, playersOut, board, tile)
 	if not (serv.hasDragonTile == player3):
 		print "dragonTileElim2 failed: hasDragonTile value is ", serv.hasDragonTile, " instead of player3"
 	else:
 		print "dragonTileElim2 passed"

#Tests whether dragon tile owner gets set to False if owner is eliminated and no one else needs it
def dragonOwnerElim():
	serv = Server()
	board = Board()
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	player3 = sPlayer("green", 30)
	playersIn = [player3, player1, player2]
	playersOut = []
	tile = Tile([[0,4],[1,7],[2,3],[5,6]])
	drawPile = copy.deepcopy(tilelist)
	board.placePlayer(playersIn[0], 0, 0, 0)
 	board.placePlayer(playersIn[1], 0, 0, 1)
 	board.placePlayer(playersIn[2], 0, 2, 0)
 	drawPile = serv.dealTiles(playersIn, drawPile)
 	#Player 2 has dragon tile. Everyone else has full hand
 	player2.hand = player2.hand[1:]
 	drawPile = []
 	serv.hasDragonTile = player2
 	serv.play_a_turn(drawPile, playersIn, playersOut, board, tile)
 	if serv.hasDragonTile:
 		print "dragonOwnerElim failed: hasDragonTile value is ", serv.hasDragonTile, " instead of False"
 	else:
 		print "dragonOwnerElim passed"

#Tests whether hasDragonTile is reset to false when dragon tile owner eliminates self
def dragonOwnerSelfElim():
	serv = Server()
	board = Board()
	player1 = sPlayer("blue", 20)
	player2 = sPlayer("red", 30)
	player3 = sPlayer("green", 30)
	playersIn = [player1, player2, player3]
	playersOut = []
	tile = Tile([[0,1],[2,3],[4,5],[6,7]])
	drawPile = copy.deepcopy(tilelist)
	board.placePlayer(playersIn[0], 0, 0, 0)
 	board.placePlayer(playersIn[1], 0, 0, 1)
 	board.placePlayer(playersIn[2], 0, 2, 0)
 	drawPile = serv.dealTiles(playersIn, drawPile)
 	#Player 1 has dragon tile. Everyone else has full hand
 	player1.hand = player1.hand[1:]
 	drawPile = []
 	serv.hasDragonTile = player1
 	serv.play_a_turn(drawPile, playersIn, playersOut, board, tile)
 	if serv.hasDragonTile:
 		print "dragonOwnerSelfElim failed: hasDragonTile value is ", serv.hasDragonTile, " instead of False"
 	else:
 		print "dragonOwnerSelfElim passed"



#Test for whether dealing function results in all players having hands of 3 cards

def runAllTests():
	print "Running Movement Tests:"
	moveFromEdge()
	multiTileMove()
	multiPlayerMove()
	multiElimMove()
	addRotatedTile()
	blockIllegal()
	print "Movement Tests Complete. Running Dragon Tile Tests:"
	noDragonTile()
	dragonTileOwner()
	dragonTileElim1()
	dragonTileElim2()
	dragonOwnerElim()
	dragonOwnerSelfElim()
	print "Dragon Tile Tests Complete."

runAllTests()