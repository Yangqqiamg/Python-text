#CSV 中文可以叫做都好分隔符或祖父分割值，是纯文本形式储存表格数据。
#就是特定字符分割的纯文本

import csv

with open('writ.csv', 'w') as csvfile:
    #初始化一个对象
    #delimiter='*' 修改列与列之间的分隔符为 ‘*’
    writer = csv.writer(csvfile, delimiter='*')
    #写入语句
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 10])
    writer.writerow(['40050', 'mary', 55])
    writer.writerow(['10005', 'bob', 40])

#使用字典写入
#中文的话要指定表那格式
with open('dis.csv', 'w', encoding='utf-8') as text:
    first = ['id', 'name', 'age']
    #fieldnames=first, 指定字典键名
    #DictWriter 初始化一个字典写入对象
    writer = csv.DictWriter(text, fieldnames=first)
    #调用writeheader() 先写入头信息
    writer.writeheader()
    writer.writerow({'id':'10001','name':'杨', 'age':10})
    writer.writerow({'id':'10002','name':'Mary', 'age':12})
    writer.writerow({'id':'10003','name':'Bob', 'age':34})