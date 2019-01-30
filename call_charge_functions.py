#Andrew DeFran
#CSCI 160
#9/30/2018
#Lab 4

#Define all relevant module level variables here
min_before_tax_short = 59.40
min_before_tax_long = 89.00

per_second_short = 0.759
per_second_long = 1.761




VAT = 0.14



#===========================================================#
#============ Begin Function Definitions ===================#
#===========================================================#

def basic_charge(Call_duration_time, distance):
	'''
	This function will calculate the basic (pre-discount and tax)
	charge of the phone call. 

	returns: float => the basic charge of a call

	
	param name: distance
	param type: int
	'''
	# Your code begins here:
	if(int(distance) <= 50):
		basic_charge_short = min_before_tax_short + (Call_duration_time * per_second_short)
		return basic_charge_short
	else:
		basic_charge_long = min_before_tax_long + (Call_duration_time * per_second_long)
		return basic_charge_long


def off_peak_discount(distance, call_start_time, basic_charge):
	'''
	This function will calculate the discount for calls
	beginning during off-peak times. 
	Discount will be calculated from the basic_charge

	The distance of the call must be factored in

	returns: 		float => the discount amount

	param name: 	distance
	param type: 	int
	description:	the call distance in miles 

	param name: 	basic_charge
	param type: 	float
	description:	the basic charge of the call'''

	if(call_start_time >= 0 and call_start_time < 25200): #midnight to 65959
		if(int(distance) <= 50):		
			return basic_charge * .40
		else:
			return basic_charge * .50
	elif(call_start_time >= 68400 and call_start_time < 86401): #19-midnight
		if(int(distance) <= 50):		
			return basic_charge * .40
		else:
			return basic_charge * .50
	else:
		return 0

def conference_call_discount(distance, basic_charge):
	'''
	This function will calculate the discount for conference calls
	This discount is applied AFTER any off-peak discount.
	The distance of the call must be factored in

	returns: float => the discount amount

	param name: distance
	param type: int 
	param name: basic_charge
	param type: float
	'''
	# Your code begins here:
	if(int(distance) > 50):
		confer_discount = (basic_charge - (basic_charge * .50)) * .50 #discount only applies to long distance
		return confer_discount
	else:
		return 0


def vat(net_charge):
	'''
	This function will calculate the amount of value added tax
	The tax amount will be calculated from the net charge
	After any discounts have been applied

	returns: 		float => tax amount

	param name: 	net_charge
	param type: 	float
	description: 	the call charge after any discounts
	'''
	# Your code begins here:
	Vat = net_charge * 0.14
	return Vat


def final_charge(net_charge, vat):
	'''
	This function will calculate the amount of the final charge

	returns: 		float => final charge

	param name: 	net_charge
	param type: 	float
	description:	the call charge after any discounts

	param name: 	vat
	param type: 	float
	description:	the value added tax amount	
	'''
	# Your code begins here:
	final_c = net_charge + vat
	return final_c