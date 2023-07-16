##### Futures (concurrency == parallel tasks)
## async jobs (ABC) == A done B done C done End
## CPU (Delay time) and resource (File - network I/O)
## threading, multiprocessing (old version) -> futures packages (new easy version)
### futures has multithreading API and multiprocessing API
### promise 
### GIL == global interpreter lock : using two more threads, all the resource is locked. 
## to avoid GIL, use multiprocessing or CPython

##### concurrent.futures 1
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
# import threading
# import multiprocessing

WORK_LIST = [100000, 1000000, 10000000, 100000000]
# WORK_LIST = [func1, func2, func3, func4] # at the same time
# WORK_LIST = [https://naver.com, google, daum, ...] # at the same time
def sum_generator(n):
    return sum(n for n in range(1, n+1))

#########################################
##### concurrent.futures map 
# def main():
#     # worker count
#     worker = min(10, len(WORK_LIST))
#     # Start
#     start_tm = time.time()
#     ### result
#     ## ProcessPoolExecutor vs. ThreadPoolExecutor
#     with futures.ProcessPoolExecutor() as excutor: #  Result -> [5000050000, 500000500000, 50000005000000, 5000000050000000] Time : 4.01s
#     # with futures.ThreadPoolExecutor() as excutor: #  Result -> [5000050000, 500000500000, 50000005000000, 5000000050000000] Time : 4.43s
#         # map : start right now all jobs with the order of jobs
#         result = excutor.map(sum_generator, WORK_LIST)
#     # End
#     end_tm = time.time() - start_tm
#     msg = f'\n Result -> {list(result)} Time : {end_tm:.2f}s'
#     print(msg)
# if __name__ == '__main__':
#     main()
    
#########################################
##### concurrent.futures wait vs. concurrent.futures as_completed == yield
### sometimes fail or succeed
### different time for completing each jobs
def main():
    # worker count
    worker = min(10, len(WORK_LIST))
    # Start
    start_tm = time.time()
    futures_list = []
    ### result
    ## ProcessPoolExecutor vs. ThreadPoolExecutor
    with ProcessPoolExecutor() as excutor:
        for work in WORK_LIST:
            future = excutor.submit(sum_generator, work)
            futures_list.append(future)
            print(f'Scheduled for {work} : {future}')
        
        ##### concurrent.futures wait
        # ### wait & result    
        # result = wait(futures_list, timeout = 7)
        # # succeed
        # print('Completed Tasks : ' + str(result.done))
        # # failed
        # print('Pending ones after waiting for 7 seconds Tasks : ' + str(result.not_done))
        # # result
        # print([future.result() for future in result.done])
        # #####################
        
        ##### concurrent.futures as_completed == yield
        ### as_completed & result
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled
            
            print(f'Future Result : {result}, Done : {done}')
            print(f'Future Cancelled :{cancelled}') # state=finished
        
    # End
    end_tm = time.time() - start_tm
    msg = f'\nTime : {end_tm:.2f}s'
    print(msg)
if __name__ == '__main__':
    main()


#########################################

