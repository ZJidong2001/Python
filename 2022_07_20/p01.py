"""
序列有字符串,列表,元组
"""
"""
序列索引
"""

# 正向索引,下标从0开始;反向索引,下标从-1开始
string = "Hello 1牛3 Python"
print(string[0])  # "H"
print(string[-11])  # " "
print(string[10])  # "P"
print(string[-1])  # "n"
print(string[4])  # "o"
print(string[-7])  # " "
print(string[6])  # "1"

list1 = ["H", "e", "l", "l", "o", " ", "1", "牛", "3", " ", "P", "y", "t", "h", "o", "n"]
print(list1[0])
print(list1[-11])
print(list1[10])
print(list1[-1])
print(list1[4])
print(list1[-7])

tup = ("H", "e", "l", "l", "o", " ", "1", "牛", "3", " ", "P", "y", "t", "h", "o", "n")
print(tup[0])
print(tup[-11])
print(tup[10])
print(tup[-1])
print(tup[4])
print(tup[-7])
