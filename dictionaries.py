'''
Dictionaries in Python are associative arrays
Structures with key : value pairs
Created with a hash table
the 'key' is transformed into an index via a hash function
'''

nicknames = {	
	'skwrl'	:	'Josh Seeley',
	'migs'	: 	'Miguel Maldanado',
	'ale'	: 	'Alejandro Servetto',
	'jen'	: 	'Jennifer Knowels',
	'nick'	:	'Nick Figures',
	'nick'	: 	'Nick Brown',
	'crazy old man': 'Ken Whitener',
}

print("\nWho is 'skwrl'?:", nicknames['skwrl'])
print("\nWho is 'crazy old man'?:", nicknames['crazy old man'], "\n")

for key,val in nicknames.items():
    print(key, "\t=>\t", val)

#generate a cluster to illustrate collision resolution
#values will all hash to index 5
#simple_hash = key % array_size
hash_cluster = []
array_size = 60
from random import randint
for i in range(1, 1000):
	if(i % array_size == 5):
		hash_cluster.append(i)

print(hash_cluster)
	
