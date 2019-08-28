# A program to add two matrices and display the sum matrix using lists.

m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m2 = [[9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]]

m3 = [4*[0] for x in range(3)]
print(m3)

for i in range(3):
    for j in range(4):
        m3[i][j] = m1[i][j] + m2[i][j]

for i in range(3):
    for j in range(4):
        print(m3[i][j], end=' ')
    print()

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# 10 12 14 16 
# 10 12 14 16 
# 10 12 14 16 