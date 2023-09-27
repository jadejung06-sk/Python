"""
lambda : 익명, 힙 영역에서 사용 즉시 소멸(메모리 절약), pythonic code, 파이썬 가비지 컬렉션(count = 0) <-> 재사용성을 위한 일반 함수
reduce : 시퀀스형 전처리로 메모리 절약
map : 시퀀스형 전처리로 메모리 절약
filter : 시퀀스형 전처리로 메모리 절약

"""

##### Ex 1
cul = lambda a, b, c : a * b + c
print('Ex 1 > ', cul(10, 15, 20))

##### Ex 2
digits1 = [x * 10 for x in range(1, 11)]
print('Ex2 > ', digits1)
result = map(lambda i : i ** 2, digits1) # result = map(func, list) ## <map object at 0x00000207D1C35B70>
print(list(result))