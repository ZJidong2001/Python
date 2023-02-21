print("执行第1行啦")
print(2 / 0)  # 报错
print("执行第3行啦")
a = 123


def add(left, right):
    print("执行第8行啦")
    print("执行第9行啦", left + right)


print("执行第12行啦")
add(3, 4)
a = 124
print("执行第15行啦")

"""
学会查看Python语法提示、报错提示以及代码调试(debug)
"""
