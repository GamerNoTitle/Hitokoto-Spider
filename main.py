import requests as r
import json as js
import csv
import os
import datetime
from array import array
# 程序运行时间开始
start_Pro=datetime.datetime.now()
def create_csv(path):
    with open(path,"w+",newline="",encoding="utf8") as file:    # 打开文件，也相当于一个回车，避免覆盖文档
        csv_file = csv.writer(file)
        head = ["id","sort","hitokoto"] # 创建csv表头
        csv_file.writerow(head)
def append_csv(path):
    with open(path,"a+",newline='',encoding="utf8") as file:
        csv_file = csv.writer(file)
        data = [inputs]
        csv_file.writerows(data)
print("请输入文件输出名：")
path=input()    # 输出文件
print("请输入抓取的数量，如果要抓取全部请到https://hitokoto.cn/status查看现在的一言总数并填入：")
num=int(input()) # 抓取数量
create_csv(path)
sorts=""
i=1
temp=array('i',[0])   # 初始化temp变量，用于放置已抓取的ID
for i in range(num):
    print("正在获取新的一言……")
    res = r.get('https://international.v1.hitokoto.cn/',timeout=60) # 得到服务器回应，此时回应的内容为json文件（res.text）和状态码
    data=res.json() # 将获取到的结果转为json字符串
    temp_minus=len(temp)-1
    if temp_minus!=0:
        t=1
        print("正在检测是否抓取过结果……")
        for t in range(len(temp)):
            if(data["id"]==temp[t]):
                print("发现已经抓取到的结果，正在丢弃……")
                i=i-1
                break
            elif(t==len(temp)-1 & data["id"]!=temp[t]):
                print("未抓取过的结果，正在存入文件……")
                if data["type"]== "a": sorts=("Anime")  # 自动把分类码还原为分类
                if data["type"]== "b": sorts=("Comic")
                if data["type"]== "c": sorts=("Game")
                if data["type"]== "d": sorts=("Novel")
                if data["type"]== "e": sorts=("Myself")
                if data["type"]== "f": sorts=("Internet")
                if data["type"]== "g": sorts=("Other")
                inputs=[data["id"],sorts,data["hitokoto"]]
                print(res.text)
                append_csv(path)
                temp.append(data["id"])
                end_Pro=datetime.datetime.now()
                print("已完成数量："+str(i+1)+'，已经用时：'+str(end_Pro-start_Pro))
                break
    else:
        if data["type"]== "a": sorts=("Anime")  # 自动把分类码还原为分类
        if data["type"]== "b": sorts=("Comic")
        if data["type"]== "c": sorts=("Game")
        if data["type"]== "d": sorts=("Novel")
        if data["type"]== "e": sorts=("Myself")
        if data["type"]== "f": sorts=("Internet")
        if data["type"]== "g": sorts=("Other")
        inputs=[data["id"],sorts,data["hitokoto"]]
        print(res.text)
        append_csv(path)
        temp.append(data["id"])
        end_Pro=datetime.datetime.now()
        print("已完成数量："+str(i+1)+'，已经用时：'+str(end_Pro-start_Pro))
