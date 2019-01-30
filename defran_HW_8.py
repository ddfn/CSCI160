#Andrew DeFran
#CSCI 160
#11/27/2018

#HW 8

#function definitions

#1 member function
def is_member(value, lst):
	#traverse
	for i in range(0, len(lst)):
		if(lst[i] == value):
			return True

	return False

#member function test data
#x = 5
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#call
#print("It is", is_member(x, a), "that the value of x is in list a")


#2 overlapping function
def overlapping(lst1, lst2):
	lst3 = lst1 + lst2
	
	count = 0
	#traverse
	for i in range(0, len(lst3)):
		if(lst3[i] in lst1 and lst3[i] in lst2):
			count += 1
			
	return count > 1
	

#overlapping function test data
#lst1 = [1, 11, 12, 13, 14, 15]
#lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
#call function
#print("it is", overlapping(lst1, lst2), "that the two lists overlap.")

#3 remove duplicates
def remove_doops(lst):
	new_lst = []
	new_lst.append(lst[0])

	for i in lst:
		if(is_member(i, new_lst) == False):
				new_lst.append(i)

	return new_lst

#dupes test data
lst = [1, 2, 2, 3, 4, 5]
#call
#print("your new list without dupes is", remove_doops(lst), ".")


#4 intersection function
def intersection(lst1, lst2):
	new_lst = []
	
	for i in lst1:
		if(is_member(i, lst2) == True):
			new_lst.append(i)

	return new_lst


#test intersection data
lst1 = [1, 2, 3, 10, 11, 12]
lst2 = [1, 2, 3, 20, 21, 22]
#call
#print("Here is your new list of common elements ", intersection(lst1, lst2))

#5 complement function
def complement(lsta, lstb):
	new_lst = []
	
	for i in lstb:
		if(is_member(i, lsta) == False):
			new_lst.append(i)

	return new_lst

#test complement data
lsta = [1, 2, 3, 10, 11, 12]
lstb = [1, 2, 3, 20, 21, 22]
#call
#print("items in list b that are NOT in a are:", complement(lsta, lstb))

#menu logic

#welcome
print("Welcome to Drew's HW# 8\n")

#menu loop
option = 0
while(option != 6):
	#input
	option = int(input("Please input an option from the menu\n\n"
				   "Option 1: Members Club?\n"
				   "Option 2: Do Lists Overlap?\n"
				   "Option 3: Remove tha doops?\n"
				   "Option 4: let's find the intersection?\n"
				   "Option 5: Complement Me?\n"
				   "Option 6: Dammit all and quit: "))
	
	if(option == 1):
		x = 5
		a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		
		print("\nIt is", is_member(x, a), "that the value of", x, "is in list", a, "\n")

	if(option == 2):
		lst1 = [1, 11, 12, 13, 14, 15]
		lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
		
		print("\nit is", overlapping(lst1, lst2), "that the two list", lst1, "and list", lst2, "have at least one item in common.\n")

	if(option == 3):
		import time
		lst = [1, 2, 2, 3, 4, 5]
		print("\nThe list", lst, "has duplicates.")
		time.sleep(2)
		print("And presto! your new list without dupes is", remove_doops(lst), ".\n")

	if(option == 4):
		lst1 = [1, 2, 3, 10, 11, 12]
		lst2 = [1, 2, 3, 20, 21, 22]
		
		print("\nThe list", lst1, "and list", lst2, "have common items.")
		print("Here is your new list of common elements ", intersection(lst1, lst2), "\n")

	if(option == 5):
		lsta = [1, 2, 3, 10, 11, 12]
		lstb = [1, 2, 3, 20, 21, 22]
		
		print("\nYou have list a", lsta, "and list b", lstb, ".")
		print("items in list b that are NOT in a are:", complement(lsta, lstb), "\n")


print("\ng'won then. Git!")
