# input : One Two Three Four Five
# output: One owT Three ruoF Five

s = input('Enter some string: ')
l = s.split()
l1 = []
i = 0
while i < len(l):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i += 1
output = ' '.join(l1)
print(output)

# Enter some string: One Two Three Four Five
# One owT Three ruoF Five