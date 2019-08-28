# input : Durga Software Solutions
# output: agruD erawtfoS snoituloS

str = input('Enter a string : ')
s = str.split()
l1 = []
i = 0
while i < len(s):
    l1.append(s[i][::-1])
    i = i + 1
output = ' '.join(l1)
print(output)

# Enter a string : Durga Software Solutions
# agruD erawtfoS snoituloS