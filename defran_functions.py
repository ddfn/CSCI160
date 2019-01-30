#Andrew DeFran
#CSCI 160
#9/25/2018
#HW 4

#functions module

#cloud cover function
def cloudiness(cover):
	if(cover <= 30):
		return "Clear"
	elif(cover <= 70):
		return "Partly Cloudy"
	elif(cover <= 99):
		return "Cloudy"
	elif(cover == 100):
		return "overcast"
	else:
		return "ERROR: C'mon man, more than 100%? What are you my football coach?"

#Library function

def library_floors(callnumber):
	if(callnumber in range(100, 200)):
		return "Basement"
	elif(callnumber in range(200, 501) or callnumber >= 900):
		return "Main Floor"
	elif(callnumber in range(501, 700) or callnumber in range(751, 901)):
		return "Upper Floor"
	elif(callnumber in range(700, 751)):
		return "Archives"
	else:
		return "ERROR: Thank you Mario, but your princess is in another castle."


#IRS Function
def irs_reward(money):
	if(money >= 4225000):
		reward1 = (75000 * 0.1)
		reward2 = (25000 * 0.05)
		reward3 = (50000 - reward1 - reward2)
		return reward1 + reward2 + reward3

	elif(money <= 75000):
		return (money * 0.1)

	elif(money <= 100000):
		reward1 = (75000 * 0.1)
		reward2 = (25000 * 0.05)
		total1 = reward1 + ((money-75000) * 0.05) 
		return total1

	elif(money < 4225000):
		reward1 = (75000 * 0.1)
		reward2 = (25000 * 0.05)
		total2 = reward1 + reward2 + ((money - 100000)* 0.01)
		return total2

	else:
		return "no reward"




