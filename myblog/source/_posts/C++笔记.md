---

title:  c++ 笔记
date: 
categories: 
mathjax: true
tags: 
---

c++ 笔记
<!-- more -->



#### C++11 Lambda表达式

Lambda表达式完整的声明格式:

```c++
[capture list](params list) mutable exception-> return type {function body}
```

各项具体含义如下：

1.  capture list：捕获外部变量列表
2.  params list：形参列表
3.  mutable指示符：用来说用是否可以修改捕获的变量
4.  exception：异常设定
5.  return type：返回类型
6.  function body：函数体





**[[C++ 11中几个我比较喜欢的语法](https://www.cnblogs.com/TianFang/p/3163229.html)]**

*   原生字符串 

 string path = R"(C:\Program Files\Microsoft.NET\ADOMD.NET)";

字符串里面可以带引号，例如：

  string path = R"(this "word" is escaped)";

C++ 11 语法格式：1. 字符串前加 ‘R’ 前缀；2.字符串首尾加上括号 ()





[Rapidjson 处理多个json分离解析](https://github.com/Tencent/rapidjson/issues/1537)
