import time
# from queue import Queue
from multiprocessing import Process, Queue # Very Important
'''
Not noraml queue package but the one in multiprocessing package
'''

def consumer(q):
    while True:
        txt = q.get()
        print(txt)
        time.sleep(1)
        
def producer(q):
    while True:
        q.put("Hello there")
        print("Message Sent")
        time.sleep(1)
        # time.sleep(1)
        
if __name__ == '__main__':
    # q = Queue()
    q = Queue(maxsize=10)
    p1 = Process(target = consumer, args= (q, ))
    p2 = Process(target = producer, args= (q, ))
    p1.start()
    p2.start()