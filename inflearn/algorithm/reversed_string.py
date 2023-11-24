'''
앞으로도 뒤로도 단어가 동일하면, 
#1 YES
#2 NO 
상기 처럼 출력할 것
'''
import time
import sys
###### My method
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
start_time = time.time()
n = int(input())
for idx in range(n):
    a = input()
    a = a.lower()
    if a == a[::-1]:
        print(f'#{idx+1} YES')
    else:
        print(f'#{idx+1} NO')
print(f'Time : {time.time() - start_time } seconds') ## 0.007


###### Solution
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
# start_time = time.time()
# n = int(input())
# for idx in range(n):
#     a = input()
#     a = a.upper()
#     size = len(a)
#     for j in range(size//2):
#         if a[j] != a[-1-j]:
#             print('#%d NO' % (idx+1))
#             break
#     else:
#         print('#%d YES' % (idx+1))
# print(f'Time : {time.time() - start_time } seconds') ## 0.004