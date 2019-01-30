#Andrew DeFran
#CSCI 160
#9/6/2018
#Projectile motion, 100 years old, and Digital Sum.

#initial problem calculation
start_velocity = 50
start_height = 5
time = 3

#height_at_time = (-16) * (time ** 2) + (start_velocity * time) + start_height <-----the original alg

#ask the nice people for starting velocity and height
start_velocity = int(input("Please enter a starting velocity: "))
start_height = int(input("Please enter a starting height: "))

#calculate given inputs
height_at_time = (-16) * (time ** 2) + (start_velocity * time) + start_height

#print output given the new inputs
print("The height at 3 seconds given your input is ", height_at_time, "feet.")

#100 years problem
#ask for name and age
name = input("What's your name? Who's your daddy? Actually just your name is fine: ")
age = (int(input("Please enter your current age: ")))
year = 2018

#algo to find year given age 100
year_at_100 = year + (100 - age)

#ouput
print("Hey", name, "when you are 100 years old, the year will be", year_at_100, ".")

#Passcode problem
#ask for a 4 digit number
code = (input("Tell me your most embarrasing pin number (4 digits): "))

#make a list of integers
code_list = (list(code))
code_list_int = [int(i) for i in code_list]

#print each item in the list
for item in code_list_int:
	print(item)

#sum and print the list
print("The sum total of", code_list_int, "is", sum(code_list_int), ".")

#Passcode problem alternate modulus division method
pcode = int(input("Enter another random 4 digit number: "))

#divide by units, mod remainder, and print sequentially.
thousands = pcode // 1000
print(thousands)
pcode = pcode % 1000

hundreds = pcode // 100
print(hundreds)
pcode = pcode % 100

tens = pcode // 10
print(tens)
pcode = pcode % 10

ones = pcode // 1
print(ones)


#Sum the numbers entered.
print(str(thousands), "+", str(hundreds), "+", str(tens), "+", str(ones), "=",thousands + hundreds + tens + ones)
