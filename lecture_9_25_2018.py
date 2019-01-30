#Andrew DeFran
#csci 160
#9/25/2018



"""
def luggage_charge(weight):
#decide whether or not to show the message

	if(weight >= 120):
		return("Sorry we can't take luggage that heavy.")

	elif(weight >= 50):
		return("There is an additional $25 charge for luggage over 50 pounds.")

	elif(weight >= 10):
		return("There is an additional $10 charge for luggage over 10 pounds.")

	else:
		return("There is no charge")

w = int(input("How heavy is your luggage?:"))

#call
answer = luggage_charge(w)
print(answer)
print("After Decision")"""
'''
def net_pay(rate, hours):
	if(hours > 60):
		ot_time = (hours-60)
		ot_pay = (2 * rate) * ot_hours
		net = ot_pay + (rate * 60)

		return net

	else:
		return hours * rate

h = int(input("Enter hours worked:"))
r = float(input("Enter pay rate: $"))

#call the function

pay = net_pay(h, r)
print("Your pay is: ", round(pay, 2))
'''
"""
def number_type(number):
	if(number > 0):
		return ("The number is positive")
	elif(number < 0):
		return ("Negative!")
	else:
		return ("I think it's zero?")

#input
numb = int(input("What's your number? "))

#call
numb_call = number_type(numb)
print(numb_call)
"""

'''
def flip():
	import random
	coin_toss = random.randrange(2)
	if(coin_toss == 1):
		return ("heads")
	else:
		return ("Tails")


toss = flip()
print("The coin landed on" , toss)
'''
'''
def even_odd(n):
'''

#long exercise



