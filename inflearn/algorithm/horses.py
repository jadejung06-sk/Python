'''
n 개의 마구간과 c 마리의 말이 존재하는데,
마구간에 한 마리씩 넣어둔다
가장 가까운 거리가 최대가 되는 경우를 구하고, 그 거리를 구하라.
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
def Count(len):
    cnt = 1
    ep = stables[0]
    for i in range(1, n):
        if stables[i] - ep >= len:
            cnt += 1
            ep = stables[i]
    return cnt


n, c = map(int, input().split())
stables = [int(input()) for _ in range(n)]
stables.sort()
lt = 1
rt = stables[n-1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
            