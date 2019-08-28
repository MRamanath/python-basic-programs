# The following possibilities are noteworthy:
# 1) It is possible to assign a function to a variable.
# 2) It is possible to define one function inside another function.
# 3) It is possible to pass a function as parameter to another function.
# 4) It is possible that a function can return another function.

# A Python program to see how to assign a function to a variable.

def display(str):
	return "Hi " + str

y = display('There!')
print(y)

# Output
# Hi There!

# A Python program to know how to define a function inside another function.

def display(str):
	def message():
		return "How are you? "
	result = message() + str
	return result

print(display('Mr. Smith'))

# Output
# How are you? Mr. Smith

# A Python program to know how to pass a function as parameter to another function.

def display(fun):
	return 'Hi ' + fun

def message():
	return "How are you? "
# call display() function and pass message() function
print(display(message()))

# Output
# Hi How are you?

# A Python program to know how a function can return another function.

def display():
	def message():
		return "How are you? "
	return message

# call display() function and it returns message() function
# in the following code, fun refers to name: message.
fun = display()
print(fun())

# Output
# How are you?