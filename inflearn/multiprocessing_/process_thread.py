'''
process를 생성하는 것은 cost가 많이 사용됨
concurrent 동시성은 single core
parallel 병렬성은 multiple core (여러 source에서 데이터를 가져옴)

parallelism with multiprocessing
1. 완전히 동일한 타이밍(시점)에 task 실행
2. 다양한 파트(부분)로 나눠서 실행 1~2500 2501~5000 등으로 나눠서 구하고 취합함
3. 멀티프로세싱의 경우, cpu가 1 core인 경우에 병렬성 없음
4. 딥러닝, 비트코인 채굴 등에 사용 가능

process vs. thread
1. 독립된 메모리 (프로세스), 공유 메모리 (스레드)
2. 많은 메모리 필요 (프로세스), 적은 메모리 (스레드)
3. 좀비(데드)프로세서 생성 가능성이 큼 (프로세스), 좀비(데드) 스레드 생성 가능성 낮음 (스레드)
4. 오버헤드 큼 (프로세스), 오버헤드 작음 (스레드)
5. 생성/소멸 등 다소 느림 (프로세스), 생성/소멸이 다소 빠름 (스레드)
6. 코드 작성 쉬우나 디버깅 어려움 (프로세스), 코드 작성 어려우나 디버깅도 어려움 (스레드)
> 데이터를 공유하지 않기에 오버헤드가 크다고 할 수 있음

terminate
is_alive
'''

from multiprocessing import Process
import time
import logging


def proc_func(name):
    print('Sub Process : {} : started'.format(name))
    time.sleep(3)
    print('Sub Process : {} : finishsed'.format(name))

def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format , level = logging.INFO, datefmt= "%H:%M:%S")

    ## 함수 인자 확인
    p = Process(target=proc_func, args = ('First', ))
    
    logging.info('Main-Process : before creating Process')
    
    ## 프로세스
    p.start()
    
    logging.info('Main-Process : During Process')
    
    ## 즉시 종료
    # logging.info('Main-Process : Terminated Process')
    # p.terminate()
    ############ 
    
    logging.info('Main-Process : Joined Process')
    p.join()
    
    ## 프로세스 상태 확인
    print(f'Process p is alive : {p.is_alive()}')
    

## 메인 영역

if __name__ == "__main__":
    main()