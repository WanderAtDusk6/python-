# -*- coding: gb2312 -*-
# ����е�ֵ
from math import *
from time import clock
clock()    #������ʱ
# k��ʾ������t��ʾ��ʽ���ĳ������
n, k, t, pi1 = 1, 1, 1.0, 0.0
while abs(t) > 1.0E-8 :
    pi1 = pi1 + t
    n = n + 2
    k = -k
    t = (1.0/n)*k

print('���������Ħе�ֵ�� ', 4*pi1)
print('mathģ��Ħ�ֵ�� ', pi)
print('����ʱ�䣺 ', clock(), 's')