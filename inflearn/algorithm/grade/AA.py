'''
n 명의 학생들의 평균과 가장 가까운 학생이 몇 번째 학생인지 출력
가장 가까운 학생이 여러명일 경우, 높은 성적의 학생 번호를 출력하고,
점수가 동일한 학생이 여러명일 경우, 빠른 번호를 출력하라.
'''
import time
import sys
##### Method 1
start_time = time.time()
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
sums = [0] * (n)
for i in range(len(a)):
    # print(i, a[i])
    for val in str(a[i]):
        # print(val)
        sums[i] += int(val)
maxIdx = sums.index(max(sums))
print(a[maxIdx])
# print(f'Time : {time.time() - start_time } seconds')