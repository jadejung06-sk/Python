import sys
# sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
nums, m = map(int, input().split())
nums = list(str(nums))
m = len(nums) - m
targets = set()
for i in range(9, 0, -1):
    answers = []
    for n in nums:
        targets.add(i)
        if int(n) in targets:
            answers.append(str(n))
            if len(answers) == m:
                break
print(''.join(answers))
