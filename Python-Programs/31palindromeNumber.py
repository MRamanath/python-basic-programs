# A Program to display palindrome number within range.

min, max = [int(x) for x in input('Enter the minimum and maximum range: ').split()]
for x in range(min, max + 1):
    temp = x
    rev = 0
    while temp != 0:
        r = temp % 10
        rev = rev * 10 + r
        temp = temp // 10
    if x == rev:
        print(x, end = '\t')

# Output
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\31palindromeNumber.py
# Enter the minimum and maximum range: 1 44
# 1       2       3       4       5       6       7       8       9       11      22      33      44