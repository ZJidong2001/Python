"""
变量
"""

a = 999  # C中定义变量可以不用初始化赋值,但是Python必须赋值
a = b = c = 999
a = 1
b = 2
c = 3
a = 999
print(a + 1)

# 数字字母下划线,数字不开头
luckyNum = 999  # 小驼峰命名法——除第一个单词之外,其他单词首字母大写
LuckyNum = 888  # 大驼峰命名法——每个单词首字母都大写

# 不能使用Python的关键字及内置函数名作变量名
"""关键字查询"""
help("keywords")  # 查询1

import keyword  # 查询2
print(keyword.kwlist)

"""内置函数查询"""
import builtins  # 查看Python的内置函数
print(dir(builtins))
