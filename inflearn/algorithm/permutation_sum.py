'''
n개의 순열이 존재하고, n을 앞에서 부터 더해가면서, m이 되는 경우의 수를 구하라.
'''
##### My solution
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
start_idx = 0
end_idx = start_idx +1
cnt = 0
while n >= end_idx:
    # print(a[start_idx:end_idx])
    if sum(a[start_idx:end_idx]) > m :        
        start_idx += 1
    elif sum(a[start_idx:end_idx]) == m :
        cnt += 1        
        start_idx += 1
    else:
        end_idx += 1
print(cnt)


##### Solution
# import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# lt = 0
# rt = 1
# tot = a[0]
# cnt = 0
# while True:
#     if tot < m:
#         if rt < n :
#             tot += a [rt]
#             rt += 1
#         else:
#             break
#     elif tot == m:
#         cnt += 1
#         tot -= a[lt]
#         lt += 1
#     else:
#         tot -= a[lt]
#         lt += 1
# print(cnt)