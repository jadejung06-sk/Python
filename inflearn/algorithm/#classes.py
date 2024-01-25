'''queue'''
import sys
from collections import deque
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
# classes = input()
# class_old = deque(classes)

# n = int(input())
# simulations = [input() for _ in range(n)]
# # print(simulations) ## ['AYKGDHEJ', 'AQKWDERTFYP', 'CTFKSBDEA', 'ASKGHDEF', 'WOPASFKGHDEF']
# for idx in range(len(simulations)):
#     while class_old:
#         for val in class_old:
#             for j in range(len(simulations[idx])):
#                 print(simulations[idx][j]) ## A-Y-K-G-D-H-E-F
           
#         # if simulations[idx][j] in class_old:           

# # for idx, val in enumerate(simulations):
# #     # print(idx, val)
# #     for i in range(len(val)):
# #         if val[i] in class_old:
# #             class_old.popleft()
# #             if len(class_old) == 0 and (len(val) - 1) == i:
# #                 print(f'#{idx+1} YES')
# #             else:
# #                 print(f'#{idx+1} NO')
    
##### Solution
need = input()
n = int(input())

for _ in range(n):
    plan = input() # AYKGDHEJ
    dq = deque(need)
    for x in plan: # A-Y-K-G-D-H-E-J
        if x in dq: # AKDEF
            if x!= dq.popleft():
                print(f'#{_+1} NO')
                break
    else:
        if len(dq) == 0:
            print(f'#{_+1} YES')
        else:
            print(f'#{_+1} NO')