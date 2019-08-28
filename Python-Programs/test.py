def display(lst):
	for i in lst:
		print(i)

lst = input('Enter strings seperated by comma: ').split(',')
print(type(lst))
display(lst)

# Output
# Enter strings seperated by comma: a,b,c,d
# <class 'list'>
# a
# b
# c
# d

def display1(lst):
	for i in lst:
		print(i)

lst1 = [x for x in input('Enter strings seperated by comma: ').split(',')]
display1(lst1)

# Output
# Enter strings seperated by comma: f,g,h,i,j
# f
# g
# h
# i
# j
