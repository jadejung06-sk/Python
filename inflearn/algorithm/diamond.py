'''
격자 형태에서, 다이아몬드에 위치한 숫자를 합하라.
'''

import sys
sys.stdin = open(r'inflearn/algorithm/grade/input.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n) ]
p1 = ((n-1)//2 )
p2 = ((n-1)//2 ) + 1
tot = 0
for vals in a:
    tot += sum(vals[p1:p2])
    p1 -= 1
    p2 += 1
    if p1 == 0:
        break
for vals in a[(n-1)//2:]:
    tot += sum(vals[p1:p2])
    p1 += 1
    p2 -= 1
    if not vals[p1:p2]:
        break
print(tot)