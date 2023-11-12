'''

Multiprocessing vs. Threading vs. AsyncIO
CPU Bound
I/O Bound
Async IO 

CPU BOUND : 싱글 프로세스인 경우, 시간에 따라서 작업을 수행함 (멀티 프로세싱 패키지 활용시, 성능 극대화)
 프로세스 진행이 CPU 속도에 의해 제한(결정) -> 행렬곱, 고속연산, 압축파일, 집합연산에 CPU에서 연산 위주 작업
 CPU 연산 위주 작업
I/O BOUND : 싱글 프로세스인 경우, IO Wating 시간이 수반되어 작업을 수행함
 파일 쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 작업에 의해서 병목(수행시간)이 결정
 CPU 성능 지표가 수행시간 단축에 크게 영향을 미치지 않음
 메모리 바인딩, 캐시 바운딩
 작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요함 
sync / async는 기다림은 동일하며, 단지 작업 완료 여부를 알려주는 주체만이 다름

Multiprocessing : Multiple processes, 고가용성(CPU) utilization -> CPU Bound -> 10개 부엌에 10명의 요리사가, 10개의 요리를 진행함
Threading : Single(Multi) process, Multiple threads, OS decides task switching -> Fast I/O Bound -> 1개 부엌에 10명의 요리사가 10개의 요리를 진행함
Async IO : Single process, single thread, cooperative multitasking, tasks cooperatatively decide switching -> Slow I/O Bound -> 1개 부엌에서 1명의 요리사가 10개의 요리를 진행함


I/O Bound, requests 
'''
##### I/O Bound GIL
import concurrent.futures
import threading
import requests
import time

## 각 스레드에 생성되는 객체(독립된 네임스페이스)
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"): ## attribute가 존재하는지 묻는 함수, dict으로 추가
        thread_local.session = requests.Session()
    return thread_local.session
        
## 실행함수1 (다운로드)
def request_site(url): ##
    
    session = get_session() 
    ## 세션 확인
    print(session)
    # print(session.headers)
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, status Code : {response.status_code}] from {url}')

## 실행함수2 (요청)
def request_all_sites(urls):
    ## 멀티스레드 실행
    ## 반드시 max_worker 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)
        '''
        requst_site(url, session)
        Downloaded 9 sites in 0.006001472473144531 seconds
        '''


def main():
    ## 테스트 URLS
    urls = ["https://www.jython.org", "http://olympus.realpython.org/dice", "https://realpython.com"] * 3

    ## 실행 시간 측정
    start_time = time.time()

    ## 실행
    request_all_sites(urls)   
    
    ## 실행 시간 종료
    duration = time.time() - start_time
    print()
    
    ## 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()