# We want to retrieve only the first letter of each word from the above list
# and store those first letters into another list.

words = ['Apple', 'Banana', 'Grapes', 'Orange']
lst = [w[0] for w in words]
print(lst)

# ['A', 'B', 'G', 'O']

lst = []
for w in words:
    lst.append(w[0])
print(lst)

# ['A', 'B', 'G', 'O']