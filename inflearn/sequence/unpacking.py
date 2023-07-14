##### unpacking b, a = a, b
print(divmod(100, 9))
print(divmod(*(100, 9)))
# print(divmod((100, 9))) # TypeError: divmod expected 2 arguments, got 1
print(*divmod(100, 9)) # 11 1
x, y, *rest = range(10)
print(x, y, rest) # 0 1 [2, 3, 4, ...]
x, y, *rest = range(2)
print(x, y, rest) # 0, 1 []
x, y, *rest = 0, 1, 2, 3, 4, 5
print(x, y, rest) # 0, 1 [2, 3, 4, 5]


##### immutable vs. mutable (memory)
t = (15, 20, 25)
l = [15, 20, 25]
print(t, id(t))
print(l, id(l))

t = t * 2
l = l * 2 # different id
print(t, id(t))
print(l, id(l)) # 1704727349824

t *= 2
l *= 2 # same id
print(t, id(t))
print(l, id(l)) # 1704727349824 # when the data used, the same id means low memory.

##### sort vs. sorted
## reverse, key = len, key= str.lower, key = func