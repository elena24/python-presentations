# creating a list
l1 = ['a', 'b', 'example', 1, 2, 3, True]
print(l1)           # will print ['a', 'b', 'example', 1, 2, 3, True]
print(l1[0])        # will print a
print(l1[-1])       # will print True

new_list = list("example")
print(new_list)     # will print ['e', 'x', 'a', 'm', 'p', 'l', 'e']

# slicing a list
print(l1[1:3])      # will print ['b', 'example']
print(l1[1:-2])     # will print ['b', 'example', 1, 2]
print(l1[:3])       # will print ['a', 'b', 'example']
print(l1[0:5:2])    # will print ['a', 'example', 2]

# adding items to a list
"""
concatenation with +
difference between append and extend
insert an item
"""
l2 = ['a']
l2 = l2 + [2.0, 3]
print(l2)                # will print ['a', 2.0, 3]
l2.append(True)
print(l2)                # will print ['a', 2.0, 3, True]
l2.extend(['four', '0'])
print(l2)                # will print ['a', 2.0, 3, True, 'four', '0']
l2.append(['four', '0'])
print(l2)                # ['a', 2.0, 3, True, 'four', '0', ['four', '0']]
print(len(l2))           # will print 8
l2.insert(0, "Q")
print(l2)                # ['Q', 'a', 2.0, 3, True, 'four', '0', ['four', '0']]

a = [1, 2, 3, [1, 2, 3]]
b = list(a)
b.append("test")
b[3].append("test2")
print("b:", b)         # will print b: [1, 2, 3, [1, 2, 3, 'test2'], 'test']
print("a:", a)         # will print a: [1, 2, 3, [1, 2, 3, 'test2']]

# searching for a value in a list
l3 = ['a', 'b', 'new', 'example', 'new']
print(l3.count('new'))  # will print 2
print('new' in l3)      # will print True
print('c' in l3)        # will print False
print(l3.index('example'))  # will print 3
print(l3.index('new', 3))    # will print 4
#print(l3.index('c'))    # ValueError: 'c' is not in list

# removing items from a list
l4 = ['a', 'b', 'new', 'example', 'new']
del l4[1]
print(l4)               # will print ['a', 'new', 'example', 'new']
l4.remove('new')
print(l4)               # will print ['a', 'example', 'new']
#l4.remove('c')          # ValueError: list.remove(x): x not in list

# list as a stack
l5 = ['a', 'b', 'new', 'example']
print(l5.pop())         # will print 'example'
print(l5)               # will print ['a', 'b', 'new']
print(l5.pop(1))        # will print 'b'
print(l5)               # will print ['a', 'new']
l5.pop()
l5.pop()
# l5.pop()                # IndexError: pop from empty list

# list comprehension
squares = [x**2 for x in range(10)]
print(squares)          # will print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# nested lists
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
transposed = []
for i in range(len(matrix)):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)       # will print [[1, 5, 9], [2, 6, 10], [3, 7, 11]]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
transposed = []
for i in range(len(matrix)):
    transposed.append([row[i] for row in matrix])
print(transposed)       # will print [[1, 5, 9], [2, 6, 10], [3, 7, 11]]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed)       # will print [[1, 5, 9], [2, 6, 10], [3, 7, 11]]

# zip
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
l = zip(list1, list2)
print(l)        # <zip object at 0x0302A760>
print(list(l))  # [(1, 'a'), (2, 'b'), (3, 'c')]

a = [1, 2, 3]
# same elements, but distinct objects
print(a[:2] == a[:2])   # will print True
print(a[:2] is a[:2])   # will print False

a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a1)               # will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[1:4] = [-1]
print(a1)               # will print [0, -1, 4, 5, 6, 7, 8, 9]


# Tuples
t1 = ('a', 'b', 'new', 'example', 2, True)
print(t1)           # will print ('a', 'b', 'new', 'example', 2, True)
print(t1[1])        # will print b
print(t1[2:4])      # will print ('new', 'example')

"""
tuples can't be changes; they are immutable
they have no method that allow changes, like append, insert, remove, ...
"""
#t1[1] = 'c'         # TypeError: 'tuple' object does not support item assignment
