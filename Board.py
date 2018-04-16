class Board:
	
	def __init__(self, rows = 6, cols = 6):
		self.rows = rows
		self.cols = cols
		spaces = []
		#creates a matrix of empty spaces
		for row in range(rows):
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
				print space		
				spaces.append(space)
		self.spaces = spaces

	def addTileToBoard(tile, x, y)
		for path in tile.paths:
			start = path[0]
			end = path[1]
			spaces[x][y][start][1] = end
			spaces[x][y][end][1] = start

	def removeTile(x, y)
		for i in range(8):
			spaces[x][y][i][2] = "X"

	#Checks which moves would result in the death of the player. Returns list of these moves
	 def findIllegalMoves(player, board):
	 	
	 	boardCopy = board
	 	currRow = player.location[0]
	 	currCol = player.location[1]
	 	originalLocations = []
	 	illegalMoves = []
	 	
	 	#stores original locations of players
	 	for p in playersIn:
	 		originalLocations.append([p.location, p])
	 	
	 	#iterates through every rotation of every tile
	 	for tile in player.hand:
	 		for i in range(4):
	 			tile.rotate()

	 			#plays out a turn, moving players a checking for collisions
	 			boardCopy.addTileToBoard(tile, currRow, currCol)
	 			for pl in playersIn:
	 				movePlayer(pl)
	 			collisionCheck()

	 			#if at some point the player died, add the tile info to the illegal moves list
	 			if (player.dead):
	 				illegalMoves.append(tile.paths)

	 			for pl in playersIn:
	 				pl.dead = False

	 			#reverts board
	 			board.removeTile(currRow, currCol)
	 			for x in originalLocations
	 				x[1].updateLocation(x[0][0], x[0][1],x[0][2])

	 	#If all moves are illegal, then none are			
	 	if (len(illegalMoves) == (4* len(player.hand))):
	 		illegalMoves = []
	 	
	 	return illegalMoves


	 #Returns true if edge, false if not
	 def checkCurrTick(player):
	 	if (board.spaces[player.location[0]][player.location[1]][player.location[2]] == 1):
	 		return True
	 	else:
	 		return False

	 #Determines what tick/tile is adjacent to the current player position
	 def checkAdjacentTick(player):
	 	newLoc = []
	 	currRow = player.location[0]
	 	currCol = player.location[1]
	 	currTick = player.location[2]
	 	if (not checkCurrTick(player)):
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
	def movePlayer(player):
	 	currRow = player.location[0]
	 	currCol = player.location[1]
	 	currTick = player.location[2]

	 	#tracks the player's path this turn for collision detection
	 	ticksVisited.append([player.location, player])

	 	#looks at what tick the current path leads to
	 	connector = board.spaces[currRow][currCol][currTick][1]
	 	if (connector != "X"): #if a path exists
	 		if (connector >= 0 and connector <= 7):
	 			#Move player to tick at end of path
	 			player.updateLocation(currRow, currCol, connector)
	 			ticksVisited.append(player.location)
	 		else:
	 			print "Something went wrong - invalid path"

		 	#check if player hit a wall
		 	if (checkCurrTick(player)):
		 		player.dead = True
		 		return

		 	#otherwise, check tick of adjacent tile to see if path continues and keep moving if so
		 	else:
		 		newLocation = checkAdjacentTick(player)
		 		player.updateLocation(newLocation[0], newLocation[1], newLocation[2])
		 		movePlayer(player)

	#Checks for collisions
	def collisionCheck():
		for i in range(len(ticksVisited)-1):
			for j in range(i+1, len(ticksVisited)):
				#checks whether a location has been visited twice
				if (ticksVisited[i][0] == ticksVisited[j][0]):
					#kills both players if so
					if (ticksVisited[i][1].dead == False):
						ticksVisited[i][1].dead == True
					if (ticksVisited[j][1].dead == False):
						ticksVisited[j][1].dead == True
					break
		ticksVisited = []






