#server representation of class

class sPlayer:

	#color passed in to constructor
	def __init__(self, color, age):
		#token color
		self.color = color
		#easter egg
		if(age > 117):
			print("CONGRATULATIONS, YOU'RE THE OLDEST PERSON IN THE WORLD!")
		self.age = age

	#list of tiles in player hand; max 3
	hand = []