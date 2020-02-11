from concurrent.futures import ThreadPoolExecutor,as_completed
import requests as r
import json as js
import pandas as pd
res = r.get('https://v1.hitokoto.cn/') # Get Response from the Link
print(res.text)

def worker(pageNum):
    try:
        res = r.get('https://v1.hitokoto.cn/')
        data = res.json()[res.text]
        for item in data:
            author = item['id']['hitokoto']
            # 一条答案包括 content 和 excerpt 两部分
            content = item['id']
            excerpt = item['hitokoto']
            answer = content + excerpt
            # 去掉富文本标签
            answer = re.sub("<.*?>","",answer)
            return [author,answer]

    except Exception as e:
        print(e)

# 4线程
executor = ThreadPoolExecutor(max_workers=4)
# 获取 10 个
all_tasks = [executor.submit(worker, (i)) for i in range(10)]

# as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞，
# 在有某个任务完成的时候，会yield这个任务，就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。
# 从结果也可以看出，先完成的任务会先通知主线程

answers = []
for future in as_completed(all_tasks):
    data = future.result()
    print(data)
    answers.append(data)

col = ['author','answer']
df = pd.DataFrame(data=answers,columns=col)

df.to_csv("answers.csv",encoding="utf-8")


