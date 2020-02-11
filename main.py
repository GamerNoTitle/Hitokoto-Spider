import requests as r
import json as js
import csv
def create_csv(path):
    with open(path,"w+",newline="") as file:    # 打开文件，也相当于一个回车，避免覆盖文档
        csv_file = csv.writer(file)
        head = ["id","sort","hitokoto"] # 创建csv表头
        csv_file.writerow(head)
def append_csv(path):
    with open(path,"a+",newline='') as file:
        csv_file = csv.writer(file)
        data = [temp]
        csv_file.writerows(data)
print("请输入文件输出名：")
path=input()    # 输出文件
print("请输入抓取的数量，如果要抓取全部请到https://hitokoto.cn/status查看现在的一言总数并填入：")
num=int(input()) # 抓取数量
create_csv(path)
sorts=""
ids=['0']
i=1
for i in range(num):
    res = r.get('https://international.v1.hitokoto.cn/') # 得到服务器回应，此时回应的内容为json文件（res.text）和状态码
    data=res.json() # 将获取到的结果转为json字符串
    t=1
    for t in range(i):
        if data["id"]==ids[t]:  # ID已经存在，即已经抓到过
            break
        else:
            t=t+1   # 自增
            if t==i:
                ids.append(data["id"])
    if data["type"]== "a": sorts=("Anime")
    if data["type"]== "b": sorts=("Comic")
    if data["type"]== "c": sorts=("Game")
    if data["type"]== "d": sorts=("Novel")
    if data["type"]== "e": sorts=("Myself")
    if data["type"]== "f": sorts=("Internet")
    if data["type"]== "g": sorts=("Other")
    temp=[data["id"],sorts,data["hitokoto"]]
    print(res.text)
    append_csv(path)
    print("已完成数量："+str(i+1))
