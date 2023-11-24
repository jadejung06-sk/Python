'''
문자에서 자연수만을 추출하고 이어서 숫자를 출력
출력한 숫자의 약수 개수를 다음주에 출력
120
'''
##### My solution
import sys
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = input()
digits = ''
for i in n:
    if i.isdigit():
        digits += i
digits = int(digits) ## 3 1 2 // # 1000 
# digits = 3
print(digits)
cnt = 1
for val in range(1, digits//2+1):
    if digits % val == 0:
       cnt += 1
    #    print(digits, val, digits % val, cnt)
print(cnt)

##### Solution
import sys
sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = input()
res = 0
for x in n:
    if x.isdecimal():
        res = res*10 + int(x)
print(res)
cnt = 0
for val in range(1, res+1):
    if res % val == 0:
       cnt += 1
print(cnt)