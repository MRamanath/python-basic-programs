# A program to insert a new element into a tuple of elements at a specified position.

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

names = names1 + names[pos-1:]
print('Names -->', names)

# Names --> ('A', 'B', 'C', 'D', 'E')
# Enter a the new element: P
# New --> ('P',)
# Enter the specified position: 4
# Names1 --> ('A', 'B', 'C')
# Names1 --> ('A', 'B', 'C', 'P')
# Names --> ('A', 'B', 'C', 'P', 'D', 'E')