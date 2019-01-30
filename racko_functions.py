#Andrew DeFran
#CSCI160
#12/1/2018

#Racko functions

#builds a deck function
def build_deck():
	from random import randint
	deck = []

	while(len(deck) != 60):
		card = randint(1, 60)
		#no dupes!
		if(card not in deck):
			deck.append(card) 
	
	return deck

#test
#deck = build_deck()
#print("original deck: ", deck)


#shuffle a deck function
def shuffle(deck):
	count = 0

	#shuffle loop cut deck ....10 times
	while(count <= 10):
		#split up the deck 
		lst1 = deck[:len(deck) // 2]
		lst2 = deck[len(deck) // 2:]
		lst3 = lst2[:len(lst2) // 2]
		lst4 = lst2[len(lst2) // 2:]
		
		
		#recombine in opposite order
		deck = lst4 + lst3 + lst1
		
		#increment
		count += 1
	return deck

#test
#shuffled_deck = shuffle(deck)
#print("shuffled deck", shuffled_deck)

#check for racko function
def check_racko(rack):
	#loop through rack
	for i in range(0, len(rack) - 1):
		check = rack[i] - rack[i + 1]
		
		#racko check
		if(check <= 0):
			return False
		
	return True

#test
#rack = [60, 50, 45, 30, 5, 48]
#print(check_racko(rack))

#deal a card function
def deal_card(deck):
	card = deck.pop(0)
	return card

#test
#print(deal_card(shuffled_deck))

#deal hands function
def deal_hands(deck):
	user = []
	comp = []
	hands = [user, comp]

	for i in range(0, 10):
		#deal top card to computer
		c = deal_card(deck)
		comp.append(c)
		#deal next card to player
		p = deal_card(deck)
		user.append(p)

	return hands
	
#test
#print(deal_hands(shuffled_deck))

#print out racks
def print_rack(rack):
	rack_place = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
	user_rack = rack

	print("\nUsers Rack\n"
		  "Slot" + "\t" + "Card")

	for i in range(len(rack_place)):
		print(rack_place[i] + "\t", user_rack[i])

#test
#hand = deal_hands(shuffled_deck)
#user_rack = hand[0]
#print(print_rack(user_rack))

#find and replace function

def find_and_replace(new_card, card_replaced, hand, discard):
	#validation check
	if(int(card_replaced) not in hand[0] and int(card_replaced) not in hand[1]):
		return False

	elif(int(card_replaced) in hand[0] or int(card_replaced) in hand[1]):
		#traverse through hand and inner lists
		for i in range(0, len(hand)):
			for j in range(0, len(hand[i])):
			#replace
				if(hand[i][j] == int(card_replaced)):
					trash = int(card_replaced)
					hand[i][j] = new_card
					discard.pop(0)
					discard = [trash] + discard

	return hand + [discard]
#test
#hand = [[1,2,3], [4,5,6]]
#discard = [20, 21, 22]
#new_card = 60
#card_replaced = 2
#output = find_and_replace(new_card, card_replaced, hand, discard)
#print(output)




#discard function---> maybe not necessary
def discard(card, discard):
	discard = [card] + discard

	return discard

#test
#a = 14
#b = [1, 2, 3]
#print(discard(a, b))

#Computer turn function
def computer_turn(hand, deck, discard_pile):
	import time
	dis_card = discard_pile[0]
	comp_rack = hand[1]
	deck_card = 0
	
	#computer decisions
	#push out the ends
	if(dis_card > comp_rack[0]):
		trash = comp_rack[0]
		comp_rack[0] = dis_card
		time.sleep(3)
		print("Computer takes card: ", dis_card)
		#replace card
		discard_pile.pop(0)
		discard_pile = discard(trash, discard_pile)
		
		return (comp_rack , discard_pile) 

	elif(dis_card < comp_rack[-1]):
		trash = comp_rack[-1]
		comp_rack[-1] = dis_card
		time.sleep(3)
		print("Computer takes card: ", dis_card)
		#replace card
		discard_pile.pop(0)
		discard_pile = discard(trash, discard_pile)
		
		return (comp_rack , discard_pile)

	else:
		#try to make use of the discard then discard the old
		for i in range(0, len(comp_rack)):
			if((dis_card > comp_rack[i + 1]) and (dis_card < comp_rack[i])):
				trash = comp_rack[i + 1]
				comp_rack[i + 1] = dis_card
				time.sleep(3)
				print("Computer takes card: ", dis_card)
				#replace card
				discard_pile.pop(0)
				discard_pile = discard(trash, discard_pile)
				
				
				return (comp_rack , discard_pile)

		#can't use discard, so draw a card
	
		print("\nComputer wants to draw a card from the deck\n")
		deck_card = deal_card(deck)
		time.sleep(2)
		print("The computer drew:", deck_card, "!")

		#same strategy as above
		if(deck_card > comp_rack[0]):
			trash = comp_rack[0]
			comp_rack[0] = deck_card
			time.sleep(3)
			print("Computer takes card: ", deck_card)
			discard_pile = discard(trash, discard_pile)
			
			return (comp_rack , discard_pile)

		elif(deck_card < comp_rack[-1]):
			trash = comp_rack[-1]
			comp_rack[-1] = deck_card
			time.sleep(3)
			print("Computer takes card: ", deck_card)
			discard_pile = discard(trash, discard_pile)
			
			return (comp_rack , discard_pile)

		else:		
			#use the card?/ discard the old
			for i in range(0, len(comp_rack) - 1):
				if(deck_card < comp_rack[i + 1] and deck_card > comp_rack[i]):
					trash = comp_rack[i + 1]
					comp_rack[i + 1] = deck_card
					time.sleep(3)
					print("Computer takes card: ", deck_card)
					discard_pile = discard(trash, discard_pile)
						
					return (comp_rack , discard_pile)

				#refuse the card and add to discard
				else:
					time.sleep(1)
					print("\nThe computer chooses to pass and discard the card")
					discard_pile = discard(deck_card, discard_pile)
					
					return (comp_rack , discard_pile)

#test
#hand = [[1,2,3,4,5,6,7,8,9,10], [50,26,27,21,15,24,17,30,19,1]]
#discard_pile = [25, 22]
#deck = [12, 45, 59, 23, 34, 38, 18, 55, 45]
#print(computer_turn(hand, deck, discard_pile))

