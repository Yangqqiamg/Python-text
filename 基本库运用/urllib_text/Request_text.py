from urllib import request, parse

"""Request()参数使用模板：

class urllib.request.Request(url, data=None, headers={}, origin_req_host=None,
                            unverifiable=False, method=None)
(1) url：必填参数
(2) data: 如果要传，必须传bytes类型(可使用urllib.parse中的urlencode()转换)
(3) headers: 是一个字典，就是请求头,最常用的方法就是通过修改User-Agent来伪装浏览器
(4) oringin_req_host: 指的是请求方的host名称或者是IP地址
(5) unverifiable: 默认值是False,意思是用户没有足够的权限来获取这个请求的结果
(6) method: 用来指示请求使用的方法， 如： GET, POST和PUT等
"""
#url = 'https://python.org'
url = 'http://httpbin.org/post'
"""先手添加header信息
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; windows NT)',# 伪装信息
    'Host': 'httpbin.org'
}"""
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')  # 进行转码为bytes类型
req = request.Request(url=url, data=data, method='POST')
# 后手添加header信息
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; windows NT)')


"""urlopen()参数使用模板：

urllib.request.urlopen(url, data=None, [timeout,]*,cafile=None, capath=None,
                        cadefault=Fales, context=None)

"""
response = request.urlopen(req)

print(response.read().decode('utf-8'))  # 将utf-8编码的解码
print(response.getheaders())  # 显示响应头
