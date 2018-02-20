# -*- coding: 2312 -*-
# 用列表模拟队列
queue = []

def en_queue() :
    x = input('输入一个字符串： ').strip()
    queue.append(x)
    print('字符串： ', x, '进队')


def out_queue() :
    if len(queue)==0:
        print('不能从空队列里弹出数据')
    else:
        print('字符串： ', queue.pop(0), '已移除')

