# A program to demonstrate fibonacci series.

n = int(input('How many numbers : '))
f1 = 0
f2 = 1
c = 2
if n == 0:
    print(f1)
elif n == 1:
    print(f2)
else:
    print(f1, '\n', f2, sep = '')
    while c < n:
        f3 = f1 + f2
        print(f3)
        f1, f2 = f2, f3
        c += 1

# Output
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\30fibonacci.py
# How many numbers : 5
# 0
# 1
# 1
# 2
# 3