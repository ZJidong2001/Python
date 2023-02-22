"""
序列切片
"""

# 格式:[起始索引:结束索引:步长]
# 从序列中截取起始索引到结束索引的那部分子序列,包括起始索引,但不包括结束索引
# 当起始索引没有指定时,默认为0,当结束索引没有指定时,默认为序列的长度(前提:步长为正)
# 步长不写默认为1,代表切片时索引依次+1来选择元素,如果步长为2,则切片时索引依次+2来选择元素;如果步长为负数,则从后面开始切片,索引依次做减法

string = "Hello 1牛3 Python"
print(string[7:9])  # "牛3"
print(string[-9:-7])  # "牛3"
print(string[:2])  # "He"(前提步长为正数)
print(string[1:])  # "ello 1牛3 Python"(前提步长为正数)
print(string[:])  # "Hello 1牛3 Python"(前提步长为正数)
print(string[0: 16])  # "Hello 1牛3 Python"(前提步长为正数)
print(string[0:len(string)])  # "Hello 1牛3 Python"(前提步长为正数)
print(string[:1000])  # "Hello 1牛3 Python",索引不能超出范围,切片可以
print(string[0:1000:2])  # "Hlo13Pto",索引不能超出范围,切片可以
print(string[0:5:2])  # "Hlo"
print(string[-3:-8:-2])  # "hy "
print(string[-3:-8])  # error,虽然不会报错,但什么都没有切到,为空
print(string[13:8:-2])  # "hy"
print(string[::-1])  # 步长为负时,默认倒着输出
print(string[-1::-1])
print(string[len(string)-1:-len(string)-1:-1])
print(string[-1:5:-1])  # 起始索引和结束索引不必管二者正负,只在二者之间对应的这一段截取
