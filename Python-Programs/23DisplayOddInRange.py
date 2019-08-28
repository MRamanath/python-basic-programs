# A program to display odd numbers within a range.

min, max = [int(x) for x in input('Enter the minimum and maximum range : ').split()]
x = min
if x % 2 == 0:
    x = x + 1
print('Odd numbers are as follows --- ')
while x >= min and x <= max:
    print(x, end = '\t')
    x = x + 2

# Output
# Enter the minimum and maximum range : 10 19
# Odd numbers are as follows ---
# 11      13      15      17      19