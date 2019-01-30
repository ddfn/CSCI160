#Andrew DeFran
#CSCI 160
#9/20/2018
#exam 1
#function calls

#welcome statement
print("Welcome to my first programming exam! :please clap: ")

#sphere volume problem
#ask for input

sphere_radius = (int(input("Ok first, tell me the radius of a sphere: ")))

#call the function
from defran_ExamOne_functions import sphere_volume

sphere_volu = sphere_volume(sphere_radius)

#print output
print("The volume of a sphere with a radius of ", sphere_radius, "is", round(sphere_volu, 2), ".")

#cylinder volume problem
#ask for input

cylinder_radius = (int(input("Hahah! now for my next trick.  Tell me the radius of a cylinder!: ")))
cylinder_height = (int(input("and tell me the height of this cylinder: ")))

#call the function
from defran_ExamOne_functions import cylinder_volume

cylinder_volu = cylinder_volume(cylinder_radius, cylinder_height)

#print output
print("The volume of a cylinder with a radius of", cylinder_radius, "and a height of", cylinder_height, "is", round(cylinder_volu, 2), "!")

#cylinder surface area problem
#inputs exist so call the function
from defran_ExamOne_functions import cylinder_surface_area

cylinder_surf = cylinder_surface_area(cylinder_radius, cylinder_height)

#print output
print("Oh by the way, the surface area of that cylinder with a radius of", cylinder_radius, "and and height of", cylinder_height, "is", round(cylinder_surf, 2), ".")

#ellipsoid volume problem
#ask for input
radius1 = (int(input("Give me a radius length: ")))
radius2 = (int(input("And another: ")))
radius3 = (int(input("And another: ")))

#import and call
from defran_ExamOne_functions import ellipsoid_volume

ellipsoid_vol = ellipsoid_volume(radius1, radius2, radius3)

#print output
print("Finally, the volume of an ellipsoid with radii", radius1, radius2, "and", radius3, "is", round(ellipsoid_vol, 2), ".")

print("That's our show folks! so long, farewell, until we meet again. Adios, Au Revoir, until we meet again...")