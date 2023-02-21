"""
输出
"""
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects：输出的对象,输出多个对象时,需要用,分隔,对象会被转成字符串再输出(不定长参数)
# sep：输出的对象用什么间隔开来,默认值是一个空格(默认参数)
# end：输出最后用什么结尾,默认值是换行符\n(默认参数)
# file：要写入的文件对象,默认为sys.stdout,指向控制台(默认参数)
# flush：通常输出是否被缓存决定于flush,如果flush参数为True,流会被强制刷新(默认参数)

# objects
print(1, 2, 3, 4)  # 中途有str()转成字符串的操作
print()  # 相当于换行,因为无对象时end默认换行

# sep
print(1, 2, 3, 4, sep='-')  # 默认空格间隔
print(1, 2, 3, 4, sep='9')  # 默认空格间隔

# end
print(5)  # 默认末尾换行
print(1, 2, 3, 4)
print(5, end='—')  # 默认末尾换行
print(1, 2, 3, 4)
print(1, 2, 3, sep="-", end="\n\n")  # 把三个数字1,2,3转成字符串写入流,并用"-"分隔,结尾换两行
print(5)

# file
# print默认在终端输出
with open('./abc.txt', mode='w')as f:  # 目前了解即可
    print(12345, file=f)  # 把12345直接写入abc.txt文件

# flush
import time  # 需要用到模块里的sleep函数
print("Loading", end="")
for i in range(10):
    # 如果这里flush为False,则要等10次循环结束之后,终端才会现实结果
    # 而flush为True,则每次循环都会刷新一次结果,看起来就是动态的效果
    print(".", end='', flush=True)
    time.sleep(0.3)  # 延迟0.3秒再往后执行
