#Andrew DeFran
#CSCI 160
#10/20/2018

#lottery functions module

#import statements
import random

#Lottery number generator function
def gimme_3_unique_random(start, end, quan): 
	# Function to generate 3 unique random numbers
	# param name:	start 	= starting range
	# param type:	int 
	# param name: 	end 	= ending range 
	# param type:	int
	# param name:	quan 	= quantity
	# param type:	int

	# returns a list of quan random numbers

	# list to hold generated numbers
    res = [] 
    while(len(res) != quan):
        n = random.randint(start, end)
        if (n not in res):
            res.append(n)
    # return the list
    return res 


#function to validate input numbers
def is_valid(number1, number2, number3):
	if((1 <= number1 <= 100) and (1 <= number2 <= 100) and (1 <= number3 <= 100)):
		if(number1 == number2 or number1 == number3 or number2 == number3):
			return False
		else:
			return True			
	else:
		return False



#function to checks for winner winner chicken dinners
def check_win(usernum1, usernum2, usernum3, lotnum1, lotnum2, lotnum3):
	if(usernum1 == lotnum1 and usernum2 == lotnum2 and usernum3 == lotnum3):
		return int(4)
	elif((usernum1 == lotnum1 or usernum1 == lotnum2 or usernum1 == lotnum3) and (usernum2 == lotnum1 or usernum2 == lotnum2 or usernum2 == lotnum3) and (usernum3 == lotnum1 or usernum3 == lotnum2 or usernum3 == lotnum3 )):
		return int(3)
	elif((usernum1 == lotnum1 or usernum1 == lotnum2 or usernum1 == lotnum3) and (usernum2 == lotnum1 or usernum2 == lotnum2 or usernum2 == lotnum3) or (usernum3 == lotnum1 or usernum3 == lotnum2 or usernum3 == lotnum3)):
		return int(2)
	elif((usernum2 == lotnum1 or usernum2 == lotnum2 or usernum2 == lotnum3) and (usernum3 == lotnum1 or usernum3 == lotnum2 or usernum3 == lotnum3)):
		return int(2)
	else:
		return int(0)		


#function to dole out the prize 
def assign_prize(winlevel):
	if(winlevel == 4):
		return 100000
	elif(winlevel == 3):
		return 10000
	elif(winlevel == 2):
		return 1000
	else:
		return 0

