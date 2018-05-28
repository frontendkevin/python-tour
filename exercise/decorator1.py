#装饰器原理
def w1(func):
    def inner():
        print('----正在验证-----')
        func()
    return inner
def f1():
    print('-----f1-------')
f1=w1(f1)
f1()   
#装饰器语法
def w2(func):
    def inner():
        print('----正在验证-----')
        func()
    return inner
@w2 
def f2():
    print('-----f2-------')  
f2()  
#两个装饰器
def w3(func):
    print('---------正在装饰3--------')
    def inner():
        func()
    return inner    
def w4(func):
    print('------正在装饰4--------')
    def inner():
        func()
    return inner
@w3
@w4
def f3():
    print('-----f3------')
f3()
#通用装饰器
def decFunc(func):
    def inner(*args,**kargs):
        return func(*args,**kargs)
    return inner    
@decFunc
def f4(a,b):
    print('-------pppp---------')
f4(1,3)           
    