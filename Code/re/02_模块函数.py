import re

# 1.查找一个匹配项

# 案例1
text = 'a天下b，天下b'
pattern = r'天下b'
# 查找任意位置
print('search:', re.search(pattern, text).group())  # search: 天下b
# 从字符串开头匹配
print('match:', re.match(pattern, text))            # match: None
# 整个字符串完全匹配
print('fullmatch:', re.fullmatch(pattern, text))    # fullmatch: None

"""
- search函数是在字符串中任意位置匹配，只要符合正则表达式的字符串就能匹配成功，如上有两个匹配项，但search函数值返回一个。
- match函数要从头开始匹配，而字符串开头多了个字母a，所以无法匹配
- fullmatch函数需要完全相同
"""

# 案例2，将开头字母 a 去掉
text = '天下b，天下b'
pattern = r'天下b'
# 查找任意位置
print('search:', re.search(pattern, text).group())  # search: 天下b
# 从字符串开头匹配
print('match:', re.match(pattern, text).group())    # match: 天下b
# 整个字符串完全匹配
print('fullmatch:', re.fullmatch(pattern, text))    # fullmatch: None

"""
案例2删除了text最开头的字母a，这样match函数可以匹配，而fullmatch函数依然不能完全匹配！
"""

# 案例3，只保留一段
text = '天下b'
pattern = r'天下b'
# 查找任意位置
print('search:', re.search(pattern, text).group())  # search: 天下b
# 从字符串开头匹配
print('match:', re.match(pattern, text).group())    # match: 天下b
# 整个字符串完全匹配
print('fullmatch:', re.fullmatch(pattern, text).group())    # fullmatch: 天下b

"""
只保留一段文字，并且与正则表达式一致；这时fullmatch函数可以匹配
"""

# 2.查找多个匹配项

# 案例4
text = 'a天下b，天下b'
pattern = r'天下b'
# 查找所有匹配项，返回一个list
print('findall:', re.findall(pattern, text))    # findall: ['天下b', '天下b']
# 查找所有匹配项，返回一个迭代器
print('finditer:', re.finditer(pattern, text))  # finditer: <callable_iterator object at 0x0000019D2F1493A0>

# 案例5
text = 'abc,def,ghi'
pattern = r','
# 正则切割
print('split:', re.split(pattern, text, maxsplit=1, flags=re.I))    # split: ['abc', 'def,ghi']

# 案例6
text = '1abcd,2efgh,3ijk'
pattern = r','
# repl为字符串
repl = '.'
# 替换
print('sub-repl字符串：', re.sub(pattern, repl, text, count=2, flags=re.I)) # sub-repl字符串： 1abcd.2efgh.3ijk

# 案例7
text = 'a123，b456，c789'
pattern = r'，|。'
# repl为字符串
repl = lambda matchobj: ' ' if matchobj.group(0) != '，' else ';'
# 替换
print('sub-repl函数：', re.sub(pattern, repl, text, count=2, flags=re.I))   # sub-repl函数： a123;b456;c789

# 案例8
text = '1abcd,2efgh,3ijk'
pattern = r','
# repl为字符串
repl = '.'
# 替换
print('subn-repl字符串：', re.subn(pattern, repl, text, count=2, flags=re.I)) # subn-repl字符串： ('1abcd.2efgh.3ijk', 2)


# 案例9
text = 'a123b,123b'
pattern = r'123b'
pattern_obj = re.compile(pattern)
# 查找任意位置
print('pattern_obj.search:', pattern_obj.search(text).group())  # pattern_obj.search: 123b

# 案例10：re.escape()
text = 'ab.cd*e'
pattern = r'ab\.cd\*e'
# 查找任意位置
print('search:', re.search(pattern, text).group())  # search: ab.cd*e

pattern_ = re.escape('ab.cd*e')
print(pattern_) # ab\.cd\*e




