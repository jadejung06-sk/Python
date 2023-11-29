'''
행을 결정해서, 오른쪽(1)이든 왼쪽(0)으로 횟수만큼 움직인다.
움직인 이후, 모래시계 형태로 총합을 구하라.
'''
##### My method
# import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# m = int(input())
# order = [list(map(int, input().split())) for _ in range(m)]
# ##### moving
# for i in range(m):
#     for j in range(3):
#         if j == 0:
#             row = order[i][j]
#             # print(row)
#         elif j == 1:
#             arrow = order[i][j]
#             # print(arrow)
#         else:
#             times = order[i][j]
#             # print(times)
#     if arrow == 0:
#         # print(a[row-1], row-1)
#         a[row-1] = a[row-1][times%n:] + a[row-1][0:times%n]
#     else:
#         # print(a[row-1], row-1)
#         a[row-1] = a[row-1][-(times%n):] + a[row-1][0:-(times%n)]

# ##### sum
# total = 0
# middle_idx = n // 2
# p1 = 0
# p2 = 1
# for i in range(n):
#     for j in range(p1 , p2):
#         # print(a[i][j:n-j], j, n-j)
#         total += sum(a[i][j:n-j])
#         if i >= middle_idx:
#             p1 -= 1
#             p2 -= 1
#         else:
#             p1 += 1
#             p2 += 1
# print(total)

# ### test 1
# # b = [12, 39, 30, 23, 11]
# # b_new = []
# ## 0
# # print(b[0%n:] + b[0:0%n]) # 왼 0
# # print(b[1%n:] + b[0:1%n]) # 왼 1 [39, 30, 23, 11, 12]
# # print(b[2%n:] + b[0:2%n]) # 왼 2
# # print(b[3%n:] + b[0:3%n]) # 왼 3
# # print(b[4%n:] + b[0:4%n]) # 왼 4
# # print('*' * 20)
# ## 1
# # print(b[0%n:] + b[0:0%n]) # 오 1
# # print(b[-(1%n):] + b[0:-(1%n)] ) # 오 2 [11, 12, 39, 30, 23]
# # print(b[-(2%n):] + b[0:-(2%n)] )
# # print(b[-(3%n):] + b[0:-(3%n)] )
# # print(b[-(4%n):] + b[0:-(4%n)] )


##### Solution
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
            
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)