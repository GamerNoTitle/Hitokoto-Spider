import requests as r
import json as js
import csv
import os
import datetime
from array import array
import time
# 程序运行时间开始
start_Pro=datetime.datetime.now()
def create_csv(path):
    with open(path,"w+",newline="",encoding="utf8") as file:    # 打开文件，也相当于一个回车，避免覆盖文档
        csv_file = csv.writer(file)
        head = heads # 创建csv表头
        csv_file.writerow(head)
def append_csv(path):
    with open(path,"a+",newline='',encoding="utf8") as file:
        csv_file = csv.writer(file)
        data = [inputs]
        csv_file.writerows(data)
def read_config():
    with open("config.json") as json_file:
        config = js.load(json_file)
    return config
conf = read_config()
path = conf["path"]
heads = ["id","sort","hitokoto"]
num = int(conf["times"])
delay = int(conf["delay"])
timeout = int(conf['timeout'])
if(conf['from'] == True): heads.append("from")
if(conf['from_who'] == True): heads.append("from_who")
if(conf['creator'] == True): heads.append('creator')
if(conf['creator_uid'] == True): heads.append('creator_uid')
if(conf['reviewer'] == True): heads.append('reviewer')
if(conf['uuid'] == True): heads.append('uuid')
if(conf['created_at'] == True): heads.append("created_at")
create_csv(path)
sorts=""
i=1
temp=array('i',[0])   # 初始化temp变量，用于放置已抓取的ID
while True:
    if(i==num+1):   # 如果不加1那么最后一次将无法运行
        break
    time.sleep(delay)
    print("----------------------------------------------------------")
    print("正在获取新的一言……")
    print("Fetching new Hitokoto......")
    res = r.get('https://international.v1.hitokoto.cn/',timeout=timeout) # 得到服务器回应，此时回应的内容为json文件（res.text）和状态码
    data=res.json() # 将获取到的结果转为json字符串
    temp_minus=len(temp)-1
    if temp_minus!=0:
        t=1
        print("正在检测是否抓取过结果……")
        for t in range(len(temp)):
            if(int(data["id"])==temp[t]):
                print("发现已经抓取到的结果，正在丢弃……")
                break
            elif(t==len(temp)-1):
                print("未抓取过的结果，正在存入文件……")
                if data["type"]== "a": sorts=("Anime")  # 自动把分类码还原为分类
                if data["type"]== "b": sorts=("Comic")
                if data["type"]== "c": sorts=("Game")
                if data["type"]== "d": sorts=("Novel")
                if data["type"]== "e": sorts=("Myself")
                if data["type"]== "f": sorts=("Internet")
                if data["type"]== "g": sorts=("Other")
                inputs=[data["id"],sorts,data["hitokoto"]]
                if(conf['from'] == True): inputs.append(data['from'])
                if(conf["from_who"] == True): 
                    try:
                        inputs.append(data["from_who"])
                    except KeyError:
                        inputs.append("null")
                if(conf['creator'] == True): inputs.append(data['creator'])
                if(conf['creator_uid'] == True):
                    try: 
                        inputs.append(data['creator_uid'])
                    except KeyError:
                        inputs.append("null")
                if(conf['reviewer'] == True):
                    try:
                        inputs.append(int(data['reviewer']))
                    except KeyError:
                        inputs.append('0')
                if(conf['uuid'] == True):
                    try:
                        inputs.append(data['uuid'])
                    except KeyError:
                        inputs.append("null")
                if(conf['creator'] == True): inputs.append(data['creator'])
                timeArray = time.localtime(int(data['created_at']))
                created_at = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                if(conf['created_at'] == True): inputs.append(created_at)
                # print(res.text)   # 输出一言，如需要把最前面的#去掉即可
                append_csv(path)
                temp.append(data["id"])
                end_Pro=datetime.datetime.now()
                print("已完成数量："+str(i)+'，已经用时：'+str(end_Pro-start_Pro))
                i=i+1
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
        if(conf['from'] == True): inputs.append(data['from'])
        if(conf["from_who"] == True): 
            try:
                inputs.append(data["from_who"])
            except KeyError:
                inputs.append("null")
        if(conf['creator'] == True): inputs.append(data['creator'])
        if(conf['creator_uid'] == True):
            try: 
                inputs.append(data['creator_uid'])
            except KeyError:
                inputs.append("null")
        if(conf['reviewer'] == True):
            try:
                inputs.append(int(data['reviewer']))
            except KeyError:
                inputs.append('0')
        if(conf['uuid'] == True):
            try:
                inputs.append(data['uuid'])
            except KeyError:
                inputs.append("null")
        if(conf['creator'] == True): inputs.append(data['creator'])
        timeArray = time.localtime(int(data['created_at']))
        created_at = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        if(conf['created_at'] == True): inputs.append(created_at)
        # print(res.text) # 输出一言，如需要把最前面的#去掉即可
        append_csv(path)
        temp.append(data["id"])
        end_Pro=datetime.datetime.now()
        print("已完成数量："+str(i)+'，已经用时：'+str(end_Pro-start_Pro))
        i=i+1