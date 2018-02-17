# 不知道干嘛的函数
def f(x):
    if x =='' :
        return x
    else :
        return f(x[1:]) + x[0]

f(input())



    
