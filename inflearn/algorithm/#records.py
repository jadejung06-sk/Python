'''
노래의 n 개수만큼 곡의 분 단위로 자연수가 주어진다.
해당 노래를 동일한 크기로 최소 단위의 DVD에 녹음하려고 한다.
최소 DVD의 개수를 만드는 최소 단위를 구하라.
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 1
rt = sum(a)
res = 0
maxx = max(a)

def Count(capacity):
    cnt = 1
    sum = 0
    for x in a:
        if sum  + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

while lt <= rt:
    cnt = 0
    total = 0
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:            
        res = mid
        rt = mid - 1   
    else:
        lt = mid + 1

print(res)