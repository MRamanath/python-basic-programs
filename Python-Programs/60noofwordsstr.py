# A program to find the number of words in a string.

str = input('Enter a string : ')
s = str.split()
c = 0
for i in range(len(s)):
    c = c + 1
print('No of words is = {}'.format(c))

# Enter a string : ram is a good boy
# No of words is = 5