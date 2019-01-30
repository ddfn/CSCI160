#Andrew DeFran
#CSCI 160
#10/23/2018
#HW 6



#define and call menu function
def show_menu():
	print("1) Rule of 72 problem.")
	print("2) Ball Height")
	print("3) exit program?")

#show_menu()


def rule_72():
	money = 1
	r = 0
	rul_72 = 0
	money_count = 0
	
	while(r <= 20):

		r += 1
		rul_72 = 72 / r

		while(money <= 2):
			money = money * (1 + r /100)
			money_count += 1

		print(r, round(rul_72, 1), round(money_count, 1))
	
		money = 1
		money_count = 0	
	

	
def ball_max_height(height, velocity):
	time = velocity / 32
	max_height = height + (velocity * time) - (16 * time ** 2)

	print("Max height is", round(max_height, 2), "feet")

#ball_max_height(10, 10)


def ball_hit_ground(height, velocity):
	#ask for time
	time = 0

	while(height > 0):
		time += 0.1

		height_at_t = height + (velocity * time) - (16 * time ** 2)
		print(round(height_at_t, 2), "feet")

		height = height_at_t

	print("The ball hits the ground at appx.", round(time, 2), "seconds")


#ball_hit_ground(10, 10)

def ball_height_table(height, velocity):
	time = 0
		
	while(height > 0 and time < 5):
		time += 0.25

		height_at_t = height + (velocity * time) - (16 * time ** 2)
		print(round(height_at_t, 2), "feet,", time, "seconds")

		height = height_at_t

#ball_height_table(10, 10)



#welcome statement and menu

choice = 0

while(choice != 3):
	print("\nHello and welcom to HW 6\n")
	show_menu()
	choice = int(input("\nPlease enter 1, 2, or 3: "))
	
	if(choice == 1):	
		#print rule_72
		print(rule_72())

	elif(choice == 2):
		#ask for height, velocity and an output option
		height = int(input("please enter the starting height: "))
		velocity = int(input("Please enter the starting velocity: "))
		output = int(input("Enter an output option (1, 2 or 3, -1 to cancel): "))
		

		while(output != -1):
			
			if(output == 1):
				
				ball_max_height(height, velocity)

			elif(output == 2):
				
				ball_hit_ground(height, velocity)

			elif(output == 3):
				
				ball_height_table(height, velocity)

			else:
				print("Invalid output selected")

			output = int(input("Enter an output option (1, 2 or 3, -1 to cancel): "))

	elif(choice == 3):
		print("Good bye!")
	else:
		print("input error, try again")

	
	


