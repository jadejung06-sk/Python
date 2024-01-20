'''queue'''
from collections import deque
import sys

sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
dq = [ (val, 1) if idx == m else (val, 0) for idx, val in enumerate(a) ]
dq = deque(dq)
# print(dq, max(dq)[0], dq.popleft()[0])
cnt = 0
target = dq[m]
while dq:
    cur = dq.popleft()
    # print(max(dq)[0])
    if cur[0] >= max(dq)[0]:
       cnt += 1
#        print(cnt, cur, target, max(dq))
       if cur[0] == target[0] and cur[1] == 1 :
           break
    else:
        dq.append(cur)
        # print(dq) 
print(cnt)