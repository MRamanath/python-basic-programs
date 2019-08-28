# Structured Programming
# In structured programming, the main task is divided into several parts called sub tasks
# and each of these sub tasks is represented by one or more functions. By using these
# functions programmer can accomplish the main task.

# A python program to calculate the gross salary and net salary of an employee.

# to calculate dearness allowance
def da(basic):
	"""da is 80% of basic salary"""
	da = basic*80/100
	return da

# to calculate house rent allowance
def hra(basic):
	"""hra is 15% of basic salary"""
	hra = basic*15/100
	return hra

# to calculate provident fund amount
def pf(basic):
	"""pf is 12% of basic salary"""
	pf = basic*12/100
	return pf

# to calculate income tax payable by employee
def itax(gross):
	"""tax is calculated at 10% on gross"""
	tax = gross*10/100
	return tax

# this is the main program
# calculate gross salary of employee by taking basic
basic = float(input('Enter basic salary: '))

# calculate gross salary 
gross = basic + da(basic) + hra(basic)
print('Your gross salary: {:10.2f}'.format(gross))

# calculate net salary
net = gross - pf(basic) - itax(gross)
print('Your net salary: {:10.2f}'.format(net))

# Output
# Enter basic salary: 20000
# Your gross salary:   39000.00
# Your net salary:   32700.00
