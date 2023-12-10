'''
7 * 7 격자판에 행이나 열에 5자리의 회문수가 존재한다.
회문수의 개수를 구하라.
'''
import sys

sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for k in range(3):
        row_ch = []
        col_ch = []
        for j in range(5):
            row_ch.append(a[i][j + k])
            col_ch.append(a[j + k][i])
            # print(i, j + k) # rows
            # print(j+ k , i) # cols
        if row_ch[0] == row_ch[-1] and row_ch[1] == row_ch[-2]:
            cnt += 1
        if col_ch[0] == col_ch[-1] and col_ch[1] == col_ch[-2]:
            cnt += 1

print(cnt)