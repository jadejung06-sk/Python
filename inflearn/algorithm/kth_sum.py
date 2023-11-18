'''
3장을 뽑은 총합이 k 번째 큰 수 출력 
'''
import time
import sys
start_time = time.time()
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))

# ##### trail 1
# a = sorted(a, reverse= True)
# answer = a[0] + a[1] + a[k+1] ## 147 = 54 + 53 + 40
# print(answer)

##### Answer
res = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])
print(sorted(res, reverse= True)[k-1])

##### Check
# lists = list()
# res = list()
# for i in range(n):
#     for j in range(i + 1, n):
#         for m in range(j+1, n):
#             res.append([a[i] + a[j] + a[m], a[i], a[j], a[m]])
# # print(sorted(res, reverse= True)[k-1])
# print(res) ## 152 = 54 + 52 + 46