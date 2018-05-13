from threading import Thread,Lock
import time
g_num = 0
def test1():
    global g_num
    for i in range(10000000):
        metex.acquire()
        g_num+=1
        metex.release()
    print(g_num)
def test2():
    global g_num
    for i in range(10000000):
        metex.acquire()
        g_num+=1
        metex.release()
    print(g_num)

# 创建一把互斥锁
metex = Lock()
p1 = Thread(target=test1)
p1.start()

# time.sleep(3)

p2 = Thread(target=test2)
p2.start()
