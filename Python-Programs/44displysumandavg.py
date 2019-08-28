# Display sum and average from a tuple of numbers.

tpl = eval(input('Enter elements in () : '))
sum = 0
n = len(tpl)
for i in range(n):
    sum = sum + tpl[i]
print('Sum of numbers: ', sum)
print('Average of numbers: ', sum/n)

# Enter elements in () : (12, 23 ,34)
# Sum of numbers:  69
# Average of numbers:  23.0

tpl = eval(input('Enter elements in () : '))
sum = 0
n = len(tpl)
for i in tpl:
    sum = sum + i
print('Sum of numbers: ', sum)
print('Average of numbers: ', sum/n)

# Enter elements in () : (12, 23, 34)
# Sum of numbers:  69
# Average of numbers:  23.0