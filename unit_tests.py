from sPlayer import sPlayer
from Tile import Tile
from Board import Board
from Server import Server


#game class instances to be used in testing below
player1 = sPlayer("blue", 20)
player2 = sPlayer("red", 30)
testtile = Tile(0)  #paths list is [[0,1],[2,3],[4,5],[6,7]]
testboard = Board()


"""
TILE TESTS
"""
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


"""
sPlayer TESTS
"""
#test for adding tile to hand
player1.addTileToHand(testtile)
if(len(player1.hand)==0):
	print "Add tile to hand test failed!"

#test for removing tile from hand
player1.removeTile(testtile)
if(len(player1.hand)!=0):
	print "Remove tile from hand test failed!"

""" WE KNOW THAT THIS WORKS
#test that killing player works
player1.kill(True)
if(not player1.dead):
	print "Player kill test failed!"
"""


"""
Board TESTS
"""
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
badmoves = testboard.findIllegalMoves(player1)
if(len(badmoves) != 0): #there are no bad moves since the testtile always leads to suicide
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