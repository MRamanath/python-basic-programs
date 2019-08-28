# Squares of integers from 1 to 100.

squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print(squares)

squares = [x**2 for x in range(1, 11)]
print(squares)

squares = [x**2 for x in range(1, 11) if x  % 2 == 0]
print(squares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [4, 16, 36, 64, 100]