"""
输入
"""

# input([prompt])
# prompt:提示信息,string类型(可选参数)
# 函数接受一个标准输入数据,返回为string类型
res = input()  # 以字符串的形式返回
print(res)
print(type(res))
name = input("请输入你的姓名:\n")  # \n在下一行输入
print(name, "您好,很高兴认识你！")
