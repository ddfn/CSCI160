#Andrew DeFran
#csci 160 
#practice exam 2

#app

#ask for input

side1 = int(input("give me a side length of the triangle: "))
side2 = int(input("given me another side length: "))
side3 = int(input("Please give me another side length: "))



#call is function and see if it's a triangle
from defran_practiceexam2_functions import is_triangle
triangle = is_triangle(side1, side2, side3)
print(triangle)

#call triangle type
from defran_practiceexam2_functions import triangle_type
tri_type = triangle_type(side1, side2, side3)
print(tri_type)

#pythagorean function call
from defran_practiceexam2_functions import pythagorean_triple
pythag = pythagorean_triple(side1, side2, side3)

#herons area function call
from defran_practiceexam2_functions import herons_area
h_area = herons_area(side1, side2, side3)
print(h_area)
