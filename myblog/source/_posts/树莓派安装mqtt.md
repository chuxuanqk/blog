---

title:  树莓派安装Mosquitto MQTT服务
date: 2020-03-12
categories: 
mathjax: true
tags:  
---

树莓派安装Mosquitto MQTT服务

<!-- more -->


# 树莓派安装Mosquitto MQTT服务

-   更新apt的资源列表

sudo apt-get update

-   搜索可安装的MQTT

apt search mqtt

MQTT分为服务器和客户端两部分。有很多MQTT软件包可选，我们选择比较流行的mosquitto。

-   安装mosquitto 和mosquitto-clients

sudo apt-get install mosquitto mosquitto-clients

说明：

mosquitto – the MQTT broker(MQTT代理，即MQTT服务)

mosquitto-clients – 命令行客户端，在调试时很有用。

-   查看已经安装的mosquitto软件包

dpkg -l mosquitto





## 2. 配置Mosquitto

在使用Mosquitto之前，我们需要修改配置文件。配置文件位于/etc/mosquito。

-   查看配置文件

cat /etc/mosquitto/mosquitto.conf

注释中说：

1)   将本地配置放在/etc/mosquitto/conf.d/目录中。

我们看看/etc/mosquitto/conf.d/目录：

![img](https://img-blog.csdnimg.cn/20210323234647270.png)

里面有一个说明文件，打开看看：

![img](https://img-blog.csdnimg.cn/20210323234654167.png)

放置在该目录中的任何扩展名为.conf的文件都会被代理作为配置文件加载，用作本地配置。

2)   有一个完全的配置文件说明在：/usr/share/doc/mosquitto/examples/

复制配置文件mosquitto.conf.gz到/etc/mosquitto/conf.d/目录
sudo cp /usr/share/doc/mosquitto/examples/mosquitto.conf.gz /etc/mosquitto/conf.d/



进入/etc/mosquitto/conf.d/目录


解压mosquitto.conf.gz
sudo gzip -d mosquitto.conf.gz



编辑mosquitto.conf
sudo nano /etc/mosquitto/conf.d/mosquitto.conf



这是一个很大的文件，有800多行，所有的行都被#符号注释掉了。

我们修改下面几处，去掉注释符号，修改默认值：

user mosquitto

max_queued_messages 200

message_size_limit 0

allow_zero_length_clientid true

allow_duplicate_messages false

 

port 1883

autosave_interval 900

autosave_on_changes false

persistence true

persistence_file mosquitto.db

allow_anonymous false

Password_file /etc/mosquitto/passwd.conf

退回登录时的家目录


3. 生成账号密码
下面两种方法选一种。

密文创建账户
sudo Mosquitto_passwd -c /etc/mosquitto/passwd.conf 用户名

输入两遍密码

我们的用户名为ct

sudo mosquitto_passwd -c /etc/mosquitto/passwd.conf ct





明文创建账户
sudo Mosquitto_passwd -b /etc/mosquitto/passwd.conf 用户名 密码

我们不用明文账户。

4. 测试Mosquitto服务
4.1 查看帮助
mosquitto -h



4.2 测试mosquitto
需要开3个终端。

装载指定配置，启动mosquitto服务
mosquitto -c /etc/mosquitto/mosquitto.conf -v



-v记录所有类型的日志，因为我们在调试。以后正式使用mosquitto就不需要记录日志了，因为会占用存储空间。

上面提示日志文件mosquitto.log的权限不够：

ls -l /var/log/mosquitto/mosquitto.log



修改权限：

sudo chmod 666 /var/log/mosquitto/mosquitto.log



再执行：

mosquitto -c /etc/mosquitto/mosquitto.conf -v



服务运行，终端窗口被占用。

测试publish 和subscribe
再打开两个终端：

1) 一个终端执行：

mosquitto_sub -p 1883 -u ct -P xxxxxx -t "test"



订阅subscribe主题Topic：test，等待接收消息。

2) 另一个终端执行：

mosquitto_pub -p 1883 -u ct -P xxxxxx -t test -m "Hello!"



发布主题为test的消息Hello!

3) 订阅窗口显示接收到的消息



4) 查看日志

sudo cat /var/log/mosquitto/mosquitto.log



5) 正式运行mosquitto服务

重新启动树莓派
sudo reboot



查看正在运行的mosquitto进程
ps -ef | grep mosquitto



mosquitto已经在后台启动。

 

### 参考文献

[Linux搭建MQTT服务器（mosquitto）并使用](https://zhuanlan.zhihu.com/p/164930347)