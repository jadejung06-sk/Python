##### decorator
### merit
## simple code, common function
## logging, framework >> use this common function before functions (ex. django, tensorflow ...)
### demerit
## difficult debugging
## rather than a single function

import time
def perf_clock(func):
    ## free variables
    def perf_clocked(*args):
        st = time.perf_counter()
        
        ## start func.
        result = func(*args)
        #####
        
        et = time.perf_counter() - st
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{et:.5f}s] {name}({arg_str}) -> {result}')
        return result
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)
    
def sum_func(*numbers):
    return sum(numbers)

##### no decorator
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)
print(none_deco1, none_deco1.__code__.co_freevars) # <function perf_clock.<locals>.perf_clocked at 0x000002E715F2DE10> ('func',)
print(none_deco2, none_deco2.__code__.co_freevars)

none_deco1(1.5)
none_deco2(100, 200, 300, 400, 500)

##### using decorator
@perf_clock
def time_func(seconds):
    time.sleep(seconds)
    
@perf_clock
def sum_func(*numbers):
    return sum(numbers)

time_func(1.5)
sum_func(100, 200, 300, 400, 500)