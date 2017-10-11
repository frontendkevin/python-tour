#字典的key可以是任何不可变的数据类型 例如数字 字符串 元组
#字典的值可以是任何类型
dict1={'alice':6,'kevin':9}
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del  ele of dict
del dict1['alice']
print (dict1)
#clear the whole dict
dict1.clear()
#del dict
del dict1
dict3={'Age':9}
dict2.update(dict3)
print(dict2)

for key,value in dict2.items():
    print(key,value)

