'''
숫자를 뒤집은 뒤에, 소수를 출력
예를 들어, 32면 23, 910이면 19로 숫자화, 첫 자리부터 연속된 0은 무시
def reverse(x)와 def isPrime(x) 작성하시오.
5 19 71 79 991
'''
import time
import sys
start_time = time.time()
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = int(input())
a = list(map(str, input().split()))

for i in a:
    target = int(i[::-1])
    cnt = 0
    ch = [0] * (target+1)
    for t in range(2, target+1):
        if ch[t] == 0:
            for j in range(t+1, target+1, t):
                ch[j] += 1
    if ch[-1] == 0:
        print(target, end = ' ')