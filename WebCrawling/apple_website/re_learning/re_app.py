import re

##### simple
target = 'abcde$f^g'
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
print(dol, cur)

##### or
se = re.findall('[abc]', target) # each words
print(se)