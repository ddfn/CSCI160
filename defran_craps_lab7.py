#Andrew DeFran
#CSCI 160
#10/25/2018
#Lab 7--craps


#define functions
#welcome and instructions
def welcome_instructions():
	print("Welcome to my back alley craps game!\n\n"
		  "The game is played in rounds.\n"
		  "The player starts with a bankroll of $1000.\n"
		  "The player makes Pass/Don't Pass bet before each round.\n"
		  "The player rolls die to determine win, lose or point.\n"
		  "if point, the player bets Come/Don't Come. \n"
		  "The player rolls again to determine win, lose, or new point\n"
		  "Good Luck!")



#define die
def die_roll():
	import random
	return random.randrange(1, 6 + 1)
	


#game logic
#define variables
bankroll = 1000
roll_again = "Y"
bet_valid = True
point = 0 

 
welcome_instructions()

#start game routing
begin = str(input("\nShall we play? (Y/N)): "))

if(begin == "Y" or begin == "y"):
	print("ok")
	
	#game goes here
	
	while(bankroll > 0 and roll_again == "Y"):

		#establish betting parameters
		pass_bet_type = str(input("Time for the come out roll! Pick Pass or Don't Pass bet type (enter P or DP): "))
		bet = int(input("How much do you want to bet?:"))
		
		#bet validation check
		while(bet > bankroll):
			print("You can't bet more than bankroll ya big dummy!.")
			bet = int(input("How much do you want to bet?:"))

		#come out roll
		import time
		print("rolling...")
		summ = die_roll() + die_roll()
		time.sleep(3)
		print("\nYou rolled a ", summ)

		#outcome check
		if(pass_bet_type == "P"):
			if(summ == 7 or summ == 11):
				print("You Win!")
				bankroll += bet
			elif(summ == 2 or summ == 3 or summ == 12):
				print("You Lose!")
				bankroll -= bet
			elif(summ != 7 or summ != 11 or summ != 2 or summ !=3 or summ != 12):
				point = summ


		elif(pass_bet_type == "DP"):
			if(summ == 2 or summ == 3):
				print("You win!")
				bankroll += bet
			elif(summ == 7 or summ == 11):
				print("You Lose!")
				bankroll -= bet
			elif(summ == 12):
				print("Barred!")
				bankroll = bankroll
			elif(summ != 7 or summ != 11 or summ != 2 or summ !=3 or summ != 12):
				point = summ

		#point play
		while(point > 0):
			print("\nIt's time for point play!  ")

			#remind bankroll
			print("Your bankroll stands at $", bankroll)

			#establish betting come parameters
			come_bet_type = str(input("\nPick Come or Don't Come bet type (enter C or DC): "))
			bet2 = int(input("How much do you want to bet?:"))
			
			#bet validation check
			while(bet + bet2 > bankroll):
				print("You can't bet more than bankroll, try again.")
				bet_valid = False
				bet2 = int(input("How much do you want to bet?:"))

			#point roll
			print("\nDaddy needs a new pair of shoes...")
			summ = die_roll() + die_roll()
			time.sleep(3)
			print("\nYou rolled a ", summ)

			#point roll pass outcome check
			if(pass_bet_type == "P"):
				if(summ == point):
					print("Pass Bet Win!")
					bankroll += bet
					point = 0
				elif(summ == 7):
					print("Pass Bet Lose!")
					bankroll -= bet
					point = 0

			if(pass_bet_type == "DP"):
				if(summ == 7):
					print("Pass bet Win!")
					bankroll += bet
					point = 0
				elif(summ == point):
					print("Pass Bet Lose!")
					bankroll -= bet
					point = 0

			#point roll come outcome check
			if(come_bet_type == "C"):
				if(summ == 7 or summ == 11):
					print("Come Bet Win!")
					bankroll += bet2
					point = 0
				elif(summ == 2 or summ == 3 or summ == 12):
					print("Come Bet Lose")
					bankroll -= bet2
					point = 0
				elif(summ != 7 or summ != 11 or summ != 2 or summ !=3 or summ != 12):
					point = summ

			elif(pass_bet_type == "DC"):
				if(summ == 2 or summ == 3):
					print("Come Bet win!")
					bankroll += bet2
				elif(summ == 7 or summ == 11 or summ == 12):
					print("You Lose!")
					bankroll -= bet2
				elif(summ != 7 or summ != 11 or summ != 2 or summ !=3 or summ != 12):
					point = summ



		print("bankroll is $", bankroll)
		roll_again = str(input("End of round. Roll again? (Y/N): "))


elif(begin == "N" or begin == "n"):
	print("Well then, move along so the next sucker has a chance.")

else:
	print("Invalid entry, restart program")

