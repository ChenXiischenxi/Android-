# Kotlin 使用命令行编译

> 来源: https://www.runoob.com/kotlin/kotlin-command-line.html

## 代码块 1

```kotlin
$ curl -s https://get.sdkman.io | bash
$ source "$HOME/.sdkman/bin/sdkman-init.sh"
$ sdk install kotlin

Downloading: kotlin 2.2.0
In progress...
Installing: kotlin 2.2.0
Done installing!

Setting kotlin 2.2.0 as default.
```

## 代码块 2

```kotlin
$ export PATH="$PATH:/opt/kotlinc/bin"

# 把上面这行写进 ~/.zshrc 或 ~/.bashrc，重启终端后永久生效
```

## 代码块 3

```kotlin
$ kotlinc -version
info: kotlinc-jvm 2.2.0 (JRE 17.0.11+9)
```

## 代码块 4

```kotlin
// 文件路径：hello.kt

fun main() {

    println("Hello, Runoob!")            // 输出一行文本

    println("欢迎来到 www.runoob.com")

}
```

## 代码块 5

```kotlin
$ kotlinc hello.kt -include-runtime -d hello.jar
$ java -jar hello.jar

Hello, Runoob!
欢迎来到 www.runoob.com
```

## 代码块 6

```kotlin
$ kotlinc hello.kt -d out

$ ls out
HelloKt.class        # 顶层 main 函数所在的类，由文件名加 Kt 构成
```

## 代码块 7

```kotlin
$ kotlinc hello.kt -include-runtime -d hello.jar
$ java -jar hello.jar

Hello, Runoob!
欢迎来到 www.runoob.com
```

## 代码块 8

```kotlin
$ java -cp hello.jar:kotlin-stdlib.jar HelloKt
```

## 代码块 9

```kotlin
// 文件路径：Site.kt

// 一个简单的工具库

package com.runoob


fun buildWelcome(name: String): String = "欢迎访问 $name（www.runoob.com）"


fun main() {

    println(buildWelcome("菜鸟教程"))

}
```

## 代码块 10

```kotlin
$ kotlinc Site.kt -d site.jar
$ kotlin -classpath site.jar com.runoob.SiteKt

欢迎访问 菜鸟教程（www.runoob.com）
```

## 代码块 11

```kotlin
$ kotlinc
Welcome to Kotlin version 2.2.0 (JRE 17.0.11+9)
Type :help for help, :quit for quit
>>> val siteName = "菜鸟教程"
>>> println("欢迎访问 $siteName")
欢迎访问 菜鸟教程
>>> println("网址：www.runoob.com".uppercase())
网址：WWW.RUNOOB.COM
>>> :quit
```

## 代码块 12

```kotlin
// 文件路径：hello.kts

// 脚本模式：不需要 main 函数，顶层代码直接执行

val siteName = "菜鸟教程"

val url = "www.runoob.com"


println("Hello, $siteName!")

println("站点地址：$url")

println("名称长度：${siteName.length}")
```

## 代码块 13

```kotlin
$ kotlinc -script hello.kts

Hello, 菜鸟教程!
站点地址：www.runoob.com
名称长度：4
```

## 代码块 14

```kotlin
// 文件路径：greet.kts

// 读取命令行参数并输出

val name = if (args.isNotEmpty()) args[0] else "Runoob"

println("你好，$name！欢迎访问 www.runoob.com")
```

## 代码块 15

```kotlin
$ kotlinc -script greet.kts 菜鸟教程

你好，菜鸟教程！欢迎访问 www.runoob.com
```
