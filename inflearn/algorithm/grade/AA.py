'''
몇 개의 숫자와 특정 숫자를 알려준다.
그 숫자가 오름차순 정렬에서 몇 번째인지 구하라.
'''
import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1
mid = (rt + lt) // 2
while a[mid] != m:
    mid = (rt + lt) // 2
    # print(mid)
    if a[mid] < m:
        lt = mid + 1
    else:
        rt = mid - 1
print(mid + 1)
