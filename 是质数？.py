# -*- coding: gb2312 -*-
# �ж�һ�����Ƿ�Ϊ����

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
    print('��������')
if i > int(sqrt(x)) :
    print(x,'������')
'''

# version2
from math import *
x = eval(input('������һ����'))
i = 2
while i <= int(sqrt(x)) :
    if x % i == 0 :
        print(x,':����������')
        break
    i += 1
else :
    print(x,':������')
