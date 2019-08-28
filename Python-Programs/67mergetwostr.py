# A program to merge characters of 2 strings into a single string by taking characters alternatively.
# str1: "ravi"
# str2: "teja"

str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")
output = ''
i, j = 0, 0
while i < len(str1) or j < len(str2):
    if i < len(str1):
        output = output + str1[i]
        i += 1
    if j < len(str2):
        output = output + str2[j]
        j += 1
print(output)

# Enter First String : ravi
# Enter Second String : teja
# rtaevjia
