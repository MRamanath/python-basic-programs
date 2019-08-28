# A program to delete an element of a tuple from a particular position.

names = ('A', 'B', 'C', 'D', 'E')
print('Names -->', names)

pos = int(input('Enter the specified position: '))
names1 = names[0:pos-1]
print('Names1 -->', names1)

names = names1 + names[pos:]
print('Names -->', names)

# Names --> ('A', 'B', 'C', 'D', 'E')
# Enter the specified position: 2
# Names1 --> ('A',)
# Names --> ('A', 'C', 'D', 'E')