# A Python program to pass an integer to a function and modify it.

def modify(x):
	"""reassigning a value to the variable"""
	x = 15
	print(x, id(x))

# call modify() and pass x
x = 10
modify(x)
print(x, id(x))

# Output
# 15 140711799805408
# 10 140711799805248

# Explaination:
# From the output we can understand that the value of 'x' in the function is 15 and that
# is not available outside the function. When we call the modify() function and pass 'x'
# as: modify(x)
# we should remember that we are passing the object reference to the modify() function.
# The object is 10 and its reference name is 'x'. This is being passed to the modify()
# function. Inside the function we are using:
# x = 15
# This means another object 15 is created in memory and that object is referenced by the
# name 'x'. The reason another object is created in the memory is that the integer objects
# are immutable. So, in the function when we display 'x' value, it will display the old 
# object value, i.e. 10. 

# A Python program to pass a list to a function and modify it.

def modify(lst):
	"""To add a new element to list"""
	lst.append(9)
	print(lst, id(lst))

# call modify() and pass lst
lst = [1, 2, 3, 4]
modify(lst)
print(lst, id(lst))

# Output
# [1, 2, 3, 4, 9] 2275567100488
# [1, 2, 3, 4, 9] 2275567100488

# Conclusion
# In Python, values are passed to functions by object references. If the object is immutable,
# the modified value is not available outside the function and if the object is mutable, its
# modified value is available outside the function.

# A Python program to create a new object inside the function, does not modify outside
# object.

def modify(lst):
	'''To create a new list'''
	lst = [1, 2, 3, 4]
	print(lst, id(lst))

lst = [56, 67, 55]
modify(lst)
print(lst, id(lst))

# Output
# [1, 2, 3, 4] 3012307083848
# [56, 67, 55] 3012310208776

# Explaination
# If we create altogether a new object inside the function, then it will not be available 
# outside the function. 
# we are passing [56, 67, 55] to the modify() function.
# But inside the function we are creating a new list as: lst = [1, 2, 3, 4]
# It means a new object is created in the function and  that is referenced by the name 
# 'lst'. So, inside the function the list is displayed as: [1, 2, 3, 4]
# But the object that is outside the function is different. Hence it remains as it is,
# i.e. [56, 67, 55].
