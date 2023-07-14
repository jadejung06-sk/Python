##### hash table : data with keys and values == dict
## no duplicated keys == immutable
print(__builtins__.__dict__)
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
# print(hash(t1)) # In hash, immutable
# print(hash(t2)) # TypeError: unhashable type: 'list'


##### usage of dict Setdefault 
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}
## no use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v] # {'k1': ['val1']}
        # break
print(new_dict1)
## use setdefault
for k, v in source:
    # new_dict2.setdefault(k, v) #  {'k1': 'val1', 'k2': 'val3'}
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)
## nothing
new_dict3 = {k : v for k, v in source}
print(new_dict3) # {'k1': 'val2', 'k2': 'val5'}