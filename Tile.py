#tile class

#import legal tilelist
from tilelist import tilelist

class Tile:
	
	# tile # passed in
	def __init__(self, paths):
		#tuple containing the path connections
		self.paths = paths


	#function to rotate tile (90 degrees clockwise)
	#assuming tile.paths is a 4-element list of double-element lists 

	def rotate(self):
		for path in paths:
			for end in path
			#add 2 - representing translating path end 90 degrees clockwise
			end += 2
			#if path end is on left side of tile, then restart number
			if(end >= 8):
				end -= 8