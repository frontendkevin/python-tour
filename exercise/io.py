
# 复制图片
with open('./files/bg.png','rb') as f:
    w=open('./files/bg1.png','wb')
    w.write(f.read())
# 复制文本
with open('./files/hello.txt','r') as a:
    b=open('./files/world.txt','a')
    b.write(a.read())