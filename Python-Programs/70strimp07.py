# input: a4b3c2
# output: aaaabbbcc

str = input('Enter a string: ')
output = ''
for x in str:
    if x.isalpha():
        alpha = x
    else:
        output = output + alpha*int(x)
print(''.join(sorted(output)))

# Enter a string: a4b3c2
# aaaabbbcc