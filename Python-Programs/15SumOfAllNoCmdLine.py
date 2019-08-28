# A program to find sum of all numbers using command line arguments.

from sys import argv
args = argv[1:]
sum = 0
for x in args:
    n = int(x)
    sum = sum + n

print('The sum of all numbers is : ', sum)

# Output
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\15SumOfAllNoCmdLine.py 11 22 33 44 55
# The sum of all numbers is :  165