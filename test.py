from sPlayer import *

player1 = sPlayer("blue", 20)

def killThePlayer(player):
	player.kill(True)
	return

killThePlayer(player1)

print player1.dead