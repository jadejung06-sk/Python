### single python tread
import time
from threading import Thread

### vs.
# def do_work():
#     print('Starting work')
#     time.sleep(1)
#     print('Finshed work')
    
def do_work():
    print('Starting work')
    i = 0
    for _ in range(20000000):
        i += 1
    print('Finshed work')
    

### vs.
# for _ in range(5):
    # do_work() 

for _ in range(5):
    # do_work()# CPU 9%
    t = Thread(target=do_work,args=())
    t.start() # CPU 11%
### 