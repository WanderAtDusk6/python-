# -*- coding: gb2312 -*-
# 计算π的值
from math import *
from time import clock
clock()    #启动计时
# k表示正负，t表示公式里的某项数据
n, k, t, pi1 = 1, 1, 1.0, 0.0
while abs(t) > 1.0E-8 :
    pi1 = pi1 + t
    n = n + 2
    k = -k
    t = (1.0/n)*k

print('程序计算出的π的值： ', 4*pi1)
print('math模块的π值： ', pi)
print('运行时间： ', clock(), 's')