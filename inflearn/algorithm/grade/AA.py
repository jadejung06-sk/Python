import sys
from collections import deque
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
set1 = set(input() for _ in range(n))
set2 = set(input() for _ in range(n - 1))
print(list(set1.difference(set2))[0])