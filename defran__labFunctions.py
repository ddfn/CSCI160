#Andrew DeFran
#CSCI 160
#9/13/2018


#define a function that calculates distance between two points.
def distance(x1, y1, x2, y2):
	from math import sqrt
	d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	return d

#define a function that calculates the area of a circle using the distance function.
def circle_area(x1, y1, x2, y2):
	from math import pi
	radius = distance(x1, y1, x2, y2)
	area = pi * radius ** 2

	return area 

#define a function that calculates the area of a rectangle.
def rectangle_area(length, width):
	rec_area = length * width

	return rec_area

#define a function that calculates the perimeter of a rectangle.
def rectangle_perimeter(l1, w1):
	rec_peri = (l1 * 2) + (w1 * 2) 

	return rec_peri

#define a function that calculates the area of a triangle.
def triangle_area(base, height):
	tri_area = 0.5 * base * height

	return tri_area

#define a function that calculates the perimeter of a triangle.
def triangle_perimeter(side1, side2, side3):
	tri_peri = side1 + side2 + side3

	return tri_peri