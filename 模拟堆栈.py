# -*- coding: gb2312 -*-
# 用列表进行堆栈模拟
stack = []


def push():
    x = input('请输入一个字符串： '.strip())  # s.strip([chars]) 删除字符串s两边的空格或指定的字符
    stack.append(x)
    print('字符串： ', x, '入栈')


def pop():  # pop() 删除指定位置上的元素 有返回值
    if len(stack) == 0:
        print('不能从空栈中弹出数据')
    else:
        print('字符串：', stack.pop(), '已删除')


def checkstack():
    print(stack)


dict = {'1': push, '2': pop, '3': checkstack}


def simu_stack():
    ch = '请输入你的选择： 1---push, 2---pop, 3---check, q---退出'
    while True:
        while True:
            try:
                choice = input(ch).strip()[0].lower()  # 目测这个lower()是为了防大写Q，
            except(KeyboardInterrupt, IndexError):
                choice = 'q'
            print('\n你输入：[%s]' % choice)
            if choice not in '123q':
                print('无效选项，请重试')
            else:
                break
        if choice == 'q':
            break
        dict[choice]()


simu_stack()
