'''
1~20까지의 카드 배열이 존재
행마다 숫자가 존재, 예를 들어 5 10이면, 5번째에서 10번째의 카드 배열을 역순으로 배치해라.
계속해서 반복해서 마지막 카드 배열을 출력하라. 
'''
##### My solution
# # sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
# questions = []
# with open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r') as f:
#     string = f.read()
#     strings = string.split('\n')
#     for val in strings:
#         questions.append(val.split(' '))
# cards = [i for i in range(1, 21)]
# for start, end in questions:
#     if len(cards[int(start)-1:int(end)]) == len(cards[int(end)-1:int(start)-2:-1]):
#         cards[int(end)-1:int(start)-2:-1] = cards[int(start)-1:int(end)]
#     else:
#         cards[int(end)-1::-1] = cards[int(start)-1:int(end)]
# print(cards)
#     # print(start, end, cards[int(start)-1:int(end)],cards[int(end)-1:int(start)-2:-1] ) ## the same size
#     # print(start, end, cards[int(start)-1:int(end)],cards[int(end)-1::-1] ) ## the different size
    
    
##### Solution
import sys
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end = ' ')