#Andrew DeFran
#CSCI 160
#12/1/2018

#Racko Main


#main function game
def main():
	start = "N"
	#welcome and start menu
	start = str.capitalize(input("Welcome to Rack-o. The game your new step-dad's family\n" 
								 "wants to play. Do you dare? (Y/N): "))

	#game loop
	while(start != "N"):
		print("\n Ok! you've been warned...")
		#import functions
		from racko_functions import build_deck
		from racko_functions import shuffle
		from racko_functions import check_racko
		from racko_functions import deal_card
		from racko_functions import deal_hands
		from racko_functions import print_rack
		from racko_functions import find_and_replace
		from racko_functions import discard
		from racko_functions import computer_turn
		from random import randint
		import time

		#build variables
		game_deck = build_deck()
		hand = []
		discard_pile = []
		user_rack = []
		comp_rack = []
		card_drawn_comp = 0
		card_drawn_user = 0
		turn = True #true=comp, false=user
		racko = False #function check will flip
		count_round = 0 #hopefully tally rounds
		

		#turn portion message
		time.sleep(2)
		print("\nHey Champ! Let's determine who goes first! The computer and player\n"
			  "will pick a card from the deck and the larger(dominant) goes first.\n"
			  "The computer pre-empts you into a pincer attack. Shuffling...shuffling....")

		#shuffle deck
		shuffle(game_deck)
		#computer draw
		card_drawn_comp = deal_card(game_deck)
		print("\nComputer drew: ", card_drawn_comp)
		#user draw
		time.sleep(2)
		card_drawn_user = deal_card(game_deck)
		print("User Drews a: ", card_drawn_user)

		#turn choice
		if(card_drawn_user > card_drawn_comp):
			turn = False
			print("\nYou strike first!")
		else:
			print("\nDa robit goes foist!")

		#reshuffle everything
		game_deck = build_deck()
		
		#deal hands
		time.sleep(3)
		print("\nOk I'll deal out the hands...")

		hand = deal_hands(game_deck)
		
		#assign racks
		user_rack = hand[0]
		comp_rack = hand[1]

		#discard pile reveal
		print("\nNow to flip a card and start a discard pile...")
		discard_pile += [deal_card(game_deck)]
		time.sleep(1)
		print("That card is: ", discard_pile)
		
		#rack check game loop
		while(racko != True):
			hand = [user_rack, comp_rack]
			count_round += 1
			
			#racko check
			if(check_racko(user_rack) == True):
				print("\nOoo-wa-ah-ah-ah(disturbed voice)! You have Rack-O!\n"
					  "You celebrate with a phat dab offa your Juul.")
				racko = True
			elif(check_racko(comp_rack) == True):
				print("\nZounds and gadzooks! The computer has Rack-O my man.\n"
					  "Your step-dad takes away your Juul and grounds you.")
				racko = True

			#do we need to reshuffle?
			
			if(len(discard_pile) == 40):
				game_deck = discard_pile
				discard_pile = [deal_card(game_deck)]
				print("\nOut of cards. Reshuffle deck and create a new discard pile...")
				time.sleep(3)
				print("The new discard pile starts with:", discard_pile)

			#computer turn
			while(turn == True):
				print("\nThe Matrix's turn!")
				time.sleep(1)
				print("Computing....Computing...zippity...blurp...hic")

				#call computer turn function and assign new rack
				comp_rack_disc_list = computer_turn(hand, game_deck, discard_pile)
				comp_rack = (comp_rack_disc_list[0])
				discard_pile = (comp_rack_disc_list[1])
				turn = False

				time.sleep(3)
				print("\nPlayer Play-on!")

			#between turns racko check
			if(check_racko(user_rack) == True):
				print("\nOoo-wa-ah-ah-ah(disturbed voice)! You have Rack-O!\n"
					  "You celebrate with a phat dab offa your Juul.")
				racko = True

			elif(check_racko(comp_rack) == True):
				print("\nZounds and gadzooks! The computer has Rack-O my man.\n"
					  "Your step-dad takes away your Juul and grounds you.")
				racko = True

			#users turn	
			while(turn == False):
				#print users rack
				time.sleep(1)
				print_rack(user_rack)

				#check discard pile if full
				if(len(discard_pile) == 40):
					game_deck = discard_pile
					discard_pile = [deal_card(game_deck)]
					print("\nOut of cards. Reshuffle deck and create a new discard pile...")

					time.sleep(3)
					print("The new discard pile starts with:", discard_pile)

				#print discard pile top
				print("\nThe top of the discard pile reads:", discard_pile[0])
				decision1 =  str.capitalize(input("\nWill you pick up and use the card on the discard pile (Y/N)? "))

				if(decision1 == "Y"):
					new_card = int(discard_pile[0])
					card_replaced = int(input("\nWhich card would you like to replace in your rack (card number)? "))

					#validate
					while(card_replaced not in user_rack):
						print("\nHey dum dum, that is an invalid selection.")
						card_replaced = int(input("\nWhich card would you like to replace in your rack (card number)? "))
	
					#swap it
					print("\nOk, we'll swip-swap it.")

					new_hand = find_and_replace(new_card, card_replaced, hand, discard_pile)
					user_rack = new_hand[0]
					discard_pile = new_hand[2]
					turn = True
					
				elif(decision1 == "N"):
					print("Feelin chancy? Fine, we'll draw from the deck...")

					#draw a card
					card_drawn_user = deal_card(game_deck)
					print("You drew a:", card_drawn_user)

					#use it?
					decision2 = str.capitalize(input("Will you use the card (Y/N)? "))
					new_card = card_drawn_user

					if(decision2 == "Y"):
						card_replaced = int(input("\nWhich card would you like to replace in your rack (card number)? "))

						#validate
						while(card_replaced not in user_rack):
							print("\nHey dum dum, that is an invalid selection.")
							card_replaced = int(input("\nWhich card would you like to replace in your rack (card number)? "))

						#swap it
						print("Ok, we'll swip-swap it.")

						new_hand = find_and_replace(new_card, card_replaced, hand, discard_pile)
						user_rack = new_hand[0]
						discard_pile = new_hand[2]
						turn = True
						
					elif(decision2 == "N"):
						discard_pile = discard(new_card,discard_pile)
						turn = True
						
				#final racko check
			if(check_racko(user_rack) == True):
				print("\nOoo-wa-ah-ah-ah(disturbed voice)! You have Rack-O!\n"
					  "You celebrate with a phat dab offa your Juul.")
				racko = True
			elif(check_racko(comp_rack) == True):
				print("\nZounds and gadzooks! The computer has Rack-O my man.\n"
					  "Your step-dad takes away your Juul and grounds you.")
				racko = True
				
				#round summary
				time.sleep(3)
				print("\nEnd of Round:", count_round)
				print_rack(user_rack)
				print("\nDiscard pile:", discard_pile[0])
				

			#keep playing?
			start = str.capitalize(input("\nContinue? (Y/N)"))
			if(start == "N"):
				racko = True

		#game summary	
		print("\nThe winner won in", count_round, "rounds")
		print("user rack:", user_rack)
		print("comp rack:", comp_rack)
		#turn off loop/play again
		start = str.capitalize(input("\nOh My God you can't possibly want more!? (Y/N)"))

	#end game message
	print("You have opted for the inevitable choice: defenestration. Farewell.")

main()

#if __name__ == ’__main__’:       main() 