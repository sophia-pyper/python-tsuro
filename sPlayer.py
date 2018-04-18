#server representation of class

class sPlayer:

	"""

	"""

	#[x,y,z] - x and y representing which space and z representing which tick (based on convention below)
	"""
	    0  1
	  ________
	7 |       | 2
	  |       |
	6 |_______| 3
	    5  4

	"""

	def __init__(self, color, age):
		#token color
		self.color = color
		#easter egg
		if(age >= 117):
			print("CONGRATULATIONS, YOU'RE THE OLDEST PERSON IN THE WORLD!")
		self.age = age
		#set player location on board, x and y representing which space and z representing which tick
		self.location = []
		#list of tiles in hand. max three
		self.hand = []
		#flags player to be removed from game
		self.dead = False

	def updateLocation(self,r,c,t):
		self.location = [r,c,t]

	def kill(self,b):
		self.dead = b

	def addTileToHand(self,tile):
		self.hand.append(tile)

	def getTileChoice(self, tile):
		return self.hand[0]

	def removeTile(self, tile):
		for t in range(len(self.hand)):
			if (self.hand[t] == tile):
				del self.hand[t]
				return