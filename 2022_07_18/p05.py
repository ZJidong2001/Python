"""
拼接
"""

# 显式的行拼接——使用反斜杠(\)
# 下面 a,b 两种写法都是可以的,结果是一样的
a = 1 + 2 + 3
b = 1 + \
    2 + \
    3
print(a)
print(b)


# 隐式的行拼接——圆括号、方括号或花括号以内的多行语句,无需使用反斜杠(\)
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
