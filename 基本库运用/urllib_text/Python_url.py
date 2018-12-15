import urllib.request


"""urlopen()参数使用模板：

urllib.request.urlopen(url, data=None, [timeout,]*,cafile=None, capath=None,
                        cadefault=Fales, context=None)

"""
requert = urllib.request.urlopen('https://www.python.org')

# print(requert.read().decode('utf-8'))#抓取整个网页

# print(type(requert))# 抓取返回响应类型

"""得出是一个HTTPResponse类型，可使用函数：
    read(), readinto(), getheaders(), getheader('name'), fileno()
"""

print(requert.status)  # 抓取响应的状态码
print(requert.getheaders())  # 抓取响应头response headers的信息
print(requert.getheader('Server'))  # 抓取响应头response headers信息中的Server
