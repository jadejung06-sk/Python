'''
행을 결정해서, 오른쪽이든 왼쪽으로 횟수만큼 움직인다.
움직인 이후, 모래시계 형태로 총합을 구하라.
'''

import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
order = [list(map(int, input().split())) for _ in range(m)]

### test 1
# b = [12, 39, 30, 23, 11]
# b_new = []
# print(b[0%n:] + b[0:0%n]) # 
# print(b[1%n:] + b[0:1%n]) # 왼 1 [39, 30, 23, 11, 12]
# print(b[2%n:] + b[0:2%n]) # 왼 2
# print(b[3%n:] + b[0:3%n]) # 왼 3
# print(b[4%n:] + b[0:4%n]) # 왼 4
# print('*' * 20)
# print(b[0%n:] + b[0:0%n]) # 오 1
# print(b[-(1%n):] + b[0:-(1%n)] ) # 오 2 [11, 12, 39, 30, 23]
# print(b[-(2%n):] + b[0:-(2%n)] )
# print(b[-(3%n):] + b[0:-(3%n)] )
# print(b[-(4%n):] + b[0:-(4%n)] )

for i in range(m):
    for j in range(m):
        if j == 0:
            row = order[i][j]
        elif j == 1:
            arrow = order[i][j]
        else:
            times = order[i][j]         
    a
