##### generator (concurrency)
## councurrency : a cpu(a thread) runs several tasks at the same time. == remembers the last thing
## parallelism : cpus run several tasks at the same time.
## coroutine : a single thread == asyncronize tasks using stack == start and stop whenever it restarts  
## thread : os monitoring, CPU core in real time, asyncronize tasks (complex, context swiching overhead)
## yield : main <-> sub == duplex communication
def generator_ex1():
    print('Start')
    yield 'A Point' # ----1---- crawling on naver
    print('Countinue')
    yield 'B Point' # ----2---- crawling on google
    print('End')    # ----3----
    
# temp = generator_ex1() # <generator object generator_ex1 at 0x000002007D063E60>
temp = iter(generator_ex1()) # <generator object generator_ex1 at 0x0000028300FC1FC0>
# print(temp)
# print(next(temp))
# print(next(temp))
# print(next(temp)) # StopIteration
# for v in generator_ex1():
#     print(v)

temp2 = [x * 3 for x in generator_ex1()] # ['A PointA PointA Point', 'B PointB PointB Point']
temp3 = (x * 3 for x in generator_ex1()) # <generator object <genexpr> at 0x000001B262373E60>
# for i in temp3:
#     print(i)

##### count, takewhile, filterfalse, accumulate, chain, product, groupby ...
import itertools
gen1 = itertools.count(1, 2.5) # infinite
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1)) # ...
gen2 = itertools.takewhile(lambda n : n <1000, itertools.count(1, 2.5))
# for v in gen2:
#     print(v)

## filterfalse
gen3 = itertools.filterfalse(lambda n : n <3, [1,2,3,4,5]) # 4 5
# for v in gen3:
    # print(v)

## accumulate
gen4 = itertools.accumulate([x for x in range(1, 101)]) # 4950 5050
# for v in gen4:
    # print(v)
    
## chain 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5)) # ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

## chain 2
gen6 = itertools.chain(enumerate('ABCDE')) # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
print(list(gen6))

## product 1
gen7 = itertools.product('ABCDE') # [('A',), ('B',), ('C',), ('D',), ('E',)]
print(list(gen7))

## product 2 == number of cases
gen8 = itertools.product('ABCDE', repeat = 4) 
print(list(gen8))

## groupby
gen9 = itertools.groupby('AAABBCCCCDDEEE') # [('A', <itertools._grouper object at 0x0000016B3EC5BDF0>), ('B', <itertools._grouper object at 0x0000016B3EC5BD60>), 
# print(list(gen9))
for chr, group in gen9:
    print(chr, ':', list(group))
'''
A : ['A', 'A', 'A']
B : ['B', 'B']
C : ['C', 'C', 'C', 'C']
D : ['D', 'D']
E : ['E', 'E', 'E']
'''