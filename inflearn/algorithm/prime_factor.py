'''
[에라토스테네스 체]
1에서 N까지의 소수의 개수를 출력
제한시간은 1초
'''
import time
import sys
start_time = time.time()
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
n = int(input())
ch = [0] * (n+1)
cnt = 0 
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
           ch[j] = 1
print(cnt)    