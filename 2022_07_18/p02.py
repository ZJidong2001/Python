"""
行结构
"""

print(123)  # 一般来说:一个语句就是一行代码,不会跨越多行
print(123456)
print(123); print(456); print(123456)  # 等价写法

a = 4
if a < 3:
    print(True)
else:
    print(False)  # 复合语句可以跨越多行
a = 4
print(True) if a < 3 else print(False)  # 整个复合语句也可以包含于一行之内
