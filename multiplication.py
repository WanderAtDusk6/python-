# -*- coding: gb2312 -*-
# 乘法表（multiplication）
'''
# version1
print()
for x in range(1,10):
    for y in range(1,10):
        print(x*y,end = '\t')
    print()
'''

# version2
m = 1
while m <= 9:
    n = 1
    while n <= m:
        print(m*n,end = '\t')
        n = n+1
    m += 1
    print()
        


        
