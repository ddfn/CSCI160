#validate the length of each individual field. 
#They ALL must be valid for the entire date to be valid
def are_valid_lengths(m, d, y):
    return not(len(m) < 1 or len(m) > 2 or len(d) < 1 or len(d) > 2 or len(y) < 4 or len(y) > 4)

def is_leap_year(year):
	if(year  %  4 == 0):
		if(year % 100 == 0):
			if(year % 400 == 0):
				return True
			else:
				return False
		else:
			return True	
	else:
		return False

def is_valid_date(m, y, d):
	if(month >= 1 and month <= 12):
		#valid month
		if(len(str(year))) < 5:
			#valid month And a valid year
			if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
			#if(str(month) in "1,3,5,7,8,10,12"):	#python only
				if(day >= 1 and day <= 31):
					return True
				else:
					return False  #stop here to test
			elif(month == 4 or month == 6 or month == 9 or month == 11):
				if(day >= 1 and day <= 30):
					return True
				else:
					return False
			else:
				#february
				if(is_leap_year(year) and day >= 1 and day <= 29):
					return True
				elif(day >= 1 and day <= 28):
					return True
				else:
					return False
		else:
			return False
	else:
		return False
