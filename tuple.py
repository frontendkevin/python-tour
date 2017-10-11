#创建元组
tup1=(1,2,1,2,1,2)
tup2=(2,4,'sdf','sd')
#visit tuple
print(tup1[1])
print(tup2[3])
#updating tuple is not allowed
#元组的元素是不能删除的  但是可以用del 删除整个元组
del tup1
# print(tup1) 报错了
tup3=tup2[0:]
print(tup3 is tup2)
#元组也可以不用小括号包裹 任何用逗号隔开的序列都可以叫元组
# tuple()可以将列表转化为元组 list()可以将元组转化为列表
# 定义一个只有一个元素的元组必须加一个逗号
tup4=(0,)

#tuple定义后是不可变的 但是tuple 内的列表或者字典的元素是可以变的

