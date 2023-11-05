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
def producer(queue, event):
    '''I/O 또는 네트워크 대기 상태로 서버'''
    while not event.is_set(): ## event 는 0이므로 not을 붙여줘야 계속 반복
        message = random.randint(1, 11)
        logging.info('Producer gets message: %s', message)
        queue.put(message)
        
    logging.info('Producer sends event in the end') ## event 0 to 1        

## 소비자 : 만들어진 data를 사용하는
def consumer(queue, event):
    '''CPU 작업으로 응답 받고 소비하는 사용자 or DB 저장 or web에 보여줌'''
    while not event.is_set() or not queue.empty(): ## queue가 비어있으면 실행하지 않음
        message = queue.get()
        logging.info('Consumer stores message : %s (size=%d)', message, queue.qsize())

    logging.info('Consumer received event in the end')


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
        executor.submit(consumer, pipeline, event) ## 함수, para1, para2 실행
        ## 실행 시간 조정 (실무 - 서버)
        # while True:
            # pass  
        ## 실행 시간 조정
        time.sleep(2)
        logging.info('Main : about to set event')
        ## 프로그램 종료
        event.set()
        