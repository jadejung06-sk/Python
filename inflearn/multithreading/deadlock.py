'''
lock
deadlock
race condition
thread synchronization


1. semaphore 세마포어 : "여러 프로세스 간" 공유된 자원에 접근시 문제 발생 가능성
 경쟁 상태 예방, 한 개의 프로세스만 접근 처리 고안 
2. mutex 뮤텍스 : 공유된 자원의 데이터를 "여러 스레드"가 접근하는 것을 막는 것
 경쟁 상태 예방
3. lock : 상호 배제를 위한 잠금 처리
 데이터 경쟁 상태
4. deadlock : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황으로 교착 상태라고 함
5. thread synchronization (스레드 동기화)를 통해서 안정적으로 동작하게 처리 가능
 동기화 메소드, 동기화 블럭 가능
6. semaphoe와 mutex : 
 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용하는 공통점
 뮤텍스 개체는 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
 세마포어는 리소스에 대한 제한된 수를 동시 엑세스 소비 허용
 세마포어는 뮤텍스를 포괄하지만, 뮤텍스는 그렇지 않음 
'''
import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    def __init__(self):
        self.value = 0
        
        

if __name__ == "__main__":
    ## Logging Format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    ## 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info('Testing update. Started value is %d', store.value)
    
    ## with Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Thrid']:
            executor.submit(store.update, n)
            
    logging.info('Testing update. Finished value is %d', store.value)