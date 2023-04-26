import time
from threading import Thread, Condition

### Instead of Lock, Condition Variables 


class StingySpendy:
    money = 100
    # mutex = Lock()
    cv = Condition()
    
    def stingy(self):
        for i in range(1000000):
            self.cv.acquire()
            # self.mutex.acquire() #
            self.money += 10
            # self.mutex.release() #
            self.cv.notify()
            self.cv.release()
        print("Stingy Done")
        
    def spendy(self):
        for i in range(500000): # the same amount 500000 x 20
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
                
            # self.mutex.acquire() #
            # self.money -= 10
            self.money -= 20
            if self.money < 0:
                print('Money in bank', self.money)
            # self.mutex.release() #
            self.cv.release()
        print("Spendy Done")
        
        
ss = StingySpendy()
Thread(target = ss.stingy, args = ()).start()
Thread(target = ss.spendy, args = ()).start()
time.sleep(5)
print('Money in tne end', ss.money)

## The case of something without # 
'''
every time, ss.money is different
'''