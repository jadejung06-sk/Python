'''
memory sharing
array
value
data
'''
##### 프로세스 메모리 공유 비교 예제로 공유 안 되는 경우
# from multiprocessing import Process, current_process
# import os
## 실행 함수
# def generate_update_number(v: int):
#     for _ in range(50):
#         v += 1
#     print(current_process().name, "data", v)
   
# def main():
#     ## 부모 프로세스 아이디
#     parent_process_id = os.getpid()
#     print(f'Parent Process ID {parent_process_id}')
    
#     ## 프로세스 리스트 선언
#     processes = list()
    
#     ## 프로세스 메모리 공유 변수
#     shared_value = 0
    
#     for _ in range(1, 10):
#         ## 생성
#         p = Process(target = generate_update_number, args = (shared_value, ))
#         ## 배열 담기
#         processes.append(p)
#         p.start()
        
#     ## join
#     for p in processes:
#         p.join()
#     print('shared_value : ', shared_value) ## 0
# if __name__ == "__main__":
#     main()
    
    
##### 프로세스 메모리 공유 비교 예제로 공유되는 경우
# >>> https://docs.python.org/3/library/multiprocessing.shared_memory.html
# from multprocessing import shared_memory
# from multiprocessing import Manager
from multiprocessing import Process, current_process, Value, Array
import os
## 실행 함수
def generate_update_number(v: int):
    for _ in range(50):
        v.value += 1 ## v.value
    print(current_process().name, "data", v.value)
   
def main():
    ## 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f'Parent Process ID {parent_process_id}')
    
    ## 프로세스 리스트 선언
    processes = list()
    
    ## 프로세스 메모리 공유 변수
    # shared_value = 0
    shared_value = Value('i', 0) ## i, f, c, l  
    ## shared_numbers = Array('i', range(50))
    
    
    for _ in range(1, 10):
        ## 생성
        p = Process(target = generate_update_number, args = (shared_value, ))
        ## 배열 담기
        processes.append(p)
        p.start()
        
    ## join
    for p in processes:
        p.join()
    print('shared_value : ', shared_value) ## 0 
    
    '''
    TypeError: unsupported operand type(s) for +: 'Synchronized' and 'int'
    shared_value :  <Synchronized wrapper for c_long(0)>  ## Object
    '''
    
    
if __name__ == "__main__":
    main()