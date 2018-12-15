from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

try:
    #python2.x 版本
    from urllib2 import urllib
except ImportError:
    from urllib.request import urlopen


                    ##### 运用urloen #####
#import json
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# #读取数据
# req = response.read()
# #将数据写入文件
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)

# #开始加载json格式
# file_urllib = json.loads(req)
# print(file_urllib)

                    ##### 运用requexts ####

import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
#将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
file_requests = req.json()