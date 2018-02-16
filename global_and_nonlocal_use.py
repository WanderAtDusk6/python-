# -*- coding: gb2312 -*-
# 变量层次的转化 全局（global）与只是向上一层的（nonlocal）

# gobal //e.g. 将第二层转为全局
a = 1
def second():
    global a
    a = 2
    def thirth():
        a = 3
        print('third a:',a)
    thirth()
    print('second a:',a)
second()
print('first a:',a)     # 输出应是 3a 3\  2a 2\ 1a 2


# nonlocal //e.g. 将第四层上移一层
print()
a = 1
def second():
    a = 2
    def third():
        a = 3
        def fourth():
            nonlocal a
            a = 4
            print('fourth_a',a)
        fourth()
        print('third_a',a)
    third()
    print('second_a',a)
second()
print('first_a',a)       # 输出4a 4\3a 4\2a 2\1a 1
