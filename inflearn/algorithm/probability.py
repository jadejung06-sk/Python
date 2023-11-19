'''
두 개의 정 n면체와 정 m면체의 두 개의 주사위를 던져서 나오는 두 눈의 합 중
가장 확률이 높은 숫자를 출력하시오.
정답이 여러개일 경우, 오름차순으로 출력
'''
import time
import sys
start_time = time.time()
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
ns, ms = list(map(int, input().split()))
values = []
valDict = { key:0 for key in range(1, 41) }
for n in range(1, ns+1):
    for m in range(1, ms+1):
        values.append(n + m)
        valDict[n + m] += 1
maxVal = max(valDict.values())
answers = ''
for key, val in valDict.items():
    if maxVal == val:
        answers += f'{key} '
print(answers[:-1])
print(f'Time : {time.time() - start_time } seconds')


