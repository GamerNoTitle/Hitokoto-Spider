# Hitokoto-Spider
###### 网易云音乐爬虫请往这里走https://github.com/GamerNoTitle/Netease-Comment-Spider

这个项目是与一言的库相关的项目，一直想用python来爬取一言的文本库，所以就有了这个项目。本项目正在开发，需要用到requests库，第一次使用请输入

```bash
$ pip install requests
```
来安装所需要的python库！爬取的链接为：https://international.v1.hitokoto.cn/

已经实现在追加写入的前提下去重，现已支持断点续抓！

## 打开方式

首先，请到config.json修改你的配置，默认的配置如下：

```json
{
    "path": "Hitokoto.csv",
    "times": 3,
    "delay": 0,
    "timeout": 60,
    "retry": 3,
    "from": false,
    "from_who": false,
    "creator": false,
    "creator_uid": false,
    "reviewer": false,
    "uuid": false,
    "created_at": false,
    "duplicate": false,
    "print": false
}
```

``path``修改为你要输出的文件路径，必须自己带后缀且必须为csv

``times``修改为抓取条数，如果你的目录下有已经抓取过的文件，会进入断点续抓模式，例如我需要抓2000条，文件中已经有1000条记录，则只会抓取1000条

``delay``修改为每次抓取完成后等待的时长，单位为秒（参考一言的QPS做的这个选项）

``timeout``为http请求超时时间，单位为秒

``retry``表示重试次数，当返回的状态码不是200的时候会自动进行重试，支持任意非负整数

``from``表示来源，这个来源是作品，只支持true和false

``from_who``表示来源，这个来源是人，指的是说这句话的人，只支持true和false

``creator``表示该条目的创建者，将返回创建者的昵称，只支持true和false

``creator_uid``表示该条目创建者的UID，将返回创建者的UID，只支持true和false

``reviewer``说实话这个参数我都不知道返回的是什么值，先留着吧……只支持true和false

``uuid``表示条目创建者的uuid，将返回条目创建者的uuid，只支持true和false

``created_at``表示该条目提交的时间，一言返回的值为时间戳，我将它转成了``YYYY-MM-DD HH-MM-SS``的格式

``duplicate``表示是否存入重复结果，设置为true则存入，设置为false则不存入，只支持true和false（还未完成）

``print``表示是否每次打印抓取到的结果在控制台，只支持true和false

使用了UTF8的编码方式存储csv文件，所以gbk解码是无效的，会乱码，之所以采用UTF8是因为有些字符gbk处理不了……

**如果你要用Excel查看文件，请务必先用vscode之类的软件将文件以UTF-8的编码方式打开，以gbk编码保存，否则会乱码！！！**

开发日记已发布到http://bili33.top/2020/02/11/Hitokoto-Spider/

高中生无聊时做的，望大佬指教！

# 进度一览
- [x] 获取一言内容
- [x] 导出为csv文件
- [x] 自动分类一言类别
- [x] 去除重复一言
- [x] 自定义输出路径
- [x] 自定义抓取数
- [x] 自定义延时
- [x] json配置文件支持
- [x] 断点续抓
- [ ] 重复条目存入选项  [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [x] 打印抓取结果选项  [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [x] 重复率显示        [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [x] 重复抓取次数显示  [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [ ] Excel表格格式存储功能     [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [x] 在原有的表格上追加写入    [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [x] 在追加写入的前提下去重    [#3](https://github.com/GamerNoTitle/Hitokoto-Spider/issues/3)
- [ ] GUI支持   