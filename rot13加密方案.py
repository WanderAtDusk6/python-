# -*- coding: gb2312 -*-
# ���ֵ�ʵ�����ݼ���
s = 'This is a example that I provide for you' # ԭ��
s1 = 'ABCDEFGHIJKLMNOPQRXTUVWXYZabcdefghijklmnopqrstuvwxyz'
s2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
l1 = list(s1)
l2 = list(s2)
d = dict(zip(l1,l2))
# print(l1,l2,d)  # for test!!!
l1 = []   # ��ʼ�� #### �����ظ�����_(:�١���)_
for c in s :
    if c in d :
        data = d.get(c)
    else :
        data = c  # ��Ӧ�����ǣ�s�������������Լ�
    l1.append(data)

l2 = ['']
for c in l1 :
    l2[0] = l2[0]+c

print(l2[0])


# ����ϼ��ܻ��������ҳ����ִ�͸���д��ͼ�ν���
# ѧ����������ٸ�����д��
