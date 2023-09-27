"""
Chapter 1
scope
global 전역변수는 주로 변하지 않는 고정 값에 사용, 전역 변수를 지역 내에서 수정하는 것을 권장하지 않음
nonlocal 지역변수는 함수 내에 로직 해결에 국한하여 소멸주기를 함수 실행 해제
locals()
globals()
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

##### Ex 5 (중요, 클로저 활용)
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

##### Ex 6 (지역 변수 전체 출력)
def func(var):
    x = 10
    def printer():
        print('Ex6 > ', 'Printer Func Inner')
    print('Func Inner', locals())
    
func('Hi')

##### Ex 7 (전역 변수 전체 출력)
test_variable = 100 
'''
== globals()['test_variable] = 100
'''
print('Ex7 > ', globals())

##### Ex 8 (중요, 지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k

print('Ex8 > ', plus_5_5)
print('Ex8 > ', plus_9_2)