'''
Greedy
comparsion for heights and weights
'''
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]
people.sort()
# print(a)
cnt = 0
start_idx = 0

while start_idx < n:
    target_height = people[start_idx][0]
    target_weight = people[start_idx][1]
    for num, val in enumerate(people[start_idx:]): # h, w
        if num != 0:
            # print(target_height,  target_weight, val[0], val[1])
            if target_height < val[0] and target_weight < val[1]:
                cnt += 1
                break
    start_idx += 1
print(n - cnt)