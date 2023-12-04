'''
행, 열, 6 면에 1~9가 존재하는지 확인하여
한 개라도 미존재하면 NO를 출력
모두 존재하면 YES를 출력하라
'''

import sys

sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')

a = [list(map(int, input().split())) for _ in range(9)  ]
# rows = [i for i in range(9)]
# print(a)

res = 'NO'
##### rows
for x in a:
    checkDict = { i:0 for i in range(1, 10)}
    for val in x:
        checkDict[val] += 1
        if checkDict[val] > 1:
            print(res)
            break
    
##### cols
