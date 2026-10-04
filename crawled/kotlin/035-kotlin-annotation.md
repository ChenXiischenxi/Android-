# Kotlin 注解

> 来源: https://www.runoob.com/kotlin/kotlin-annotation.html

## 代码块 1

```kotlin
// 定义一个注解：@Target 限定能用在哪里，@Retention 决定能否在运行时读到

@Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION)

@Retention(AnnotationRetention.RUNTIME)

@MustBeDocumented

annotation class ApiDoc(

    val author: String,                  // 必填参数

    val version: String = "1.0",         // 可选参数，有默认值

    val tags: Array<String> = []         // 数组参数

)


@ApiDoc(author = "RUNOOB", version = "2.2", tags = ["collection", "annotation"])

class SiteService {

    @ApiDoc(author = "RUNOOB")

    fun listSites(): List<String> = listOf("runoob", "RUNOOB")

}


fun main() {

    // 通过 Java 反射读取运行时注解，不需要额外引入 kotlin-reflect

    val clazz = SiteService::class.java

    val classDoc = clazz.getAnnotation(ApiDoc::class.java)

    println("类注解：author=${classDoc.author}, version=${classDoc.version}, tags=${classDoc.tags.toList()}")


    // 方法上的注解同样可以读取

    val method = clazz.getDeclaredMethod("listSites")

    val methodDoc = method.getAnnotation(ApiDoc::class.java)

    println("方法注解：author=${methodDoc.author}, version=${methodDoc.version}")

}
```

## 代码块 2

```kotlin
类注解：author=RUNOOB, version=2.2, tags=[collection, annotation]
方法注解：author=RUNOOB, version=1.0
```

## 代码块 3

```kotlin
// 枚举类型也可以作为注解参数

enum class Level { LOW, HIGH }


// 再定义一个注解，用于嵌套

annotation class Author(val name: String)


@Target(AnnotationTarget.CLASS)

@Retention(AnnotationRetention.RUNTIME)

annotation class Config(

    val count: Int,                        // 基本类型

    val label: String,                     // String

    val type: Level,                       // 枚举

    val target: kotlin.reflect.KClass<*>,  // 类字面量

    val owner: Author,                     // 嵌套的另一个注解

    val aliases: Array<String> = []        // 数组

)


@Config(

    count = 2,

    label = "runoob",

    type = Level.HIGH,

    target = String::class,

    owner = Author("RUNOOB"),

    aliases = ["www.runoob.com", "RUNOOB"]

)

class Site


fun main() {

    val config = Site::class.java.getAnnotation(Config::class.java)

    println("count=${config.count}, label=${config.label}, type=${config.type}")

    println("target=${config.target.java.simpleName}, owner=${config.owner.name}")

    println("aliases=${config.aliases.toList()}")

}
```

## 代码块 4

```kotlin
count=2, label=runoob, type=HIGH
target=String, owner=RUNOOB
aliases=[www.runoob.com, RUNOOB]
```

## 代码块 5

```kotlin
// 自定义注解，允许用在属性、字段、getter、setter、构造参数上

@Target(

    AnnotationTarget.PROPERTY,

    AnnotationTarget.FIELD,

    AnnotationTarget.PROPERTY_GETTER,

    AnnotationTarget.PROPERTY_SETTER,

    AnnotationTarget.VALUE_PARAMETER

)

@Retention(AnnotationRetention.RUNTIME)

annotation class Marker(val desc: String)


class Site(

    @get:Marker("作用于 getter")        // 只标注在生成的 getter 上

    val name: String = "runoob",


    @param:Marker("作用于构造参数")      // 构造器参数的默认位置就是 param

    val age: Int = 12

) {

    @field:Marker("作用于 JVM 字段")

    @Transient                           // 等价于 @field:Transient，字段不参与序列化

    var cache: String = ""


    @property:Marker("作用于属性本身")    // 属性本身，仅 Kotlin 代码中可见

    val host: String = "www.runoob.com"

}


fun main() {

    val site = Site()

    println("${site.name} / ${site.age} / ${site.host}")


    // 用反射验证注解确实落在 getter 上

    val getter = Site::class.java.getDeclaredMethod("getName")

    println("getter 上的注解：${getter.getAnnotation(Marker::class.java).desc}")

}
```

## 代码块 6

```kotlin
runoob / 12 / www.runoob.com
getter 上的注解：作用于 getter
```

## 代码块 7

```kotlin
// 文件路径：RunoobUtils.kt

// @file:JvmName 修改整个文件编译后生成的类名

@file:JvmName("RunoobUtils")


package com.runoob.demo


// 顶层函数会被放进 RunoobUtils 类，Java 调用时写 RunoobUtils.getHost()

fun getHost(): String = "www.runoob.com"
```

## 代码块 8

```kotlin
class SiteUtils {

    companion object {

        @JvmStatic                            // 生成静态方法，Java 可写 SiteUtils.getHost()

        fun getHost(): String = "www.runoob.com"


        @JvmField                             // 暴露为静态字段，不再生成 getter

        val DEFAULT_NAME: String = "RUNOOB"

    }


    // 为带默认参数的函数生成多个重载，方便 Java 调用

    @JvmOverloads

    fun greet(name: String = "runoob", times: Int = 1): String {

        return buildString {

            repeat(times) { append("Hello $name! ") }

        }.trim()

    }


    // 修改 JVM 上看到的方法名

    @JvmName("runoobGreet")

    fun greetRunoob(): String = "Hello RUNOOB"


    // 声明 Java 调用方需要处理的受检异常

    @Throws(java.io.IOException::class)

    fun readConfig(): String {

        if (DEFAULT_NAME.isEmpty()) throw java.io.IOException("配置为空")

        return DEFAULT_NAME

    }

}


// @Deprecated 的第二个参数给出替代写法，第三个参数决定警告级别

@Deprecated("请改用 SiteUtils", ReplaceWith("SiteUtils()"), DeprecationLevel.WARNING)

class OldSiteUtils


fun main() {

    val utils = SiteUtils()

    println(utils.greet())

    println(utils.greet(times = 2))

    println(utils.greetRunoob())

    println(SiteUtils.getHost())

    println(SiteUtils.DEFAULT_NAME)

    println(utils.readConfig())

}
```

## 代码块 9

```kotlin
Hello runoob!
Hello runoob! Hello runoob!
Hello RUNOOB
www.runoob.com
RUNOOB
RUNOOB
```

## 代码块 10

```kotlin
class Counter {

    private var count = 0


    @Synchronized                    // 给方法加锁，保证多线程下计数不丢失

    fun increment(): Int {

        count++

        return count

    }


    @Volatile                        // 保证修改对其他线程立即可见

    var stopped: Boolean = false

}


fun main() {

    val counter = Counter()

    println(counter.increment())

    println(counter.increment())


    counter.stopped = true

    println("stopped=${counter.stopped}")

}
```

## 代码块 11

```kotlin
1
2
stopped=true
```

## 代码块 12

```kotlin
// @Repeatable：同一个注解可以在同一位置出现多次

@Repeatable

@Target(AnnotationTarget.CLASS)

@Retention(AnnotationRetention.RUNTIME)

annotation class Tag(val name: String)


@Tag("collection")

@Tag("annotation")

class Site


fun main() {

    // Kotlin 自动生成容器注解，Java 侧用 getAnnotationsByType 读取全部

    val tags = Site::class.java.getAnnotationsByType(Tag::class.java).map { it.name }

    println(tags)

}
```

## 代码块 13

```kotlin
[collection, annotation]
```

## 代码块 14

```kotlin
// 用 @RequiresOptIn 标记一个实验性 API，两个注解从 Kotlin 1.4 起提供

@RequiresOptIn(

    message = "这是实验性 API，未来版本可能变更",

    level = RequiresOptIn.Level.WARNING

)

@Retention(AnnotationRetention.BINARY)

@Target(AnnotationTarget.FUNCTION)

annotation class ExperimentalSiteApi


@ExperimentalSiteApi

fun fetchSite(): String = "www.runoob.com"


// 使用方显式声明"我已知晓风险并同意使用"

@OptIn(ExperimentalSiteApi::class)

fun main() {

    println(fetchSite())

}
```

## 代码块 15

```kotlin
www.runoob.com
```

## 代码块 16

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("jvm") version "2.2.0"

    id("com.google.devtools.ksp") version "2.2.0-2.0.2"   // KSP 版本号跟随 Kotlin 版本

}


dependencies {

    implementation("com.google.dagger:hilt-android:2.51")

    ksp("com.google.dagger:hilt-android-compiler:2.51")   // 用 ksp 代替 kapt

}


// 如果注解处理器只支持 Java，才需要退回 kapt：

// plugins { kotlin("kapt") }

// dependencies { kapt("com.example:processor:1.0") }
```
