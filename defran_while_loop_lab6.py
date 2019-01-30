#Andrew DeFran
#CSCI160
#10/18/2018
#Lab 6- Loopty lab


#1-odd loop------------
print("\nProblem 1")
number = 0
while(number < 100):
	number += 1
	if(number % 2 != 0):
		print(number)

#2- start end loop---------
print("\nProblem 2")
def start_end_loop(num1, num2):
	if(num1 < num2):
		while(num1 < (num2 - 1)):
			num1 += 1
			print(num1)
	elif(num2 < num1):
		while(num2 < (num1 - 1)):
			num2 += 1
			print(num2)
	else:
		print("The numbers are equivalent!")		



num1 = int(input("gimme a number: "))
num2 = int(input("gimme another number: "))
start_end_loop(num1, num2)



#3-pattern loop--------
print("\nProblem 3")
n = 0
print(n)
while(n < 20):
	n += 1
	num = n ** 2
	print(num)


#4-Fib function--------
print("\nProblem 4")
def fib(num):
	if(num == 0 or num == 1):
		return 1
	
	return fib(num - 1) + fib(num - 2)

#ask for input
num = int(input("Give me an integer: "))

for i in range(1, num + 1):
	print(fib(i))


#5-random int-----------
print("\nProblem 5")
import random
def random_average():
	n = 0
	r = 0
	while(n <= 50):
		n += 1
		r += random.randint(1, 101)		
	return (round((r / n), 2))

print("The average of 50 random numbers is...")
print(random_average())		


#6-largest factor----------
print("\nProblem 6")
def largest_factor(num):
	n = 0
	big_boi = 0
	while(num >= n):
		n += 1
		num -= 1
		if(num % n == 0):
			#print(n)---so you can count the factors 
			big_boi = n
		 
	return big_boi
	if(big_boi == 1):
		return "Prime time baby!"
	

#Ask for input
num = int(input("Give me an integer puh-lease: "))
print("The largest factor of ", num, " besides your input is...")
print(largest_factor(num))


#7 number of factors----------
print("\nProblem 7")
def num_factor(num):
	n = 0
	factor_num = 0
	while(num >= n):
		n += 1
		if(num % n == 0):
			#print(n)---so you can count them yourself
			factor_num += 1
	return int(factor_num)			

#Ask for input
num = int(input("Give me yet another number: "))
print("The number of factors in", num, "is...")
print(num_factor(num))


#8 range loop
print("\nProblem 8")
def range():
	sentinel = -1
	start = 0
	num = int(input("Tell me a number (-1 to stop): "))
	smallest = num
	largest = num

	while(num != sentinel):
		if(num > largest):
			largest = num
		elif(num < smallest):
			smallest = num 

		num = int(input("Tell me a number (-1 to stop): "))
	
	return(largest - smallest)		

	
#Function call and print
print(range())



#9 number length-----------
print("\nProblem 9")
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
	
num = int(input("Enter a number yo: "))
print("that number has", number_length(num), "digit(s).")


#10 separate function---------
print("\nProblem 10")
def separate(num):
	exp = number_length(num) - 1
	summ = 0
	largest = -1 
	smallest = 10
	digit = 0 
	
	
	while(num > 1):
		digit = num // (10 ** exp)
		print(digit)
		summ += digit
		num = num % (10 ** exp)
		exp -= 1

		if(digit < smallest):
			smallest = digit
		elif(digit > largest):
			largest = digit

	print("sum is", summ)
	print("max is", largest)
	print("min is", smallest )


#ask for input eventually
#num = int(input("number please: "))
num = int(input("Enter a number and I'll separate: "))
separate(num)


#11 fizz buzz-------
print("\nProblem 11")
def fizz_buzz(fibz):
	counter = 0
	while(counter != fibz):
		counter += 1

		if(counter % 3 == 0 and counter % 5 == 0):
			print("FizzBuzz")
		elif(counter % 5 == 0):
			print("Buzz")
		elif(counter % 3 == 0):
			print("Fizz")
		else:
			print(counter)

#ask for input and call
fibz = int(input("Please give me one final number: "))
fizz_buzz(fibz)
