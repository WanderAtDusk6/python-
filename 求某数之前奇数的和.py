# -*- coding: gb2312 -*-
#求一个输入数(例如七)之前的奇数之和
s = 0
for i in range(1,11) :
    if i % 2 ==0 :
        continue
    if i % 10 == 7 :
        break
    s+=i
print('s=',s)
       
