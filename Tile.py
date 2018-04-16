#tile class

#import legal tilelist
from tilelist import tilelist

class Tile:
	
	# tile # passed in
	def __init__(self, path):
		#tuple containing the path connections
		self.path = path


	#function to rotate tile (90 degrees clockwise)
	#assuming tile.paths is a 4-element list of double-element lists 

	def rotate(self):
		for connection in path:
			for end in connection
			#add 2 - representing translating path end 90 degrees clockwise
			end += 2
			#if path end is on left side of tile, then restart number
			if(end >= 8):
				end -= 8