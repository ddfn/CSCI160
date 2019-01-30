#Andrew DeFran
#CSCI 160
#11/27/2018

#notes

#create a list
empty_list = []
empty_string = ""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_string = "12345678910"

print("Length of the list: ", len(my_list))
print("Length of the list: ", len(my_string))

print(my_list) #prints exaclty how you type it

#to print all do a traversal
for i in range(0, len(my_list)):
	print(my_list[i], end ="")

print()
for i in my_list:
	print(i, end = " ")	


print("The largest number is: ", max(my_list))
print("The sum is: ", sum(my_list))

#what are the algorithms for sort and max??

def summ(list_param):
	total = 0

	for index in range(0, len(list_param)):
		#also total = total plus + list_param[index]
		total += list_param[index]
	return total

print("The sum is:", summ(my_list))


def maxx(list_param):
	m = list_param[0]
	index = 0

	while(index < len(list_param)):
		if(list_param[index] > m):
			m = list_param[index]

		index += 1
	return m	

print("The max number: ", max(my_list))

def fill_list():
	from random import randint
	new_list = []
	
	for n in range(1 , 100 + 1):
		new_list.append(randint(1, 101))

	return new_list

lst = fill_list()

def count(lst, item):
	counter = 0

	for i in lst:
		if(i == item):
			counter += 1
	return counter

a = count(lst, 23)
b = lst.count(23)

print("We say there are", a, "23s") 
print("python says there are", b, "23s") 		



#sorting! beginning! bubble sort
def bubble_sort(lst):
	for i in range(0, len(lst)):
		for j in range(0 , len(lst) - 1):
			if(lst[j] > lst[j + 1]):
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp

bubble_sort(lst)
print(lst)

