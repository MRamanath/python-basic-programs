# input: a4k3b2
# output: aeknbd

str = input('Enter a string : ')
output = ''
for x in str:
    if x.isalpha():
        output = output + x
        alpha = x
    else:
        output = output + chr(ord(alpha) + int(x))
print(output)

# Enter a string : a4k3b2
# aeknbd