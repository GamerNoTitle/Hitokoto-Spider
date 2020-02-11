import requests as r
import json as js
res = r.get('https://international.v1.hitokoto.cn/') # Get Response from the Link
print(res.text)