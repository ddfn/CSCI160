#Andrew DeFran
#CSCI 160
#HW number 5
#10/16/2018


#restitution problem
def restitution(coef, height):
	bounces = 0
	while(height >= 10):
		height = height - (height * coef)
		#print(height, "Centimeters")
		bounces += 1

	return bounces

coef = .5
height = 1500
print("The ball used has a coefficient of", coef, "and when dropped from a height of", height, "cms, bounced", restitution(coef, height), "times.")


#population problem
def population():
	year = 1959
	pop = 3000000000
	while(pop > 6000000):
		pop = pop - (pop / 2)
		year = year - 40
	return year

print("The last year the world population was under 6 million was", population(), "." )


#cobalt problem
def cobalt60(weight):
	year = 0
	while(year <= 5):
		weight = weight * .88
		#print(round(weight, 2))
		year += 1
	return weight

weight = 100
print("After five years,", weight, "grams of Cobalt 60 will be", round(cobalt60(weight), 2), "grams." )




