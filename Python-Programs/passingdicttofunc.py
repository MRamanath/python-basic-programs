# Passing a dictionary to a function

def dict_pass(dict):
    for i,j in dict.items():
        print('i = {} -------> j = {}'.format(i, j))

d = {1: 'a', 2: 'b'}
dict_pass(d)

# i = 1 -------> j = a
# i = 2 -------> j = b