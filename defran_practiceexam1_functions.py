#Andrew DeFran
#csci 160
#9/18/2018

#practice exam functions

def gross_pay(hoursworked, payrate):
	gro_pay = hoursworked * payrate

	return gro_pay

def federal_income_tax(grosspay):
	fedtax_amt = grosspay * .15

	return fedtax_amt

def state_income_tax(grosspay):
	statetax_amt = grosspay * .035

	return statetax_amt

def social_sec_tax(grosspay):
	socsec = grosspay * .0575

	return socsec

def medicare_medicaid_tax(grosspay):
	medcare_medcaid = grosspay * .0275

	return medcare_medcaid

def pension_plan(grosspay):
	pension = grosspay * .05

	return pension

def net_pay(grosspay):
	a = federal_income_tax(grosspay)
	b = state_income_tax(grosspay)
	c = social_sec_tax(grosspay)
	d = medicare_medicaid_tax(grosspay)
	e = pension_plan(grosspay)

	total_deduction_value =  float(a + b + c + d + e)
	net_pay = grosspay - total_deduction_value

	return float(net_pay)

