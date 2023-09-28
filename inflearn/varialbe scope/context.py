"""
Context Manager : 원하는 타이밍에 정확하게 리소스를 할당하고 제공, 반환하는 역할 - 가장 대표적인 with 구문 이해 필요
Contextlib
__enter__
__exit__
exception
"""

##### Ex 1
file = open('D:/2022/Python/inflearn/varialbe scope/testfile1.txt', 'w') ## 자원 할당
try:
    file.write('Context Manager Test1\nContextlib Test1.')
finally:
    file.close()
    
##### Ex 2
with open('D:/2022/Python/inflearn/varialbe scope/testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2.')
    
    
##### Ex 3 (with class as alias:)
## use class -> Context Manager with exception handling

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)
        
    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()
        

with MyFileWriter('D:/2022/Python/inflearn/varialbe scope/testfile3.txt', 'w') as f:
    f.write('Context Manager Test3\nContextlib Test3.')