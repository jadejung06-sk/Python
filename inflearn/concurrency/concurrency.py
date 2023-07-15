#####
## generator returns iterator
## iterable == collections, text file, list, dict, set, tuple, unpacking, *args ... == iter(x) 

## 
t = "ABCDEFGHIJKLMNOPQRSTQVWXYZ" # __iter__

for c in t:
    print(c)
##     
w = iter(t)
# print(dir(w)) # __next__
# print(next(w))
# print(next(w))
# print(next(w)) # remember the index and value
while True:
    try:
        print(next(w))
    except StopIteration:
        break

##### check iterabilty
from collections import abc # abstract class
print(dir(t)) 
print(hasattr(t, '__iter__')) # True
print(isinstance(t, abc.Iterable))

##### class next pattern like generator
# next()
# class WordSplitter:
#     def __init__(self, text):
#         self._idx = 0
#         self._text = text.split(' ')
        
#     def __next__(self):
#         print("Called __next__")
#         try:
#             word = self._text[self._idx]
#         except IndexError:
#             raise StopIteration('Stopped Itertion.')
#         self._idx += 1
#         return word
    
#     def __repr__(self):
#         return f'WordSplit({self._text})'
    
# wi = WordSplitter('Do today what you could do tomorrow')
# print(wi)
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))

##### generator pattern
## big list, dictionary, set > generator
## corotine
## low memory

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
        
    def __iter__(self):
        for word in self._text:
            yield word # generator (remember index and value)
            
    def __repr__(self):
        return f'WordSplitGenerator({self._text})'
    
    
wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg) #  <generator object WordSplitGenerator.__iter__ at 0x000001922E3A3D10
print(wg, wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt)) # StopIteration