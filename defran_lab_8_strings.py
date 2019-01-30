#Andrew DeFran
#csci 160
#11/11/2018

#Lab 8

#1-in function
def is_in(string, char):
	s_normed = string.lower()
	c_normed = char.lower()
	length = len(s_normed)
	included = False

	for i in range(0, length):
		#character check	
		if(c_normed == s_normed[i]):
			included = True

	return included


#input/output
"""
string = input(str("Please enter a string: "))
char = input(str("please pick a character to check if it's in the string: "))

if(is_in(string, char) == True):
	print(is_in(string, char), "....", char, "is in the string:", string)
elif(is_in(string, char) == False):
	print(is_in(string, char), ".....", char, "is NOT in the string:", string)
"""

#2-traversal function---unfinished
def traverse_for(string):
	#get rid of spaces
	smoosh = string.replace(" ", "")
	new_string = ""
	counter = 0


	#loop over index
	for i in range(0, len(smoosh)):
		new_string += smoosh[i]
		counter += 1
		if(counter == 5):
			new_string += "\n"
			counter = 0
		else:
			new_string += "-"
	return new_string


#input/output
#string = str("The quick brown fox jumps over the lazy dog")
#print(traverse_for(string))


#3-vowel function
def is_vowel(char):
	vowels = "aeiouyAEIOUY"

	if(is_in(vowels, char) == True):
		return True
	else:
		return False

#input/output
#char = input(str("Enter a character: "))
#print(is_vowel(char))



#4-count the vowels function
def count_vowels(string):
	counter = 0

	for i in range(0, len(string)):
		if(is_vowel(string[i]) == True):
			counter += 1
	return counter		


#input/ouput
#v_count = input(str("Please enter a string: "))
#print("There are", count_vowels(v_count), "Vowels in that string.")


#5-count letters function
def count_letter_occurences(string, char):
	normed = string.lower()
	length = len(normed)
	counter = 0

	for i in range(0, length):
		#character check	
		if(char == normed[i]):
			counter += 1
	return counter 


#input/output
#string = input(str("Please enter a string: "))
#char = input(str("please enter a letter to test: "))
#print("The letter appears", count_letter_occurences(string, char), "times.")


#6-date conversion string-unfinished
def date_convert(date):
	month = date[:2]

	if(month == "01"):
		month = "January"
	elif(month == "02"):
		month = "February"
	elif(month == "03"):
		month = "March"
	elif(month == "04"):
		month = "April"
	elif(month == "05"):
		month = "May"
	elif(month =="06"):
		month = "June"
	elif(month == "07"):
		month = "July"
	elif(month == "08"):
		month = "August"
	elif(month == "09"):
		month = "September"
	elif(month == "10"):
		month = "October"
	elif(month == "11"):
		month = "November"
	elif(month == "12"):
		month = "December"

	
	new_date = month + date[2:]
	
	year = new_date[-4:]
	day = new_date[-7:-5]

	print(month, day + ",", year)
		


#input/output
date = input(str("Please give me a date in mm/dd/yyyy format: "))
date_convert(date)



#7-valid email function
def is_valid_email(email):
	email = email.lower()
	at = chr(64)

	for i in range(0, len(email)):
		if(at in email and email[-4:] == ".com" or email[-4:] == ".net" or email[-4:] == ".edu" or email[-4:] == ".gov"):
			return True
		else:
			return False


#input/ouput
#email = input(str("Enter an email address: "))
#print(is_valid_email(email))


#8-remove vowels function
def remove_vowels(string):
	vowels = "aeiouy"

	for i in string.lower():
		if i in vowels:
			string = string.replace(i, "")

	return string

#input/output
#v_remove = input(str("Enter a string: "))
#print(remove_vowels(v_remove))
		
	
