# -*- coding: gb2312 -*-
# ���б���ж�ջģ��
stack = []


def push():
    x = input('������һ���ַ����� '.strip())  # s.strip([chars]) ɾ���ַ���s���ߵĿո��ָ�����ַ�
    stack.append(x)
    print('�ַ����� ', x, '��ջ')


def pop():  # pop() ɾ��ָ��λ���ϵ�Ԫ�� �з���ֵ
    if len(stack) == 0:
        print('���ܴӿ�ջ�е�������')
    else:
        print('�ַ�����', stack.pop(), '��ɾ��')


def checkstack():
    print(stack)


dict = {'1': push, '2': pop, '3': checkstack}


def simu_stack():
    ch = '���������ѡ�� 1---push, 2---pop, 3---check, q---�˳�'
    while True:
        while True:
            try:
                choice = input(ch).strip()[0].lower()  # Ŀ�����lower()��Ϊ�˷���дQ��
            except(KeyboardInterrupt, IndexError):
                choice = 'q'
            print('\n�����룺[%s]' % choice)
            if choice not in '123q':
                print('��Чѡ�������')
            else:
                break
        if choice == 'q':
            break
        dict[choice]()


simu_stack()
