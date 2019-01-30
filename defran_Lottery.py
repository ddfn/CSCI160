#Andrew DeFran
#CSCI 160
#10/20/2018

#lottery inputs, function calls and outputs

#Welcome statement
print("Welcome to my Lottery Game! ")

#ask for inputs

pick1 = int(input("Please enter a number between 1 and 100: "))
pick2 = int(input("Please pick another number between 1 and 100: "))
pick3 = int(input("Please pick your final number between 1 and 100: "))

#display
print("You picked", pick1, ",", pick2, ", and", pick3, ".")
  
#validity check
#import and call function
from defran_Lottery_functions import is_valid
valid = is_valid(pick1, pick2, pick3)

if(valid == True):

	#import the lottery number generator from module
	from defran_Lottery_functions import gimme_3_unique_random


	q = 3 	# gimme 3
	s = 1 	# lower boundary
	e = 100	# upper boundary
	# call the function and store the results
	nums = gimme_3_unique_random(s, e, q)
	# display the answer
	 
	# extract the 3 numbers for use
	num1 = nums.pop()
	num2 = nums.pop()
	num3 = nums.pop()

	print("Here are your 3 unique lottery numbers\nnum1 =", num1, "\nnum2 =", num2, "\nnum3 =", num3)

	#check win function call
	from defran_Lottery_functions import check_win
	from defran_Lottery_functions import assign_prize
	win_level = check_win(pick1, pick2, pick3, num1, num2, num3)

	result = assign_prize(win_level)
	
	if(win_level >= 1):
		print("Your winnings total $", result, "drachmas! Don't spread all of that cheddar on one cracker!")
	else:
		print("You get nothing! You Lose! Good Day sir!")
else:
	print("Invalid inputs: reinitialize and please select new numbers.")