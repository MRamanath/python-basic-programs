# A program to display and count command line arguments.

from sys import argv
print('The number of command line arguments : ', len(argv))
print('The command line arguments are : ')
for x in argv:
    print(x)

# Output
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\12CountCmdArgs.py 12 23 45 78
# The number of command line arguments :  5
# The command line arguments are :
# .\12CountCmdArgs.py
# 12
# 23
# 45
# 78