# Passing group of elements to a function.
# A function to accept a group of numbers and find their total average.

def calculate(lst):
	n = len(lst)
	sum = 0
	for i in lst:
		sum += i
	avg = sum / n
	return sum, avg

# lst = [10, 20, 30, 40, 51]
lst = [int(x) for x in input('Enter numbers seperated by space: ').split()]
x, y = calculate(lst)
print('Total = ', x)
print('Average = ', y)

# Output
# Enter numbers seperated by space: 12 12 12 12
# Total =  48
# Average =  12.0

# A function to display a group of strings.
def display(lst):
	for i in lst:
		print(i)

lst = [x for x in input('Enter strings seperated by comma: ').split(',')]
display(lst)

# Output
# Enter strings seperated by comma: aa,bb,cc,dd,ee,ff,gg
# aa
# bb
# cc
# dd
# ee
# ff
# gg
