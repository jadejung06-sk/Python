'''
상하좌우의 값을 확인해서, 봉우리의 개수를 구하라.
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
di = [-1, 0, 1, 0] # 북 # 동 # 남 # 서
dj = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)   ]
##### padding
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0)
    
cnt = 0
for i in range(1, n+1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i+di[k]][j+dj[k]] for k in range(4)):
            cnt +=1
print(cnt)