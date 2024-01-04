import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
nums, m = map(int, input().split())
# print(len(str(nums)))
length = len(str(nums)) - m
# max(list(str(nums)))
print(list(str(nums)).index('9'))
