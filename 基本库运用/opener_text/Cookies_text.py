"""Cookies:

获取网站上的Cookies
"""
import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()  # 声明一个cookie对象
hander = urllib.request.HTTPCookieProcessor(cookie)  # 构建一个Hander
opener = urllib.request.build_opener(hander)  # 构建一个Opener
response = opener.open('https://www.baidu.com')  # 通过Opener打开链接
for item in cookie:
    print(item.name + '=' + item.value)  # 循环打印cookie的键值对

'''
把cookies输出文本格式
'''
filename = 'cookies.txt'  # 文本名称
# 通过MozillaCookieJar类来处理读取或保存Cookies,保存为Mozilla型浏览器的Cookies格式
cookie = http.cookiejar.MozillaCookieJar(filename)
# 通过LWPCookieJar类来处理读取或保存Cookies,保存为LWP格式的Cookies文件
# 即输出LWP格式
#cookie = http.cookiejar.LWPCookieJar(filename)
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
