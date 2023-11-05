'''
Prod producer :
Cons consumer :

생산자 소비자 패턴 (producer/consumer pattern)
1. 멀티스레드 디자인 패턴의 정석
2. 서버측 프로그래밍의 핵심
3. 주로 허리 역할로 중요

Python Event 객체를 사용할 예정
1. Flag는 초기값이 0
2. set() 함수를 쓰면 1
3. clear() 함수를 쓰면 0
4. wait() 함수를 쓰면 1이면 리턴 / 0이면 대기
5. isSet() 함수는 현 flag 값을 알 수 있음
'''

import concurrent.futures
import logging
import queue
import random
import threading
import time

## 생산자 : data를 만들어내는 
def producer():
    pass

## 소비자 : 만들어진 data를 사용하는
def consumer():
    pass

if __name__ == "__main__":
    ## Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
    
    ## 적절한 사이즈 조절이 중요한 Queue
    pipeline = queue.Queue(maxsize = 10)
    
    ## 이벤트 플래그 초기값은 0
    event = threading.Event()
    
    ## with context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event) ## 함수, para1, para2 실행