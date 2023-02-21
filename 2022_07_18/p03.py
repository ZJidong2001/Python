"""
缩进
"""

a = 4
if a < 3:
    print(True)  # 缩进默认4个空格(Tab键)
print(789)

a = 4
if a < 3:
    print(True)
        print(123)  # 这个缩进不对,同为if语句下的代码,应该和上面一个print缩进一样
else:
        print(False)  # 这个缩进没问题,它在else语句下面,可以和if语句下的print缩进不一样
print(789)  # 这个print是在if...else...语句外面的,是平级的,不需要缩进
