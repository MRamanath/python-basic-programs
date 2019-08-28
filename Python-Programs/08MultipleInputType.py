# A Program that demonstrate various ways of taking input from the kyb.

# Int type input
a = int(input('Enter a number : '))
print(type(a))
print(a)

# float type input
a = float(input('Enter a number : '))
print(type(a))
print(a)

# str type input
a = input('Enter a character : ')
print(type(a))
print(a)

# bool type input
a = eval(input('Enter a boolean value[True|False] : '))
print(type(a))
print(a)

# Enter a number : 12
# <class 'int'>
# 12
# Enter a number : 12.111
# <class 'float'>
# 12.111
# Enter a character : abc
# <class 'str'>
# abc
# Enter a boolean value[True|False] : False
# <class 'bool'>
# False