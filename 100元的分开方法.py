# -*- coding: gb2312 -*-
# 将一百元分成各种零钱，有多少种方法

def fn(n):
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    d = [0 for i in range(n + 1)]   # 产生了n个0的列表
    d[0] = 1
    for i in m:
        for j in range(i, n+1):
            d[j] += d[j-1]
    return d[n] 
        
print(fn(10000))

# MD,变态
