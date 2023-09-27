"""
Chapter 1
scope
global
nonlocal
locals
globals
"""

##### Ex 1
a = 10 # global variable
def foo():
    # Read global variable
    print('Ex 1 > ', a)    
foo()
# Read global variable
print('Global : ', a)

##### Ex 2
b = 20
def bar():
    b = 30 # Local variable
    print('Ex 2 > ', b) # Read local variable
bar()
print('Global : ', b)

##### Ex 3
c = 40
def foobar():
    # c = c + 10
    # c += 10
    print('Ex 3 > ', c) # UnboundLocalError: local variable 'c' referenced before assignment   
foobar()

##### Ex 4 : global (중요)
d = 50
def barfoo():
    global d
    d = 60
    d += 100 # 160
    print('Ex 4 > ', d)
    
barfoo()
print('Ex4 > ', d) # 160

##### Ex 5 (중요)
'''
def outer():
    e = 70 # local variable
    def inner():
        e += 10 # UnboundLocalError: 
        print('Ex5 > ', e)
    return inner
in_test = outer() # closure
in_test()
'''
def outer():
    e = 70 # local variable
    def inner():
        nonlocal e # not inner local variable
        e += 10 #  
        print('Ex5 > ', e)
    return inner
in_test = outer() # closure
in_test() # keep variable 80
in_test() # keep variable 90
