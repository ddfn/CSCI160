#Andrew DeFran
#csci 160
#9/18/2018

#call statements and outputs

#welcome statement
print("Hello and welcome to your payment calculator.")

#ask for inputs
hours = float(input("How many hours did you work? "))
payrate = float(input("And how many dollars do you earn per hour? $ "))

#function call and output statements
#import and call gross pay
from defran_practiceexam1_functions import gross_pay

grossypay = gross_pay(hours, payrate)

#print gross pay statement
print("The gross pay for working", hours, "hours", "at $", payrate, "per hour is $", round(grossypay, 2))

#import and call net pay
from defran_practiceexam1_functions import net_pay


netty_pay = net_pay(grossypay)

#print net pay statement
print("The after tax net pay is $", netty_pay, "." )