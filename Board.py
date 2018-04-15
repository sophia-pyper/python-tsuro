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






