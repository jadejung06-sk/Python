'''
행, 열, 6 면에 1~9가 존재하는지 확인하여
한 개라도 미존재하면 NO를 출력
모두 존재하면 YES를 출력하라
'''
# import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
##### My Solution
# a = [list(map(int, input().split())) for _ in range(9)  ]
# # rows = [i for i in range(9)]
# # print(a)

# res = 'NO'
# ##### rows
# for x in a:
#     checkDict = { i:0 for i in range(1, 10)}
#     for val in x:
#         checkDict[val] += 1
#         if checkDict[val] > 1:
#             print(res)
#             break
    
# ##### cols
# for i in range(9):
#     checkDict = { i:0 for i in range(1, 10)}
#     for j in range(9):
#         checkDict[a[j][i]] += 1
#         # for key, val in checkDict.items():
#         #     if checkDict[key] > 1:
#         #         print(res)
#         #         break


# ###### digonal
# di = [0, -1, -1, -1, 0, 1, 1, 1, 0]
# dj = [0, -1, 0, 1, 1, 1, 0, -1, -1]
# centers = [1, 4, 7]
# for i in range(9):
#     checkDict = { i:0 for i in range(1, 10)}
#     for j in range(9):
#         if i in centers and j in centers:
#             # print(i, j)
#             for idx in range(9):
#                 checkDict[a[i + di[idx]][j + dj[idx]]] += 1
#         # for key, val in checkDict.items():
#         #     if checkDict[key] > 1:
#         #         print(res)
#         #         break
            
##### The Solution
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10 
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print('YES')
else:
    print('NO')