'''
Select a single number on the Right or the Left.
The outputs are the largest number of numbers and Right / Left.
'''
import sys
from collections import deque

# sys.stdin = open(r"D:/2022/Python/inflearn/algorithm/grade/input.txt", 'r')
n = int(input())
a = list(map(int, input().split()))
a = deque(a)

cnt = 0
last_num = -1
maxNum = -1
answer = ''
for _ in range(n):
    if _ == 0:
        if a[0] >= a[-1]:
            last_num = a[-1]
            answer += 'R'
            cnt += 1
            a.pop()
        else:
            last_num = a[0]
            answer += 'L'
            cnt += 1
            a.popleft()     
    else:
        if a[0] >= a[-1]:
            last_num = a[0]
            if last_num < maxNum:
                break
            maxNum = last_num
            answer += 'L'
            cnt += 1
            a.popleft()
        else:
            last_num = a[-1]
            if last_num < maxNum:
                break
            maxNum = last_num
            answer += 'R'
            cnt += 1
            a.pop()
print(cnt)
print(answer)
        