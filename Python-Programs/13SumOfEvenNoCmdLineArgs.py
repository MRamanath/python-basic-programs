# A program to find the sum of even numbers using command line arguments.

from sys import argv
args = argv[1:]
sum = 0
for x in args:
    n = int(x)
    if n % 2 == 0:
        sum = sum + n
print('The sum of all even numbers is : ', sum)

# Output
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\13SumOfEvenNoCmdLineArgs.py 0 2 4 5 7 8 10
# The sum of all even numbers is :  24