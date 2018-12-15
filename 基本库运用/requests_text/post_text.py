import requests



#POST请求一般用于表单请求，把数据提交给网站
data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
