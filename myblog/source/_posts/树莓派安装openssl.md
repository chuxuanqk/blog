---

title:  树莓派安装OpenSSL
date: 2020-03-12
categories: 
mathjax: true
tags: 
---

树莓派安装OpenSSL

<!-- more -->




```
wget  --no-check-certificate  https://www.openssl.org/source/openssl-1.1.1d.tar.gz
tar zxf openssl-1.1.1d.tar.gz
cd openssl-1.1.1d
./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl 
make -j4 && make install
```

