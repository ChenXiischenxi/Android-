# Kotlin 编码规范与惯用法

> 来源: https://www.runoob.com/kotlin/kotlin-style.html

## 代码块 1

```kotlin
// 文件路径：src/main/kotlin/com/runoob/Site.kt

package com.runoob


// 类名大驼峰

data class Site(val name: String, val url: String) {

    // 布尔属性用 is 开头，读起来像一句话

    val isSecure: Boolean

        get() = url.startsWith("https://")

}


// 顶层常量全大写

const val MAX_SITE_COUNT = 100


// 顶层函数小驼峰

fun describeSite(site: Site): String = "${site.name} -> ${site.url}"


fun main() {

    val site = Site("Runoob", "https://www.runoob.com")

    println(describeSite(site))

    println("是否安全连接：${site.isSecure}")

    println("最大站点数：$MAX_SITE_COUNT")

}
```

## 代码块 2

```kotlin
Runoob -> https://www.runoob.com
是否安全连接：true
最大站点数：100
```

## 代码块 3

```kotlin
// 文件路径：src/main/kotlin/com/runoob/Config.kt

package com.runoob


// 多行参数列表使用尾逗号，之后增删参数时 diff 只影响一行

fun createSiteMap(

    name: String,

    url: String,

    port: Int,

): Map<String, Any> {

    return mapOf(

        "name" to name,

        "url" to url,

        "port" to port,

    )

}


fun main() {

    println(createSiteMap("Runoob", "www.runoob.com", 443))

}
```

## 代码块 4

```kotlin
{name=Runoob, url=www.runoob.com, port=443}
```

## 代码块 5

```kotlin
fun main() {

    // 推荐：值确定后不再变化，用 val

    val siteName = "Runoob"

    val url = "www.runoob.com"


    // 需要累加时才用 var

    var visitCount = 0

    visitCount += 1


    println("$siteName -> $url，访问次数 $visitCount")

}
```

## 代码块 6

```kotlin
Runoob -> www.runoob.com，访问次数 1
```

## 代码块 7

```kotlin
// 一行声明换来五个自动生成的方法

data class Site(val name: String, val url: String)


fun main() {

    val site = Site("Runoob", "www.runoob.com")

    // toString 自动生成

    println(site)

    // copy 复制对象并修改指定字段

    val mobile = site.copy(url = "m.runoob.com")

    println(mobile)

    // equals 按内容比较

    println(site == Site("Runoob", "www.runoob.com"))

}
```

## 代码块 8

```kotlin
Site(name=Runoob, url=www.runoob.com)
Site(name=Runoob, url=m.runoob.com)
true
```

## 代码块 9

```kotlin
// 推荐：给 String 加一个扩展函数，而不是新建工具类

fun String.toDomain(): String =

    substringAfter("://").substringBefore("/")


fun main() {

    val url = "https://www.runoob.com/kotlin"

    println(url.toDomain())

}
```

## 代码块 10

```kotlin
www.runoob.com
```

## 代码块 11

```kotlin
data class Site(var name: String, var url: String)


fun main() {

    // apply 的返回值就是配置好的对象，省去临时变量

    val site = Site("", "").apply {

        name = "Runoob"

        url = "www.runoob.com"

    }


    // also 返回对象本身，常用于打日志

    val upper = site.also { println("配置完成：$it") }

        .url.uppercase()


    println(upper)

}
```

## 代码块 12

```kotlin
配置完成：Site(name=Runoob, url=www.runoob.com)
WWW.RUNOOB.COM
```

## 代码块 13

```kotlin
sealed interface Result


data class Success(val data: String) : Result

data class Failure(val message: String) : Result


// 作为表达式使用时，sealed 的所有子类型都覆盖了，不需要 else 分支

fun describe(result: Result): String = when (result) {

    is Success -> "成功：${result.data}"

    is Failure -> "失败：${result.message}"

}


fun main() {

    println(describe(Success("RUNOOB")))

    println(describe(Failure("网络超时")))

}
```

## 代码块 14

```kotlin
成功：RUNOOB
失败：网络超时
```

## 代码块 15

```kotlin
fun main() {

    val name: String? = null


    // 安全调用加 Elvis，为空时给出默认值

    println(name?.length ?: 0)

    println(name?.uppercase() ?: "未知")


    val site: String? = "www.runoob.com"

    // 非空时才执行后续操作

    site?.let { println("站点长度：${it.length}") }

}
```

## 代码块 16

```kotlin
0
未知
站点长度：14
```
