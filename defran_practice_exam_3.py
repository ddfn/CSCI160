#Andrew DeFran
#CSCI 160
#10/31/2018
#practice Exam 3


#number length function.
def number_length(num):
	base = 10
	exp = 0
	divisor = base ** exp
	if(num / divisor < 10):
		return exp + 1
	
	else:
		while(num / divisor >= 10):
			exp += 1
			divisor = base ** exp
		return exp + 1


#seperates the digits in an integer.
def separate(num):
	exp = number_length(num) - 1
	summ = 0
	digit = 0 
	
	
	while(num > 1):
		digit = num // (10 ** exp)
		print(digit)
		summ += digit
		num = num % (10 ** exp)
		exp -= 1

#num = int(input("Enter a number and I'll separate: "))
#separate(num)


#reverse function
def reverse(number):




"""
#Armstrong function
def armstrong(number):
	base = 10
	exp = number_length(number) - 1
	arm_number = 0


	
	


number = 1000
armstrong(number)	
"""