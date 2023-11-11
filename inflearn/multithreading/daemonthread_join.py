'''
Daemon Thread(데몬 스레드)
1. 스레드 안에서 새로운 스레드를 만들어서 실행하기에 백그라운드에서 실행
2. **메인 스레드 종료 시, 즉시 강제 종료
3. 주로 메인 영역의 백그라운드는 무한 대기(while)하면서, 이벤트 발생 시에 실행하는 부분을 담당하는 보조적인 역할
 -> JVM (가비지 컬렉션), 문서 작업할 때 자동 저장되는 CASE, WEB SERVER의 용도로 사용 가능
 > 문서의 자동 저장 기능에 사용 가능
'''

import logging
import threading
import time

def thread_func(name, nums):
    ## 서브 스레드 활용 코드
    logging.info("Sub-Thread %s : started", name) 
    # time.sleep(3)
    for num in nums:
        print(num)
    logging.info("Sub-Thread %s : finished", name)
    
    

## 1. 메인 스레드 영역
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    ## 함수 인자 확인 + daemon thread
    x = threading.Thread(target = thread_func, args = ('First', range(20000)), daemon= True)
    y = threading.Thread(target = thread_func, args = ('Second',range(10000)), daemon= True)
    logging.info("Main-Thread: before running thread")
    
    ## 서브 스레드 시작
    x.start()
    y.start()
    
    ## Daemon Thread인지 확인
    print(x.isDaemon())
    print(y.isDaemon())    
    
    logging.info("Main-Thread: wait for the sub-thread to finish")
    logging.info("Main-Thread: the main-thread is done")
    
    
## 2. 메인 스레드 영역
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
#     logging.info("Main-Thread: before creating thread")
    
#     ## 함수 인자 확인 + daemon thread
#     x = threading.Thread(target = thread_func, args = ('First', range(20000)), daemon= True)
#     y = threading.Thread(target = thread_func, args = ('Second',range(10000)), daemon= True)
#     logging.info("Main-Thread: before running thread")
    
#     ## 서브 스레드 시작
#     x.start()
#     y.start() 

#     ## 대기 기능 (daemon thread의 경우에는 상충되는 역할로 사용하지 말 것)
#     x.join()
#     y.join()    
#     logging.info("Main-Thread: wait for the sub-thread to finish")
#     logging.info("Main-Thread: the main-thread is done")