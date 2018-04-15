#tile class

#import legal tilelist
from tilelist import tilelist

class Tile:
	
	# tile # passed in
	def __init__(self, tnum):

		#tilenum is the tile # (a way to identify the tile in simple manner)
		self.tilenum = tnum
		#contains the actual paths
		self.paths = tilelist[tnum]


	#function to rotate tile (90 degrees clockwise)
	#assuming tile.paths is a 4-element list of double-element lists 

	def rotate(self):

		#for each double-element list (representing one path in tile)
		for path in self.paths:

			#for each element of path (representing one end of the path)
			for end in path:

				#add 2 - representing translating path end 90 degrees clockwise
				end += 2
				#if path end is on left side of tile, then restart number
				if(end >= 8):
					end -= 8