import requests as r
import json as js
import xlsxwriter
import csv
# import panda as pd
def create_csv(path):
    with open(path,"w+",newline="") as file:    # 打开文件，也相当于一个回车，避免覆盖文档
        csv_file = csv.writer(file)
        head = ["id","sort","hitokoto"] # 创建csv表头
        csv_file.writerow(head)
print("请输入文件输出名：")
path=input()    # 输出文件
print("请输入抓取的数量，如果要抓取全部请到https://hitokoto.cn/status查看现在的一言总数并填入：")
num=input() # 抓取数量
create_csv(path)
ids=[]
sorts=[]
hitokoto=[]
res = r.get('https://international.v1.hitokoto.cn/') # 得到服务器回应，此时回应的内容为json文件（res.text）和状态码
for i in range num:
    data=res.json() # 将获取到的结果转为json字符串
    for t in range i:
        if t<=i & data["id"]!=ids[t]
        ids.append(data["id"])
    print(data["id"])
