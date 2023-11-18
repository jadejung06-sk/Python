'''
n 명의 학생들의 평균과 가장 가까운 학생이 몇 번째 학생인지 출력
가장 가까운 학생이 여러명일 경우, 높은 성적의 학생 번호를 출력하고,
점수가 동일한 학생이 여러명일 경우, 빠른 번호를 출력하라.
'''
import time
import sys
##### Method 1
# start_time = time.time()
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
# T = int(input())
# a = list(map(int, input().split()))
# meanVal = round(sum(a) / T)
# meanVal = int(sum(a) / T + 0.5)
# # print(meanVal)
# minVal = float('inf')
# answerDict = {}
# for t in range(T):
#     diffVal = abs(a[t] - meanVal)
#     if minVal > diffVal:
#         minVal = diffVal
#         answerDict[t] = minVal
# # print(answerDict)
# minVal = float('inf')
# minIdx = 0
# for key, val in answerDict.items():
#     # print(key, val)
#     if minVal > val:
#         minVal = val
#         minIdx = key
# print(meanVal, key+1)
# # print(f'Time : {time.time() - start_time } seconds')


##### Method 2
### round in python == round_half_even (4.5000 ==> 4, 5.5000 ==> 6) even
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
# avg = round(sum(a) / n)
avg = int(sum(a) / n + 0.5)
min = float('inf')
# print(min)
for idx, x in enumerate(a):
    tmp = abs(x - avg)
    if tmp < min :
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
# print(round(4.5), round(3.5)) ## 4 4