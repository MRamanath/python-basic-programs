# Display string index wise.
str = input('Enter a string: ')
i = 0
l = len(str)

for x in str:
    print('{} is found at positive index {} and negative index {}'.format(x, i, i-l))
    i = i + 1

# Enter a string: Ramanath
# R is found at positive index 0 and negative index -8
# a is found at positive index 1 and negative index -7
# m is found at positive index 2 and negative index -6
# a is found at positive index 3 and negative index -5
# n is found at positive index 4 and negative index -4
# a is found at positive index 5 and negative index -3
# t is found at positive index 6 and negative index -2
# h is found at positive index 7 and negative index -1