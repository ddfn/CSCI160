#Andrew DeFran
#csci 160 
#practice exam 2

#functions

#input validity test
def is_valid(s1, s2, s3):
	if(s1, s2, s3 > 0):
		return True
	else:
		return False

#function to test whether it's a triangle
def is_triangle(s1,s2,s3):
	if(s1 < (s2 + s3) and (s2 < (s1 + s3)) and (s3 < (s1 + s2))):
		return True
	else:
		return False

#Function to tell what type of triangle
def triangle_type(s1, s2, s3):
	if(s1 == s2 and s1 == s3 and s2 == s3):
		return "Triangle is equitlateral"
	elif(s1 == s2 or s1 == s3 or s2 == s3):
		return "Triangle is isoscoles"
	else:
		return False

#function for pythagorean triple
def pythagorean_triple(s1, s2, s3):
	if(s2 ** 2 + s3 ** 2 == s1 ** 2):
		return True
	elif(s1 ** 2 + s3 ** 2 == s2 ** 2):
		return True
	elif(s1 ** 2 + s2 ** 2 == s3 ** 2):
		return True
	else:
		return False

#area function
def herons_area(s1, s2, s3):
	from math import sqrt
	ess = (s1 + s2 + s3) / 2
	area = sqrt(ess * (ess - s1) * (ess - s2) * (ess - s3))
	return int(area)
