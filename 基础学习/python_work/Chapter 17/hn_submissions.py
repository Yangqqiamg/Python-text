import requests

from operator import itemgetter

#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code", r.status_code)

#处理有关每篇文章的信息
submissions_ids = r.json()
submissions_dicts = []
for submissions_id in submissions_ids[:30]:
    #对于每篇文章,都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/vo/item' +
            str(submissions_id) + '.json')
    submissions_r = requests.get(url)
    print(submissions_r.status_code)
    response_dict = submissions_r.json()

    submissions_dict = {
        'title':response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id' + str(submissions_id),
        'comments': response_dict.get('descendants', 0)
        }
    submissions_dicts.append(submissions_dict)

submissions_dicts = sorted(submissions_dicts,key=itemgetter('comments'),
                            reverse=True)

for submissions_dict in submissions_dicts:
    print("\nTitle:", submissions_dict['title'])
    print("Discussion link:", submissions_dict['link'])
    print("Comments:", submissions_dict['comments'])
