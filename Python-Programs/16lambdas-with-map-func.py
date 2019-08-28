# Lambdas with map() function
# The map() function is similar to filter() function but it acts on each element of the
# sequence and perhaps changes the elements. The format of map() function is :
# map(function, sequence)
# The 'function' performs a specified operation on all the elements of the sequence and the
# modifief elements are returned which can be stored in another sequence.

# A Python program to find squares of elements in a list.
# map() function that gives squares 
def squares(x):
	return x*x

lst = [1, 2, 3, 4, 5]
lst1 = list(map(squares, lst))
print(lst1)

# Output
# [1, 4, 9, 16, 25]

# A lambda function that returns squares of elements in a list.
lst = [1, 2, 3, 4, 5]
lst1 = list(map(lambda x: x*x, lst))
print(lst1)

# Output
# [1, 4, 9, 16, 25]

# A Python program to find the products of elements of two different lists using
# lambda function.
lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 20, 30, 40, 50]
lst3 = list(map(lambda x, y: x*y, lst1, lst2))
print(lst3)

# Output
# [10, 40, 90, 160, 250]

