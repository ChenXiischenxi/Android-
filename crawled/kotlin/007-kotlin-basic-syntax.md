# Kotlin 基础语法

> 来源: https://www.runoob.com/kotlin/kotlin-basic-syntax.html

## 代码块 1

```kotlin
// 文件路径：com/runoob/Util.kt

package com.runoob                    // 包声明必须在文件第一行（注释除外）


import kotlin.math.PI                 // 导入单个声明

import kotlin.math.sqrt               // 每行导入一个


fun circleArea(r: Double): Double = PI * r * r


fun main() {

    println("半径 2 的圆面积：${sqrt(circleArea(2.0) / PI)}")

}
```

## 代码块 2

```kotlin
半径 2 的圆面积：2.0
```

## 代码块 3

```kotlin
// 文件路径：Alias.kt

import kotlin.math.PI as PI_VALUE      // 起别名，避免与同名符号冲突

import java.util.Date as JavaDate      // 区分两个不同来源的同名类


fun main() {

    println("圆周率约等于 $PI_VALUE")

    println(JavaDate::class.java.simpleName)

}
```

## 代码块 4

```kotlin
圆周率约等于 3.141592653589793
Date
```

## 代码块 5

```kotlin
// 文件路径：Wildcard.kt

import kotlin.math.*                   // 导入 kotlin.math 下的全部声明


fun main() {

    println(max(3, 7))                 // 无需再写 kotlin.math.max

    println(abs(-5))

}
```

## 代码块 6

```kotlin
7
5
```

## 代码块 7

```kotlin
// 文件路径：Main.kt

fun main() {

    println("Hello, Runoob!")

}
```

## 代码块 8

```kotlin
Hello, Runoob!
```

## 代码块 9

```kotlin
// 文件路径：Args.kt

fun main(args: Array<String>) {

    println("参数个数：${args.size}")                 // 未传参时为 0

    val name = args.firstOrNull() ?: "Runoob"         // 没有参数时给个默认值

    println("欢迎访问 $name")

}
```

## 代码块 10

```kotlin
$ kotlinc Args.kt -include-runtime -d args.jar
$ java -jar args.jar 菜鸟教程

参数个数：1
欢迎访问 菜鸟教程
```

## 代码块 11

```kotlin
// 文件路径：SuspendMain.kt

// suspend fun main 从 Kotlin 1.3 起支持，入口本身就是一个挂起函数

suspend fun fetchSite(): String {

    return "www.runoob.com"        // 真实场景中这里可能是网络请求

}


suspend fun main() {

    println("正在获取站点信息…")

    println("站点地址：" + fetchSite())

}
```

## 代码块 12

```kotlin
正在获取站点信息…
站点地址：www.runoob.com
```

## 代码块 13

```kotlin
// 文件路径：Variables.kt

fun main() {

    val siteName = "菜鸟教程"        // val：不可重新赋值

    var count = 1                   // var：可以重新赋值


    count = count + 1               // 合法，count 是 var

    println("$siteName 第 $count 次访问")


    // siteName = "RUNOOB"          // 取消注释会编译报错：Val cannot be reassigned

}
```

## 代码块 14

```kotlin
菜鸟教程 第 2 次访问
```

## 代码块 15

```kotlin
// 文件路径：Inference.kt

fun main() {

    val name = "Runoob"             // 推断为 String

    val age = 25                    // 推断为 Int

    val price = 9.9                 // 推断为 Double

    val isOpen = true               // 推断为 Boolean


    println("$name $age $price $isOpen")

    println(name::class.simpleName) // 打印运行时类型名

}
```

## 代码块 16

```kotlin
Runoob 25 9.9 true
String
```

## 代码块 17

```kotlin
// 文件路径：ExplicitType.kt

fun main() {

    val siteName: String = "菜鸟教程"    // 显式指定类型

    var age: Int                         // 只声明不赋值，此时必须写类型


    age = 25                             // 之后再赋值

    println("$siteName，age = $age")

}
```

## 代码块 18

```kotlin
菜鸟教程，age = 25
```

## 代码块 19

```kotlin
// 文件路径：Comments.kt


// 这是单行注释，从 // 到行尾都会被忽略


/*

 * 这是块注释

 * 可以跨越多行

 */

fun main() {

    println("RUNOOB")     // 行尾注释

}
```

## 代码块 20

```kotlin
RUNOOB
```

## 代码块 21

```kotlin
// 文件路径：NestedComment.kt

/* 外层注释开始

   /* 内层注释，Kotlin 允许块注释嵌套 */

   外层注释继续

   到这里才真正结束 */

fun main() {

    println("注释嵌套测试通过")

}
```

## 代码块 22

```kotlin
注释嵌套测试通过
```

## 代码块 23

```kotlin
// 文件路径：Template.kt

fun main() {

    val siteName = "菜鸟教程"

    val url = "www.runoob.com"


    println("欢迎访问 $siteName")                  // 直接引用变量

    println("网址：${url.uppercase()}")            // 花括号里可以放表达式

    println("名称长度：${siteName.length}")         // 调用属性

    println("明年将是 ${2026 - 2010} 周年")         // 算术表达式

}
```

## 代码块 24

```kotlin
欢迎访问 菜鸟教程
网址：WWW.RUNOOB.COM
名称长度：4
明年将是 16 周年
```

## 代码块 25

```kotlin
// 文件路径：Dollar.kt

fun main() {

    println("价格是 \$9.9")            // 转义美元符号

    println("5\$ 可以买到 1 份教程")     // 这里的 \$ 也按普通字符处理

}
```

## 代码块 26

```kotlin
价格是 $9.9
5$ 可以买到 1 份教程
```

## 代码块 27

```kotlin
// 文件路径：Semicolon.kt

fun main() {

    val a = 1                      // 推荐：一行一句，不写分号

    val b = 2


    val c = 3; val d = 4           // 合法但不推荐：一行多句用分号


    println("${a + b} ${c + d}")

}
```

## 代码块 28

```kotlin
3 7
```

## 代码块 29

```kotlin
// 文件路径：LineBreak.kt

fun main() {

    val x = 1 +

            2                      // 运算符在行尾，表达式可以跨行


    val y = 10

    - 3                          // 这里会被当成两条语句：val y = 10 与 -3


    println("x = $x, y = $y")    // y 仍然是 10

}
```

## 代码块 30

```kotlin
x = 3, y = 10
```

## 代码块 31

```kotlin
// 文件路径：NullSafety.kt

fun main() {

    val notNull: String = "Runoob"        // 非空类型，不能赋 null

    val maybeNull: String? = null         // 可空类型，允许赋 null


    println(notNull.length)               // 非空类型可以直接访问成员


    // println(maybeNull.length)          // 编译报错：Only safe call allowed

    println(maybeNull?.length)            // 安全调用，结果为 null

    println(maybeNull?.length ?: 0)       // Elvis 运算符，为 null 时给默认值

}
```

## 代码块 32

```kotlin
6
null
0
```
