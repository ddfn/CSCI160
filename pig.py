import random

def show_instructions():
    print(	" Welcome to the game of Pig. \n\n To win, be the\n"
     		" player with the most points at the end of the\n"
     		" game. The game ends at the end of a round where\n"
     		" at least one player has 100 or more points\n\n"
     
     		" On each turn, you may roll the die as many times\n"
     		" as you like to obtain more points. However, if\n"
     		" you a 1, your turn is over, and you do not\n"
     		" obtain any points that turn.\n\n")

def die_roll():
	return random.randrange(1, 6 + 1)

def human_turn():
	turn_points = 0
	roll = 0
	roll_again = "y"
	while(roll != 1 and roll_again == "y"):
		roll = die_roll()
		print("You rolled a", roll)
		roll_again = input("Would you like to roll again y/n: ")

human_turn()

"""
def play_game():
	h_points = 0
	c_points = 0

	while(game is not over)
		human_turn()

		Computer_turn()
"""