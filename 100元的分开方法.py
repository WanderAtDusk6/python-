# -*- coding: gb2312 -*-
# ��һ��Ԫ�ֳɸ�����Ǯ���ж����ַ���

def fn(n):
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    d = [0 for i in range(n + 1)]   # ������n��0���б�
    d[0] = 1
    for i in m:
        for j in range(i, n+1):
            d[j] += d[j-1]
    return d[n] 
        
print(fn(10000))

# MD,��̬
