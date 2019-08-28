# input : B4A1D3
# output: ABD134

s = input('Enter some string: ')
s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x

# output = ''.join(sorted(s1)) + ''.join(sorted(s2))
# print(output)
# print()

for y in sorted(s1):
    output = output + y
for y in sorted(s2):
    output = output + y

print(output)

# Enter some string: B4A1D3
# ABD134