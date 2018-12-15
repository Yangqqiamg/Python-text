import urllib.parse
import urllib.request

#使用data参数需要使用bytes()方法将参数转化为字节流码格式（即bytes类型）
#并请求方法要使用POST
#第一个参数需为字符串， 第二个参数指定编码格式
#模拟了表单提交的方式输出的是'word':'hello'
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')

"""urlopen()参数使用模板：

urllib.request.urlopen(url, data=None, [timeout,]*,cafile=None, capath=None,
                        cadefault=Fales, context=None)

"""
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read())