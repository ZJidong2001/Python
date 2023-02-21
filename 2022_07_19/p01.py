"""
数字4种类型+type内置函数
"""

# int、float、bool、complex

print(3.)  # 小数点后面无数字也是浮点数
print(4e210)  # 科学计数法也是浮点数,为4*10^210
print(1.23e5)
print(123e5)

print(True)  # True默认为1,关键字
print(False)  # False默认为0,关键字
print(True + 3)
print(False + 5)

print(1j)  # 复数j前面的系数不能省略,能省略的话与变量矛盾,而前面有系数肯定不是变量,变量名定义数字不开头
print(0j == 0)  # 复数0j等于整数0

# type内置函数,返回对象的数据类型
tp1 = type(1234)  # tp1是变量,返回结果交给变量
print(tp1)
print(type(1234))  # 内置函数type,返回类型让print打印
print(type(1234.))
print(type(1e3))
print(type(True))
print(type(0j))  # 尽管值等于整数0,但数据类型仍是复数
