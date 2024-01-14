'''stack'''

import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
a = input()
stack = []
res = ''
sign = '()+*-/'

for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(': ## 여는 괄호 전 까지만
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(': ## 여는 괄호 전 까지만
                res += stack.pop()
            stack.pop()
while stack: ## 빌 때까지만
    res += stack.pop()
print(res)