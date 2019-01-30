#Andrew DeFran
#CSCI 160
#10/11/2018
#Exam2

#App

#Welcome statement
print("Welcome to the TV bill calculator!")

#ask for inputs
actnum = str(input("Please enter your 4 digit account number: "))
acttype = str(input("is this for a business or residential account? (type b or r): "))

#validity check
from defran_exam_functions import is_valid
isvalid = is_valid(acttype)
if(isvalid == True):
	if(acttype == "R" or acttype == "r"):
		#ask for channel input
		channum = int(input("How many channels do you want? "))

		#call residential function
		from defran_exam_functions import calc_residential
		res_calc = calc_residential(channum)
		print("Dear customer #" + actnum, ", your bill comes to $", round(res_calc, 2), ".")

	elif(acttype == "B" or acttype == "b"):
		#ask for connections
		connections = int(input("How many connections do you want? "))
		#ask for channels
		premium = int(input("How many channels do you want? "))

		#call function
		from defran_exam_functions import calc_business
		bus_calc = calc_business(connections, premium)
		print("Dear customer #" + actnum, ", your bill comes to $", round(bus_calc, 2), ".")

else:
	print("ERROR: invalid account type. Try again.")

