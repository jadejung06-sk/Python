import time
import sys
###### My method
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = int(input())
for idx in range(n):
    a = input()
    if a.lower() == a[::-1].lower():
        print(f'#{idx+1} YES')
    else:
        print(f'#{idx+1} NO')