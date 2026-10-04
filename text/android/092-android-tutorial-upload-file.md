# 7.3.1 Android 文件上传

> 来源: https://www.runoob.com/w3cnote/android-tutorial-upload-file.html

## 本节引言

> 本节和下一节文件下载一样，慎入...现在实际开发涉及文件上传不会自己写上传代码，一般
> 会集成第三网络库来做图片上传，比如android-async-http，okhttp等，另外还有七牛也提供
> 了下载和上传的API，喜欢的可以去官网查看相关的API文档！本节的话有兴趣看看就好！
> ![图1](../../images/37937851.jpg)

## 1.项目用到的图片上传的关键方法：

思前想后，还是决定先贴下公司项目中用到的图片上传的核心方法，这里用到一个第三方的库：
android-async-http.jar，自己到github下下这个库~然后调用一下下面的方法即可，自己改下url!

上传图片的核心方法如下：

---

## 2.使用HttpConnection上传文件：

![图2](../../images/34820616.jpg)简直卧槽...各种设置，各种麻烦...还是建议用1的方法吧，当然，实在太闲可以看看,
有轮子可用还是先别自己造轮子了...

偶然发现一篇以前转载的，可以搭配着上面的看看...：[使用HttpConnection上传mp3文件](http://blog.csdn.net/coder_pig/article/details/39453489)

## 本节小结：

> 本节还是直接无视吧...关于文件上传等进阶部分直接教大家用第三方算了，项目中需要用到
> 第三方直接复制1的代码，导入个android-async-http即可！

### 图片清单

1. 图1 -> images/37937851.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/09/37937851.jpg）
2. 图2 -> images/34820616.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/09/34820616.jpg）
