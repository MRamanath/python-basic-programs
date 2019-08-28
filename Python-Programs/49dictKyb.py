# A program to create a dictionary from keyboard and display the elements.

d = {}
x = int(input('Enter How many elements: '))
for i in range(x):
    print('Enter Key : ', end='')
    key = input()
    print('Enter Value : ', end='')
    value = input()
    d.update({key:value})
print('the dictionary is : ', d)
for k, v in d.items():
    print('Key = {} and Value = {} '.format(k,v))

# Enter How many elements: 3
# Enter Key : A
# Enter Value : 123
# Enter Key : B
# Enter Value : 321
# Enter Key : C
# Enter Value : 453
# the dictionary is :  {'A': '123', 'B': '321', 'C': '453'}
# Key = A and Value = 123 
# Key = B and Value = 321 
# Key = C and Value = 453 