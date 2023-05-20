import re

##### simple
target = '5AAaaabcde$3567^g123'
a_obj = re.search('abc', 'abcdefg') # object
a_lst = re.findall('abc', 'abcdefg') # list
print(a_obj)
print(a_lst)

##### first & last
a_first = re.findall('^a', target)
g_last = re.findall('g$', 'abcdefg')
print(a_first)
print(g_last)

##### special symbols
dol = re.findall('\$', target)
cur = re.findall('\^', target)
print('symbols: ', dol, cur)

##### or
se = re.findall('[abc]', target) # each words
alphabet_all = re.findall('[abcdefghijklmnopqrstuvwxyzABCDEFG]', target) # each words
alphabet_simple = re.findall('[a-zA-Z]', target) # each words
numbers = re.findall('[0-9]', target)
korean = re.findall('[가-힣ㄱ-ㅎ]', target)
print('or: ', se, alphabet_all, alphabet_simple, korean)

##### not []
not_numbers = re.findall('[^0-9]', target)
print('not []: ', not_numbers)

##### sepcial numbers
num1 = re.findall('\d', target) # 5abcde$3567^g123 ['5', '3', '5', '6', '7', '1', '2', '3'] 
num2 = re.findall('\d\d', target) # 5abcde$3567^g123 ['35', '67', '12'] 
num3 = re.findall('\d\d\d', target) # 5abcde$3567^g123 ['356', '123']
num3_multi = re.findall('\d{3}', target) # 5abcde$3567^g123 ['356', '123']
not_num1 = re.findall('\D', target) # 5abcde$3567^g123 ['35', '67', '12']
print(f'special \d: {target} vs. ', num1, num2, num3, num3_multi, not_num1)

##### special spaces
space1 = re.findall('\s', target)
not_space = re.findall('\S', target)
print(f'special \s: {target} vs. ', space1, not_space)

##### + * greedy
greedy_plus = re.findall('a+', target)
## capital
capital_words = re.findall('ABC', target, re.IGNORECASE)
print(f'greedy_plus: {target} vs. ', greedy_plus) # ['aaa']
print(f'capital: {target} vs. ', capital_words) # ['abc']
#########################

##### substi.
org_time = '2023-01-01'
chg_time = re.sub('-', '.', org_time)
print(org_time, 'vs.', chg_time)

new_target = re.sub('\d', '', target)
print(target, 'vs.', new_target)

##### test
test1 = re.findall('a', target)
test2 =re.findall('^a', target)
test3 = re.findall('[\d\W]', target)
print(test1, test2, test3)


