import requests

r = requests.get('https://www.baidu.com/')
# 其他POST、PUT、DELETE等请求
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')
print(type(r))  # 获取类型
print(r.status_code)  # 获取状态码
print(type(r.text))  # 获取响应体类型
print(r.text, sep='\n')  # 获取响应体内容
print(r.cookies, sep='\n')  # 获取Cookies
