'''
pip install asyncio
pip install beautifulsoup4
'''

'''
Async IO 비동기 IO Coroutine 작업에 사용
Non-blocking 비동기 처리
'''

##### Non-blocking vs. blocking
## Non-blocking IO : 호출된 함수가 return 후, 호출한 함수 (메인 루틴)에 제어권 전달, 타 함수는 일을 계속함
## blocking IO : 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 가지고 있어, 타 함수는 대기함
### But requests, urllib 은 blocking이기에, asyncIO와 함께 써도 non-blocking이 안 됨

##### Thread vs. Coroutine
## coroutine : 하나의 루틴만 실행하여, 락 관리가 필요 없음. 제어권으로 실행하는 방식, 사용 함수가 비동식으로 고려하여 코딩 필요
## thread : 디버깅 어렵고, 자원 접근 시 레이스컨디션(경쟁상태), 데드락(dead lock) 등의 고려할 부분이 있어서, 고려하며 코딩 필요
### asyncIO : Coroutine에서 확장된 비동기 IO 방식
import sys
import io
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup

start = timeit.default_timer()

urls = ["http://daum.net", "https://naver.com", "http://mlbpark.donga.com", "https://tistory.com", "https://wemakeprice.com/"]

async def fetch(url, executor):
    print('Thread name : ', threading.current_thread().getName(), 'Start', url)
    res = await loop.run_in_executor(executor, urlopen, url) ## loop in main   
    soup = BeautifulSoup(res.read(), 'html.parser')
    # print(soup.prettify()) ## 전체 페이지 소스
    result_data = soup.title ## Title
    print('Thread name : ', threading.current_thread().getName(), 'Done', url)
    return result_data

async def main():
    executor = ThreadPoolExecutor(max_workers=10)
    ## future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    ## 결과 취합
    rst = await asyncio.gather(*futures)
    print()
    print('Result : ', rst)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start
    print("Total Runnning Time : ", duration)