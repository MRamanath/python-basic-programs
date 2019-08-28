# Anonymous Function
# A function without a name is called 'anonymous function'.
# They are defined using the keyword lambda and hence they are also called 
# 'Lambda Functions'.
# The format of lambda function is :
# lambda argument_list : expression
# lambda functions return a function and hence they should be assigned to a function as:
# f = lambda x: x*x

# A python program to create a lambda function that returns a square value of a 
# given number.

f = lambda x: x*x
value = f(5)
print('Square of 5 is ', value)

# Output
# Square of 5 is  25

# A lambda function to calculate the sum of two numbers.
f = lambda x, y: x+y
result = f(1.55, 10)
print('Sum = ', result)

# Output
# Sum =  11.55

# A lambda function to find the bigger number in two given numbers.
max = lambda x, y: x if x>y else y
a, b = [int(i) for i in input('Enter two numbers: ').split(',')]
print('The bigger number is = ', max(a, b))

# Output
# Enter two numbers: 122, 4555
# The bigger number is =  4555

