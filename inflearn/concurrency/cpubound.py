'''
CPU BOUND : 싱글 프로세스인 경우, 시간에 따라서 작업을 수행함 (멀티 프로세싱 패키지 활용시, 성능 극대화)
 프로세스 진행이 CPU 속도에 의해 제한(결정) -> 행렬곱, 고속연산, 압축파일, 집합연산에 CPU에서 연산 위주 작업
 I/O 작업이 최소화이면서, CPU 연산이 위주인 작업
I/O BOUND : 싱글 프로세스인 경우, IO Wating 시간이 수반되어 작업을 수행함
 파일 쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 작업에 의해서 병목(수행시간)이 결정
 CPU 성능 지표가 수행시간 단축에 크게 영향을 미치지 않음
 메모리 바인딩, 캐시 바운딩
 작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요함
 
Synchronous
'''

##### CPU Bound
import time

## 실행 함수1 (계산)
def cpu_bound(number):
    return sum(i * i for i in range(number))

## 실행 함수2
def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    ## 확인
    print(numbers, type(numbers))
    
    ## 실행 시간 측정
    start_time = time.time()
    
    
    ## 실행
    total = find_sums(numbers)
    print()

    ## 결과 출력
    print(f'Total list : {total}')
    print(f'Sum : {sum(total)}')
    
    ## 실행 시간 종료
    duration = time.time() - start_time
    print()
    
    ## 수행시간
    print(f'Duration : {duration} seconds')

if __name__ == "__main__":
    main()

