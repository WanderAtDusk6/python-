# -*- coding: gb2312 -*-
#��һ��������(������)֮ǰ������֮��
s = 0
for i in range(1,11) :
    if i % 2 ==0 :
        continue
    if i % 10 == 7 :
        break
    s+=i
print('s=',s)
       
