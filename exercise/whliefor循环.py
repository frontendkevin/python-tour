# 求一百以内的指数
nums=[]

for i in range(3,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            nums.append(i)

print(nums)

# for。。。 else。。。当for循环被完整执行完的时候执行else语句 如果被break 那么不会执行else 后的语句
#enumerate() 可以将列表转化为一个索引为key 的序列
list1=['ab','cd','aa']
for index , value in enumerate(list1):
    print(index,value)


print(str)