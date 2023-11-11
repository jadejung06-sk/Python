'''
ProcessPoolExecutor
as_completed
futures
timeout
dict

'''
from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

## 조회 urls
URLS = ['http://www.daum.net/', 'http://www.cnn.com/', 'http://naver.com', 'http://ruliweb.com', 'http://some-made-up-domain.com']

## 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout = timeout) as conn:
        # print(conn.read())
        return conn.read()

def main():
    ## ProcessPool Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        ## Futures 로드만 실행이 아님
        future_to_url = {executor.submit(load_url, url, 5) : url for url in URLS}
        
        ## 중간 확인
        # print(future_to_url)
        
        for future in as_completed(future_to_url): ##
            ## key 값이 Future 객체 / value 값은 url
            # print('futue : ', future) ## <Future at 0x20118556800 state=finished returned bytes>
            url = future_to_url[future] ## == future_to_url.get()

            try:
                data = future.result() ##
            except Exception as exc:
                ## 에외 처리
                print('%r generated an exception : %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))
                ## 'http://ruliweb' generated an exception : <urlopen error [Errno 11001] getaddrinfo failed> -> http://ruliweb.com


## 메인 시작
if __name__ == "__main__":
    main()