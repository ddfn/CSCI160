#Andrew DeFran
#CSCI 160
#9/20/2018
#Exam 1
#functions

#define functions using formulas and import necessary modules 
def sphere_volume(radius):
	from math import pi

	sphere_vol = (4 / 3) * pi * radius ** 3

	return sphere_vol

def cylinder_volume(radius, height):
	from math import pi

	cyl_volume = pi * (radius ** 2) * height

	return cyl_volume

def cylinder_surface_area(radius, height):
	from math import pi

	surface_area = (2 * pi * radius ** 2) + (2 * pi * radius) * height

	return surface_area

def ellipsoid_volume(radius1, radius2, radius3):
	from math import pi

	ellipsoid_vol = (4 / 3) * pi * (radius1 * radius2 * radius3)

	return ellipsoid_vol
