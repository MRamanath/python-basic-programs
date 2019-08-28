# A python program to search for an element in a list.

list1 = [1, 2, 3, 4, 5]
search = int(input('Enter the searching element : '))

for i in list1:
    if i == search:
        print('{} is found in the list'.format(search))
        break
else:
    print('{} is not found in the list'.format(search))

# Output
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\28searchList.py
# Enter the searching element : 5
# 5 is found in the list
# PS C:\Users\RAMANATH\Documents\PythonPrograms> py .\28searchList.py
# Enter the searching element : 11
# 11 is not found in the list