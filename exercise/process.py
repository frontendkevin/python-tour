import os
import time 

num = 100
ret = os.fork()
print("====",ret)
if ret == 0:
    print('process1')
    num+=1
    print("---%d---"%num)
    print(os.getpid())
    print("++++",ret)
else:
    time.sleep(3)
    print('process2')
    print("----%d----"%num)