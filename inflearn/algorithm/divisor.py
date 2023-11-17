'''
약수 n과 k번째 작은 수
k 번째가 n의 수를 넘는 경우 -1 출력
'''
import time
import sys
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
start_time = time.time()
n, k = map(int, input().split())
answer = 0
divisors = []
for i in range(1, 1+n):
    if n % i == 0:
         divisors.append(i)
try:
    answer = divisors[k-1]
except IndexError as e:
    answer = -1
print(answer)
print(f'Time : {time.time() - start_time } seconds')

# import sys
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
# n, k = map(int, input().split())
# cnt = 0
# for i in range(1, 1+n):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)