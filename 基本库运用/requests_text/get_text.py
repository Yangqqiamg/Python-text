import requests

#附加信息到链接,构建字典，使用参数params构成
data = {
    'name': 'germey',
    'age': '52',
}

r = requests.get('http://httpbin.org/get', params=data)
print(type(r))
print(type(r.text))
print(r.text)# 打印响应体内容
print(r.status_code)
print(type(r.json()))#获取为json格式的类型
print(r.json())#获取为json格式


