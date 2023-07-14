##### set : not ordered
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3} # set
s4_1 = {} # dict
s4 = set() # set
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}) # Read only

s1.add('Melon')
print(s1)
# s5.add('Melon') # AttributeError: 'frozenset' object has no attribute 'add'

##### byte codes -> python interpreter
from dis import dis
from unicodedata import name
print(dis('{10}'))
print(dis('set([10])'))
print({chr(i) for i in range(0, 256)})
print({name(chr(i),'' ) for i in range(0, 256)})
