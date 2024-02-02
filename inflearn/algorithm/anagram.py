import sys
from collections import defaultdict
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
a1 = defaultdict(int)
a2 = defaultdict(int)

for key in input():
    a1[key] += 1

for key in input():
    a2[key] += 1    

for key, val in a1.items():
    # print(key, val, a2[key])
    if a2[key] != val:
        print('NO')
        break
else:
    print('YES')    


##### Solution
# a = input()
# b = input()
# str1 = dict()
# str2 = dict()
# for x in a:
#     str1[x] = str1.get(x, 0) + 1

# for x in b:
#     str2[x] = str2.get(x, 0) + 1

# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print('NO')
#             break
#     else:
#         print('NO')
#         break
# else: ## Nomal End
#     print('YES')