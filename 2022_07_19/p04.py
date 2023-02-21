"""
数字类型转换
"""

# int([x], base=10)
# x:数字或字符串
# base:进制数,默认十进制(要用其他进制时,x必须为字符串)
# [x]:带方框表示该参数为可选参数,将x转换为整数并返回,如果没有指定 x,则返回 0
a = int()  # 不传入参数时,返回0
print(a)  # 0
a = int(3.99)  # 将浮点型转为整型,直接舍弃小数点后面的数,不考虑四舍五入
print(a)  # 3
a = int("12")  # 把整数型字符串"12"转为整型
print(a)  # 12
# a = int("12.1")  # 浮点型的字符串是不行的,会报错
# print(a)
a = int("101010", base=2)  # 基于2进制的"101010"转为十进制的整型
print(a)  # 42
a = int("0b101010", base=2)  # 前面加0b说明是二进制,结果同上
print(a)  # 42
a = int("11", base=8)  # 基于8进制的"11"转为十进制的整型
print(a)  # 9
a = int("0o11", base=8)  # 前面加0o说明是八进制,结果同上
print(a)  # 9
a = int('17', base=16)  # 基于16进制的"17"转为十进制的整型
print(a)  # 23
a = int('0x17', base=16)  # 前面加0x说明是十六进制,结果同上
print(a)  # 23


# float([x])
# x:数字或数字型字符串
# 将x转换成浮点数并返回,不传入参数,则返回0.0
# 字符串两头的空格不影响
a = 123
b = "123"
c = "1.23"  # int不行,float行
print(float())  # 0.0
a1 = float(a)
print(a1)  # 123.0
b1 = float(b)
print(b1)  # 123.0
c1 = float(c)
print(c1)  # 1.23


# bool([x])
# 将给定参数转换为布尔类型,True 或 False
# 如果没有参数,返回 False
# 在进行bool判断时,数字0、False、None、所有的空的容器(比如:空字符串/列表/元组/字典/集合)会被判定为False
# 除此以外,其他均判断为True
print(bool())  # 没有参数,返回False
print(bool(0))  # 0判断为False
print(bool(None))  # None判断为False
print(bool([]))  # 空的都判断为False
print(bool(1))  # True
print(bool(2))  # True
print(bool("0"))  # True


# complex([real], [imag])
# 创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数
# 如果没有参数,则返回0j
# 如果没有参数,则返回0j
print(complex())  # 0j
# 传入两个数字,返回值为real+imag*j的复数
print(complex(3.2, 1))  # (3.2+1j)
# 只传入一个数字,imag则默认为0
print(complex(3.2))  # (3.2+0j)
# 如果第1个参数是字符串,则它被解释为一个复数,不能传第2个参数,第2个参数不能是字符串
print(complex("3.2"))  # (3.2+0j)
print(complex("3.2+1j"))  # (3.2+1j),注意:"+"号两边不能有空格,否则报错
