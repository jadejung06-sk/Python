##### Sequence (Ordered)
### Category
## Container : all kinds of types (list, yuple, collections.deque) 
# ex) [3, 3.0, 'a']
## Flat : only one type (str, bytes, bytearray, array.array, memoryview) 

### mutable vs. immutable
## mutable (list, bytearray, array.array, memoryview, deque)
## immutable (tuple, str, bytes)

##### Comprehending lists + map, fliter(func or data)
## Sequence Flat immutable str
chars = '+-)(*&^%$#@!)'
# chars[2] = 'h' # TypeError: 'str' object does not support item assignment (immutable)
code_list1 = []
for s in chars:
    code_list1.append(ord(s)) # str to unicode
print(code_list1) 
code_list2 = [ord(s) for s in chars]
print(code_list2)
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list3, code_list4)
print([chr(s) for s in code_list1]) # unicode to str
print([chr(s) for s in code_list2]) # unicode to str
print([chr(s) for s in code_list3]) # unicode to str
print([chr(s) for s in code_list4]) # unicode to str

##### generator : make a sequence == powerful iterrator (memory X, one item once)
print(dir(chars)) # '__iter__', ... 
### Sequence flat mutalbe array.array
## tuple generator
import array
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(tuple_g) # <generator object <genexpr> at 0x000001B423207C30> make a sequence yet
print(type(tuple_g)) # <class 'generator'>
# print(next(tuple_g)) # 43
# print(next(tuple_g)) # 45
# print(next(tuple_g)) # 41
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g)) # StopIteration
# print(next(tuple_g))
## array
print(array_g)
print(type(array_g)) # <class 'array.array'>
print(array_g.tolist()) # [43, 45, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33, 41]

## Usage of generator
print((f'{c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)}')) # <generator object <genexpr> at 0x00000227AF707CA0>
for s in (c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
    print(s)