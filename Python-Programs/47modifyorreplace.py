# A program to modify or replace an existing element of a tuple with a new element.

names = ('A', 'B', 'C', 'D', 'E')
print('Names -->', names)

lst = [input('Enter a the new element: ')]
t = tuple(lst)
print('New -->', t)

pos = int(input('Enter the specified position: '))
names1 = names[0:pos-1]
print('Names1 -->', names1)

names1 = names1 + t
print('Names1 -->', names1)

names = names1 + names[pos:]
print('Names -->', names)

# Names --> ('A', 'B', 'C', 'D', 'E')
# Enter a the new element: 4
# New --> ('4',)
# Enter the specified position: 4
# Names1 --> ('A', 'B', 'C')
# Names1 --> ('A', 'B', 'C', '4')
# Names --> ('A', 'B', 'C', '4', 'E')