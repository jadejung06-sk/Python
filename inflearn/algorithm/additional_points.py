'''
연달아 맞는 경우에, 1 2 3 4 0 1 2 0 1 2 3 4 5 0 1 2 식으로 가산점의 점수를 준다.
총점을 구하라.
'''
import time
import sys
###### My method
# start_time = time.time()
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
# print(n, a )
points = 0
additional_point = 0
for i in a:
    if i == 0:
        additional_point = 0
    else:
        additional_point += 1
    points += additional_point
print(points)