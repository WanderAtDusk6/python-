# -*- coding: gb2312 -*-
# �����Լ������С������

from math import *
m = eval(input('�������һ����:'))
n = eval(input('������ڶ�����:'))

if m < n :
    m,n = n,m
    b1 = m*n      # t = m*n
while m % n != 0 :
    a = m % n
    m = n
    n = a
b2 = b1/a

print('���ǵ����Լ���ǣ�',a)
print('���ǵ���С�������ǣ�',b2)  #print('��С������'��t//a)
