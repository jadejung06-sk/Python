"""
파이썬에서는 모든 것을 객체 취급
객체의 복사 종류 : copy, shallow copy, deep copy -> 정확한 이해 필요
가변 : list, set, dict
불변 : tuple, int, str, float, bool, unicode
"""
### call by value, call by reference, call by share

##### Ex 1 - copy (중요)
## call by reference (immutal)
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list
print('Ex 1 > ', id(a_list), id(b_list))

b_list[2] = 100
print('Ex 1 > ', id(a_list), id(b_list), a_list, b_list)

b_list[3][2] = 100
print('Ex 1 > ', id(a_list), id(b_list), a_list, b_list)

##### Ex 2 - shallow copy (중요)
## call by value
import copy
c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)
print('Ex 2 > ', id(c_list), id(d_list)) # 1503908096256 1503905131712

d_list[1] = 100 ## different reference
print('Ex 2 > ', id(c_list), id(d_list), c_list, d_list) 

d_list[3].append(1000) ## inner same reference
d_list[4][1] = 10000
print('Ex 2 > ', id(c_list), id(d_list), c_list, d_list) ## [1, 2, 3, [4, 5, 6, 1000], [7, 10000, 9]] [1, 100, 3, [4, 5, 6, 1000], [7, 10000, 9]]  

##### Ex 3 - deep copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list) ## inner call by reference

print('Ex 3 > ', id(e_list), id(f_list))

f_list[3].append(1000)
f_list[4][1] = 10000
print('Ex 3 > ', id(e_list), id(f_list), e_list, f_list)