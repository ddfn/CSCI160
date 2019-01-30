#Andrew DeFran
#CSCI 160
#9/30/2018
#Lab 4

#prompt for the input. No need to validate input
start 		= input("Enter the starting time of the call (HH:MM:SS): ")
duration 	= input("Enter the duration of the call (MM:SS): ")
distance    = input("Enter the distance of the call (miles): ")
conference  = input("Was the call a conference call (Y/N)? ")

#split the times into separate values and convert each time segment to an int
#call the split method on the string at delimiter ':'
start_h, start_m, start_s  = [int(time_segment) for time_segment in start.split(":")]
dur_m, dur_s = [int(time_segment) for time_segment in duration.split(":")]

print("Call began at:", start_h, "hours", start_m, "minutes", start_s, "seconds")
print("Call lasted:", dur_m, "minutes and", dur_s, "seconds")

#convert time input to seconds
total_start_seconds = (start_h * 3600) + (start_m * 60) + (start_s)
total_duration_seconds = (dur_m * 60) + (dur_s)


#test function calls
#basic charge function call and output
from call_charge_functions import basic_charge
basic_c = basic_charge(total_duration_seconds, distance) / 100 #convert to dollars from cents
print("Your basic rate is $", round(basic_c, 2), ".")

#off peak discount function call and ouput
from call_charge_functions import off_peak_discount
off_peak_disc = off_peak_discount(distance, total_start_seconds, basic_c) 
print("Your off-peak discount is $", round(off_peak_disc, 2), ".")

#conference discount function call and output
from call_charge_functions import conference_call_discount
if(conference == 'Y'):
	conference_disc = conference_call_discount(distance, basic_c) 
	print("The additional conference discount amount is $", round(conference_disc, 2))
else:
	print("No conference discount applied is $", round(conference_disc, 2), ".")

#calculate net charge
net_charge = (basic_c - off_peak_disc - conference_disc) 
print("The net charge with discounts applied is $", round(net_charge, 2), ".")

#call VAT function and print output
from call_charge_functions import vat
vat_tax = vat(net_charge)
print("VAT tax will be $", round(vat_tax, 2), ".")

#call final charge function and print ouptut
from call_charge_functions import final_charge
final_char = final_charge(net_charge, vat_tax)
print("Your final charge is $", round(final_char, 2), "!")
print("Can you hear me now!? Good.")
