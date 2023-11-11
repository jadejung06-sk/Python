'''
Queue
Pipe
Commnunications between processes
'''

## 프로세스 통신 구현 Pipe
from multiprocessing import Process, Pipe, current_process
import time
import os


## 실행 함수 영역
def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name
    
    ## 누적
    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
        
    ## Produce
    # q.put(sub_total)
    conn.send(sub_total)
    conn.close()

    ## 정보 출력
    print(f'Process ID: {process_id}, Process name: {process_name} ID : {id}')
    print(f'Result : {sub_total}')

def main():
    pass
    ## 부모 프로세스 아이디
    parent_process_id = os.getpid()
    ## 출력
    print(f'Parent Proceess ID {parent_process_id}')
    
    
    ## 프로세스 리스트 선언
    # processes = list()
    
    ## 시작 시각
    start_time = time.time()
    
    ## Pipe 선언
    # q = Queue()
    parent_conn, child_conn = Pipe()
    # for i in range(3): ## 활용 Process 갯수에 따라 시간이 다르게 걸리는 것 확인 가능 
    t = Process(name = '1', target = worker, args= (1, 100000000, child_conn ))
        # t = Process(name = str(i), target = worker, args= (i, 100000000, q ))
        # processes.append(t)
        # t.start()
    t.start()
    # for process in processes:
        # process.join()
    t.join()
    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))
    # 종료 플래그
    # q.put('exit')
    ## 무한대기
    # total = 0 
    # while True:
    #     tmp = q.get()
    #     if tmp == 'exit':
    #         break
    #     else:
    #         total += tmp
            
    print()
    
    print('Main - Processing Total Count = {}'.format(parent_conn.recv()))
    print('Main - Processing Done!')


if __name__ == "__main__":
    main()