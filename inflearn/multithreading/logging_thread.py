'''
Threading basic : thread는 logging 모듈을 함께 쓰는 것이 좋음
1. x.start()만 있는 경우, 서브 스레드는 메인 스레드가 종료되어도, 본인의 일을 끝까지 끝냄
2. x.start()이후 x.join()을 추가하면, 서브 스레드가 끝날 때까지 메인 스레드가 기다리고 끝냄
'''
import logging
import threading
import time

def thread_func(name):
    ## 서브 스레드 활용 코드
    logging.info("Sub-Thread %s : started", name) 
    time.sleep(3)
    logging.info("Sub-Thread %s : finished", name)
    
    

## 1. 메인 스레드 영역
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    ## 함수 인자 확인
    x = threading.Thread(target = thread_func, args = ('First', ))
    logging.info("Main-Thread: before running thread")
    
    ## 서브 스레드 시작
    x.start()     
    
    logging.info("Main-Thread: wait for the sub-thread to finish")
    logging.info("Main-Thread: the main-thread is done")
    
    
## 2. 메인 스레드 영역
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
#     logging.info("Main-Thread: before creating thread")
    
#     ## 함수 인자 확인
#     x = threading.Thread(target = thread_func, args = ('First', ))
#     logging.info("Main-Thread: before running thread")
    
#     ## 서브 스레드 시작
#     x.start()     
    # x.join()
    
#     logging.info("Main-Thread: wait for the sub-thread to finish")
#     logging.info("Main-Thread: the main-thread is done")