# -*- coding: gb2312 -*-
# ������ε�ת�� ȫ�֣�global����ֻ������һ��ģ�nonlocal��

# gobal //e.g. ���ڶ���תΪȫ��
a = 1
def second():
    global a
    a = 2
    def thirth():
        a = 3
        print('third a:',a)
    thirth()
    print('second a:',a)
second()
print('first a:',a)     # ���Ӧ�� 3a 3\  2a 2\ 1a 2


# nonlocal //e.g. �����Ĳ�����һ��
print()
a = 1
def second():
    a = 2
    def third():
        a = 3
        def fourth():
            nonlocal a
            a = 4
            print('fourth_a',a)
        fourth()
        print('third_a',a)
    third()
    print('second_a',a)
second()
print('first_a',a)       # ���4a 4\3a 4\2a 2\1a 1
