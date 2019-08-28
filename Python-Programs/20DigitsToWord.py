# A program to accept a numeric digit from keyboard and display it.

a = int(input('Enter a single digit : '))
if a == 0:
    print('Zero')
elif a == 1:
    print('One')
elif a == 2:
    print('Two')
elif a == 3:
    print('Three')
elif a == 4:
    print('Four')
elif a == 5:
    print('Five')
elif a == 6:
    print('Six')
elif a == 7:
    print('Seven')
elif a == 8:
    print('Eight')
elif a == 9:
    print('Nine')
else:
    print('Something went wrong...Try again!')


# Output
# Enter a single digit : 1
# One

# Enter a single digit : 2
# Two

# Enter a single digit : 9
# Nine

# Enter a single digit : 900
# Something went wrong...Try again!
