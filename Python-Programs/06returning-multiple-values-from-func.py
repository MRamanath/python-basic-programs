# A Python program to understand how a function returns two values.

def sum_sub(a, b):
	c = a + b
	d = a - b
	return c, d

x, y = sum_sub(23, 12)

# display the results
print('Result of addition: ', x)
print('Result of subtraction: ', y)

# Output
# Result of addition:  35
# Result of subtraction:  11

# A Python function that returns the results of addition, subtraction, multiplication 
# and division.

def sum_sub_mul_div(a, b):
	c = a + b
	d = a - b
	e = a * b
	f = a / b
	return c, d, e, f

t = sum_sub_mul_div(10, 5)
print(type(t))
# display the results using for loop
print('The results are: ')
for i in t:
	print(i, end = ', ')

# Output
# <class 'tuple'>
# The results are:
# 15, 5, 50, 2.0,
