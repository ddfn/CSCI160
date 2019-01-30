#Andrew DeFran
#CSCI 160
#11/1/2018
#Exam 3

#task 1
#function definition
def hailstone(N):
	count = 1
	n_disp = 37
	print("hailstone sequence for:", N)

	while(N > 1):

		if(N % 2 == 0):
			N = N / 2
		elif(N % 2 != 0):
			N = (3 * N) + 1

		print(int(N), end=' ',)

		count += 1

	print("\nHailstone sequence for ", n_disp, "has", count, "elements")		

#modified function
def longest_hailstone(number):
	count = 1
	longest = -1
	
	
	#check numbers from 100k to 1
	while(number > 1):
		N = number
		#hailstone the range and count elements
		while(N > 1):

			if(N % 2 == 0):
				N = N / 2
			elif(N % 2 != 0):
				N = (3 * N) + 1

			
			count += 1
		elements = count	
			
		#check the count for which is larger
		if(elements > longest):
			longest = elements
			num_long = number 

			
		#decrement and check next number
		number -= 1
		count = 0
	
	print(num_long, "has the longest hailstone sequence with ", longest + 1, "elements.")
	
#display
N = 37

if(N > 0):
	hailstone(N)
else:
	print("Hailstone must begin with a positive number")

#task 2
#longest hailstone display

number = 100000
longest_hailstone(number)

