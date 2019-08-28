# input : Learning Python Is Very Easy
# output: Easy Very Is Python Learning

str = input('Enter a string : ')
s = str.split()
l = len(s) - 1
l1 = []
while l >= 0:
    l1.append(s[l])
    l = l - 1
output = ' '.join(l1)
print(output)

# Enter a string : Learning Python Is Very Easy
# Easy Very Is Python Learning