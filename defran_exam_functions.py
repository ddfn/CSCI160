#Andrew DeFran
#CSCI 160
#10/11/2018
#Exam2

#Functions

#function for to calculate costs for residential customers
def calc_residential(channum):
	bill_process_fee = 4.50
	basic_service_fee = 20.50
	channel_cost = channum * 7.50
	total_res_cost = bill_process_fee + basic_service_fee + channel_cost

	return total_res_cost

def calc_business(basic, premium):
	bill_process_fee = 15.00
	
	if(basic <= 10):
		return bill_process_fee + 75 + (premium * 50)
	else:
		return bill_process_fee + 75 + ((basic - 10) * 5) + (premium * 50)

def is_valid(acttype):
	if(acttype == "B" or acttype == "b" or acttype == "R" or acttype == "r"):
		return True
	else:
		return False