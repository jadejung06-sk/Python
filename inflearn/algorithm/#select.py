'''
Select a single number on the Right or the Left.
The outputs are the largest number of numbers and Right / Left.
'''
import sys
from collections import deque
sys.stdin = open(r"D:/2022/Python/inflearn/algorithm/grade/input.txt", 'r')
n = int(input())
a = list(map(int, input().split()))
a = deque(a)
last = 0
lt = 0
rt = n - 1
res = ""
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
            