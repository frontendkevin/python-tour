import pymysql
#open connenction
conn =  pymysql.connect(host='127.0.0.1',port=3306,user='root',password='luyun123',db='mybase')
#cursor
cursor = conn.cursor()

#查询
cursor.execute('SELECT VERSION()')

#使用fetchone 方法获取单挑数据
data = cursor.fetchone()

print("data version is : %s " %data)

#关闭数据库

conn.close()