"""
转义字符+Raw字符串+str内置函数
"""

# '\t'——横向制表符(字符和空格一起占8个字符)
print("abcd\tefgh")
print("abcdef\tgh")

# '\b'——往前退一格
str1 = "abcd\befgh"
print(str1)

"""
很多时候我们并不希望字符串转义,比方说在输入一串网址的时候,里面正好有
反斜杠和字母造成了转义,此时为了让该字符串不转义,可以在字符串前面加一
个字母r,表示原始字符串,所有转义都不进行,也就是起到了抑制转义的效果
"""
# http:\\www.abc.com\nc\a\t 想要输出该字符串,但是不想让其转义,挨个加\太多了,麻烦
s1 = "http:\\www.abc.com\nc\a\t1"
print(s1)
s2 = "http:\\\\www.abc.com\\nc\\a\\t"
print(s2)
s3 = r"http:\\www.abc.com\nc\a\t"  # 字符串前面加上r,所有的\都不会转义
print(s3)
s4 = r"http:\\www.abc.com\nc\a\t"  # 字符串前面加上R,所有的\都不会转义
print(s4)

# str()返回参数的字符串形式;不传参时,返回空字符串
print(str())
print(str("abcd+efgh"))
print(str(123))
print(type(str(123)))
print(str(True))
print(type(str(True)))
