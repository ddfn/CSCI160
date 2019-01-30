#Andrew DeFran
#9/4/2018
#HW two

#Triathlon problem

print("Welcome to your triathlon log!")

#define activity variable calorie amounts
cyc = 200
run = 475
swim = 275

#ask for hours for each activity and convert to int

total_cyc_cals = (int(input("How many hours spent cycling? ")) * cyc)
total_run_cals = (int(input("How many hours spent running? ")) * run)
total_swim_cals = (int(input("How many hours spent swimming? ")) * swim)


#total cals expressed in pound burnt
pound_cals = (1 / 3500)
melt_pounds = ((total_cyc_cals + total_run_cals + total_swim_cals) * pound_cals)
#output
print("Congratulations Iron Man, you shed ", round(melt_pounds, 1), "pounds!")

#Car speed problem

print("Welcome to the faster and more furiouser problem!")
#import math package
import math 
#define variables and ask for input

skid_dist = (int(input("Hey Tokyo drifter, how many feet did you skid? ")))

#calc car speed
car_speed = math.sqrt(24 * skid_dist)
#output
print("Vin Diesal over here was estimated going", round(car_speed), "MPH.")

#Electricity problem
print("How much will this 100 watt bulb cost for x hours?")

#define variables
bulb_watt = 100
kwh_cost_cents = 1176

#ask for # of hours input
hours_used = int(input("How many hours was the bulb in use? "))

#calculate the cost
cost = (bulb_watt * hours_used) / (1000 * kwh_cost_cents)

#convert cost back to dollars
dollar_cost = cost * 100

#output
print("If you use the bulb for", hours_used, "hours, then the cost will be $", float(dollar_cost), ".")



