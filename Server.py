from tilelist import tilelist
from Board import Board

class Server:
	 def __init__(self, numPlayers = 2):
	 	#dummy code for now. we'll figure out player choice later
	 	player1 = 1#SPlayer("blue", 28)
	 	player2 = 2#SPlayer("red", 14)
	 	self.playersIn = [player1, player2]
	 	self.tileList = tilelist
	 	self.playersOut = []
	 	self.board = Board()
	 	self.gameStarted = False
	 	self.firstPlayer = player1

	 def startGame():
	 	#arbitrarily places players on board for now. we'll change this later


	 def playGame():
	 	if (not gameStarted):
	 		#initialize players on board on first turn
	 		startGame()
	 		gameStarted = True
	 	if (playersIn.length == 1):
	 		return "Player ",playersIn[0]," has won!"
	 	for player in playersIn:
	 		player.getTileChoice() #get tile choice from player


newServ = Server()

newServ.startGame()


