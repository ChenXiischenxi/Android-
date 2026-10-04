# Kotlin 协程

> 来源: https://www.runoob.com/kotlin/kotlin-coroutines.html

## 代码块 1

```kotlin
import kotlinx.coroutines.delay

import kotlinx.coroutines.launch

import kotlinx.coroutines.runBlocking


fun main() = runBlocking {          // 阻塞主线程，直到内部协程全部完成

    println("开始，线程：${Thread.currentThread().name}")


    launch {                       // 启动协程，不阻塞后面的代码

        delay(100)                 // 挂起 100 毫秒，线程此时可以去干别的

        println("协程 A 完成")

    }


    launch {

        delay(50)

        println("协程 B 完成")

    }


    println("main 协程继续执行")

}
```

## 代码块 2

```kotlin
开始，线程：main
main 协程继续执行
协程 B 完成
协程 A 完成
```

## 代码块 3

```kotlin
import kotlinx.coroutines.delay

import kotlinx.coroutines.runBlocking


// suspend 函数：模拟一次网络请求

suspend fun fetchSite(): String {

    delay(100)                     // 挂起，不占用线程

    return "www.runoob.com"

}


suspend fun printSite() {

    println("开始获取")

    val site = fetchSite()         // 在 suspend 函数里调用 suspend 函数

    println("站点：$site")

}


fun main() = runBlocking {

    printSite()

}
```

## 代码块 4

```kotlin
开始获取
站点：www.runoob.com
```

## 代码块 5

```kotlin
import kotlinx.coroutines.coroutineScope

import kotlinx.coroutines.delay

import kotlinx.coroutines.launch

import kotlinx.coroutines.runBlocking


suspend fun loadHomePage() = coroutineScope {

    launch {

        delay(200)

        println("模块 A 加载完成")

    }

    launch {

        delay(100)

        println("模块 B 加载完成")

    }

    println("等待所有子协程……")

}   // 这里会挂起，直到两个子协程都结束


fun main() = runBlocking {

    loadHomePage()

    println("首页全部就绪")

}
```

## 代码块 6

```kotlin
等待所有子协程……
模块 B 加载完成
模块 A 加载完成
首页全部就绪
```

## 代码块 7

```kotlin
import kotlinx.coroutines.Dispatchers

import kotlinx.coroutines.runBlocking

import kotlinx.coroutines.withContext


fun main() = runBlocking {

    println("主线程：${Thread.currentThread().name}")


    withContext(Dispatchers.Default) {

        println("Default 在主线程吗：${Thread.currentThread().name == "main"}")

    }


    withContext(Dispatchers.IO) {

        println("IO 在主线程吗：${Thread.currentThread().name == "main"}")

    }


    println("结束时仍在：${Thread.currentThread().name}")

}
```

## 代码块 8

```kotlin
主线程：main
Default 在主线程吗：false
IO 在主线程吗：false
结束时仍在：main
```

## 代码块 9

```kotlin
import kotlinx.coroutines.delay

import kotlinx.coroutines.launch

import kotlinx.coroutines.runBlocking

import kotlinx.coroutines.withTimeoutOrNull


fun main() = runBlocking {

    // 取消一个长时间运行的协程

    val job = launch {

        repeat(5) { i ->

            delay(200)                 // 挂起点会检查是否已被取消

            println("第 $i 次下载……")

        }

    }

    delay(450)                         // 让它先跑一会儿

    println("取消任务")

    job.cancel()                       // 发出取消请求

    job.join()                         // 等待取消真正完成

    println("任务已停止，isCancelled = ${job.isCancelled}")


    // 超时控制

    val result = withTimeoutOrNull(300) {

        delay(1000)                    // 超过 300 毫秒就放弃

        "下载完成"

    }

    println("超时结果：$result")

}
```

## 代码块 10

```kotlin
第 0 次下载……
第 1 次下载……
取消任务
任务已停止，isCancelled = true
超时结果：null
```

## 代码块 11

```kotlin
import kotlinx.coroutines.ensureActive

import kotlinx.coroutines.launch

import kotlinx.coroutines.runBlocking


fun main() = runBlocking {

    val job = launch {

        var sum = 0L

        for (i in 1..1_000_000_000) {

            sum += i

            if (i % 10_000_000 == 0) {

                ensureActive()         // 主动检查取消状态

                println("已计算到 $i")

            }

        }

    }

    job.cancel()                       // 立刻取消

    job.join()

    println("已取消：${job.isCancelled}")

}
```

## 代码块 12

```kotlin
已取消：true
```

## 代码块 13

```kotlin
import kotlinx.coroutines.async

import kotlinx.coroutines.delay

import kotlinx.coroutines.runBlocking

import kotlin.system.measureTimeMillis


// 模拟一个耗时模块

suspend fun loadModule(name: String, cost: Long): String {

    delay(cost)

    return "$name 加载完成"

}


fun main() = runBlocking {

    val time = measureTimeMillis {

        val a = async { loadModule("模块 A", 300) }   // 立即开始执行

        val b = async { loadModule("模块 B", 300) }   // 立即开始执行

        println(a.await())                            // 等 A

        println(b.await())                            // 等 B

    }

    // 串行执行需要 600 毫秒左右，并行明显更快

    println("是否并行执行：${time < 600}")

}
```

## 代码块 14

```kotlin
模块 A 加载完成
模块 B 加载完成
是否并行执行：true
```

## 代码块 15

```kotlin
import kotlinx.coroutines.flow.collect

import kotlinx.coroutines.flow.filter

import kotlinx.coroutines.flow.flow

import kotlinx.coroutines.flow.map

import kotlinx.coroutines.flow.toList

import kotlinx.coroutines.runBlocking


// 冷流：每个收集者都会触发一次完整的执行

fun numberFlow() = flow {

    for (i in 1..5) {

        emit(i)                       // 逐个发出元素

    }

}


fun main() = runBlocking {

    // map 和 filter 是中间操作，不会立即执行

    val result = numberFlow()

        .map { it * 10 }              // 每个元素乘以 10

        .filter { it > 20 }           // 只保留大于 20 的

        .toList()                     // 末端操作，触发整个流


    println(result)


    // collect 逐个消费元素

    numberFlow().collect { value ->

        println("收到：$value")

    }

}
```

## 代码块 16

```kotlin
[30, 40, 50]
收到：1
收到：2
收到：3
收到：4
收到：5
```

## 代码块 17

```kotlin
import kotlinx.coroutines.Dispatchers

import kotlinx.coroutines.flow.catch

import kotlinx.coroutines.flow.flow

import kotlinx.coroutines.flow.flowOn

import kotlinx.coroutines.flow.toList

import kotlinx.coroutines.runBlocking


fun riskyFlow() = flow {

    emit("第一项")

    throw IllegalStateException("数据源断开")

}.catch { e ->

    emit("捕获到异常：${e.message}")     // 在流内部兜底

}


fun main() = runBlocking {

    // flowOn 让发射逻辑跑在 IO 线程，收集仍在主线程

    val list = riskyFlow()

        .flowOn(Dispatchers.IO)

        .toList()

    println(list)

}
```

## 代码块 18

```kotlin
[第一项, 捕获到异常：数据源断开]
```

## 代码块 19

```kotlin
import kotlinx.coroutines.coroutineScope

import kotlinx.coroutines.delay

import kotlinx.coroutines.launch

import kotlinx.coroutines.runBlocking


suspend fun loadData(): String {

    delay(100)

    throw IllegalStateException("服务器返回 500")

}


fun main() = runBlocking {

    // 方式一：在协程内部 try/catch

    launch {

        try {

            loadData()

        } catch (e: Exception) {

            println("内部捕获：${e.message}")

        }

    }


    // 方式二：coroutineScope 把异常抛给调用者

    try {

        coroutineScope {

            loadData()

        }

    } catch (e: Exception) {

        println("外层捕获：${e.message}")

    }

}
```

## 代码块 20

```kotlin
内部捕获：服务器返回 500
外层捕获：服务器返回 500
```

## 代码块 21

```kotlin
import kotlinx.coroutines.CoroutineExceptionHandler

import kotlinx.coroutines.launch

import kotlinx.coroutines.runBlocking


fun main() = runBlocking {

    // 处理器只对根协程生效，且必须在作用域上声明

    val handler = CoroutineExceptionHandler { _, e ->

        println("全局处理：${e.message}")

    }


    val job = launch(handler) {

        throw RuntimeException("任务失败")

    }

    job.join()

    println("主流程继续")

}
```

## 代码块 22

```kotlin
全局处理：任务失败
主流程继续
```

## 代码块 23

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("jvm") version "2.2.0"

}


dependencies {

    // 核心库，所有平台都要

    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.10.2")


    // Android 上使用 Dispatchers.Main 时需要

    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")


    // 协程测试工具 runTest / TestDispatcher

    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.10.2")

}
```

## 代码块 24

```xml
<!-- 文件路径：pom.xml -->

<dependency>

    <groupId>org.jetbrains.kotlinx</groupId>

    <artifactId>kotlinx-coroutines-core-jvm</artifactId>

    <version>1.10.2</version>

</dependency>
```
