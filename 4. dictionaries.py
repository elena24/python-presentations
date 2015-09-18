"""
create a new dictionary
"""
d1 = {'key1': 'value1', 'key2': 'value2'}
print(d1)           # will print {'key2': 'value2', 'key1': 'value1'}
print(d1['key1'])   # will print value1
# print(d1['value1']) # KeyError: 'value1'
d = dict([('k1', 4139), ('k2', 4127), ('k3', 4098)])
print(d)            # will print {'k1': 4139, 'k2': 4127, 'k3': 4098}
new_dict = {x: x**2 for x in (2, 4, 6)}
print(new_dict)     # will print {2: 4, 4: 16, 6: 36}

d2 = {"even": [0, 2, 4, 6, 8], "odd": [1, 3, 5, 7, 9]}
print(len(d2))          # will print 2
print("even" in d2)     # will print True
print(d2["even"][1])    # will print 2

"""
modify a dictionary
"""
d3 = {'k1': 1, 'k2': 2, 'k3': 3}
print(d3)           # will print {'k1': 1, 'k2': 2, 'k3': 3}
d3['k1']=3
print(d3)           # will print {'k1': 3, 'k2': 2, 'k3': 3} or {'k2': 2, 'k3': 3, 'k1': 3} or ...
d3['k4']=4
print(d3)           # will print {'k1': 3, 'k4': 4, 'k2': 2, 'k3': 3} or {'k2': 2, 'k4': 4, 'k3': 3, 'k1': 3} or ...

"""
find keys and values
"""
d4 = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
print(d4.keys())        # will print dict_keys(['k3', 'k1', 'k4', 'k2'])
print(d4.values())      # will print dict_values([1, 2, 4, 3])
print(list(d4.keys()))  # print ['k3', 'k4', 'k2', 'k1']


d5 = {"key": {"deeper": {"more": {"enough": "value"}}}}
print(d5['key']['deeper'])  # will print {'more': {'enough': 'value'}}

"""
looping
"""
d5 = {'key1': 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
for k, v in d5.items():
    print(k, v)

for k in d5.keys():
    print(k, d5[k])

"""
setdefault method
"""
a = {}
a.setdefault('b', 1)
print(a['b'])           # will print 1
a.setdefault('b', 2)
print(a['b'])           # will print 1
