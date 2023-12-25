'''
Greedy Algorithm
one meeting room
several meetings
get the number of maximum meetings
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
'''[(18, 19), (2, 20), (4, 21), (2, 22), (12, 15), (12, 23), (2, 8), (5, 20), (22, 23), (1, 5), (13, 21), (16, 20), (9, 19), (5, 9), (14, 20), (16, 22), (11, 12), (4, 16), (21, 23), (11, 13)]'''
a.sort()
'''[(1, 5), (2, 8), (2, 20), (2, 22), (4, 16), (4, 21), (5, 9), (5, 20), (9, 19), (11, 12), (11, 13), (12, 15), (12, 23), (13, 21), (14, 20), (16, 20), (16, 22), (18, 19), (21, 23), (22, 23)]'''
start_idx = 0
start_point = 0
end_point = a[0][1] 
cnt = 0
maxCnt = 0
##### Values for test
# print(end_point) ## 5
# print(a[n:]) ## []
########################

#### Prep for while
# for val in a[start_idx:]:
#     start_idx += 1
#     if val[0] >= end_point:
#         cnt += 1
#         end_point = val[1]
# if maxCnt < cnt:
#     maxCnt = cnt
# print(maxCnt)
########################

while start_idx < n:
    for val in a[start_idx:]:
        # print(start_idx, val)
        if val[0] >= end_point:
            cnt += 1
            end_point = val[1]
            # print(end_point)
    start_idx += 1
    if maxCnt < cnt:
        maxCnt = cnt
print(maxCnt)    
    
    
    

