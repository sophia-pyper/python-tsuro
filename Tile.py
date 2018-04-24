#tile class


class Tile:
	
	# tile # passed in
	def __init__(self, paths):
		#tuple containing the path connections
		self.paths = paths
	
	#function to rotate tile (90 degrees clockwise)
	#assuming tile.paths is a 4-element list of double-element lists 

	def rotate(self):
		for p in range(len(self.paths)):
			self.paths[p][0] += 2
			self.paths[p][1] += 2
			
			if(self.paths[p][0] >= 8):
				self.paths[p][0] -= 8

			if(self.paths[p][1] >= 8):
				self.paths[p][1] -= 8