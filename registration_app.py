from registration_functions import class_level

#grab input
cr = int(input("How many credits have you completed?"))
level = class_level(cr)
print("With", cr, "credits, you are a", level)