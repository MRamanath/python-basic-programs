# Global Keyword
# Sometimes, the global variable and local variable may have same name. In that case,
# the function, by default, refers to the local variable and ignores the global variable.
# So, the global variable is not accessible inside the function but outside of it, it is
# accessible.

# A Python program to understand global and local variables.

# same name for global and local variables
a = 1
def myfunc():
	a = 2 # this i a local var
	print('a = ', a) # display local var

myfunc()
print('a = ', a) # display global var

# Output
# a =  2
# a =  1

# When the programmer wants to use the global variable inside a function, he can use the
# word 'global' before the variable in the beginning of the function body as:
# global a
# In this way the global variable is made available  to the function and the programmer can
# work with it as he wishes.

# A Python program to access global variable inside a function and modify it.

# accessing the global variable inside a function
a = 1 # this is global var
def myfunction():
	global a # this is global var
	print('global a = ', a) # display global var
	a = 2 # modify global var value
	print('modified a = ', a) # display new value

myfunction()
print('global a = ', a) # diplay modified value

# Output
# global a =  1
# modified a =  2
# global a =  2

# A Python program to get a copy of global variable into a function and work with it.
# globals() is a built in function which returns a table of current global variables
# in the form of a dictionary. Hence, using this function, we can refer to the global 
# variable 'a', as: globals()['a'].
# same name for global and local variables
a = 1 # this is a global var
def fun():
	a = 2 # a is local var
	x = globals()['a'] # get global var into x
	print('global var a = ', x)
	print('local var a = ', a)

fun()
print('global var a = ', a)

# Output
# global var a =  1
# local var a =  2
# global var a =  1
