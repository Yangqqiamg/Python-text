import pymongo

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

#*********************************************
#更新数据
#使用update()

#选择更新的目标信息
condition = {'name': 'Jady'}
#寻找
student = collection.find_one(condition)
#修改
student['age'] = 3
#更新
result = collection.update(condition, {'$set': student})
print(result)

#使用update_one()和 update_many()

#选择更新的目标信息
condition = {'name': 'ady'}
#寻找
student = collection.find_one(condition)
#修改
student['age'] = 61
#更新
result = collection.update_one(condition, {'$set': student})
print(result)
#matched_count: 获得匹配的数据条数
#modified_count: 获得影响的数据条数
print(result.matched_count, result.modified_count)


#选择更新的目标信息, 年龄大于5
condition = {'age': {'$gt': 5}}
#更新，把符合的年龄都加 1
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
#matched_count: 获得匹配的数据条数
#modified_count: 获得影响的数据条数
print(result.matched_count, result.modified_count)