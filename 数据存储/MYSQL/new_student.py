import pymysql


#*************
#目的：在数据库spiders中，创建一个名为students的表
#*************

#创建数据库之后，谅解时需要指定参数 db=‘数据库名’
db = pymysql.connect(host='localhost', user='root', password='weisha7740',
                     port=3306, db='spiders')
#获得操作游标
cursor = db.cursor()
#MySQL支持创建持数据表时判断是否存在，存在不创建，不存在则创建表students
#ID 长度不超过（255）不为空
#NAME 长度不超过（255）不为空
#AGE 为int型 且不为空
#主关键字(primary key)是表中的一个或多个字段，它的值用于唯一地标识表中的某一条记录，
#在两个表的关系中，主关键字用来在一个表中引用来自于另一个表中的特定记录
sql = 'CREATE TABLE IF NOT EXISTS text(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
#执行
cursor.execute(sql)
#关闭
db.close()