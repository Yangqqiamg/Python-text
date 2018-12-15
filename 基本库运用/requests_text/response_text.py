import requests

UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'
headers = {
    'User-Agent': UA1+UA2,  # 进行伪装，防止被禁止抓取
}

r = requests.get('http://www.jianshu.com', headers=headers)
print(type(r.status_code), r.status_code)   #状态码及类型
print(type(r.headers), r.headers)           #响应头及类型
print(type(r.cookies), r.cookies)           #cookies及类型
print(type(r.url), r.url)                   #url及类型
print(type(r.history), r.history)           #history及类型

#判断如果状态码不成功的话就程序终止，否则打印成功
exit() if not r.status_code ==requests.codes.ok else print('Request Successfully')