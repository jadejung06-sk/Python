'''
3개의 주사위를 던져서, 
같은 눈 3개면 10000 + (눈수) * 1000
같은 눈 2개면 1000 + (눈수) * 100
다른 눈이면, (가장 큰 눈) * 100
가장 큰 상금을 출력하시오.
'''
import time
import sys
start_time = time.time()
# sys.stdin = open("D:/2022/Python/inflearn/algorithm/grade/input.txt", "rt")
n = int(input())


def get_prize(values):
    prize = 0
    maxVal = -2147000000
    dice = {i:0 for i in range(1, 7)}
    for value in values:
        dice[value] +=1
    for idx, val in dice.items():
        if val == 3:
            prize = 10000 + idx * 1000
            return prize
            break
        elif val == 2:
            prize = 1000 + idx * 100
            return prize
            break
        elif val == 1:
            if maxVal < idx:
                maxVal = idx
    prize = maxVal * 100        
    return prize    

maxPrize = -2147000000
for _ in range(n):
    a = list(map(int, input().split()))
    prize = get_prize(a)
    if maxPrize < prize:
        maxPrize = prize
print(maxPrize)