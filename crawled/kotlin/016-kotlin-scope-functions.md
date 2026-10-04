# Kotlin 作用域函数

> 来源: https://www.runoob.com/kotlin/kotlin-scope-functions.html

## 代码块 1

```kotlin
// 文件路径：Main.kt

fun main() {

    val site: String? = "www.runoob.com"


    // 只有 site 非空时，lambda 才会执行，it 就是 site

    site?.let {

        println("站点：$it")

        println("长度：${it.length}")

    }


    val nullSite: String? = null


    // 用 Elvis 运算符兜底，让表达式一定有值

    val length = nullSite?.let { it.length } ?: 0

    println("空对象兜底长度：$length")

}
```

## 代码块 2

```kotlin
站点：www.runoob.com
长度：14
空对象兜底长度：0
```

## 代码块 3

```kotlin
// 文件路径：Main.kt

class Site(val name: String, val url: String) {

    // 重写 toString，让打印结果可读

    override fun toString(): String = "$name - $url"

}


fun main() {

    // let 返回 lambda 的结果，这里把字符串转换成了 Site 对象

    val site = "RUNOOB|www.runoob.com".let { text ->

        val parts = text.split("|")

        Site(parts[0], parts[1])

    }


    println(site)

}
```

## 代码块 4

```kotlin
RUNOOB - www.runoob.com
```

## 代码块 5

```kotlin
// 文件路径：Main.kt

class Site(var name: String = "", var url: String = "")


fun main() {

    val site = Site("RUNOOB", "www.runoob.com")


    // run 用 this 引用接收者，访问成员时可以直接写属性名

    val info = site.run {

        name = name.uppercase()

        "$name -> $url"

    }


    println(info)

    println("对象本身也被修改：${site.name}")

}
```

## 代码块 6

```kotlin
RUNOOB -> www.runoob.com
对象本身也被修改：RUNOOB
```

## 代码块 7

```kotlin
// 文件路径：Main.kt

fun main() {

    // 非扩展 run：把多条语句收成一个块，块的最后一行的值就是整个表达式的值

    val total = run {

        val a = 10

        val b = 20

        println("计算 $a + $b")

        a + b

    }


    println("结果：$total")

}
```

## 代码块 8

```kotlin
计算 10 + 20
结果：30
```

## 代码块 9

```kotlin
// 文件路径：Main.kt

fun main() {

    // "RUNOOB" 不是合法数字，toInt() 会抛出异常，被 runCatching 捕获

    val fail = runCatching { "RUNOOB".toInt() }


    println("是否成功：${fail.isSuccess}")

    println("是否失败：${fail.isFailure}")

    println("异常类型：${fail.exceptionOrNull()?.let { it::class.simpleName }}")

    println("安全取值：${fail.getOrNull()}")

    println("兜底取值：${fail.getOrDefault(0)}")


    fail.onFailure { println("onFailure 收到：${it::class.simpleName}") }


    val ok = runCatching { "100".toInt() }

    ok.onSuccess { println("onSuccess 收到：$it") }

}
```

## 代码块 10

```kotlin
是否成功：false
是否失败：true
异常类型：NumberFormatException
安全取值：null
兜底取值：0
onFailure 收到：NumberFormatException
onSuccess 收到：100
```

## 代码块 11

```kotlin
// 文件路径：Main.kt

fun main() {

    val builder = StringBuilder()


    // with 把 builder 作为接收者，可以连续调用它的方法

    val text = with(builder) {

        append("Runoob")

        append(" - ")

        append("www.runoob.com")

        toString()

    }


    println(text)

    println("builder 也被修改：$builder")

}
```

## 代码块 12

```kotlin
Runoob - www.runoob.com
builder 也被修改：Runoob - www.runoob.com
```

## 代码块 13

```kotlin
// 文件路径：Main.kt

class Site {

    var name: String = ""

    var url: String = ""

    var visits: Int = 0


    override fun toString(): String = "Site(name=$name, url=$url, visits=$visits)"

}


fun main() {

    // apply 返回接收者，所以花括号结束后拿到的就是配置好的 Site 对象

    val site = Site().apply {

        name = "RUNOOB"

        url = "www.runoob.com"

        visits = 100

    }


    println(site)

    println("类型仍是 Site：${site::class.simpleName}")

}
```

## 代码块 14

```kotlin
Site(name=RUNOOB, url=www.runoob.com, visits=100)
类型仍是 Site：Site
```

## 代码块 15

```kotlin
// 文件路径：Main.kt

fun main() {

    // also 返回接收者，可以继续往后链式调用

    val sites = mutableListOf("Runoob", "RUNOOB")

        .also { println("创建完成，元素个数：${it.size}") }

        .also { it.add("www.runoob.com") }


    println(sites)

}
```

## 代码块 16

```kotlin
创建完成，元素个数：2
[Runoob, RUNOOB, www.runoob.com]
```

## 代码块 17

```kotlin
// 文件路径：Main.kt

fun main() {

    // 不推荐：以为结果是 "RUNOOB"，实际上 apply 返回的是原始字符串

    val wrong = "runoob".apply { uppercase() }

    println(wrong)


    // 推荐：需要转换结果时用 let 或 run

    val right = "runoob".run { uppercase() }

    println(right)

}
```

## 代码块 18

```kotlin
runoob
RUNOOB
```

## 代码块 19

```kotlin
// 文件路径：Main.kt

fun main() {

    val words = listOf("runoob", "kotlin")


    // 不推荐：两层都用隐式 it，内层 it 遮蔽外层 it

    val bad = words.map { it.let { it.uppercase() } }

    println(bad)


    // 推荐：内层参数显式命名，语义一目了然

    val good = words.map { word -> word.let { text -> "[$text]" } }

    println(good.joinToString())

}
```

## 代码块 20

```kotlin
[RUNOOB, KOTLIN]
[runoob], [kotlin]
```

## 代码块 21

```kotlin
// 文件路径：Main.kt

class Site(val name: String)


fun main() {

    val nullSite: Site? = null

    val realSite: Site? = Site("RUNOOB")


    // 编译错误：可空类型不能直接调用作用域函数

    // nullSite.let { println(it.name) }


    // 正确：用安全调用，对象为 null 时整个调用被跳过

    nullSite?.let { println("不会执行：${it.name}") }


    realSite?.let { println("执行了：${it.name}") }

    realSite?.also { println("also 也能配合安全调用：${it.name}") }

}
```

## 代码块 22

```kotlin
执行了：RUNOOB
also 也能配合安全调用：RUNOOB
```
