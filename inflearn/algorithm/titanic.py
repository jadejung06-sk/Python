'''
n 승객수
m 무게 제한
최대 2명이 하나의 구명보트를 타고 탈출하고 있다.
구명보트의 최소수를 구하라.
'''

# import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# # print(a) # ascending
# total = 0
# cnt = 0
# while len(a) != 0:
#     if len(a) != 1:
#         for val in a:
#             total = a[0] + a[- 1]
#             if total > m:
#                 a.pop(0)
#                 cnt += 1
#             else:
#                 a.pop()
#                 a.pop(0)
#                 cnt += 1
#     else:
#         cnt += 1
#         break
# print(cnt)


##### The Solution
import sys
from collections import deque
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p) # index를 새로 할당하지 않는 구조
cnt = 0 
while p :
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        # p.pop(0)
        p.popleft()
        p.pop()
        cnt += 1
print(cnt)