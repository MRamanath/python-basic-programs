# A program to create a dictionary that does not change its order.

from collections import OrderedDict
d = OrderedDict()
d[1] = 'a'
d[2] = 'b'
d[3] = 'c'
for i, j in d.items():
    print(i, j)

# 1 a
# 2 b
# 3 c