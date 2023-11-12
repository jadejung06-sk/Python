'''
동시 프로그래밍 패러다임 변화 
싱글 코어 -> 처리향상 미미 -> 비동기 프로그래밍 대두 -> CPU연산, DB연동, API 호출 대기 시간 늘어남 -> Non Blocking
자바스크립트는 비동기식
파이썬 3.4에서 비동기 표준라이브러리 등장 (asyncio)
 비동기식함수에서 비동기식함수를 부르려면 async def 함수 내 await 함수를 활용해야함
 순서가 보장되어 있지 않음
 만들어진 함수를 가져오더라도 await 함수로 무조건 활용해야한다 (비동기 함수를 검색해서 사용해야함)
async def함수는 coroutine Object을 생성함

'''

import time
import asyncio


async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        # time.sleep(1)
        # asyncio.sleep(1) ## RuntimeWarning: Enable tracemalloc to get the object allocation traceback
        await asyncio.sleep(1)
    print(f'{name} - {n} done!')


async def process_async():
    start = time.time()
    
    await asyncio.wait([    
    exe_calculate_async('one', 3),
    exe_calculate_async('two', 2),
    exe_calculate_async('three', 1)
    ])
    
    end = time.time()
    
    print(f'>>> total seconds : {end - start}')


def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} done!')

def process_sync():
    start = time.time()
    
    exe_calculate_sync('one', 3)
    exe_calculate_sync('two', 2)
    exe_calculate_sync('three', 1)
    
    end = time.time()
    
    print(f'>>> total seconds : {end - start}')


if __name__ == "__main__":
    ## Sync 실행
    # process_sync()
    
    ## Async 실행
    ## 파이썬 3.7 이상인 경우
    asyncio.run(process_async())
    ## 파이썬 3.7 미만인 경우
    # asyncio.get_event_loop().run_until_complete(process_sync())