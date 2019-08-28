# A program to create a list with employee data and then retrieve a particular employee details.

emp = []
n = int(input('How many employees ? '))
for i in range(n):
    print('Enter employee ID: ', end = '')
    emp.append(int(input()))
    print('Enter employee name: ', end = '')
    emp.append(input())
    print('Enter employee salary: ', end = '')
    emp.append(float(input()))

print('The list is created with employee data.')
id = int(input('Enter employee ID: '))
for i in range(len(emp)):
    if id == emp[i]:
        print('ID = {}, Name = {}, Salary = {}'.format(emp[i], emp[i+1], emp[i+2]))
        break

# How many employees ? 3
# Enter employee ID: 123
# Enter employee name: Ramanath
# Enter employee salary: 12000
# Enter employee ID: 121
# Enter employee name: Sourav
# Enter employee salary: 23000 
# Enter employee ID: 120
# Enter employee name: Kumkum
# Enter employee salary: 21000
# The list is created with employee data.
# Enter employee ID: 120
# ID = 120, Name = Kumkum, Salary = 21000.0