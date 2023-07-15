##### generator (concurrency)
## councurrency : a cpu(a thread) runs several tasks at the same time. == remembers the last thing
## parallelism : cpus run several tasks at the same time.
## coroutine : a single thread == asyncronize tasks using stack == start and stop whenever it restarts  
## thread : os monitoring, CPU core in real time, asyncronize tasks (complex, context swiching overhead)
## yield : main <-> sub == duplex communication
## generator or coroutine or functions in def

##### coroutine
def coroutine1():
    print('>>> coroutine started') # ---- 1 ----
    i = yield
    print(f'>>> coroutine received : {i}') # ---- 2 ----
    
## main routine
cr1 = coroutine1()
print(cr1, type(cr1)) # <generator object coroutine1 at 0x000002BC6C053E60> <class 'generator'>
# next(cr1)
# next(cr1) # StopIteration != not raise in for setence

## send() == main routine <-> sub routine
# next(cr1)
# cr1.send(100) # has next(), default = None


##### bad example
### at the yield, you can use send()
## TypeError: can't send non-None value to a just-started generator
cr2 = coroutine1()
cr2.send(100)
