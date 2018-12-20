from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

#基础网站，后边组合
base_url = 'https://m.weibo.cn/api/container/getIndex?'#

UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'
headers = {
    'Host':'m.weibo.cn',                            #指定请求资源的主机IP和端口号
    'Referer': 'https://m.weibo.cn/u/2830678474',   #标识这个请求时从哪个网页发过来的
    'User-Agent': UA1+UA2,                          # 进行伪装，防止被禁止抓取
    'X-Requestd-With': 'XMLHttpRequest',            #可以用来判断客户端的请求是Ajax请求还是其他请求
    }

###########################
#  构建后半URL和捕获信息   #
##########################

def get_page(page):
    #构建URL参数，使用urlencode转换
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page,
    }
    #使用urlencode()方法整合，形成类似https://m.weibo.cn/api/container/getIndex?
    #type=uid&value=2830678474&containerid=1076032830678474&page=2 的URL
    url = base_url + urlencode(params)
    try:
        #用requests请求这个链接，添加headers属性
        response = requests.get(url, headers=headers)
        #判断响应码是否正常
        if response.status_code == 200:
            #解析为JSON并返回信息
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

############################
#解析方法，提取想要的信息   #
##########################

def parse_page(json):
    if json:
        #获取资源内 data 中 cards 的内容
        items = json.get('data').get('cards')
        #print(items)
        #遍历cards内
        #enumerate() 给每项编号(index参数)
        for index, item in enumerate(items):
            #跳过他关注的博主这一项(即第一页第二项)
            if page == 1 and index ==1:
                continue
            else:
                #获取 mblog 选项内容
                item = item.get('mblog')
                #print(item)
                weibo = {}
                weibo['id'] = item.get('id')
                #使用 pyquery 将正文中的HTML标签去掉 （用法：py(html文本).text()
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                #迭代 weibo内容 相当于只有所有信息添加完了才 return
                yield weibo

##########################
# 上传到MongoDB          ##
# #########################

#链接数据库
client = MongoClient(host='localhost', port=27017)
#指定数据库
db = client['weibo']
#指定集合(类似表)
collection = db['weibo']

def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mpngo')

#######################
#    主程序           #
######################

#判断是否在本文件执行函数
#当其他文件导入本文件时不执行下边代码
if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        # print(json)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
        #parse_page(json)



