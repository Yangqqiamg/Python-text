import socket
import urllib.request
import urllib.error


"""urlopen()参数使用模板：

urllib.request.urlopen(url, data=None, [timeout,]*,cafile=None, capath=None,
                        cadefault=Fales, context=None)

"""
try:
    #限时1ms
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.5)
    print(response.read())
#检查错误
except urllib.error.URLError as e:
    #判断错误是否为timeout
    if isinstance(e.reason, socket.timeout):
        print('Time Out')

