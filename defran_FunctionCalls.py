#Andrew DeFran
#CSCI 160
#9/13/2018

#Welcome statement.
print(str.title("welcome to andrew deFran's lab 3 script. enjoy your stay!"))	

#Script to call the distance function

#import distance function from other script
from defran_Functions import distance

#ask for input and call the function.
x_1 = int(input("Give me a value for x1 (integer) :"))
y_1 = int(input("Give me a value for y1 (integer) :")) 
x_2 = int(input("Give me a value for x2 (integer) :")) 
y_2 = int(input("Give me a value for y2 (integer) :"))  

dist_points = distance(x_1, y_1, x_2, y_2)

#print output
print("The distance between", "(", x_1, ",", x_2, ") and", "(", y_1, ",", y_2, ")", "is:", dist_points, ".")

#task 3: call the circle function and print output

#import the circle area function.
from defran_Functions import circle_area

circ_area = circle_area(x_1, y_1, x_2, y_2)

#print output
print("The area of the circle is:", circ_area, ".")


#task 4: call shape functions and print output

#ask for input data for rectangle area function.
rec_length = int(input("Tell me the length of your rectangle: "))
rec_width = int(input("Tell me the width of your rectangle: "))

#import call function and print output.
from defran_Functions import rectangle_area
rect_area = rectangle_area(rec_length, rec_width)
print("The area of your rectangle is", rect_area, ".")

#use rectangle input for perimeter function.

#import call function and print output
from defran_Functions import rectangle_perimeter
rect_per = rectangle_perimeter(rec_length, rec_width)
print("The perimeter of your rectangle is:", rect_per, ".")

#ask for input data for the Triangle area function.
tri_base = int(input("Tell me the base of your triangle: "))
tri_height = int(input("Tell me the height of this triangle:"))

#import call function and print output
from defran_Functions import triangle_area
tri_area = triangle_area(tri_base, tri_height)
print("Your triangle has an area of", int(tri_area), ".")

#ask for input data for the Triangle perimeter function.
tri_side1 = int(input("Tell me a side length of your triangle: "))
tri_side2 = int(input("Tell me another side length of this triangle:"))
tri_side3 = int(input("Tell me another side length of this triangle:"))

#import call function and print output
from defran_Functions import triangle_perimeter
tri_per = triangle_perimeter(tri_side1, tri_side2, tri_side3)
print("Your triangle has an perimeter of", int(tri_per), ".")