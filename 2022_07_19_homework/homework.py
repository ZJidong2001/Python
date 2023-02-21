"""
编写一个 n + 1 的程序, 当用户输入一个整数 n, 则输出 n + 1
例: 用户输入 4, 则程序输出 5
"""

n = int(input("请输入一个整数:"))
print(n+1)

"""
编写一个程序，帮助水果店实现计价功能，用户输入水果单价(元/kg)和重量(kg)，计算出需要花费的金额
例: 用户输入单价 3.98, 输入重量 2.5, 输出 9.95
提示: Python中的乘法用 * 表示
"""

unit_price = float(input("请输入水果单价(元/kg):"))
weight = float(input("请输入水果重量(kg):"))
total_price = unit_price*weight
print("您所花费的金额为", total_price, "元")
