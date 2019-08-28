# Local and Global Variables
# Local Variable
# When we declare a variable inside a function, it becomes a local variable. A local variable
# is a variable whose scope is limited only to that function where t is created.
# That means the local variable value is available only in that function and not outside of 
# function.

# Global Variable
# When a variable is declared above a function, it becomes global variable. Such variables
# are available to all the functions which are written after it.
# The scope of the global variable is the entire program body written below it.

# Local variable example:
def myfunc():
	a = 1 # this is a local var
	a += 1 # increment it
	print(a) # displays 2

myfunc()
print(a) # error, not available

# Output
# 2
# Traceback (most recent call last):
#   File "10local-and-global-variables.py", line 20, in <module>
#     print(a) # error, not available
# NameError: name 'a' is not defined

# Global Variable example:
a = 1 # thsi is a global var
def myfunc1():
	b = 2 # this is a local var
	print('a = ', a)
	print('b = ', b)

myfunc1()
print(a) # available
print(b) # error, not available

# Output
# a =  1
# b =  2
# 1
# Traceback (most recent call last):
#   File "10local-and-global-variables.py", line 38, in <module>
#     print(b) # error, not available
# NameError: name 'b' is not defined


