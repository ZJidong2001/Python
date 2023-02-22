"""
字符串对象方法
"""


# str.replace(old, new, [count])

s = "Line1 Line2 Line4"
# 用 "b" 替换所有的 "Li"
rs = s.replace("Li", "b")
print(rs)  # bne1 bne2 bne4
print(s)  # 并不是在原字符串上进行替换,而是赋值新的字符串再替换
# 用 "b" 替换 "Li" 2次
rs = s.replace("Li", "b", 2)
print(rs)  # bne1 bne2 Line4


# str.strip([chars])

str1 = ' \thello wrold h \n'
# 没有传参,删除字符串两边的空白符(空格、换行符、制表符)
print(str1.strip())  # hello wrold h
str2 = "ooho hello wrold"
# 移除str2头尾的字符"o",头部有两个连续的,都移除,尾部没有可以移除的
print(str2.strip('o'))  # ho hello wrold
# 会考虑"mecow."的所有组合情况来移除头尾的字符
str3 = 'www.example.com'
print(str3.strip("mecow."))  # xampl


# str.center(width, [fillchar])

str1 = "hello "
print(str1.center(11, "F"))
print(str1.center(3, "F"))
print("这是一条完整的分割线".center(80, '-'))


# str.ljust(width, [fillchar])

str1 = "hello "
print(str1.ljust(11, "F"))
print(str1.ljust(3, "F"))
print(str1.rjust(11, "F"))
print(str1.rjust(3, "F"))


# str.partition(sep)

str1 = "hello world"
print(str1.partition("l"))
print(str1.partition("ll"))
print(str1.partition("hd"))
print(str1.rpartition("l"))
print(str1.rpartition("ll"))
print(str1.rpartition("hd"))


# str.startswith(prefix, [start], [end])

str1 = "hello world"
print(str1.startswith("h"))
print(str1.startswith("he"))
print(str1.startswith(" w"))
print(str1.startswith(" w", 5, 8))
print(str1.startswith((" w", "h")))


# str.endswith(suffix, [start], [end])

str1 = "hello world"
print(str1.endswith("d"))
print(str1.endswith("ld"))
print(str1.endswith("lo"))
print(str1.endswith("lo", 1, 5))
print(str1.endswith(("d", "lo")))


# str.isalnum() 如果字符串中的所有字符都是字母、文字或数字,则返回True,否则为False
# str.isalpha() 如果字符串中的所有字符都是字母、文字,则返回True,否则为False
# str.isdigit() 如果字符串中的所有字符都是数字，则返回True,否则为False
# str.isspace() 如果字符串中只有空白符(空格、换行符、制表符等),则返回True,否则为False

str1 = "abc牛123"
print(str1.isalnum())  # True
print(str1.isalpha())  # False
str2 = "abc"
print(str2.isalpha())  # True
print(str1.isdigit())  # False
print(str2.isdigit())  # False
str3 = "123"
print(str3.isdigit())  # True
print(str1.isspace())  # False
str4 = " "
print(str4.isspace())  # True
str5 = "\t"
print(str5.isspace())  # True
str6 = "\n"
print(str6.isspace())  # True


# str.join(iterable)

a = "\\"  # 单个反斜杠
s1 = "hello world"
print(a.join(s1))
print("-".join("abcdef"))
s2 = ["1", "2", "3", "4"]
print(a.join(s2))
s3 = ("1", "2", "3", "4")
print(a.join(s3))
# 字典只取键,不取值
s4 = {"身高": 175, "体重": 65}
print(a.join(s4))
# 集合无序,所以这里结果不是确定的
s5 = {"1", "2", "3", "1"}  # 去重
print(a.join(s5))


# str.count(sub, start, end)

a = "hello world"
a1 = a.count("l")  # 3
a2 = a.count("l", 0, 3)  # 1
a3 = a.count("hel", 0, 3)  # 1
a4 = a.count("hle", 0, 3)  # 0
print(a1)  # 3
print(a2)  # 1
print(a3)  # 1
print(a4)  # 0
print("hello world".count("l"))  # 3
print("llll".count("ll"))  # 2,非重叠次数


# str.find(sub[, start[, end]]) 返回从左开始第一次找到指定子字符串时的索引,找不到就返回-1
# str.rfind(sub[, start[, end]]) 返回从右开始第一次找到指定子字符串时的索引,找不到就返回-1
# str.index(sub[, start[, end]]) 类似于find(),唯一不同在于,找不到就会报错,其他都一样
# str.rindex(sub[, start[, end]]) 类似于rfind(),唯一不同在于,找不到就会报错,其他都一样

s = "hello world"
a = s.find("l")  # 2
b = s.rfind("l")  # 9
print(a, b)
a = s.find("l", 4)  # 9
b = s.rfind("l", 4)  # 9
print(a, b)
a = s.find("ell", 1, 5)  # 1
b = s.rfind("ell", 1, 5)  # 1
print(a, b)


# str.capitalize() 将字符串的首字母变成大写,其他字母变小写,并返回
# str.title() 将字符串中所有单词的首字母变成大写,其他字母变小写,并返回
# str.upper() 将字符串中所有字符变成大写,并返回
# str.lower() 将字符串中所有字符变成小写,并返回
# str.swapcase() 将字符串中所有大写字符变成小写,小写变成大写,并返回

a = "hello world"
b = a.capitalize()
print(b)  # Hello world
c = a.title()
print(c)  # Hello World
d = a.upper()
print(d)  # HELLO WORLD
e = d.lower()
print(e)  # hello world
f = c.swapcase()
print(f)  # hELLO wORLD


# str.split(sep=None, maxsplit=-1)

s = " Line1-abcdef   \nLine2-abc \nLine4-abcd"
print(s.split("Li"))
# 默认按照所有的空白符(空格、换行、制表符等)来分割,并从结果中丢弃空字符串
a = s.split()
print(a)
# 按照指定的一个空格" "来分割
a = s.split(" ")
print(a)
# 按照指定的"Li"来分割2次
a = s.split("Li", 2)
print(a)
# maxsplit按照指定的"Li"从右边开始
a = s.rsplit("Li", 2)
print(a)
