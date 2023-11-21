'''
숫자를 뒤집은 뒤에, 소수를 출력
예를 들어, 32면 23, 910이면 19로 숫자화, 첫 자리부터 연속된 0은 무시
def reverse(x)와 def isPrime(x) 작성하시오.
5 19 71 79 991
'''
import time
import sys
start_time = time.time()
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = int(input())
a = list(map(str, input().split()))

def reverse(x:str):
    x = int(x[::-1])
    return x

def isPrime(x:int):
    cnt = 0
    for i in range(2, x+1):
        if x % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
    
# def isPrime(x:int):
#     if x == 1:
#         return False
#     for i in range(2, x//2+1):
#         if x % i == 0:
#             return False
#     else:
#         return True
    
for i in a:
    target = reverse(i)
    if isPrime(target):
        print(target, end = ' ')