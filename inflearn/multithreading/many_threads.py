'''
many threads == group thread을 사용할 경우, concurrent.Futures package 활용
코드의 가독성도 좋고, 라이프 사이클을 쉽게 관리 가능
(Thread)PoolExecutor 활용

Group Thread
1. Python 3.2 이상 표준 라이브러리에서 사용 가능
2. concurrent.Futures 패키지에서 활용
3. with 사용으로 생성하고, 소멸하여 라이프사이클을 관리하기 용이
4. 디버깅하기가 난해하다는 단점이 있음
5. 대기중인 작업이 존재하는 경우에 Queue를 활용하여, 완료 상태를 조사하여, 결과 또는 예외를 확인할 수 있음
 -> 단일화(캡슐화)
'''

import logging
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    logging.info("Sub-Thread %s : started", name)
    result = 0
    for i in range(10001):
        result += i
    logging.info("Sub-Thread %s : finished result : %d", name, result)
    return result


def main():
    ##### 1. 실행 방법1 (좋은 방법은 아닌 형태)
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")    
    # logging.info("Main-Thread: before creating and running thread")

    # ## 실행 방법1
    # # max_workers : 작업의 개수가 넘어가면, 직접 설정이 유리
    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ('First', ))
    # task2 = excutor.submit(task, ('Second', ))
    # ## 결과 값이 있는 경우 (return) / 없는 경우에는 None
    # print(task1.result())
    
    ##### 2. 실행 방법2 (더 나은 방법)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")    
    logging.info("Main-Thread: before creating and running thread")

    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ['First', 'Second'])
        ## 결과 값이 있는 경우 (return) / 없는 경우에는 None
        print(list(tasks))

if __name__ == "__main__":
    main()