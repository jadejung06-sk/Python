'''
주어진 랜선의 k 개수를 활용해서, n 개수의 최대한으로 길이가 긴 동일한 랜선을 만들어라.
그 길이를 구하라. 
'''

import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')

# k, n = map(int, input().split())
# a = [int(input()) for _ in range(k)]
# length = 50
# cnt = 0
# while cnt != n:
#     cnt = 0
#     for x in a:
#         cnt += x // length 
#         # print(x, cnt)
#         if cnt < n:
#             length += 1
#         else:
#             length -= 1
# print(length)


###### The Solution
def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())
line= []
largest = 0
res = 0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
        
print(res)