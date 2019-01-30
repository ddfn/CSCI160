#Andrew DeFran
#CSCI 160
#9/11/2018

#Functions homework

#population density problem: write a function that accepts population and land area and returns density

#define the function
def pop_density(population, area):
	pop = pop_in
	area = area_in

	pop_dens_calc = (pop / area)

	return pop_dens_calc


#function call and ask for inputs
pop_in = int(input("Enter the population: "))
area_in = int(input("Enter the area: "))
pop_dens = pop_density(pop_in, area_in)

#print statement
print("The population given your inputs is", pop_dens, ".")

#Average problem: have a function accept 3 numbers and average the result

#define a function.
def average(num1, num2, num3):
	num1 = num1_in
	num2 = num2_in
	num3 = num3_in

	result = (num1 + num2 + num3) / 3

	return result

#function call
num1_in = int(input("Give me a number: "))
num2_in = int(input("Give me another number: "))
num3_in = int(input("Give me another number: "))

average_num = average(num1_in, num2_in, num3_in)

#Print statement
print("The average of the numbers you entered is", average_num, "!")

#Heart rate problem: write a function that accepts age and resting heart rate and returns training heart rate.

#define function
def train_heart_rate(age, rest_heart_rate):
	max_heart_rate = 220 - your_age
	math_rate = (max_heart_rate - rest_heart) * 0.60
	THR = math_rate + rest_heart

	return THR

#function call and inputs.
your_age = int(input("Tell me your age: "))
rest_heart = int(input("Disclose your resting heart rate "))

train_hr = train_heart_rate(your_age, rest_heart)

#print output
print("Your training heart rate is", train_hr, ".")

#Body Mass Calc: write a function that calculates and returns the BMI

#define the function
def body_mass_index(weight, height):
	BMI = (weight_input * 703) / (height_input ** 2)

	return BMI

#function call and inputs
weight_input = int(input("Don't be shy, tell me your weight(pounds): "))
height_input = int(input("Additionally, tell me your height(inches): "))
bmi_calc = round(body_mass_index(weight_input, height_input), 2)

#print statement
print("Your body mass index measurment is", bmi_calc, ".")









