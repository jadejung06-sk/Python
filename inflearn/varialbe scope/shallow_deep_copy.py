"""
파이썬에서는 모든 것을 객체 취급
객체의 복사 종류 : copy, shallow copy, deep copy -> 정확한 이해 필요
가변 : list, set, dict
불변 : tuple, int, str, float, bool, unicode
"""

##### Ex 1 - copy (중요)
### call by value, call by reference, call by share
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list
print('Ex 1 > ', id(a_list), id(b_list))

b_list[2] = 100
print('Ex 1 > ', id(a_list), id(b_list), a_list, b_list)

b_list[3][2] = 100
print('Ex 1 > ', id(a_list), id(b_list), a_list, b_list)

##### Ex 2 - shallow copy
import copy



##### Ex 3 - deep copy
