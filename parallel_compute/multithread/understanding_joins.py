import time
from threading import Thread

def child():
    print("Child Thread doing work...")
    time.sleep(5)
    print("Child Thread done...")
    
def parent():
    t = Thread(target=child, args = ([]))
    t.start()
    print("Parent Thread is wating...")
    t.join()
    print("Parent Thread is unblocked...")
    
parent()

'''
Child Thread doing work...
Parent Thread is wating...
Child Thread done...
Parent Thread is unblocked...
'''