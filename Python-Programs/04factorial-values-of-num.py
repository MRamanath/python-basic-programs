# A Python program to calculate factorial values of numbers.

def fact(x):
	i = 1
	while x >= 1:
		i = i * x
		x = x - 1
	return i
	# k = 1
	# for j in range(1, x+1):
	# 	k = k*x
	# return j

for x in range(1, 11):
	print('Factorial of {} is {} '.format(x, fact(x)))

# Output
# Factorial of 1 is 1
# Factorial of 2 is 2
# Factorial of 3 is 6
# Factorial of 4 is 24
# Factorial of 5 is 120
# Factorial of 6 is 720
# Factorial of 7 is 5040
# Factorial of 8 is 40320
# Factorial of 9 is 362880
# Factorial of 10 is 3628800
