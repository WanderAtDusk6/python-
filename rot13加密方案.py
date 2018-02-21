# -*- coding: gb2312 -*-
# 用字典实现数据加密
s = 'This is a example that I provide for you' # 原文
s1 = 'ABCDEFGHIJKLMNOPQRXTUVWXYZabcdefghijklmnopqrstuvwxyz'
s2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
l1 = list(s1)
l2 = list(s2)
d = dict(zip(l1,l2))
# print(l1,l2,d)  # for test!!!
l1 = []   # 初始化 #### 算是重复利用_(:з」∠)_
for c in s :
    if c in d :
        data = d.get(c)
    else :
        data = c  # 这应该是是（s）其他语言用自己
    l1.append(data)

l2 = ['']
for c in l1 :
    l2[0] = l2[0]+c

print(l2[0])


# 这麻瓜加密还不错，等我出新手村就给它写个图形界面
# 学完面向对象再给你重写下
