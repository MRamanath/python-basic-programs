# A program to split a string and store its 1st letter as key.

str = input('Enter a string : ')
s = str.split()
d = {}
for i in s:
    d[i[0]] = i
print(d)

# Enter a string : Learning Python Is Easy
# {'L': 'Learning', 'P': 'Python', 'I': 'Is', 'E': 'Easy'}