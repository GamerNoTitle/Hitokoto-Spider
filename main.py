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
if(conf['from']): heads.append("from")
if(conf['from_who']): heads.append("from_who")
if(conf['creator']): heads.append('creator')
if(conf['creator_uid']): heads.append('creator_uid')
if(conf['reviewer']): heads.append('reviewer')
if(conf['uuid']): heads.append('uuid')
if(conf['created_at']): heads.append("created_at")
create_csv(path)
sorts=""
i=1
dup=0
temp=array('i',[0])   # 初始化temp变量，用于放置已抓取的ID
all=0   # 总抓取次数
while True:
    if(i==num+1):   # 如果不加1那么最后一次将无法运行
        break
    time.sleep(delay)
    print("----------------------------------------------------------")
    print("正在获取新的一言……")
    print("Fetching new Hitokoto......")
    res = r.get('https://international.v1.hitokoto.cn/',timeout=timeout) # 得到服务器回应，此时回应的内容为json文件（res.text）和状态码
    if(res.status_code!=200):
        print("获取失败，正在尝试重新获取……")
        for t in range(conf['retry']):
            print("正在尝试第"+str(t)+"次连接……")
            res = r.get('https://international.v1.hitokoto.cn/',timeout=timeout)
            if(res.status_code==200):
                break
            elif(t==conf['retry']):
                print("重试次数超过设定值，将不再重试！请检查网络连接！")
                exit
    all=all+1
    data=res.json() # 将获取到的结果转为json字符串
    temp_minus=len(temp)-1
    if temp_minus!=0:
        t=1
        print("正在检测是否抓取过结果……")
        for t in range(len(temp)):
            if(int(data["id"])==temp[t]):
                dup=dup+1
                end_Pro=datetime.datetime.now()
                print("发现已经抓取到的结果，正在丢弃……")
                print("已完成数量：{}/{}，已经用时：{} ，总抓取{}次，重复次数{}次，重复率{}".format(i,num,end_Pro-start_Pro,all,dup,dup/i))
                break
            elif(t==len(temp)-1):
                print("未抓取过的结果，正在存入文件……")
                if data["type"]== "a": sorts=("Anime")  # 自动把分类码还原为分类
                elif data["type"]== "b": sorts=("Comic")
                elif data["type"]== "c": sorts=("Game")
                elif data["type"]== "d": sorts=("Novel")
                elif data["type"]== "e": sorts=("Myself")
                elif data["type"]== "f": sorts=("Internet")
                elif data["type"]== "g": sorts=("Other")
                elif data['type']== 'h': sorts=("Movie")
                elif data['type']== 'i': sorts=("Poem")
                elif data['type']== 'j': sorts=("Netease")
                elif data['type']== 'k': sorts=("Philosophy")
                elif data['type']== 'l': sorts=('Intelligent')
                else: sorts=('Unknown')
                inputs=[data["id"],sorts,data["hitokoto"]]
                if(conf['from']): inputs.append(data['from'])
                if(conf["from_who"]): 
                    try:
                        inputs.append(data["from_who"])
                    except KeyError:
                        inputs.append("null")
                if(conf['creator']): inputs.append(data['creator'])
                if(conf['creator_uid']):
                    try: 
                        inputs.append(data['creator_uid'])
                    except KeyError:
                        inputs.append("null")
                if(conf['reviewer']):
                    try:
                        inputs.append(int(data['reviewer']))
                    except KeyError:
                        inputs.append('0')
                if(conf['uuid']):
                    try:
                        inputs.append(data['uuid'])
                    except KeyError:
                        inputs.append("null")
                if(conf['creator']): inputs.append(data['creator'])
                try:
                    timeArray = time.localtime(int(data['created_at']))
                    created_at = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                except ValueError:
                    created_at = ('null')
                except OSError:
                    timeArray = time.localtime(int(data['created_at'])/1000)
                    created_at = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                if(conf['created_at']): inputs.append(created_at)
                if(conf['print']): print(res.text)
                append_csv(path)
                temp.append(data["id"])
                end_Pro=datetime.datetime.now()
                print("已完成数量：{}/{}，已经用时：{} ，总抓取{}次，重复次数{}次，重复率{}".format(i,num,end_Pro-start_Pro,all,dup,dup/i))
                i=i+1
                break
    else:
        if data["type"]== "a": sorts=("Anime")  # 自动把分类码还原为分类
        elif data["type"]== "b": sorts=("Comic")
        elif data["type"]== "c": sorts=("Game")
        elif data["type"]== "d": sorts=("Novel")
        elif data["type"]== "e": sorts=("Myself")
        elif data["type"]== "f": sorts=("Internet")
        elif data["type"]== "g": sorts=("Other")
        elif data['type']== 'h': sorts=("Movie")
        elif data['type']== 'i': sorts=("Poem")
        elif data['type']== 'j': sorts=("Netease")
        elif data['type']== 'k': sorts=("Philosophy")
        elif data['type']== 'l': sorts=('Intelligent')
        else: sorts=('Unknown')
        inputs=[data["id"],sorts,data["hitokoto"]]
        if(conf['from']): inputs.append(data['from'])
        if(conf["from_who"]): 
            try:
                inputs.append(data["from_who"])
            except KeyError:
                inputs.append("null")
        if(conf['creator']): inputs.append(data['creator'])
        if(conf['creator_uid']):
            try: 
                inputs.append(data['creator_uid'])
            except KeyError:
                inputs.append("null")
        if(conf['reviewer']):
            try:
                inputs.append(int(data['reviewer']))
            except KeyError:
                inputs.append('0')
        if(conf['uuid']):
            try:
                inputs.append(data['uuid'])
            except KeyError:
                inputs.append("null")
        if(conf['creator']): inputs.append(data['creator'])
        try:
            timeArray = time.localtime(int(data['created_at']))
            created_at = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        except ValueError:
            created_at = ('null')
        except OSError:
            timeArray = time.localtime(int(data['created_at'])/1000)
            created_at = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        if(conf['created_at']): inputs.append(created_at)
        if(conf['print']): print(res.text)
        append_csv(path)
        temp.append(data["id"])
        end_Pro=datetime.datetime.now()
        print("已完成数量：{}/{}，已经用时：{} ，总抓取{}次，重复次数{}次，重复率{}".format(i,num,end_Pro-start_Pro,all,dup,dup/i))
        i=i+1
print('----------------------------------------------------------')
print('已抓取完成！抓取数量{}，用时{}，总抓取{}次，重复{}次，重复率{}'.format(i,end_Pro-start_Pro,all,dup,dup/i))