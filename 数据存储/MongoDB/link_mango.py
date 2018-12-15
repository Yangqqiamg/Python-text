import pymongo
#*********************************************************
#链接数据库

#第一个参数为地址， 第二个为端口(不传的话默认27017)
#可以写为：
#client = pymongo.MongoClient('mongodb://localhost:27017/')
client = pymongo.MongoClient(host='localhost', port=27017)
#指定数据库
#也可以用clinet的test属性返回test数据库：
#db = client['text']
db = client.text
#指定集合(类似表)
collection = db.students
#collection = db.['students']

#**********************************************************
#插入数据
student1 = {
    'id': '20151442',
    'name': 'Job',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20151443',
    'name': 'Jady',
    'age': 21,
    'gender': 'high'
}

result = collection.insert([student1, student2])
#返回的是一个每个数据的 _id的集合
print(result)

#**********
#使用insert_one()和 inser_many()来cherubic单条记录和多条记录
student3 = {
    'id': '20151444',
    'name': 'Jdy',
    'age': 14,
    'gender': 'high'
}
student4 = {
    'id': '20151445',
    'name': 'Jay',
    'age': 11,
    'gender': 'high'
}
student5 = {
    'id': '20151446',
    'name': 'ady',
    'age': 31,
    'gender': 'high'
}
result1 = collection.insert_one(student3)
print(result1)
#这里result1 返回的是InsertOneResult对象，可调用 inserted_id属性获取_id
print(result1.inserted_id)

#多条数据使用列表形式传递
result2 = collection.insert_many([student4, student5])
print(result2)
#这里result2 返回的是InsertOneResult多个对象，可调用 inserted_ids属性获取_id
print(result2.inserted_ids)
print('\n')

#**********************************************
#查询信息
#使用 find_one():得到的是单给结果
#    find():返回的是一个生成器，需要用 for语句导出

result3 = collection.find_one({'id': '20151444'})
print(result3)

result4 = collection.find({'age': 20})
print(result4)
for re in result4:
    print(re)
print('\n')

#***********************************************
#计数
#使用count()

count = collection.find().count()
print(count)

count1 = collection.find({'age': 20}).count()
print(count1)
print('\n')

#************************************************
#排序
#使用：sort():传入 pymongo.ASCENDING 指定升序排列
#            传入 pymongo.DESCENDING 指定降序排列

result5 = collection.find().sort('name', pymongo.ASCENDING)
print([resu1['name'] for resu1 in result5])
print('\n')

#************************************************
#偏移
#使用skip()忽略前边几个元素
#使用limit()限制获得几个元素

result5 = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)

