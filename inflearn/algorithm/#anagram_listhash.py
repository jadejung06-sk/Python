# text = '''I'''
# text1 = 'Ⅰ'
# text2 = '''Ⅱ'''
# text3 = '''Ⅲ'''
# text4 = '''Ⅹ'''

# print(ord(text), ord(text1), ord(text2), ord(text3), ord(text4))

# if ord(text) == 8544:
#     print(text.replace(text, text1))
import sys 
sys.stdin = open(r'D:\2022\Python\inflearn\algorithm\grade\input.txt', 'r')
a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

### method 1
# if str1 == str2:
#     print('YES')
# else:
#     print('NO')

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print('YES')