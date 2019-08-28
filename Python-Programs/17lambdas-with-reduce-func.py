# Using Lambdas with reduce() function.
# The reduce() function reduces a sequence of elements to a single value by processing
# the elements according to a function supplied. The format of the reduce() is:
# reduce(function, sequence)

# A lambda function to calculate products of elements of a list
from functools import *
lst = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x*y, lst)
print(result)

# Output
# 120

# A lambda function to calculate sum of numbers from 1 to 50.
from functools import *
sum = reduce(lambda a, b: a+b, range(1, 51))
print(sum)

# Output
# 1275
