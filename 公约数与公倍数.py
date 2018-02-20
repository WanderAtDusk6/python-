# -*- coding: gb2312 -*-
# 求最大公约数与最小公倍数

from math import *
m = eval(input('请输入第一个数:'))
n = eval(input('请输入第二个数:'))

if m < n :
    m,n = n,m
    b1 = m*n      # t = m*n
while m % n != 0 :
    a = m % n
    m = n
    n = a
b2 = b1/a

print('它们的最大公约数是：',a)
print('它们的最小公倍数是：',b2)  #print('最小公倍数'，t//a)
