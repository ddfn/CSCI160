#Andrew DeFran
#csci 160
#class notes

"""
schoolName = "Washington-Lee H.S."




#loop through variable
for character in schoolName:
	if(character.isalpha() == True):
		print(character)

#print an alphabet
alphabet = ""
for ASCII in range(ord("A"), ord("A") + 26):
	alphabet += chr(ASCII)
print(alphabet)

#loop through school name with while-loop
index = 0
while(index < len(schoolName)):
	print(schoolName[index])
	index += 1


for index in range(0, len(schoolName)):
	if(schoolName[index].isalpha()):
		print(schoolName[index])
"""


#pig latin
def is_vowel(letter):
	vowels = "AEIOU"
	if(letter.upper() in vowels):
		return True
	else:
		return False

def consonant_prefix_length(word):
	con_count = 0
	for letter in word:
		if(not is_vowel(letter)):
			con_count += 1
		else:
			return con_count


def pig_latinize(word):
	if(is_vowel(word[0])):
		#concatenate way to the end
		return word + "way"
	else:
		#find the first vowel
		prefix_count = consonant_prefix_length(word)
		print("There are", prefix_count, "consanantes at the beginning")
		return word[prefix_count:] + word[:prefix_count] + "ay"
		




w = input("Enter a word to pig latinze: ")
p = pig_latinize(w)
print(p)

