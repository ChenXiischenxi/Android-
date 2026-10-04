# 7.6.4 基于UDP协议的Socket通信

> 来源: https://www.runoob.com/w3cnote/android-tutorial-udp-socket.html

## 本节引言：

> 本节给大家带来Socket的最后一节：基于UDP协议的Socket通信，在第一节中我们已经详细地
> 比较了两者的区别，TCP和UDP最大的区别在于是否需要客户端与服务端建立连接后才能进行
> 数据传输，如果你学了前两节TCP的，传输前先开服务端，accept，等客户端接入，然后获得
> 客户端socket然后进行IO操作，而UDP则不用，UDP以数据报作为数据的传输载体，在进行传输时
> 首先要把传输的数据定义成数据报(Datagram)，在数据报中指明数据要到达的Socket(主机地址
> 和端口号)，然后再将数据以数据报的形式发送出去，然后就没有然后了，服务端收不收到我就
> 不知道了，除非服务端收到后又给我回一段确认的数据报~时间关系就不另外写Android例子了
> 直接上Java代码~

## 1.服务端实现步骤：

> **Step 1**：创建DatagramSocket，指定端口号
> **Step 2**：创建DatagramPacket
> **Step 3**：接收客户端发送的数据信息
> **Step 4**：读取数据

**示例代码**：

---

## 2.客户端实现步骤：

> **Step 1**：定义发送信息
> **Step 2**：创建DatagramPacket，包含将要发送的信息
> **Step 3**：创建DatagramSocket
> **Step 4**：发送数据

## 本节小结：

本节内容比较简单，无非就是将数据转换为字节，然后放到**DatagramPacket**(数据报包中)，发送的
时候带上接受者的IP地址和端口号，而接收时，用一个字节数组来缓存！发送的时候需要创建一个
**DatagramSocket**(端到端通信的类)对象，然后调用send方法给接受者发送数据报包~
本节代码来源于慕客网上的一个JavaSocket教程~有兴趣的可以看看：
[Java Socket应用---通信是这样练成的](http://www.imooc.com/learn/161)
