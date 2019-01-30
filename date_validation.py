'''
This program will perform validation on an entered Date
1) It will validate the format: slashes must be present and each field must be an appropriate length
2) It will validate the months as being 1 - 12
3) It will validate the days of month depending on the following
    a: Is it a leap year? Then February can have 29 days. Otherwise 28
    b: Each month has a separate amount of valid days
'''

from date_functions import are_valid_lengths, is_valid_date

d = input("Enter a date (mm/dd/yyyy) and I will tell you if it is valid: ")

# locate the slashes in the date using the string find method
slash1 = d.find("/")
# locate the second slash by beginning search AFTER the first slash
slash2 = d.find("/", slash1 + 1)

#test the slashes first to see if they are present
if(slash1 < 0 or slash2 < 0):
    # something wrong with the slashes
    print(d, "is not a valid date")
#slashes were there so let's continue testing the individual date fields
else:
    #extract the individual date fields
    month   = d[0:slash1]           #extract everything up to first slash
    day     = d[slash1+1:slash2]    #start AFTER slash1, extract UP TO slash2
    year    = d[slash2+1:]          #start AFTER slash2, extract until end


if(are_valid_lengths(month, day, year)):
        #format is invalid
    month = int(month)
    year = int(year)
    day = int(day)
    print(d, "is a valid date")
        
    if(is_leap_year(int(year))): 
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else: 



if(is_valid_date(month, year, day)):
    print("valid")
else: 
    print("Not valid")



           
