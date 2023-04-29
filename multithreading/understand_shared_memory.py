import multiprocessing
from multiprocessing import Process
import time

def print_array_contents(array):
    while True:
        print(*array, sep = ", ")
        time.sleep(1)

if __name__ == '__main__':
    arr = [-1] * 10 # [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    # print(*arr) # -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
    ##### without Process 
    # print_array_contents(arr) # No break
    # -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
    ##### with Process
    # p = Process(target = print_array_contents, args = ([arr])).start()
    # -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j
