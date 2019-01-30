#letter counter
def histogram():
	#create a blank dictionary
	hist = dict()
	#open file
	file = open("words.txt")
	#loop through the lines
	for line in file:
		#loop through the letters in the line
		for letter in line.strip():
			if(letter not in hist):
				hist[letter] = 1
			else:
				hist[letter] += 1
	return hist

def find_max(h):
	largest = 1
	k = ''
	for key in h:
		if(h[key] > largest):
			largest = h[key]
			k = key
	return [k,largest]

histo = histogram()
print("The length of the histogram is:", len(histo))
results = find_max(histo)
print("The letter", results[0], "occurs the most with", results[1], "occurences")
for key,val in histo.items():
    print(key, "\t=>\t", val)
	
	
	
	
