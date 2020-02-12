# Hitokoto-Spider
这个项目是与一言的库相关的项目，一直想用python来爬取一言的文本库，所以就有了这个项目。本项目正在开发，需要用到requests库，第一次使用请输入
```bash
$ pip install requests
```
来安装所需要的python库！爬取的链接为：https://international.v1.hitokoto.cn/

本项目效率个人认为极慢，而且需要非常优秀的网络环境，有人愿意帮我改良一下算法嘛……

使用了UTF8的编码方式存储csv文件，所以gbk解码是无效的，会乱码，之所以采用UTF8是因为有些字符gbk处理不了……

**<font color=#FF0000>如果你要用Excel查看文件，请务必先用vscode之类的软件将文件以UTF-8的编码方式打开，以gbk编码保存，否则会乱码！！！</font>**

开发日记已发布到http://bili33.top/2020/02/11/Hitokoto-Spider/

# 进度一览
- [x] 获取一言内容
- [x] 导出为csv文件
- [x] 自动分类一言类别
- [x] 去除重复一言
- [x] 自定义输出路径
- [x] 自定义抓取数
- [x] 自定义延时
- [ ] json配置文件支持
- [ ] GUI支持