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

#*************************
#删除
#使用remove()
result = collection.remove({'name': 'Jady'})
print(result)

#使用delete_one()和delete_many()
#删除第一条满足条件的信息
result1 = collection.delete_one({'name': 'ady'})
print(result1)
print(result1.deleted_count)
#删除所有年龄小于10的信息
result2 = collection.delete_many({'age': {'$lt': 50}})
print(result2)
print(result1.deleted_count)

