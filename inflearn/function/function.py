##### first fucntion
## runtime init
## variable
## func for args
## return func.

def factorial(n):
    '''Factorial function -> n : int'''
    if n == 1:
        return 1
    return n * factorial(n - 1)

class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A)) # <class 'function'> 
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
'''{'__get__', '__globals__', '__annotations__', '__defaults__', '__call__', '__builtins__', '__closure__', '__qualname__', '__name__', '__kwdefaults__', '__code__'}'''
print(factorial.__name__)
print(factorial.__code__) # <code object factorial at 0x000001BCE02EFD60, file "d:\2022\Python\inflearn\function\function.py", line 7>

##### variables
var_func = factorial
print(var_func) # <function factorial at 0x000001BCE0213E20>
print(var_func(10)) # 3628800
print(map(var_func, range(1, 11))) # <map object at 0x000002ADFE96E710>
print(list(map(var_func, range(1, 11))))

##### higher-order function
## map, filter
## es6
print(list(map(var_func, filter(lambda x : x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2]) # odds
## reduce
from functools import reduce
from operator import add
print(reduce(add, range(1, 11))) # cumsum
print(sum(range(1, 11)))
## lambda
print(reduce(lambda x, t : x + t, range(1, 11)))

##### callable : method == function() True / False
print(callable(str), callable(A), callable(var_func), callable(factorial), callable(3.14))
# str('a')
# 3.14() # X
# A()
# var_func()
# factorial()

###### partial == callaback function
from operator import mul
from functools import partial

print(mul(10, 10))
# fixed arg
five = partial(mul, 5) # 5 * 
print(five(10))
print(five(100))
six = partial(five, 6)
print(six()) # 30
# print(six(10)) # TypeError: mul expected 2 arguments, got 3
print([five(i) for i in range(1, 10)])
print(list(map(five, range(1, 10))))