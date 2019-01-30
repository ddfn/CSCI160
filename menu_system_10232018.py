#Andrew DeFran
#menu systmem template

def function():
	#define solutions to 
	#single problem here
	print("\ninside function 1\n")

def function2():
	#define solutions to 
	#single problem here
	print("\ninside function 2\n")

def show_menu():
	print("\n1) Print All Primes up to N")
	print("2) problem two")
	print("3) exit program\n")

def print_all_primes_up_to_N(N):
	for number in range(1, N + 1):
		if(is_prime(number) == True):
			print(number, "is prime")



def is_prime(N):
	divisor = 2
	if(N == 1):
		return True
	while(N % divisor != 0):
		divisor += 1
	if(divisor == N):
		return True
	else:
		return False	


#define choice
choice = 0

while(choice != 3):
	choice = int(input("Enter 1, 2, or 3: "))
	show_menu()
	if(choice == 1):
		N = int(input("Enter a value for N: "))
		print_all_primes_up_to_N(N)
	elif(choice == 2):
		function2()
	elif(choice == 3):
		print("Good bye!")
	else:
		print("ID10T error")