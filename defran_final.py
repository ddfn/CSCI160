#Andrew DeFran
#CSCI 160
#12/11/2018

#Final Exam

#create deck function
def create_deck(suits, ranks):
	deck = []
	new_suits = []
	new_ranks = []
	ranks1 = []
	ranks2 = []
	
	#modify suits to just first letter
	for i in range(0, len(suits)):
		new_suits += suits[i][0]

	#modify ranks similarly/split
	for i in range(0, len(ranks[:-4])):
		ranks1.append(ranks[i])

	for i in range(9, 13):
		ranks2.append(ranks[i])

	#transform high cards
	for i in range(0, len(ranks2)):
		ranks2[i] = ranks2[i][0]

	#string interger numbers
	for i in range(0, len(ranks1)):
		ranks1[i] = str(ranks1[i])

	#combine the standardized lists
	new_ranks = ranks1 + ranks2

	#make the deck
	for i in range(0, len(new_suits)):
		for j in range(0, len(new_ranks)):
			deck.append(new_ranks[j] +  new_suits[i])
		
	return deck

#test
suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


#shuffle deck function
def shuffle_deck(deck):
	import random
	random.shuffle(deck)
	
	return deck


#deal function
def deal(deck):
	card = deck.pop(0)
	return card


#how many function
def how_many(deck):
	#count variables
	count_d = 0
	count_h = 0
	count_c = 0
	count_s = 0
	deal_count = 0
	stop = False

	#shuffle deck
	deck = shuffle_deck(deck)
	
	#deal cards and count
	while(stop == False):
		#deal a card
		card = deal(deck)

		if(card[1] == "D"):
			count_d += 1
			deal_count += 1

		elif(card[1] == "H"):
			count_h += 1
			deal_count += 1

		elif(card[1] == "C"):
			count_c += 1
			deal_count += 1

		elif(card[1] == "S"):
			count_s += 1
			deal_count += 1

		#stop conditions	
		if(count_h >= 1 and count_d >= 1 and count_s >= 1 and count_c >= 1):
			stop = True
	
	deck = create_deck(suits, ranks)
	return deal_count

#test
#print(how_many(deck))

#deck = create_deck(suits, ranks)

#simulation code
#tab variable
summ = 0
counter = 0
turn = 0
while(counter <= 10000):
	deck = create_deck(suits, ranks)
	turn = how_many(deck)
	summ += turn

	#increment count
	counter += 1

average = summ // 10000
#output
print("The average number of turns before you get to each suit is ", average, ".")

