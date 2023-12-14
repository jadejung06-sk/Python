'''
n 개의 마구간과 c 마리의 말이 존재하는데,
마구간에 한 마리씩 넣어둔다
가장 가까운 거리가 최대가 되는 경우를 구하고, 그 거리를 구하라.
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
def Count(length):
    cnt = 1
    start_p = stables[0]
    for i in range(1, n):
        if stables[i] - start_p >= length:
            cnt += 1
            start_p = stables[i]
    return cnt

n, c = map(int, input().split())
stables = [int(input()) for _ in range(n)]
stables.sort()
lt = stables[0]
rt = stables[n-1]
while lt <= rt:
    mid = (lt + rt) // 2 # 둘 사이의 거리의 최대 (a + b) // 2
    if Count(mid) >= c: # 말이 모자르게 마구간에 들어가는 게 문제일 뿐, 그 이외는 모두 허용
        res = mid
        lt = mid + 1 # 같거나 크면, 더 커져도 되므로 시작점을 옮김 
    else:
        rt = mid - 1 # 작으면 ...
print(res)
            