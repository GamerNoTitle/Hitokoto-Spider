# Hitokoto-Spider
这个项目是与一言的库相关的项目，一直想用python来爬取一言的文本库，所以就有了这个项目。本项目正在开发，需要用到requests库，第一次使用请输入
```bash
$ pip install requests
```
来安装所需要的python库！爬取的链接为：https://international.v1.hitokoto.cn/

## 打开方式

首先，请到config.json修改你的配置，默认的配置如下：

```json
{
    "path": "Hitokoto.csv",
    "times": 3,
    "delay": 0,
    "timeout": 60,
    "from": false,
    "from_who": false,
    "creator": false,
    "created_at": false
}
```

将``path``后面的内容修改为你要输出的文件路径

``times``修改为抓取次数

``delay``修改为每次抓取完成后等待的时长，单位为秒（参考一言的QPS做的这个选项）

``timeout``改为http请求超时时间，单位为秒

``from``表示来源，这个来源是作品，只支持true和false

``from_who``表示来源，这个来源是人，指的是说这句话的人，只支持true和false，目前开启会报KeyError，正在修复！

``creator``表示该条目的创建者，将返回创建者的昵称，只支持true和false

``created_at``表示该条目提交的时间，一言返回的值为时间戳，我将它转成了``YYYY-MM-DD HH-MM-SS``的格式

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
- [ ] GUI支持