import time
import functools
# def deco(func):
#     def wraper(a,b):
#         startTime = time.time()
#         func(a,b)
#         endTime = time.time()
#         msg = (endTime - startTime) * 1000
#         print(msg)
#     return wraper;
#
# def  myfunc(a,b):
#     print('start')
#     time.sleep(0.6)
#     s=a+b;
#     print(s)
#
# myfunc=deco(myfunc)
# myfunc(1,3)

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call $s():' func.__name__)
        return func(*args,**kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
