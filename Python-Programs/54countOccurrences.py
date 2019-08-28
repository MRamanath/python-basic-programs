# WAP to count the ocurrences of a substring and point out the indexes where it occurred.

str = input('Enter the main string: ')
sub = input('Enter the sub string: ')

i = str.find(sub)
if i == -1:
    print('{} not found in the main string'.format(sub))
while i!= -1:
    print('\'{}\' occurred at {}'.format(sub, i))
    i = str.find(sub, i+len(sub), len(str))
print('The no of occurrences of substr \'{}\' is {}'.format(sub, str.count(sub)))

# Enter the main string: abaababaaba
# Enter the sub string: aa
# 'aa' occurred at 2
# 'aa' occurred at 7
# The no of occurrences of substr 'aa' is 2