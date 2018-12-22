#***************************#
# 功能：爬取今日头条街拍美照  #
# *************************#

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


#########################
#构建基础 url ，并获取信息，转为JSON格式
#########################
def get_page(offset):
    UA1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_14)'
    UA2 = 'AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.166 Safari/537.36'
    headers = {
        'Host':'www.toutiao.com',                            #指定请求资源的主机IP和端口号
        'Referer': 'https://www.toutiao.com/search/?keyword=街拍',   #标识这个请求时从哪个网页发过来的
        'User-Agent': UA1+UA2,                          # 进行伪装，防止被禁止抓取
        'X-Requestd-With': 'XMLHttpRequest',            #可以用来判断客户端的请求是Ajax请求还是其他请求
    }
    #构建 url 所需信息
    lists = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    url ='https://www.toutiao.com/search_content/?' + urlencode(lists)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except:
        print('error!')

# print(get_page(20))
# json = get_page(20)
# print(json.get('data'))

########################
#获取图片信息
########################

def get_images(json):
    #如果可以获取data属性内文本
    if json.get('data'):
        #遍历data文本
        for item in json.get('data'):
            #获取title属性
            title = item.get('title')
            if  item.get('cell_type'):
                continue
            #获取image_list属性
            images = item.get('image_list')
            #错误命名时使用
            group_id = item.get('group_id')
            #遍历image
            for image in images:
                #构建生成器
                yield{
                    #获取 URL属性
                    'image': 'http:'+ image.get('url'),
                    'title': title,
                    'error_id': 'url_' + group_id
                }

#########################
#保存图片信息
#########################

def save_image(item):

    #os.path.exists(path)
    #如果path存在，返回True；如果path不存在，返回False。
    #新建一个放图片集的文件夹
    if not os.path.exists('image'):
        os.mkdir('image')
    #新建一个放各类图片的子文件夹
    if not os.path.exists('image/' + item.get('title')):
        try:
            #建立一个文件夹名为title
            os.mkdir('image/' + item.get('title'))
        #假如出现了命名问题错误，就使用 error_id 进行命名
        except NotADirectoryError:
            if not os.path.exists('image/' + item.get('error_id')):
                print("worry")
                os.mkdir('image/' + item.get('error_id'))
    try:
        #获取item属性的 image值
        response = requests.get(item.get('image'))
        if response.status_code ==200:
            #使用format()方法套入{}构建名字，方法 md5()获取内容的MD5值
            file_path = '{0}/{1}/{2}.{3}' .format('image',item.get('title'), md5(response.content).hexdigest(), 'jpg')
            try :
                #判断是否已下载本图片
                if not os.path.exists(file_path):
                    #新建文件
                    with open(file_path, 'wb') as f:
                        #下载
                        f.write(response.content)
                else :
                    print('Already Dowmloaded', file_path)
            #如果出现了命名错误，则会导致找不到路径错误，就使用下边方法
            except OSError:
                error_path = '{0}/{1}/{2}.{3}' .format('image',item.get('error_id'), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(error_path):
                    #新建文件
                    with open(error_path, 'wb') as f:
                        #下载
                        f.write(response.content)
                else :
                    print('Already Dowmloaded', error_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

START = 0       #设置开始位置
END = 1         #设置结束位置

# def get_offset():
#     groups = ([x*20 for x in range(0 , 6)])
#     return groups
#########################
#       主程序
#########################
# json = get_page(20)
# for item in get_images(json):
#     print(item)
#     save_image(item)
def main(offset):
    # offsets = get_(offset)
    # for offset in offsets:
        json = get_page(offset)
        for item in get_images(json):
            print(item['title'])
            save_image(item)

# if __name__ == '__main__':
#     main()


################################
#函数介绍：pool = Pool()创建进程池
# Pool类：
#       1、map()：例子 ：pool.map(run, testFL）
#                       testFL:要处理的数据列表，run：处理testFL列表中数据的函数
#       2、close()： 关闭进程池，不再接受新的进程
#       3、join()： 主进程阻塞等待子进程的退出
#################################
if __name__ == '__main__':
    pool = Pool(3)                                    #创建进程池
    groups = ([x*20 for x in range(START, END+1)]) #创建需要执行的列表
    pool.map(main, groups)                           #列表里每个参数的都同时执行主函数
    pool.close()
    pool.join()