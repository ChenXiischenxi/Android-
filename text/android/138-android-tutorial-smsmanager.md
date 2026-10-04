# 10.2 SmsManager(短信管理器)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-smsmanager.html

## 本节引言：

> 本节带来的是Android中的SmsManager(短息管理器)，见名知意，就是用来管理手机短信的，
> 而该类的应用场景并不多，一般是我们发短信的时候才会用到这个API，当然这种短信是
> 文字短信，对于彩信过于复杂，而且在QQ微信各种社交APP横行的年代，你会去发1块钱一条的
> 彩信吗？所以本节我们只讨论发送普通文字短信！
> 官方文档：[SmsManager](http://androiddoc.qiniudn.com/reference/android/telephony/SmsManager.html)

## 1.调用系统发送短信功能：

> 就是把写好的收信人和内容发送到系统的发送短信的界面，用户验证收件人内容是否真正确再点击发送!
> 说白了就是调用系统发短信的窗口,这样做有一定的好处:

> 这样发短信,app安装的时候就可以**少写一条发短信的权限**，那么诸如360这类安全软件在安装的时候
> 就不会提醒用户："这个APP有短信权限，可能会偷偷滴发短信喔"，而用户对于偷偷发短信的行为是十分
> 厌恶的，当然有些人不看直接安装，而有些人可能会觉得会偷偷发短信喔，好恶心的应用，我才不装咧，
> 又或者直接禁止我们的APP发送短信，那么当我们APP在发送短信的时候就可能会出现一些异常，或者
> 应用直接崩溃等！所以如果你的应用需要发送短信进行验证或者付费这些东西的话,建议使用这种方式!

**核心代码**：

## 2.调用系统提供的短信接口发送短信

> 这个就需要发短信的权限啦

> **uses-permission android:name="android.permission.SEND_SMS"**/>

> 我们直接调用SmsManager为我们提供的短信接口发送短信：

> **sendTextMessage**(destinationAddress, scAddress, text, sentIntent, deliverIntent);

> 参数依次是：

> - **destinationAddress**：收信人的电话号码

> - **scAddress**：短信中心的号码,null的话使用当前默认的短信服务中心

> - **text**：短信内容

> - **sentIntent**：短信发送状态的信息:(发送状态的Intent)
> 如果不为null，当消息成功发送或失败这个PendingIntent就广播。结果代码是Activity.RESULT_OK
> 表示成功，或RESULT_ERROR_GENERIC_FAILURE、RESULT_ERROR_RADIO_OFF、RESULT_ERROR_NULL_PDU
> 之一表示错误。对应RESULT_ERROR_GENERIC_FAILURE，sentIntent可能包括额外的"错误代码"包含一
> 个无线电广播技术特定的值，通常只在修复故障时有用。每一个基于SMS的应用程序控制检测sentIntent。
> 如果sentIntent是空，调用者将检测所有未知的应用程序，这将导致在检测的时候发送较小数量的SMS。

> - **deliverIntent**：短信是否被对方收到的状态信息:(接收状态的Intent)
> 如果不为null，当这个短信发送到接收者那里，这个PendtingIntent会被广播，
> 状态报告生成的pdu（指对等层次之间传递的数据单位）会拓展到数据（"pdu"）

![图1](../../images/91898880.jpg)...那么复杂，pdu是什么卵？好吧，别纠结，简单知道这些参数是：

**电话号码，信息中心，短信内容，是否发送成功的监听，以及收信人是否接受的监听就好了！**

**核心代码**：

可能你还需要监听短信是否发送成功，或者收信人是否接收到信息，就把下面的加上吧：

1）处理返回发送状态的**sentIntent**

2）处理返回接收状态的**deliverIntent**：

另外这里涉及到了广播的知识，如果你对广播不怎么了解的话，可以看下：

[Android基础入门教程——BroadcastReceiver牛刀小试](https://www.runoob.com/w3cnote/android-tutorial-broadcastreceiver.html)

[Android基础入门教程——4.3.2 BroadcastReceiver庖丁解牛](//www.runoob.com/w3cnote/android-tutorial-broadcastreceiver-2.html)

## 本节小结：

> ![图2](../../images/71083142.jpg)好的，本节介绍了SmsManager发送文字短信的两种方式~非常简单~建议还是使用
> 第一种方案吧，起码用户体验好一点...

### 图片清单

1. 图1 -> images/91898880.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/10/91898880.jpg）
2. 图2 -> images/71083142.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/10/71083142.jpg）
