import json
str = """
[{
    "name":"杨",
    "gender":"啦",
    "birthday":"1992-10-18"
},{
    "name":"mike",
    "gender":"fmale",
    "birthday":"1995-11-18"
}]
"""
#调用 dumps()将json转为字符串
#输出中文需要转码， str转bytes叫encode，bytes转str叫decode
#json.dumps 序列化时对中文默认使用的ascii编码。想输出真正的中文需要指定ensure_ascii=False
with open('output.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(str, indent=2, ensure_ascii=False))