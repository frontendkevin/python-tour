#使用多进程copycopy文件
from multiprocessing import Pool,Manager
import os

def copyTask(name,oldFolderName,newFolderName,queue):
    #完成拷贝一个文件的功能
    fr = open(oldFolderName+'/'+name)
    fw = open(newFolderName+'/'+name,"w")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(name)
def main():
    #获取文件夹的名字
    oldFolderName = input('please input folder name')
    #新文件夹名字
    newFolderName = oldFolderName+"-复件"
    #创建一个新文件夹
    os.mkdir(newFolderName)
    #获取文件夹内所有文件的名字
    fileNames = os.listdir(oldFolderName)
    #使用多进程拷贝文件
    pool = Pool(4)
    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyTask,args=(name,oldFolderName,newFolderName,queue))

    num =  0
    allNum = len(fileNames)
    while True:
        queue.get()
        num+=1
        copyRate = num/allNum
        print("rate is %.2f%%"%(copyRate*100))
        if num == allNum:
            break

if __name__ == '__main__':
    main()    
