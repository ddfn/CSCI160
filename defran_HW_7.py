#Andrew Defran
#csci 160
#11/09/2018

#HW 7

#function definitions

#reverse function
def reverse(string):
	n = len(string)
	x = ""
	
	for i in range(1, n + 1):
		x += string[n - i]
	return x


#palindrome function
def is_palindrome(string):
	pal_phrase = string

	#lower case it to standardize
	pal_phrase = pal_phrase.lower()

	#reverse it
	rev_pal_phrase = reverse(pal_phrase)

	#check if equal
	if(pal_phrase == rev_pal_phrase):
		return True
	else:
		return False


#3rd person 
def make_3sg_form(verb):
	word = verb
	last = verb[-1]

	if(last == "y"):
		y_suffix = "ies"
		new_word = word[:-1] + y_suffix
		return new_word

	elif(last == "h" and verb[-2] == "c" or verb[-2] == "s"):
		ch_sh_suffix = "es"
		new_word = word + ch_sh_suffix
		return new_word

	elif(last == "o" or last == "s" or last == "x" or last == "z"):
		con_suffix = "es"
		new_word = word + con_suffix
		return new_word

	else:
		suffix = "s"
		new_word = word + suffix
		return new_word


#welcome and menu input

print("\nWelcome to homework 7.\n")


option = 0

while(option != 4):
	#ask for input
	option = input(str("\npick an option: \n"
					   "Option 1: reverse a string\n"
					   "Option 2: Do we have a palindrome\n"
					   "Option 3: 3rd person singularize a verb\n"
					   "Option 4: Exit program. "))

	option = int(option)

	if(option == 1):
		#input for reverse function"
		rev_input = input(str("Enter a string and I'll put the thing down flip it and reverse it: "))
		print(reverse(rev_input))

	elif(option == 2):
		#input for palindrome test
		pal_input = input(str("Enter a string you'd like to test for palindrome: "))
		print(is_palindrome(pal_input))
	
	elif(option == 3):
		#input for 3rd person function
		third_input = input(str("Enter a verb: "))
		print(make_3sg_form(third_input))


print("Program Terminated. Thank You!")









