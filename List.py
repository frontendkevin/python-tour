#删除列表元素
list1=[1,4,5,6,67]
del list1[2]
print(list)
#列表合并
list2=[2,43,'st']
print(list1 + list2)
#列表重复
print(list2*3)
#元素是否在列表中
print(2 in list1)
#list length
print(len(list1))
#tuple to list
print(list((123, 'Google', 'Runoob', 'Taobao')))
#retur the max in list
print(max(list1))
#return the min in list
print(min(list1))
#apend ele to the end of the list
list1.append(520)
print(list1)
#del the last ele of the list
list1.pop()
print(list1)
#get the index
print(list1.index(4))
#reverse the list
list1.reverse()
print(list1)
#List Comprehensions
list9=[str(x)+char for x in range(1,4) for char in 'abcd']
print(list9)