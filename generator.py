g = (x*x for x in range(1,9))
print(g)
print(next(g))
print(next(g))

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
for key in fib(9):
    print(key)
#generator 与函数的执行流程不一样 generator 只有在执行next() 的时候才会执行 再次调用时从上次yield语句出执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
print(next(o))
next(o)
next(o)
#杨辉三角联系
def trangel(max):
    nlist = [1]
    n=1;
    while n<max:
        yield nlist
        nlist.append(0)
        nlist = [nlist[i] + nlist[i - 1] for i in range(len(nlist))]
        n=n+1

tran=trangel(10)
for key in tran:
    print(key)

