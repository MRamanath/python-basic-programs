# A Python program to check if a given number is prime or not.

def prime(n):
	flag = 0
	for i in range(2, n):
		if n % i == 0:
			flag = 1
			break
		else:
			flag = 0
	return flag

num = int(input('Enter a number: '))
result = prime(num)
if result == 0:
	print(num, 'is Prime')
else:
	print(num, 'is not Prime')

# Output
# Enter a number: 23
# 23 is Prime

# Enter a number: 21
# 21 is not Prime

# Prime number within a range.
min, max = [int(x) for x in input('Enter the minimum and maximum range: ').split(',')]
print('Prime Numbers are: ')
for i in range(min, max + 1):
	if prime(i) == 0:
		print(i, end = '\t')

# Output
# Enter the minimum and maximum range: 2, 19
# Prime Numbers are:
# 2       3       5       7       11      13      17      19


# A Python program that generates prime numbers with the help of a function 
# to test prime or not.
num = int(input('\nHow many primes do you want? '))
i = 2 # starts with i value 2
c = 1 # this counts the no. of primes
while True:
	if prime(i) == 0:
		print(i)
		c += 1
	i += 1
	if c > num:
		break

# Output
# How many primes do you want? 10
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
