'''
n명의 학생들의 평균과 가장 가까운 학생이 몇 번째 학생인지 출력
가장 가까운 학생이 여러명일 경우, 높은 성적의 학생 번호를 출력하고,
점수가 동일한 학생이 여러명일 경우, 빠른 번호를 출력하라.
'''
import time
import sys
start_time = time.time()
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
T = int(input())
a = list(map(int, input().split()))
meanVal = round(sum(a) / T)
# print(meanVal)
minVal = float('inf')
answerDict = {}
for t in range(T):
    diffVal = abs(a[t] - meanVal)
    if minVal > diffVal:
        minVal = diffVal
        answerDict[t] = minVal
# print(answerDict)
minVal = float('inf')
minIdx = 0
for key, val in answerDict.items():
    # print(key, val)
    if minVal > val:
        minVal = val
        minIdx = key
print(meanVal, key+1)
# print(f'Time : {time.time() - start_time } seconds')


