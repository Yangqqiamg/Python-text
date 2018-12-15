import pymysql

#*************
#目的：在数据库spiders中的一个名为students的表中，添加数据
#*************

###################
#普通方法
######################

#插入内容
# i = '201514138'
# user = 'mike'
# age = 20

# #打开数据库
# db = pymysql.connect(host='localhost', user='root', password='weisha7740',
#      port=3306, db='spiders')
# #获得操作游标
# cursor = db.cursor()
# #数据插入语句， 用 %s代表数值
# sql = 'INSERT INTO text(id, name, age) values(%s, %s, %s)'
# try:
#     #执行，写入语句，且以元组的形式写入数值
#     cursor.execute(sql, (i, user, age))
#     print('ok')
#     #只用调用commit()方法后，对数据的更新、插入、删除才生效
#     db.commit()
# except:
#     #调用rollback()方法执行数据回滚，相当于什么都没发生
#     db.rollback()
#     print('no')
# db.close()

#####################
#根据字典来构建动态长度
#功能：
#可储存数据到表中，并可以更新数据
#####################

data = {
    'id': '201514180',
    'name': 'job',
    'age': 28
}
table = 'students'
#语法：  'sep'.join(seq)
#参数说明:
#sep：分隔符。可以为空
#seq：要连接的元素序列、字符串、元组、字典
#这里时获取data的键名，并以 ', '间隔
keys = ', '.join(data.keys())
#data的长度乘以 %s
values = ', '.join(['%s'] *len(data))
#打开数据库
db = pymysql.connect(host='localhost', user='root', password='weisha7740', port=3306, db='spiders')
#获得操作游标
cursor = db.cursor()

def update_msg():
    #数据插入语句， 用 %s代表数值
    #方法format() 分别替代前边的 {}的值， 可用序号或者键值对来指定
    #例子：
    #1、
    #print('hello{0} i am {1}'.format('Kevin','Tom'))
    #结果为： hello Kevin i am Tom
    #
    #2、
    #names={'name':'Kevin','name2':'Tom'}
    #print ('hello {names[name]}  i am {names[name2]}'.format(names=names))
    #结果为： hello Kevin i am Tom
    #DUPLICATE KEY UPDATE : 意思是如果主键(id)存在， 则执行更新操作
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
    #更新语句
    #从data中获取键名，并用‘，’隔开
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    #总语句为：
    # sql = INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = $s, name = %s, age = %s
    sql += update
    try:
        #执行，写入语句，且以元组的形式写入数值
        #tuple() 函数将列表转换为元组。
        #有6个%s 所以要乘以2
        if cursor.execute(sql, tuple(data.values())*2):
            print('ok')
            #只用调用commit()方法后，对数据的更新、插入、删除才生效
            db.commit()
    except:
        print('no')
        #调用rollback()方法执行数据回滚，相当于什么都没发生
        db.rollback()
    db.close()

def delete_msg():
    #***********
    #删除操作
    condition = 'age >20'

    sql ='DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
    try:
        cursor.execute(sql)
        print('success delete')
        db.commit()
    except:
        print('failed')
        db.rollback()
    db.close()

def find_msg():
    sql = 'SELECT * FROM students WHERE age >= 15'

    try:
        cursor.execute(sql)
        #调用 rowcount属性获取查询结果的条数
        print('Count:', cursor.rowcount)
        #调用方法 fetchone()获取第一条结果
        one = cursor.fetchone()
        print('One:', one)
        #获取所有数据，但因为其内部具有一个偏移指针来指向查询结果，最开始fetchone()方法获取了一次数据，
        #取了一次之后偏移到下一个数据，所以没有打印第一个数据。
        results = cursor.fetchall()
        print(type(results))
        for row in results:
            print(row)

        #建议使用如下获取逐条数据
        #原理：
        #   由于具有偏移指针，每获取一次row值的时候，指针就会向下一个偏移，
        #只要 row为真就依次获取所有值。
        # ********************************
        # *row = cursor.fetchone()       *
        # *while row:                    *
        # *     print('Row:', row)       *
        # *     row = cursor.fetchone()  *
        # ********************************
    except:
        print('Error')

#delete_msg()
#update_msg()
find_msg()