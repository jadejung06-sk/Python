'''


'''
import time
import sys
start_time = time.time()
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt.txt", "rt")
T = int(input())
# print(T) # 2
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(s, e, k, a)
    sorted_a = sorted(a[s-1:e])
    # print(k, sorted_a)
    print(f'#{t+1} {sorted_a[k-1]}')

# print(f'Time : {time.time() - start_time } seconds')


# start_time = time.time()
# n, k = map(int, input().split())
# answer = 0
# divisors = []
# for i in range(1, 1+n):
#     if n % i == 0:
#          divisors.append(i)
# try:
#     answer = divisors[k-1]
# except IndexError as e:
#     answer = -1
# print(answer)
# print(f'Time : {time.time() - start_time } seconds')