#Andrew DeFran
#9/4/2018
# Change Calculator

print("Welcome to change calculator\n\n")

#Step 1: ask for the input
purchase = input("Enter purchase amount: $")
#convert input to float
purchase = float(purchase)
payment = input("Enter payment amount: $")
payment = float(payment)

#calculate change
change = payment - purchase
print("Change = $", round(change, 2))

#calculate exact change

#move the decimal point 2 places to the right
#convert dollars and cents to cents
change = int(round(change, 2) * 100)

dollars = change // 100
print(dollars, "dollars")

change =  change % 100
quarters = change // 25
print(quarters, "quarters")

change = change % 25
dimes = change // 10
print(dimes, "dimes")

change =  change % 10
nickels = change // 5 
print(nickels, "nickels")

change = change % 5
pennies = change // 1
print(pennies, "pennies")