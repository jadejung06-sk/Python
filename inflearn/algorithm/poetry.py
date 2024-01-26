'''hash'''
# import sys
# from collections import deque
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
# n = int(input())
# set1 = set(input() for _ in range(n))
# set2 = set(input() for _ in range(n - 1))
# print(list(set1.difference(set2))[0])

##### Method
import sys
from collections import deque
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
    # print(key, val)