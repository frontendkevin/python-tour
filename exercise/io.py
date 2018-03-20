
with open('./files/hello.txt','r') as f:
    print(f.read())
w=open('./files/world.txt','w')
w.write('i want you')