import random
from Tile import Tile
#server representation of class

class sPlayer:

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

	def addTileToHand(self,tile):
		self.hand.append(tile)

	#for now, generates a random tile/roation
	def getTileChoice(self):
		index = random.randint(0, len(self.hand)-1)
		tile = self.hand[index]
		rotate = random.randint(0,3)
		for i in range(rotate):
			tile.rotate()
		return tile

	def removeTile(self, tile):
		for t in range(len(self.hand)):
			if (self.hand[t] == tile):
				del self.hand[t]
				return

