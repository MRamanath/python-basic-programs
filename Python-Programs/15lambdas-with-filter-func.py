# Lambdas with filter() function
# The filter function is useful to filter out the elements of a sequence depending on the 
# result of a function. We should supply a function and a sequence to the filter() function.
# as:
# filter(function, sequence)
# Here, the 'function' represents a function name that may return either True or False;
# and 'sequence' represents a list, string or tuple. The 'function' is applied to every 
# element of the 'sequence' and when the function returns True, the element is extracted
# otherwise it is ignored.

# A Python program using filter() to filter out even numbers from a list.
def is_even(x):
	if x%2 == 0:
		return True
	else:
		return False
lst = [10, 20 ,23, 11, 12, 100]
lst1 = list(filter(is_even, lst))
print(lst1)

# Output
# [10, 20, 12, 100]

# A lambda function that returns even numbers from a list.
lst = [10, 20 ,23, 11, 12, 100]
lst1 = list(filter(lambda x: (x%2 == 0), lst))
print(lst1)

# Output
# [10, 20, 12, 100]
