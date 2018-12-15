import pymysql

#**************
#目的：创建一个名为spders的数据库
#**************

#使用connect()声明一个连接对象 db
#host 传入本地， user和password为用户名和密码， port指定端口
db = pymysql.connect(host='localhost',user='root', password='weisha7740', port=3306)
#调用cursor()获得操作游标
cursor = db.cursor()
#使用execute()执行
#获取版本
cursor.execute('SELECT VERSION()')
#获取上一条数据
data = cursor.fetchone()
#打印
print('database version:', data)
#创建数据库， 名为spiders
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
#关闭
db.close()

