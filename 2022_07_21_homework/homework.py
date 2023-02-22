""" 把print函数输出的内容, 改为3种字符串格式化方式分别表示, 注意空格标点符号一致 """
name1 = "张三"
age1 = "18"
print("我是", name1, ", 我今年", age1, "岁了, ", "明年我", int(age1)+1, "岁!", sep="")

# %格式化
print("我是%s, 我今年%s岁了, 明年我%d岁!" % (name1, age1, int(age1)+1))
# format格式化
print("我是{}, 我今年{}岁了, 明年我{}岁!".format(name1, age1, int(age1)+1))
# f-string格式化
print(f"我是{name1}, 我今年{age1}岁了, 明年我{int(age1)+1}岁!")


# string = "hello world"，代码实现：得到字符串为 "h~e~l~l~o~w~o~r~l~d"

print("~".join("hello world".replace(" ", "")))


# string = "hello world"，代码实现：请输出字符串中最后一次出现字符"l"的索引

print("hello world".rfind("l"))


# name = " gouguoQ "，代码实现：将字符串中的第一个"o"，替换为"p"，并输出结果

print(" gouguoQ ".replace("o", "p", 1))


# name = " gouguoQ   "，代码实现：移除字符串两边的空格，并输出结果

print(" gouguoQ   ".strip())
