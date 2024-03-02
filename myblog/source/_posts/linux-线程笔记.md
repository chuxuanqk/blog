---
title:  linux 线程笔记
date: 2020-03-11 11:41:10
tags:


categories: 

---

linux 线程笔记

<!-- more -->



**Linux C++程序占用cpu**

1. 查看程序的进程号

top -c , 输入`大写P`，top的输出会按使用cpu多少排序

​	2. 查看耗CPU的线程号

命令：`top -Hp 进程号`。 同样输入`大写P`，top的输出会按使用cpu多少排序。

输入`top -Hp 4918`

3. 查看耗CPU的任务

`pstack 进程号`，会输出所有线程的堆栈信息

[Linux：获取线程的PID（TID、LWP）的几种方式](https://blog.csdn.net/test1280/article/details/87974748)



### gdb 调试多线程程序

[gdb调试利器](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html)

* info threads: 显示当前可调试的所有线程
* thread ID: 调试目标ID指定的线程
* set scheduler-locking [off|on|step]





### 多线程环境

* **可重入函数**

  如果一个函数能被多个线程同时调用且不发生竞态条件，则称它是线程安全的，或说它是可冲入函数。



## 什么时候使用Pimpl技术?

可以看到Pimpl拥有如下优点：

-   **减少依赖项（降低耦合性）：其一减少原类不必要的头文件的依赖，加速编译；其二对Impl类进行修改，无需重新编译原类。**
-   **接口和实现的分离（隐藏了类的实现）：私有成员完全可以隐藏在共有接口之外，给用户一个间接明了的使用接口，尤其适合闭源API设计。**
-   **可使用惰性分配技术：类的某部分实现可以写成按需分配或者实际使用时再分配，从而节省资源。**

Pimpl也拥有一些缺点：

-   **每个类需要占用小小额外的指针内存。**
-   **每个类每次访问具体实现时都要多一个间接指针操作的开销**，并且再使用、阅读和调试上都可能有所不便。

可以说，在性能/内存要求不敏感（非极端底层）的领域，Pimpl技术可以有相当不错的发挥和作用。





### [可变参数模板](https://zh.wikipedia.org/wiki/%E5%8F%AF%E5%8F%98%E5%8F%82%E6%95%B0%E6%A8%A1%E6%9D%BF)

```c
// 例如，STL的类模板tuple可以有任意个数的类型名（typename）作为它的模板形参（template parameter）
template<typename... Values> class tuple;
```



### [现代C++特性——std::optional](https://www.jianshu.com/p/24b4361017f9)



### [std::future](https://www.cnblogs.com/haippy/p/3280643.html)

可以用来获取异步任务的结果，可以把它当成一种简单的线程间同步的手段。



### [std::chrono]()

一个time library, chrono是一个模版库，使用简单，功能强大，只需要理解三个概念：duration、time_point、clock。



### Linux 线程函数

```c
#include <pthread.h>
// 设置线程的唯一名称，长度限制16个字符
int pthread_setname_np(pthread_t thread, const char *name);
int pthread_getname_np(pthread_t thread,
                       char *name, size_t len);
```



### c++ 线程类std::thread





### 参考文档

《Linux系统编程》

《Linux高性能服务器编程》

[Linux程序员手册](https://www.onitroad.com/jc/linux/man-pages/linux/man3/pthread_setname_np.3.html)
