# Duplicate elimination from a string
# 

str = input('Enter a string : ')
l = []
for x in str:
    if x not in l:
        l.append(x)
print(l)
output = ''.join(l)
print(output)

# Enter a string : ABBBBCDDDDKKKLMJJAAAJ
# ['A', 'B', 'C', 'D', 'K', 'L', 'M', 'J']
# ABCDKLMJ