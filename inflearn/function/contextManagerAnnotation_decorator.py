"""
Context Manager Annotation 
@contextlib.contextmanager, __enter__, __exit__
대표적인 with 구문
contextlib 데코레이터 사용 : 코드 직관적, 예외 처리 용이

"""
import contextlib
import time
##### Ex 1
# Use decorator

@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f ## == __enter__
    f.close() ## == __exit__

with my_file_writer("D:/2022/Python/inflearn/function/testfile4.txt", 'w') as f:
    f.write('Context Manager Test4.\nContextlib Test4.')
    
    
##### Ex 2
# Use decorator

@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try: ## __enter__
        yield start 
    except BaseException as e:
        print('Logging exception : {}: {}'.format(msg, e))
        raise
    else: ## __exit__
        print('{}: {:.3f}s'.format(msg, time.monotonic() - start))
        
        
with ExcuteTimerDc('Processing Time : ') as v:
    print('Received start monotonic2 : {}'.format(v))
    for i in range(1000000):
        pass
    raise ValueError('occurred.')