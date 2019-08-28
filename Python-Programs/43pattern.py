# Pattern Programs

for i in range(5):
    print('* ', end = ' ') 

# *  *  *  *  *

for i in range(5):
    print('* '*5)

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(5):
    print((str(i) + ' ')*5)

# 0 0 0 0 0
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4

for i in range(5):
    print('* '*i)

# *
# * *
# * * *
# * * * *

for i in range(5):
    print((str(i) + ' ')*i)

# 1
# 2 2
# 3 3 3
# 4 4 4 4

for i in range(5):
    print((5 - i)*'* ')

# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5):
    print(' ' * (5 - i), end = '')
    print('* ' * i)

#     *
#    * *
#   * * *
#  * * * *

