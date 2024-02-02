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
