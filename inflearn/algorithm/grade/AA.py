import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
# print(a) # ascending
total = 0
cnt = 0
while len(a) != 0:
    if len(a) != 1:
        for val in a:
            total = a[0] + a[- 1]
            if total > m:
                a.pop(0)
                cnt += 1
            else:
                a.pop()
                a.pop(0)
                cnt += 1
            # print(val, a)
    else:
        cnt += 1
        break
print(cnt)
        