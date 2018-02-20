# -*- coding: gb2312 -*-
# 判断一个数是否为质数

#version1
'''
from math import *
x = eval(input('x='))
i = 2
while i <= int(sqrt(x)) :
    if x % i == 0 :
        break
    i += 1

if i <= int(sqrt(x)) :
    print('不是质数')
if i > int(sqrt(x)) :
    print(x,'是质数')
'''

# version2
from math import *
x = eval(input('请输入一个数'))
i = 2
while i <= int(sqrt(x)) :
    if x % i == 0 :
        print(x,':并不是质数')
        break
    i += 1
else :
    print(x,':是质数')
