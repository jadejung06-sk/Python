'''stack'''

import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
bar = input()
bars = [i for i in bar]
stack = []
cnt = 0
for i in range(len(bars)):
    if bars[i] == '(':
        stack.append(bars[i])
    else:
        stack.pop()
        if bars[i-1] == "(":
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)