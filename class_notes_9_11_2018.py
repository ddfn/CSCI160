#Andrew DeFran
#notes

def triathlon(run, bike, swim):
   	#function body

   	#local variables with restricted access
   	#variable scope
   	run_cal = run * 475
   	bike_cal = bike * 200
   	swim_cal = swim * 275
   	pounds = (run_cal + bike_cal + swim_cal ) / 3500

   	return pounds

#function call
r = int(input("Enter hours running:"))
b = int(input("Enter hours biking:"))
s = int(input("Enter hours swimming:"))
pounds_burned = triathlon(r, b, s)

print("You burned", pounds_burned, "pounds")

def car_speed(distance):
	from math import sqrt
	answer = sqrt(distance * 24)

	return answer

dis = int(input("Enter the distance: "))
speed = car_speed(dis)

print("The speed was", str(speed), "with a distance of", str(dis))

# electricity 


def electricity(hours):
	wattage = 100
	cost_cents = 1176
	hrs_used = hours

	cost = (wattage * hrs_used) / (1000 * cost_cents)
	return cost

#function call
hours = int(input("How many hours did you use the bulb: "))
time = electricity(hours)

print("the bulb costs $", time, ".")