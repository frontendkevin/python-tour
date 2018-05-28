# copy file
old = input('plase input filename')
with open(old,'r') as f:
    print(f.read())
w=open('./files/world.txt','w')
w.write(f.read())
w.close()
#big file copy
# newfile= open('xxx.txt')
# oldfile=open('yy.txt')
# while True:
#     content = oldfile.read(1024)
#     if len(content)==0:
#         break
#     newfile.write(content)
# newfile.close()
# oldfile.close()
