import pymysql
db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='luyun123',
    db='mybase',
    use_unicode=True,
    charset='utf8')
#cursor
cursor = db.cursor()

#使用execute 方法执行sql 如果存在 则 删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#使用预处理语句创建表

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()
