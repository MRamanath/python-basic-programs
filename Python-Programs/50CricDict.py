# A program to create a dictionary with cricket player's name and scores in a match.
# Also we are retrieving runs by entering the player's name.

d = {}
x = int(input('Enter How many elements: '))
for i in range(x):
    print('Enter Key : ', end='')
    key = input()
    print('Enter Value : ', end='')
    value = int(input())
    d.update({key:value})
print('The dictionary is : ', d)
for k, v in d.items():
    print('Player\'s Name = {} and Runs = {} '.format(k,v))

while True:
    name = input('Enter a player\'s name : ')
    runs = d.get(name, -1)
    if runs == -1:
        print('Player not found!')
    else:
        print('Player {} has {} runs'.format(name, runs))
    option = input('Do you want to get another player\'s runs ?[YES || NO] ')
    if option == 'NO':
        break

# Enter How many elements: 3
# Enter Key : A
# Enter Value : 231
# Enter Key : B
# Enter Value : 456
# Enter Key : C
# Enter Value : 901
# The dictionary is :  {'A': 231, 'B': 456, 'C': 901}
# Player's Name = A and Runs = 231 
# Player's Name = B and Runs = 456 
# Player's Name = C and Runs = 901 
# Enter a player's name : A
# Player A has 231 runs
# Do you want to get another player's runs ?[YES || NO] NO