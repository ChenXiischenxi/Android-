# 10.4 Vibrator(振动器)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-vibrator.html

## 本节引言：

> 本节我们介绍的是**Vibrator**(振动器)，是手机自带的振动器，别去百度直接搜针振动器，因为
> 你的搜索结果可能是如图所示的神秘的道具，或者其他神秘道具：
> ![图1](../../images/99081637.jpg)

> 嗯，说回本节介绍的Vibrator，其实就是Android给我们提供的用于机身震动的一个服务！
> 比如前面我们的Notification中可以设置震动，当收到推送消息的时候我们可以设置震动
> 提醒，游戏必备，比如"打飞机"的游戏，当你的飞机给人打爆的时候，会长震动！

> 下面我们就来写个简单的例子，来熟悉下这个Vibrator的用法！

> 官方API文档：[Vibrator](http://androiddoc.qiniudn.com/reference/android/os/Vibrator.html)

## 1.获得Vibrator实例:

**Vibrator vb = (Vibrator)getSystemService(Service.VIBRATOR_SERVICE);**

## 2.可以使用的相关方法：

> - abstract void **cancel**()：关闭或者停止振动器

> - abstract boolean **hasVibrator**()：判断硬件是否有振动器

> - void **vibrate**(long milliseconds)：控制手机振动为milliseconds毫秒

> - void **vibrate**(long[] pattern,int repeat):指定手机以pattern指定的模式振动!
> 比如:pattern为new int[200,400,600,800],就是让他在200,400,600,800这个时间交替启动与关闭振动器!
> 而第二个则是重复次数,如果是-1的只振动一次,如果是0的话则一直振动
> 还有其他两个方法用得不多~
> 对了，使用振动器还需要在AndroidManifest.xml中添加下述权限：
> <**uses-permission android:name="android.permission.VIBRATE"**/>

## 3.使用示例：设置频率不同的震动器：

> 对于Vibrator用的最广泛的莫过于所谓的手机按摩器类的app，在app市场一搜，一堆，笔者随便下了
> 几个下来瞅瞅，都是大同小异的，这点小玩意竟然有8W多的下载量...好吧，好像也不算多，
> 不过普遍功能都是切换振动频率来完成，而所谓的按摩效果，是否真的有效就不得而知了,
> 那么接下来我们就来实现一个简单的按摩器吧!
> 核心其实就是：vibrate()中的数组的参数,根据自己需求写一个数组就可以了!
> 下述代码需要在真机上进行测试！

**运行效果图**：

![图2](../../images/18141865.jpg)

**实现代码**：

简单的布局文件，五个按钮：**activity_main.xml**：

接着是**MainActivity.java**部分：

对了，别漏了振动器权限哦！

## 4.示例代码下载：

[VibratorDemo.zip](http://static.runoob.com/download/VibratorDemo.zip)

## 本节小结：

> 好的，本节我们学习了Vibrator(振动器)的基本使用，代码非常简单，还不赶紧加入到
> 你的APP中，让你的应用HI起来~，嗯，就说这么多，谢谢，天色不早，小猪还是赶紧回家吧！
> 毕竟我还是个黄花闺仔！万一湿身了就不好了~![图3](../../images/71454388.jpg)

### 图片清单

1. 图1 -> images/99081637.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/10/99081637.jpg）
2. 图2 -> images/18141865.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/10/18141865.jpg）
3. 图3 -> images/71454388.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/10/71454388.jpg）
