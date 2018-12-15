import requests
import re

UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'
headers = {
    'User-Agent': UA1+UA2,  # 进行伪装，防止被知乎禁止抓取
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)# 抓取知乎发现页面
patten = re.compile('explore-feed.*question_link.*?>(.*?)</a>', re.S)  # 正则表达式
titles = re.findall(patten, r.text)
print(titles)

'''抓取图片音频视频：

这些文件本质就是二进制码组成
'''
import requests

#content 输出类型为 str
#text 输出类型为 unicode,bytes类型
v = requests.get("http://qiniuuwmp3.changba.com/1105772936.mp3")
print(v.text)
print(v.content)
# 没有‘+’则只能进行此模式
#读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件
# w     以写方式打开，
# a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+     以读写模式打开
# w+     以读写模式打开 (参见 w )
# a+     以读写模式打开 (参见 a )
# rb     以二进制读模式打开
# wb     以二进制写模式打开 (参见 w )
# ab     以二进制追加模式打开 (参见 a )
# rb+    以二进制读写模式打开 (参见 r+ )
# wb+    以二进制读写模式打开 (参见 w+ )
# ab+    以二进制读写模式打开 (参见 a+ )
with open('favicon.mp3', 'wb') as f:  #以二进制写模式打开(没有就新建一个)
    f.write(v.content)
