# 7.1.4 Android HTTP请求方式:HttpClient

> 来源: https://www.runoob.com/w3cnote/android-tutorial-httpclient.html

## 本节引言：

> 在上一节中我们对HttpURLConnection进行了学习，本节到第二种方式：HttpClient，尽管被Google
> 弃用了，但是我们我们平时也可以拿HttpClient来抓下包，配合Jsoup解析网页效果更佳！HttpClient
> 用于接收/发送Http请求/响应，但不缓存服务器响应，不执行HTML页面潜入的JS代码，不会对页面内容
> 进行任何解析，处理！开始本节内容！

## 1.HttpClient使用流程

**基本流程**：

![图1](../../images/20150604110949005)

## 2.HttpClient使用示例

### 1）使用HttpClient发送GET请求

直接贴下简单的发送Get请求的代码：

**运行截图**

![图2](../../images/20150604145450080)

另外，如果是带有参数的GET请求的话，我们可以将参数放到一个List集合中，再对参数进行URL编码，
最后和URL拼接下就好了：

### 2）使用HttpClient发送POST请求

> POST请求比GET稍微复杂一点，创建完HttpPost对象后，通过NameValuePair集合来存储等待提交
> 的参数，并将参数传递到UrlEncodedFormEntity中，最后调用setEntity(entity)完成，
> HttpClient.execute(HttpPost)即可；这里就不写例子了，暂时没找到Post的网站，又不想
> 自己写个Servlet，So,直接贴核心代码吧~

**核心代码**:

## 3.HttpClient抓数据示例(教务系统数据抓取)

> 其实关于HttpClient的例子有很多，比如笔者曾经用它来抓学校教务系统上学生的课程表:
> 这就涉及到Cookie，模拟登陆的东西，说到抓数据(爬虫)，一般我们是搭配着JSoup来解析
> 抓到数据的，有兴趣可以自己查阅相关资料，这里贴下笔者毕设app里获取网页部分的关键
> 代码！大家可以体会下：

HttpClient可以通过下述代码获取与设置Cookie：
**HttpResponse loginResponse = new DefaultHttpClient().execute(getLogin);**
获得Cookie:**cookie = loginResponse.getFirstHeader("Set-Cookie").getValue();**
请求时带上Cookie**:httpPost.setHeader("Cookie", cookie);**

---

## 4.使用HttpPut发送Put请求

**示例代码如下**：

## 本节小结：

> 好的，本节关于Android HTTP的第二种请求方式:HttpClient就到这里，
> 下节开始我们来学习XML以及Json的解析，本节就到这里，谢谢~

### 图片清单

1. 图1 -> images/20150604110949005 （原图：https://www.runoob.com/wp-content/uploads/2015/09/20150604110949005）
2. 图2 -> images/20150604145450080 （原图：https://www.runoob.com/wp-content/uploads/2015/09/20150604145450080）
