##### generator (concurrency)
## councurrency : a cpu(a thread) runs several tasks at the same time. == remembers the last thing
## parallelism : cpus run several tasks at the same time.
## coroutine : a single thread == asyncronize tasks using stack == start and stop whenever it restarts  
## thread : os monitoring, CPU core in real time, asyncronize tasks (complex, context swiching overhead)
## yield, send : main <-> sub == duplex communication
## generator or coroutine or functions in def
### python 3.5 upper
## def == async, yield == await

##### coroutine
def coroutine1():
    print('>>> coroutine started') # ---- 1 ----
    i = yield
    print(f'>>> coroutine received : {i}') # ---- 2 ----
    
## main routine
cr1 = coroutine1()
# print(cr1, type(cr1)) # <generator object coroutine1 at 0x000002BC6C053E60> <class 'generator'>
# next(cr1)
# next(cr1) # StopIteration != not raise in for setence

## send() == main routine <-> sub routine
# next(cr1)
# cr1.send(100) # has next(), default = None


##### bad example
### at the yield, you can use send()
## TypeError: can't send non-None value to a just-started generator
# cr2 = coroutine1()
# cr2.send(100)

##### get generator state
## GEN_CREATED : the first idle state
## gen_running : the running state
## GEN_SUSPENDED : yield idle state
## gen_closed : done
from inspect import getgeneratorstate
def coroutine2(x):
    print(f'>>> coroutine started : {x}') # ---- 1 ---- 
    y = yield x # (main) y gets val <-> (sub) yield x sends 
    print(f'>>> coroutine received : {y}') # ---- 2 ----
    z = yield x + y # (main) y gets val <-> (sub) yield x sends
    print(f'>>> coroutine received : {z}') # ---- 3 ----
    
cr3 = coroutine2(10)
print(getgeneratorstate(cr3))
print(next(cr3))
print(getgeneratorstate(cr3))
cr3.send(100)

##### duplicated coroutine
## StopIteration -> await (python 3.5 upper)

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y
        
t1 = generator1()
print(next(t1)) # A
print(next(t1)) # B
print(next(t1)) # 1
print(next(t1))
print(next(t1))
# print(next(t1)) # StopIteration

t2 = generator1()
print(list(t2))

def generator2():
    yield from 'AB'
    yield from range(1, 4)
    
t3 = generator2()
print(next(t3)) # A
print(next(t3)) # B
print(next(t3)) # 1
print(next(t3))
print(next(t3))
# print(next(t3)) # StopIteration
