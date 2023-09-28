"""
lambda : 익명, 힙 영역에서 사용 즉시 소멸(메모리 절약), pythonic code, 파이썬 가비지 컬렉션(count = 0) <-> 재사용성을 위한 일반 함수
reduce : 시퀀스형 전처리로 메모리 절약
map : 시퀀스형 전처리로 메모리 절약
filter : 시퀀스형 전처리로 메모리 절약

"""

##### Ex 1
cul = lambda a, b, c : a * b + c
print('Ex 1 > ', cul(10, 15, 20))
 
##### Ex 2 map
###
digits1 = [x * 10 for x in range(1, 11)]
print('Ex2 > ', digits1)
result = map(lambda i : i ** 2, digits1) # result = map(func, list) ## <map object at 0x00000207D1C35B70>
print(list(result))

###
def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)
print('Ex2 > ', list(also_square(digits1)))

##### Ex 3 filter
digits2 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = filter(lambda x : x % 2 == 0 ,digits2) # boolean

print('Ex3 > ', list(result2))
def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)

print('Ex 3-2 > ', list(also_evens(digits2)))


##### Ex 4 reduce
from functools import reduce

digits3 = [x for x in range(1, 101)]
result3 = reduce(lambda x, y : x + y, digits3)
print('Ex 4 > ', result3)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)

print('Ex 4 - 2 > ', also_add(digits3))