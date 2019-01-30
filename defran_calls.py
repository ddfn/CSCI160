#Andrew DeFran
#CSCI 160
#9/25/2018
#HW 4

#calls module

#cloudines problem
#ask fo input

c_cover = int(input("What percentage of cloud cover is there? "))

#import function
from defran_functions import cloudiness

#call the function and print result
clouds = cloudiness(c_cover)
print("At a percentage of" , c_cover, "% your daily forecast is", clouds, ".")


#library problem

#ask for input

c_number = int(input("Welcome to the library. Tell me the book call number: "))

#import function
from defran_functions import library_floors

#call function and print the result
call_number = library_floors(c_number)
print("Your book is located in the", call_number)

#IRS rewards problem and welcome
print("welcome to the death and taxes reward calculator you snitch")

#ask for input

c_IRS = int(input("What was the amount of money you recovered, you rat? $ "))

#import function
from defran_functions import irs_reward

#call function and print the result
recover = irs_reward(c_IRS)
print("With the amount recovered your reward is $", recover, "citizen.")
