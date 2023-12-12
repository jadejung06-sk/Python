'''
노래의 n 개수만큼 곡의 분 단위로 자연수가 주어진다.
해당 노래를 동일한 크기로 최소 단위의 DVD에 녹음하려고 한다.
최소 DVD의 개수를 만드는 최소 단위를 구하라.
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
# print(a[:2], a[-2:])
# idx = 2
# largest = 0
# total = 0

# while idx < n:
#     largest = min(sum(a[:idx]), sum(a[-idx:]))
#     cnt = 0
#     for x in a:
#        total += x
#        if total >= largest:  
#             cnt += 1
#             total = x
#     else:
#         cnt += 1
#         print(idx, cnt, largest, total)
#     if cnt == m:
#         print(largest)
#         break
#     else:   
#         idx += 1       
##### The Solution
lt = 1
rt = sum(a)
while lt <= rt:
    cnt = 0
    total = 0
    mid = (lt + rt) // 2
    for x in a:
        total += x
        if total >= mid:
            cnt += 1
            total = x
    # print(mid)
    if cnt < m:
        lt = mid + 1
    elif cnt > m: 
        rt = mid - 1
    else:
        print(mid)