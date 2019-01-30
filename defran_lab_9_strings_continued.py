#Andrew DeFran
#CSCI 160
#11/16/2018

#Lab 9

#Task One
def monetize(number):
	#string it and set length
	numb_string = str(number)
	comma_string = ""
	decimal_index = 0

	#decimal check
	if("." in numb_string and numb_string[-2] == "."):
		numb_string = numb_string + "0"

	elif("." not in numb_string):
		numb_string = numb_string + ".00"
	

	#decimal index logic
	for i in range(0, len(numb_string)):
		if(numb_string[i] == "."):
			decimal_index = i

	
	#decimal_index = numb_string.find(".")-->cheaters way
	decimal_suffix = numb_string[-3:]
	
	#add commas
	counter = 0
	for i in range(decimal_index - 1, -1, -1):
		#comma insert
		if(counter == 3):
			comma_string += "," 
			counter = 0
		comma_string += numb_string[i]
		counter += 1

			
	#reverse and concatenate decimal suffix
	comma_string = comma_string[::-1] + decimal_suffix

	#add dollar sign
	money_string = "$" + comma_string

	return money_string	

#input/ouput
#number = input("Enter a number to monetize: ")
#print(monetize(number))



#Task Two
def demonetize(string):
	#string it
	demon_string = str(string)
	new_demon_string = ""

	#remove dollar sign
	demon_string = demon_string[1:]


	#make a new string w/o commas
	for i in range(0, len(demon_string)):
		if(demon_string[i] != ","):
			new_demon_string += demon_string[i]

	#knock out the last zero
	if(new_demon_string[-1] == "0"):
		new_demon_string = new_demon_string[:-1]

	return new_demon_string


#string = input("Enter an amount to demonetize: ")
#print(demonetize(string))	


#Task Three
def generate_password(string):
	string = str(string)
	start_index = string[0]
	pword_string = ""
	
	for i in range(0, len(string)):
		if(string[i] == " "):
			pword_string += string[i + 1]

	return start_index + pword_string		


#function test	
#string = "NUT TOKYO xbox $ xbox 7 fruit TOKYO"


#open file
data = open('hints.txt', 'r')

#loop through lines
count = 0
for line in data:
	string = line
	print(generate_password(string))
	count += 1

print("count is: ", count)





