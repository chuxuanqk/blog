---

title:  CMake 笔记
date: 2020-03-12
categories: 
mathjax: true
tags: 
---

CMake 笔记

<!-- more -->


[CMake_资料1](https://github.com/fenneishi/cmake)



example:

```cmake
# cmake版本要求
cmake_minimum_required(VERSION 3.1)

# 项目信息
project(DummyImport CXX)

# 指定为C++11 版本
set(CMAKE_CXX_STANDARD 11)

# 添加头文件目录
include_directories(../../single_include)

# 指定生成目标
add_executable(create_json main.cpp)
```

