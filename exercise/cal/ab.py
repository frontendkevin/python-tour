#a^2+b^2=c^2
#a+b+c=1000
import time
start_time=time.time()
for a in range(1000) :
    for b in range(1000) :
        c=1000-a-b
        if a+b+c==1000 and a*a+b*b==c*c:
            print(a,b,c)

end_time=time.time()
print(end_time-start_time)                

