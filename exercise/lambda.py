student = [{"name":'a',"age":19},{"name":'c',"age":33},{"name":'r',"age":55}]
student.sort(key=lambda x:x['age'])
print(student)


def test(a,b,func):
    return func(a,b)

x = test(1,3,lambda a,b: a+b)    
print(x)

a=6 
b=4
a , b = b , a 

print(a,b)