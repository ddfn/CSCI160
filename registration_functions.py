#Andrew
#class lecture 9/25/2018

#function to determine FR,SO, JR, or SR
#based on completed credits

def class_level(credits):
	if(credits >= 91):
		return "SR"
	elif(credits >= 61):
		return "JR"
	elif(credits >= 31):
		return "SO"
	else:
		return "FR"

