import re

# 1.re.IGNORECASE
text = 'abcdE'
pattern = r'abcde'
print('默认模式：', re.findall(pattern, text))  # 默认模式： []
print('默认模式：', re.findall(pattern, text, re.I))    # 默认模式： ['abcdE']

# 在默认匹配下大写字母E无法匹配小写字母e，而在忽略大小写模式下是可以的


# 2.ASCII
text = 'a天b下c太d平'
pattern = r'\w+'
print('Unicode:', re.findall(pattern, text))    # Unicode: ['a天b下c太d平']
print('ASCII:', re.findall(pattern, text, re.A))    # ASCII: ['a', 'b', 'c', 'd']


# 3.re.DOTALL
text = 'ab\ncd'
pattern = r'.*'
print('默认模式：', re.findall(pattern, text))  # 默认模式： ['ab', '', 'cd', '']
print('.匹配所有模式：', re.findall(pattern, text, re.S))   # .匹配所有模式： ['ab\ncd', '']


# 4.MULTILINE
text = '国泰\n民安'
pattern = r'^民安'
print('默认模式：', re.findall(pattern, text))  # 默认模式： []
print('多行模式：', re.findall(pattern, text, re.M))    # 多行模式： ['民安']


# 5.VERBOSE
text = '黄绢幼妇'
pattern = r"""^黄绢     # 绝
                幼妇    # 秒
            """
print('默认模式：', re.findall(pattern, text))  # 默认模式： []
print('详细模式：', re.findall(pattern, text, re.X))    # 多行模式： ['黄绢幼妇']


# 6.re.DEBUG
text = '百毒不侵'
pattern = '不侵'
print('debug模式：', re.findall(pattern, text, re.DEBUG))
"""
LITERAL 19981
LITERAL 20405

 0. INFO 10 0b11 2 2 (to 11)
      prefix_skip 2
      prefix [0x4e0d, 0x4fb5] ('不侵')
      overlap [0, 0]
11: LITERAL 0x4e0d ('不')
13. LITERAL 0x4fb5 ('侵')
15. SUCCESS
debug模式： ['不侵']
"""


