import requests as r
import json as js
import csv
# import panda as pd
res = r.get('https://international.v1.hitokoto.cn/') # 得到服务器回应，此时回应的内容为json文件（res.text）和状态码
if(res.status_code==200):
    print(res)
    print(res.text)
data=res.json() # 将获取到的结果转为json字符串
print(data["id"])
