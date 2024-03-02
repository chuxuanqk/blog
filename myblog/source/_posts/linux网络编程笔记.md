---

title:  linux 网络编程笔记
date: 
categories: 
mathjax: true
tags: 
---

linux 网络编程相关知识点

<!-- more -->



[toc]

**linux 默认MTU: 1500字节**

```
saber@saber-VirtualBox:~$ cat /sys/class/net/enp0s3/mtu 
1500
```

**MSS决定TCP的单包传输量**

往往用MTU值代替（需要减去IP数据包包头的大小20Bytes和TCP数据段的包头20Bytes）所以往往MSS为1460

MSS为1460是由1500-20（IP头）-20（TCP头）计算出的。
实际场景下，TCP包头中会带有12字节的选项----时间戳。
这样，单个TCP包实际传输的最大量就缩减为1448字节。1448=1500-20（IP头）-32（20字节TCP头和12字节TCP选项时间戳）



#  **HTTP中Get与Post的区别**

GET方式提交的数据最多只能是1024字节"，因为GET是通过URL提交数据，那么GET可提交的数据量就跟URL的长度有直接关系 了。

POST数据是没有限制的，起限制作用的是服务器的处理程序的处理能力



**linux动态查看文件**

```shell
 tail -f -n 10 /tmp/log/Onecm_Gateway.log
```



# TCP网络编程

*   select 定时器

```c++
timeval tv;
tv.tv_sec = 1;
tv.tv_usec = 0;
select(0, NULL, NULL, NULL, &tv);
```

*   select 判断文件描述符 可读、可写

```c++
int is_writeable(int socket)
{
    fd_set fds;
    FD_ZERO(&fds);
    FD_SET(socket, &fds);

    timeval tv;
    tv.tv_sec = 3;
    tv.tv_usec = 0;

    char buf[1024] = {0};

    return select(socket + 1, NULL, &fds, NULL, &tv);
}

int _select_read(int sock, time_t sec, time_t usec)
{
    fd_set fds;
    FD_ZERO(&fds);
    FD_SET(sock, &fds);

    timeval tv;
    tv.tv_sec = static_cast<long>(sec);
    tv.tv_usec = static_cast<decltype(tv.tv_usec)>(usec);

    return handle_EINTR([&]()
                        { return select(static_cast<int>(sock + 1), &fds, nullptr, nullptr, &tv); });
}
```

*   select 判断tcp client 是否还连接，重连操作



**usleep() 有有很大的问题**

1.  在一些平台下不是线程安全，如HP-UX以及Linux
2.  *usleep()* 会影响信号
3.  在很多平台，如HP-UX以及某些Linux下，当参数的值必须小于1 * 1000 * 1000也就是1秒，否则该函数会报错，并且立即返回。
4.  大部分平台的帮助文档已经明确说了，该函数是已经被舍弃的函数。

还好，POSIX规范中有一个很好用的函数，*nanosleep()* ，该函数没有*usleep()* 的这些缺点，它的精度是纳秒级。在Solaris的多线程环境下编译器会自动把*usleep()* 连接成*nanosleep()* 。

Linux下短延时推荐使用select函数.



**1 .connect调用失败后需关闭描述符**

```
APPLICATION USAGE
       If connect() fails, the state of  the  socket  is  unspecified. Conforming  applications
       should close the file descriptor and create a new socket before attempting to reconnect.
```









# **参考文档**

[TCP传输的单个报文最大字节（MSS和MTU）]([(62条消息) TCP传输的单个报文最大字节（MSS和MTU）_luck_horse的博客-CSDN博客_tcp最大发送字节](https://blog.csdn.net/qinrenzhi/article/details/85340048))

[[关于c++中sleep_for函数的总结分析](https://www.cnblogs.com/songyuchen/p/14038180.html)](https://www.cnblogs.com/songyuchen/p/14038180.html)

