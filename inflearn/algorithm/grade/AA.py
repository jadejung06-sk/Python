###### Solution
import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = []
p1, p2 = 0, 0
for _ in range(n+m):
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
        if p1 == n:
            c += b[p2:]
            break
    else:
        c.append(b[p2])
        p2 += 1
        if p2 == m:
            c += a[p1:]
            break
for val in c:
    print(val, end = ' ')
