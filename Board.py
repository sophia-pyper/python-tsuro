import copy

class Board:
	
	def __init__(self, rows = 6, cols = 6):
		self.rows = rows
		self.cols = cols
		self.players = []
		spaces = []
		#creates a matrix of empty spaces
		for row in range(rows):
			spaces.append([])
			for col in range(cols):
				space = []
				for i in range(8): #represents the eight path positions
					if (((i == 0 or i ==1) and (row == 0)) #top of spaces for top row
						or ((i == 4 or i == 5) and (row == (rows-1))) #bottom of spaces for bottom row
						or ((i == 6 or i == 7) and (col == 0)) #left of spaces for first column
						or ((i == 2 or i == 3) and (col == (cols-1)))): #right of spaces for last column
						
						space.append([1,"X"]) #denotes walls/ticks
					else:
						space.append([0,"X"])
				#print space		
				spaces[row].append(space)
		self.spaces = spaces
		#print self.spaces

	#Puts the players on the board in the beginning of the game. Returns false if chosen starting spot is invalid
	def placePlayer(self,player, r, c, t):
		#if there is a 1, then that means edge (good), if there is a P, then that means already occupied
		if (self.spaces[r][c][t][0] == 1 and self.spaces[r][c][t][1] != "P"):
			player.updateLocation(r,c,t)
			self.players.append(player)
			self.spaces[r][c][t][1] = "P"
			return True
		else:
			return False

	def removePlayer(self,player):
		for i in range(len(players)):
			if (self.players[i] == player):
				del self.players[i]
				return

	#Adds tile to the board
	def addTileToBoard(self,tile, r, c):
		for path in tile.paths:
			start = path[0]
			end = path[1]
			self.spaces[r][c][start][1] = end
			self.spaces[r][c][end][1] = start

	#Checks which moves would result in the death of the player. Returns list of these moves
	def findIllegalMoves(self, player):
	 	
	 	boardCopy = copy.deepcopy(self)
	 	currRow = player.location[0]
	 	currCol = player.location[1]
	 	currTick = player.location[2]
	 	illegalMoves = []
	 	
	 	#iterates through every rotation of every tile
	 	for tile in player.hand:
	 		for i in range(4):
	 			tile.rotate()

	 			#plays out a turn, moving player and checking whether they die
	 			boardCopy.addTileToBoard(tile, currRow, currCol)
	 			
	 			boardCopy.movePlayer(player)

	 			#if at some point the player died, add the tile info to the illegal moves list
	 			if (player.dead):
	 				illegalMoves.append(tile.paths)
	 				player.kill(False)

	 			#reverts board
	 			boardCopy = copy.deepcopy(self)
	 			player.updateLocation(currRow, currCol, currTick)

	 	#If all moves are illegal, then none are			
	 	if (len(illegalMoves) == (4* len(player.hand))):
	 		illegalMoves = []
	 	
	 	return illegalMoves


	#Returns true if edge, false if not
	def checkCurrTick(self,player):
	 	if (self.spaces[player.location[0]][player.location[1]][player.location[2]][0] == 1):
	 		return True
	 	else:
	 		return False

	#Determines what tick/tile is adjacent to the current player position
	def checkAdjacentTick(self,player):
	 	newLoc = []
	 	currRow = player.location[0]
	 	currCol = player.location[1]
	 	currTick = player.location[2]
	 	if (not self.checkCurrTick(player)):
	 		if (currTick == 0):
	 			newLoc = [(currRow-1),currCol,5]
	 		if (currTick == 1):
	 			newLoc = [(currRow-1), currCol, 4]
	 		if (currTick == 2):
	 			newLoc = [currRow, (currCol+1), 7]
	 		if (currTick == 3):
	 			newLoc = [currRow, (currCol+1), 6]
	 		if (currTick == 4):
	 			newLoc = [(currRow+1), currCol, 1]
	 		if (currTick == 5):
	 			newLoc = [(currRow+1), currCol, 0]
	 		if (currTick == 6):
	 			newLoc = [currRow, (currCol-1), 3]
	 		if (currTick == 7):
	 			newLoc = [currRow, (currCol-1), 2]
	 	return newLoc

	#Moves the player character on the board
	def movePlayer(self,player):
	 	currRow = player.location[0]
	 	currCol = player.location[1]
	 	currTick = player.location[2]

	 	#looks at what tick the current path leads to
	 	connector = self.spaces[currRow][currCol][currTick][1]
	 	if (connector != "X"): #if a path exists
	 		if (connector >= 0 and connector <= 7):
	 			#Move player to tick at end of path
	 			player.updateLocation(currRow, currCol, connector)

	 		else:
	 			print "Something went wrong - invalid path"

		 	#check if player hit a wall. also checks for collisions inherently
		 	if (self.checkCurrTick(player)):
		 		player.kill(True)
		 		return

		 	#otherwise, check tick of adjacent tile to see if path continues and keep moving if so
		 	else:
		 		newLocation = self.checkAdjacentTick(player)
		 		player.updateLocation(newLocation[0], newLocation[1], newLocation[2])
		 		self.movePlayer(player)