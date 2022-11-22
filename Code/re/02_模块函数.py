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

