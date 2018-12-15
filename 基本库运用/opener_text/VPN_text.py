"""代理：

在爬虫时使用代理的方法
"""
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# ProxyHandler: 参数是一个字典， 键名是协议类型， 键值是代理连接， 可添加多个代理
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    #'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)  # 构建一个Opener
try:
    response = opener.open('https://www.baidu.com')  # 打开链接
    print(response.read().decode('utf-8'))  # 转码打印
except URLError as e:
    print(e.reason)
