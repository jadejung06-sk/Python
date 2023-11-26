'''
5 * 5 격자판의 행의 합, 열의 합, 대각선의 합 중 가장 큰 합을 출력하라.
'''
import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
n = int(input())
questions = []
maxVal = -247000000
for _ in range(n):
    a = list(map(int, input().split()))
    questions.append(a)
for question in questions:
    if maxVal < sum(question):
        maxVal = sum(question)

for i in range(len(questions)):
    colx = 0
    for j in range(len(questions)):
        colx += questions[j][i]
    if maxVal < colx:
        maxVal = colx

for i in range(len(questions)):
    digonalx = 0
    for j in range(i+1, len(questions)):
        if i == j:
            digonalx += questions[i][j]
            if maxVal < digonalx:
                maxVal = digonalx
   
for i in range(len(questions)):
    digonaly = 0
    for j in range(i+1, len(questions)):
        if (i + j + 1) == len(questions):
            digonaly += questions[j][j]
            if maxVal < digonaly:
                maxVal = digonaly

print(maxVal)