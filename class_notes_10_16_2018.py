#Andrew DeFran
#CSCI 160
#10/16/2018

#loops notes

#display the numbers 1-10
def display_1_to_10():
	#counting loop
	counter = 1
	while(counter <= 10):
		print("loop number: ", counter)
		counter += 1
	print("counter finished at: ", counter)


#display_1_to_10()
import time
def countdown():
	counter = 10
	print("T-minus")
	while(counter >= 1):
		print(counter)
		counter -= 1
		time.sleep(1)
	print("blastoff!")

#countdown()

def validate10():
	#user must enter a number 
	#between 1-100 inclusive
	#give infinite chances
	numChances = 1
	entry = int(input("Enter a number between 1-100: "))
	while(entry < 1 or entry > 100 and numChances < 5):
		print("ID10T Error")
		entry = int(input("Enter a number between 1-100: "))
		numChances += 1
	if(numChances == 1):
		print("congrats you got it on the first try")
	elif(numChances == 5):
		print("release the hounds!! You are locked out")
	else:
		print("It took you", numChances, "attempts")

#validate10()

def sentinel_loop():
	sentinel = -1
	numGrades = 0
	summ = 0
	grade = float(input("Enter grade (-1 to stop): "))
	while(grade != sentinel):
		#add grade to summ
		summ += grade
		numGrades += 1
		grade = float(input("Enter grade (-1 to stop): "))

	#calc the average
	if(numGrades > 0):
		return summ / numGrades
	else:
		return 0
#print("The average grade is: ", sentinel_loop())


def is_prime(N):
	divisor = 2
	while(N % divisor != 0 and divisor < N):
		divisor += 1
	if(divisor == N):
		return True
	else:
		return False

n = 17
print("is", n, "prime? ", is_prime(n))







