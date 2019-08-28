# Formal and Actual Arguments

def sum(a, b): # a, b are formal arguments
	c = a + b
	print(c)

x = 10; y = 15
sum(x, y) # x, y are actual arguments

# Output
# 25

# The actual arguments used in a function call are 4 types.
# 1) Positional Arguments
# 2) Keyword Arguments
# 3) Default Arguments
# 4) Variable Length Arguments

# A Python program to understand the positional arguments of a function.

def attach(s1, s2):
	'''To join s1 ad s2 and display total string'''
	s3 = s1 + s2
	print('Total string: ' +s3)

attach('New', 'York') 

# Output
# Total string: NewYork

# A Python program to understand the keyword arguments of a function.

def grocery(item, price):
	'''To display the given arguments'''
	print('Item = %s' % item)
	print('Price = %.2f' % price)

grocery(item = 'Sugar', price = 50.75)
grocery(price = 88.0, item = 'Oil')

# Output
# Item = Sugar
# Price = 50.75
# Item = Oil
# Price = 88.00

# A Python program to understand the use of default arguments in a function.

def grocery(item, price = 40.00):
	'''To display the given arguments'''
	print('Item = %s' % item)
	print('Price = %.2f' % price)

grocery(item = 'Sugar', price = 50.75) # pass 2 arguments
grocery(item = 'Sugar') # default value for price is used.

# Output
# Item = Sugar
# Price = 50.75
# Item = Sugar
# Price = 40.00

# A Python program to show variable length argument and its use.
def add(farg, *args): # *args can take 0 or more values
	'''To add given numbers'''
	print('Formal argument = ', farg)

	sum = 0
	for i in args:
		sum += i
	print('Sum of all numbers = ', (farg + sum))

# call add() and pass arguments
add(5, 10)
add(5, 10, 20, 30)

# Output
# Formal argument =  5
# Sum of all numbers =  15
# Formal argument =  5
# Sum of all numbers =  65

# A Python program to understand keyword variable argument.
def display(farg, **kwargs): # **kwargs can take 0 or more values
	"""To display given values"""
	print('Formal argument = ', farg)

	for x, y in kwargs.items(): # items() will give pair of items
		print('Key = {}, Value = {} '.format(x, y))

# pass 1 formal argument and 2 keyword arguments
display(5, rno = 10)
# print()

# pass 1 formal argument and 4 keyword arguments
display(5, rno = 12, name = 'Prakash')

# Output
# Formal argument =  5
# Key = rno, Value = 10
# Formal argument =  5
# Key = rno, Value = 12
# Key = name, Value = Prakash


