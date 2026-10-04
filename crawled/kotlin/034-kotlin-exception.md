# Kotlin 异常处理

> 来源: https://www.runoob.com/kotlin/kotlin-exception.html

## 代码块 1

```kotlin
fun main() {

    // 依次处理三种输入，观察不同 catch 分支的匹配

    val inputs = listOf("42", "runoob", null)


    for (input in inputs) {

        try {

            // input 是 String?，!! 在遇到 null 时抛出 NullPointerException

            val value: Int = input!!.toInt()

            println("$input 转换成功：$value")

        } catch (e: NumberFormatException) {

            // 字符串不是合法数字时进入这里

            println("数字格式错误：${e.message}")

        } catch (e: NullPointerException) {

            println("遇到 null 值")

        } finally {

            // 无论成功还是失败都会执行，适合放清理逻辑

            println("--- 处理完一轮 ---")

        }

    }


    println("循环结束，程序继续运行")

}
```

## 代码块 2

```kotlin
42 转换成功：42
--- 处理完一轮 ---
数字格式错误：For input string: "runoob"
--- 处理完一轮 ---
遇到 null 值
--- 处理完一轮 ---
循环结束，程序继续运行
```

## 代码块 3

```kotlin
// try 的返回值直接作为函数返回值

fun parseAge(text: String): Int {

    return try {

        text.toInt()          // 成功时整个 try 表达式的值

    } catch (e: NumberFormatException) {

        -1                    // 失败时整个 try 表达式的值

    }

}


fun main() {

    println(parseAge("18"))

    println(parseAge("runoob"))


    // finally 块的返回值会被忽略，不会影响 try 表达式的结果

    val age = try {

        "20".toInt()

    } finally {

        println("finally 块执行了，但不影响 try 的值")

    }

    println(age)

}
```

## 代码块 4

```kotlin
18
-1
finally 块执行了，但不影响 try 的值
20
```

## 代码块 5

```kotlin
// 返回类型 Nothing 表示这个函数永远不会正常返回

fun fail(message: String): Nothing {

    throw IllegalArgumentException(message)

}


fun checkAge(age: Int): String {

    // 因为 fail 返回 Nothing，编译器知道这里之后不会继续往下走

    if (age < 0) fail("年龄不能为负数：$age")

    return "年龄合法：$age"

}


fun main() {

    println(checkAge(18))


    try {

        checkAge(-1)

    } catch (e: IllegalArgumentException) {

        println("捕获到异常：${e.message}")

    }

}
```

## 代码块 6

```kotlin
年龄合法：18
捕获到异常：年龄不能为负数：-1
```

## 代码块 7

```kotlin
// 自定义异常通常继承 Exception；把出错的具体字段作为属性保留

class InvalidSiteNameException(val siteName: String) : Exception("非法的站点名称：$siteName")


fun registerSite(name: String) {

    // 站点名必须以 runoob 开头（不区分大小写），否则抛出自定义异常

    if (!name.startsWith("runoob", ignoreCase = true)) {

        throw InvalidSiteNameException(name)

    }

    println("注册成功：$name")

}


fun main() {

    registerSite("runoob")


    try {

        registerSite("example")

    } catch (e: InvalidSiteNameException) {

        // e.siteName 是自定义异常携带的上下文信息

        println("注册失败：${e.message}，问题字段：${e.siteName}")

    }

}
```

## 代码块 8

```kotlin
注册成功：runoob
注册失败：非法的站点名称：example，问题字段：example
```

## 代码块 9

```kotlin
import java.io.IOException


// @Throws 只在 Java 调用方需要 catch 时使用，Kotlin 侧写不写都一样

@Throws(IOException::class)

fun readConfig(path: String): String {

    if (path.isEmpty()) throw IOException("配置路径为空")

    return "配置来自 $path"

}


fun main() {

    // Kotlin 不强制 try-catch，但异常依然会在运行时抛出

    println(readConfig("runoob.conf"))


    try {

        readConfig("")

    } catch (e: IOException) {

        println("读取失败：${e.message}")

    }

}
```

## 代码块 10

```kotlin
配置来自 runoob.conf
读取失败：配置路径为空
```

## 代码块 11

```kotlin
import java.io.File


fun main() {

    // use 会在代码块结束后自动调用 close()，即使块内抛出了异常

    File("runoob.txt").bufferedWriter().use { writer ->

        writer.write("Hello RUNOOB")

        writer.newLine()                  // 写入换行符

        writer.write("Hello Kotlin")

    }


    // 读取刚才写入的内容

    File("runoob.txt").bufferedReader().use { reader ->

        reader.forEachLine { line -> println(line) }

    }


    // useLines 一次读取全部行，块结束后自动关闭文件

    File("runoob.txt").useLines { lines ->

        println("总行数：${lines.count()}")

    }

}
```

## 代码块 12

```kotlin
Hello RUNOOB
Hello Kotlin
总行数：2
```

## 代码块 13

```kotlin
import java.io.File


fun main() {

    // use 的返回值就是块内最后一行，这里得到文件的行数

    val lineCount: Int = File("runoob.txt").useLines { lines -> lines.count() }

    println("文件共有 $lineCount 行")

}
```

## 代码块 14

```kotlin
文件共有 2 行
```

## 代码块 15

```kotlin
fun main() {

    // 成功与失败都会被包装成 Result，不会中断程序

    val ok = runCatching { "42".toInt() }

    val bad = runCatching { "runoob".toInt() }


    println("成功：isSuccess=${ok.isSuccess}，值=${ok.getOrNull()}")

    println("失败：isFailure=${bad.isFailure}，值=${bad.getOrNull()}")

    println("失败时给默认值：${bad.getOrDefault(-1)}")


    // getOrElse 拿到异常，可以据此拼出兜底值

    val fallback = bad.getOrElse { e -> "兜底(${e.message})" }

    println("兜底结果：$fallback")


    // onFailure 适合打日志，不影响后续流程

    runCatching { "x".toInt() }

        .onFailure { println("onFailure：${it.javaClass.simpleName}") }

}
```

## 代码块 16

```kotlin
成功：isSuccess=true，值=42
失败：isFailure=true，值=null
失败时给默认值：-1
兜底结果：兜底(For input string: "runoob")
onFailure：NumberFormatException
```
