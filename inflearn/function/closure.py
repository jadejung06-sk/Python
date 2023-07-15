##### scope
## NameError
# def func_v1(a):
#     print(a)
#     print(b) # NameError: name 'b' is not defined    
# func_v1(10)
## global vs. local
# b = 20 # global
# def func_v2(a):
#     print(a) # local
#     print(b)
# func_v2(10)
## UnboundLocalError
# c = 30
# def func_v3(a):
#     print(a)
#     print(c) # UnboundLocalError: local variable 'c' referenced before assignment
#     c = 40
# func_v3(10)
## global vs. local
# c = 30
# def func_v3(a):
#     c = 40
#     print(a)
#     print(c)
# print('>>', c) 
# func_v3(10)  

##### global  #############################################
## before and after printing global variable
c = 30
def func_v3(a):
    global c
    print(a)
    print(c) # global
    c = 40 # global    
print('>>', c) 
func_v3(10)
print('>>>', c)
###########################################################

##### closure
## remembers local variables == concurrency control == deadlock control
## doens't share memory but sends a message
## shares all and reads only (immutable) == multithreads == coroutine programing
## snapshot == saves the state of variables in outer func. using outer func.
a = 100
## single
print( a + 100)
print( a + 1000)
## accumulate
print(sum(range(1, 51)))

##### class vs. closure
## using class
class Averager():
    def __init__(self):
        self._series = []
        
    def __call__(self, v): # like func.
        self._series.append(v)
        print(f'inner >> {self._series} / {len(self._series)}')
        return sum(self._series) / len(self._series)
averager_cls = Averager()
# print(dir(averager_cls)) __call__ == like func.
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
## using closure (saves the state of variables in outer func.)
def closure_ex1():
    ## free variables
    ## closure area
    series = []      # variable in outer func.
    def averager(v): # inner func.
        series.append(v)
        print(f"inner >>> {series} / {len(series)}")
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()
print(avg_closure1) # <function closure_ex1.<locals>.averager at 0x00000237FC02DF30>
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

##### function inspection
print(dir(avg_closure1)) # __call__ __closure__
print(dir(avg_closure1.__code__)) #  co_ ..., co_freevars
print(avg_closure1.__code__.co_freevars) # ('series',)
print(avg_closure1.__closure__[0])
print(dir(avg_closure1.__closure__[0])) # .cell_contents)
print(avg_closure1.__closure__[0].cell_contents)


##### bad example of closure
## bad case
def closure_ex2():
    # free variables
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1 # UnboundLocalError: local variable 'cnt' referenced before assignment
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))

## good case (nonlocal)
def closure_ex3():
    # free variables
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1 # UnboundLocalError: local variable 'cnt' referenced before assignment
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))
