#blog

打开博客根目录下的`_config.yml`文件，这是博客的配置文件，在这里你可以修改与博客相关的各种信息。

修改最后一行的配置：

```bash
deploy:
  type: git
  repository: https://github.com/******/*********.github.io
  branch: master
```

repository修改为你自己的github项目地址。



## 写文章、发布文章

首先在博客根目录下右键打开git bash，安装一个扩展`npm i hexo-deployer-git`。

然后输入`hexo new post "article title"`，新建一篇文章。

然后打开`blog\source\_posts`的目录，可以发现下面多了一个文件夹和一个`.md`文件，一个用来存放你的图片等数据，另一个就是你的文章文件啦。

编写完markdown文件后，根目录下输入**hexo g**生成静态网页，然后输入**hexo s**可以本地预览效果，最后输入**hexo d**上传到github上。这时打开你的github.io主页就能看到发布的文章啦。



[github push鉴权失败](https://blog.csdn.net/weixin_41010198/article/details/119698015)



1、如果 push 等操作没有出现`输入密码选项`，请先输入如下命令，之后就可以看到输入密码选项了

>   ```
>   git config --system --unset credential.helper
>   ```

token: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



### Hexo 博客无法显示图片解决方法

首先，根据 Hexo 官方文档，在 `_config.yaml` 将 `post_asset_folder` 选项设为 `true` 。然后，安装插件 `hexo-image-link`，安装命令为：

```
$ npm install hexo-image-link --save

BASH
```

如果安装了 `hexo-asset-img` 插件，需要将其卸载：

```
$ npm uninstall --save hexo-asset-img

BASH
```

然后，配置 Markdown 编辑器 Typora 如下：

插入图片时：复制到指定路径

[![Typora 配置](https://arcsin2.cloud/2023/02/23/Hexo-%E5%8D%9A%E5%AE%A2%E6%97%A0%E6%B3%95%E6%98%BE%E7%A4%BA%E5%9B%BE%E7%89%87%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/image-20230223101720679.png)](https://arcsin2.cloud/2023/02/23/Hexo-博客无法显示图片解决方法/image-20230223101720679.png)

配置完成后，在 Typora 中粘贴图片时，Typora 就会自动将图片保存到与文件名同名的目录下，并在 Markdown 中使用相对路径引用图片。这样，我们就可以在 Hexo 博客和 Typora 中同时看到图片。