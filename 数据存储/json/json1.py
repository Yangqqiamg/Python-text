#对象：他在JavaScript中是使用花括号{}包裹的内容，结构类型为{key1：value1,key2:value2, .....}
#数组：是使用方括号[]包裹起来的，数据结构为['aa','sss',.....]

import json

#*******
#注意JSON数据不可以使用单引号
#*******
str = """
[{
    "name":"bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"mike",
    "gender":"fmale",
    "birthday":"1995-11-18"
}]
"""
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
#转为JSON对象后，可以使用索引来获取对应的内容
print(data[0])
print(data[0]['gender'])
print(data[0].get('name'))