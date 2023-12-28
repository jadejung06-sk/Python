import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
target_list = list(map(int, input().split()))
m = int(input())
times = 0
while times < m:
    times += 1
    maxIdx = target_list.index(max(target_list))
    minIdx = target_list.index(min(target_list))
    target_list[maxIdx] -= 1
    target_list[minIdx] += 1
print(max(target_list) - min(target_list))

##### Solution