# Kotlin 各版本新特性速查

> 来源: https://www.runoob.com/kotlin/kotlin-new-features.html

## 代码块 1

```kotlin
// 文件路径：src/main/kotlin/com/runoob/TypeAliasDemo.kt

package com.runoob


// Kotlin 1.1 起支持类型别名

typealias UserId = Int


// Kotlin 1.1 起，sealed 类的子类只需在同一个文件里

sealed class State

class Loading : State()

class Done : State()


fun findUserName(id: UserId): String = "用户 $id"


fun main() {

    println(findUserName(1001))

}
```

## 代码块 2

```kotlin
用户 1001
```

## 代码块 3

```kotlin
// 文件路径：src/commonMain/kotlin/com/runoob/Platform.kt

// 公共源码集：只声明，不实现

expect fun platformName(): String


fun greet(): String = "运行平台：${platformName()}"
```

## 代码块 4

```kotlin
// 文件路径：src/jvmMain/kotlin/com/runoob/Platform.jvm.kt

// JVM 源码集：提供与 expect 对应的 actual 实现

actual fun platformName(): String = "JVM"
```

## 代码块 5

```kotlin
运行平台：JVM
```

## 代码块 6

```kotlin
// 文件路径：src/main/kotlin/com/runoob/UnsignedDemo.kt

package com.runoob


import kotlin.contracts.ExperimentalContracts

import kotlin.contracts.contract


// Kotlin 1.3 起引入无符号整数类型，1.5 起稳定

val maxValue: UInt = UInt.MAX_VALUE


// Kotlin 1.3 起引入契约：函数正常返回就说明参数不为 null

// 契约 API 目前仍是实验性的，需要加 @OptIn 才能使用

@OptIn(ExperimentalContracts::class)

fun requireText(value: String?): String {

    contract { returns() implies (value != null) }

    if (value == null) throw IllegalArgumentException("内容不能为空")

    return value

}


fun main() {

    println(maxValue)

    println(0xFFu)

    val text: String? = "RUNOOB"

    println(requireText(text).length)

}
```

## 代码块 7

```kotlin
4294967295
255
6
```

## 代码块 8

```kotlin
// 文件路径：src/main/kotlin/com/runoob/SamDemo.kt

package com.runoob


// Kotlin 1.4 起，声明为 fun interface 的接口支持 SAM 转换

fun interface ClickHandler {

    fun onClick(name: String)

}


// Kotlin 1.4 起支持 sealed interface

sealed interface Result

data class Success(val data: String) : Result

data class Failure(val message: String) : Result


fun main() {

    // 用 lambda 直接实现接口

    val handler = ClickHandler { println("点击了 $it") }

    handler.onClick("RUNOOB")


    // 多行参数列表的尾逗号，1.4 起允许

    val site = mapOf(

        "name" to "Runoob",

        "url" to "www.runoob.com",

    )

    println(site)

}
```

## 代码块 9

```kotlin
点击了 RUNOOB
{name=Runoob, url=www.runoob.com}
```

## 代码块 10

```kotlin
// 文件路径：src/main/kotlin/com/runoob/ValueClassDemo.kt

package com.runoob


// Kotlin 1.5 起值类稳定，编译后多数场景不产生包装对象

@JvmInline

value class UserId(val value: Int)


fun main() {

    val id = UserId(1001)

    println(id.value)

    println(id)

}
```

## 代码块 11

```kotlin
1001
UserId(value=1001)
```

## 代码块 12

```kotlin
// Kotlin 1.5 起支持声明 JVM record，要求 JDK 16+

@JvmRecord

data class Point(val x: Int, val y: Int)
```

## 代码块 13

```kotlin
// 文件路径：src/main/kotlin/com/runoob/SealedWhenDemo.kt

package com.runoob


sealed class State

object Loading : State()

object Done : State()


// Kotlin 1.6 起，when 语句（不只是表达式）也必须穷尽所有分支

fun describe(state: State) {

    when (state) {

        Loading -> println("加载中")

        Done -> println("完成")

    }

}


fun main() {

    describe(Loading)

    describe(Done)

}
```

## 代码块 14

```kotlin
加载中
完成
```

## 代码块 15

```kotlin
// 文件路径：src/main/kotlin/com/runoob/RangeDemo.kt

package com.runoob


fun main() {

    // Kotlin 1.7 起引入 ..< 运算符，1.9 起稳定

    for (i in 0..<3) {

        println(i)

    }

}
```

## 代码块 16

```kotlin
0
1
2
```

## 代码块 17

```kotlin
// 文件路径：src/main/kotlin/com/runoob/EntriesDemo.kt

package com.runoob


enum class Color { RED, GREEN, BLUE }


// Kotlin 1.8 起支持 data object

data object Runoob {

    const val SITE = "www.runoob.com"

}


fun main() {

    // 1.8 起推荐用 entries 代替 values()

    Color.entries.forEach { println(it) }

    println(Runoob)

    println(Runoob.SITE)

}
```

## 代码块 18

```kotlin
RED
GREEN
BLUE
Runoob
www.runoob.com
```

## 代码块 19

```kotlin
// 文件路径：src/main/kotlin/com/runoob/StableDemo.kt

package com.runoob


enum class Color { RED, GREEN, BLUE }


data object Runoob {

    const val SITE = "www.runoob.com"

}


fun main() {

    // ..< 在 1.9 起稳定

    println((0..<3).toList())

    // entries 在 1.9 起稳定

    println(Color.entries.map { it.name })

    // data object 在 1.9 起稳定

    println(Runoob)

}
```

## 代码块 20

```kotlin
[0, 1, 2]
[RED, GREEN, BLUE]
Runoob
```

## 代码块 21

```kotlin
// 文件路径：src/main/kotlin/com/runoob/WhenGuardDemo.kt

package com.runoob


sealed interface Response


data class Ok(val body: String) : Response

data class Error(val code: Int) : Response


fun handle(response: Response): String = when (response) {

    is Ok -> "成功：${response.body}"

    // 守卫条件：2.0 起引入，2.2 起稳定

    is Error if response.code == 404 -> "页面不存在"

    is Error -> "错误码 ${response.code}"

}


fun main() {

    println(handle(Ok("RUNOOB")))

    println(handle(Error(404)))

    println(handle(Error(500)))

}
```

## 代码块 22

```kotlin
成功：RUNOOB
页面不存在
错误码 500
```

## 代码块 23

```kotlin
// 文件路径：src/main/kotlin/com/runoob/ContextDemo.kt

package com.runoob


class Logger {

    fun log(message: String) = println(message)

}


// Kotlin 2.1 起引入 context parameters 语法（预览特性）

context(logger: Logger)

fun greet(name: String) {

    logger.log("Hello, $name")

}


fun main() {

    // 通过隐式接收者提供上下文参数

    with(Logger()) {

        greet("Runoob")

    }

}
```

## 代码块 24

```kotlin
Hello, Runoob
```

## 代码块 25

```kotlin
// 文件路径：src/main/kotlin/com/runoob/NestedAliasDemo.kt

package com.runoob


class User {

    // Kotlin 2.1 起支持嵌套类型别名（预览特性）

    typealias Id = Int


    fun find(id: Id): String = "用户 $id"

}


fun main() {

    println(User().find(1001))

}
```

## 代码块 26

```kotlin
用户 1001
```

## 代码块 27

```kotlin
// 文件路径：src/main/kotlin/com/runoob/NonLocalBreakDemo.kt

package com.runoob


fun main() {

    // 2.2 起稳定：lambda 里的 break 可以跳出外层 for 循环

    for (i in 1..3) {

        listOf(1, 2, 3).forEach {

            if (it == 2) break   // 直接跳出外层循环

            print("$i-$it ")

        }

    }

    println()

}
```

## 代码块 28

```kotlin
1-1
```

## 代码块 29

```kotlin
// 文件路径：build.gradle.kts


kotlin {

    compilerOptions {

        // 语言版本决定哪些语法可用，先与旧版本保持一致再逐步提升

        languageVersion.set(org.jetbrains.kotlin.gradle.dsl.KotlinVersion.KOTLIN_2_2)

        // API 版本决定能调用哪些标准库 API，应小于等于语言版本

        apiVersion.set(org.jetbrains.kotlin.gradle.dsl.KotlinVersion.KOTLIN_2_2)

    }

}
```
