'''
행을 결정해서, 오른쪽(1)이든 왼쪽(0)으로 횟수만큼 움직인다.
움직인 이후, 모래시계 형태로 총합을 구하라.
'''

import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
order = [list(map(int, input().split())) for _ in range(m)]

##### moving
for i in range(m):
    for j in range(3):
        if j == 0:
            row = order[i][j]
            # print(row)
        elif j == 1:
            arrow = order[i][j]
            # print(arrow)
        else:
            times = order[i][j]
            # print(times)
    if arrow == 0:
        # print(a[row-1], row-1)
        a[row-1] = a[row-1][times%n:] + a[row-1][0:times%n]
    else:
        # print(a[row-1], row-1)
        a[row-1] = a[row-1][-(times%n):] + a[row-1][0:-(times%n)]

##### sum
total = 0
middle_idx = n // 2
p1 = 0
p2 = 1
for i in range(n):
    for j in range(p1 , p2):
        # print(a[i][j:n-j], j, n-j)
        total += sum(a[i][j:n-j])
        if i >= middle_idx:
            p1 -= 1
            p2 -= 1
        else:
            p1 += 1
            p2 += 1
print(total)