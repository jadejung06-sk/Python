##### deep copy vs. swallow copy
## inner vs. outer
marks1 = [["~"] * 3 for _ in range(4)] # class list different ids inner
marks2 = [["~"] * 3] * 4 # class list same ids outer
print(marks1)
print(marks2)

marks1[0][1] = 'X' # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks2[0][1] = 'X' # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]
print(marks1)
print(marks2)
print([id(i) for i in marks1]) # [2439505426048, 2439505425728, 2439502627072, 2439502626880]
print([id(i) for i in marks2]) # [2439502908032, 2439502908032, 2439502908032, 2439502908032]