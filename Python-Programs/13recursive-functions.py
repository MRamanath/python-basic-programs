# Recursive Functions
# A function that calls itselft is known as 'recursive function'.

# A Python program to calculate factorial values using recursion.

def fact(n):
	"""To find factorial of n"""
	if n == 0:
		result = 1
	else:
		result = n*fact(n-1)
	return result

# find factorial value of first 10 numbers
for i in range(1, 11):
	print('Factorial of {} is {} '.format(i, fact(i)))

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

# A Python program to display the Fibonacci sequence up to n-th term using 
# recursive functions

def recur_fibo(n):
	"""Recursive function to print Fibonacci sequence"""
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
	print("Plese enter a positive integer")
else:
	print("Fibonacci sequence:")
	for i in range(nterms):
		print(recur_fibo(i))

# Output
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

