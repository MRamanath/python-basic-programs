# A program to find the first occurrences of an element in a tuple.

lst = [int(x) for x in input('Enter elements seperated by commas: ').split(',')]
tpl = tuple(lst)

print('The tuple is : ', tpl)
y = int(input('Enter the searching element : '))

print('{} found at position {}'.format(y, tpl.index(y)))

# Enter elements seperated by commas: 12, 2, 12, 2, 3
# The tuple is :  (12, 2, 12, 2, 3)
# Enter the searching element : 2
# 2 found at position 1


