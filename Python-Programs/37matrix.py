# A program to retrieve elements from a matrix and display them.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
print('Display the list as it is :')
print(matrix)
print('Display row by row')
for r in matrix:
    print(r)
print('Display each column in 1st row')
for c in matrix[0]:
    print(c, end='')
print()
print('Display each column in 2nd row')
for c in matrix[1]:
    print(c, end='')
print()
print('Display each column in 3rd row')
for c in matrix[2]:
    print(c, end='')
print()
print('Display all elements using for: ')
for r in matrix:
    for c in r:
        print(c, end=' ')
    print()
print('Display all elements using for: ')
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print('%d ' %matrix[r][c], end=' ')
    print()

# Display the list as it is :
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Display row by row
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# Display each column in 1st row
# 123
# Display each column in 2nd row
# 456
# Display each column in 3rd row
# 789
# Display all elements using for: 
# 1 2 3 
# 4 5 6 
# 7 8 9 
# Display all elements using for: 
# 1  2  3  
# 4  5  6  
# 7  8  9  