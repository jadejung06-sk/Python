'''
global interpreter lock
thread 사용할 경우, gil을 알 필요가 있음

GIL(Global Interpreter Lock)
 작성한 파이썬 코드를 CPython이 내부에서 해석 -> Python(bytecode) 실행 시 여러 trhead 사용할 경우 
 -> gil이 release와 acquire를 반복하며 단일 trhead만 작동하게 되어 있음 
 : 단일 스레드만이 python object에 접근하게 제한하는 mutex
 Cpython은 메모리 관리가 취약하기에, gil을 통해 thread-safe 가능
 파이썬은 단일 스레드로에서 가장 빠르며, 단일 스레드만으로 충분히 빠름
 멀티 프로세스에는 gil이 없기에, 프로세스만으로 사용 가능 (멀티 프로세스 사용하는 tensorflow, numpy)
 -> gil 외부 영역에서 효율적인 코딩 가능
 병렬 처리는 multiprocessing, asyncio 등 선택지가 다양함
 thread 동시성을 처리하고 싶다면, Jython, IronPython, StacklessPython 등이 존재한다.
 
 
CPython
메모리 관리
파이썬에서만 GIL을 사용하는 이유
'''