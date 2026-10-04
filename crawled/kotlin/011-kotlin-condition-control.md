# Kotlin 条件控制

> 来源: https://www.runoob.com/kotlin/kotlin-condition-control.html

## 代码块 1

```kotlin
fun main() {

    val age = 18


    if (age >= 18) {

        println("已成年")

    }


    // 单条语句可以省略花括号

    if (age >= 18) println("已成年（省略花括号）")


    // 条件不成立时执行 else

    if (age < 18) {

        println("未成年")

    } else {

        println("成年")

    }

}
```

## 代码块 2

```kotlin
已成年
已成年（省略花括号）
成年
```

## 代码块 3

```kotlin
fun main() {

    val a = 10

    val b = 20


    // 相当于 Java 的 a > b ? a : b

    val max = if (a > b) a else b

    println(max)          // 20


    // 分支块的最后一行就是返回值

    val desc = if (a > b) {

        println("a 更大")

        "a"

    } else {

        println("b 更大")

        "b"

    }

    println(desc)         // b


    // 没有 else 时只能当语句用，不能赋值

    // val bad = if (a > b) a   // 编译错误

}
```

## 代码块 4

```kotlin
20
b 更大
b
```

## 代码块 5

```kotlin
fun scoreToGrade(score: Int): String {

    return if (score >= 90) {

        "A"

    } else if (score >= 80) {

        "B"

    } else if (score >= 60) {

        "C"

    } else {

        "D"

    }

}


fun main() {

    println(scoreToGrade(95))   // A

    println(scoreToGrade(85))   // B

    println(scoreToGrade(60))   // C

    println(scoreToGrade(59))   // D

}
```

## 代码块 6

```kotlin
A
B
C
D
```

## 代码块 7

```kotlin
fun main() {

    val score = 85


    if (score in 90..100) {

        println("优秀")

    } else if (score in 80..<90) {      // ..< 不包含右端点 90

        println("良好")

    } else if (score in 60 until 80) {  // until 等价于 ..<

        println("及格")

    } else {

        println("不及格")

    }


    // !in 表示不在区间内

    val c = 'x'

    if (c !in 'a'..'z') {

        println("不是小写字母")

    } else {

        println("是小写字母")

    }

}
```

## 代码块 8

```kotlin
良好
是小写字母
```

## 代码块 9

```kotlin
fun describe(x: Any): String = when (x) {

    1 -> "数字 1"

    "Runoob" -> "菜鸟教程"

    is Long -> "Long 类型"

    !is String -> "不是字符串"

    else -> "其他"

}


fun main() {

    println(describe(1))        // 数字 1

    println(describe("Runoob")) // 菜鸟教程

    println(describe(100L))     // Long 类型

    println(describe(3.14))     // 不是字符串

    println(describe("hello"))  // 其他

}
```

## 代码块 10

```kotlin
数字 1
菜鸟教程
Long 类型
不是字符串
其他
```

## 代码块 11

```kotlin
fun main() {

    // 逗号多值：任意一个相等就命中

    val day = 6

    val type = when (day) {

        1, 2, 3, 4, 5 -> "工作日"

        6, 7 -> "周末"

        else -> "无效的日期"

    }

    println(type)                      // 周末


    // 区间条件

    val score = 85

    val grade = when (score) {

        in 90..100 -> "优秀"

        in 80..<90 -> "良好"

        in 60 until 80 -> "及格"

        else -> "不及格"

    }

    println(grade)                     // 良好


    // is 判断会智能转换，分支内可以直接访问成员

    val value: Any = "www.runoob.com"

    val len = when (value) {

        is String -> value.length      // 这里 value 已被当作 String

        is Int -> value

        else -> 0

    }

    println(len)                       // 14

}
```

## 代码块 12

```kotlin
周末
良好
14
```

## 代码块 13

```kotlin
fun checkNumber(n: Int): String = when {

    n < 0 -> "负数"

    n == 0 -> "零"

    n in 1..9 -> "个位数"

    else -> "多位数"

}


fun main() {

    println(checkNumber(-3))    // 负数

    println(checkNumber(0))     // 零

    println(checkNumber(7))     // 个位数

    println(checkNumber(100))   // 多位数

}
```

## 代码块 14

```kotlin
负数
零
个位数
多位数
```

## 代码块 15

```kotlin
enum class Status { LOADING, SUCCESS, ERROR }


// 枚举主语：覆盖所有枚举值，不需要 else

fun message(status: Status): String = when (status) {

    Status.LOADING -> "加载中"

    Status.SUCCESS -> "成功"

    Status.ERROR -> "失败"

}


// Boolean 主语：true 和 false 都覆盖，不需要 else

fun label(flag: Boolean): String = when (flag) {

    true -> "开"

    false -> "关"

}


fun main() {

    println(message(Status.SUCCESS))   // 成功

    println(label(true))               // 开

}
```

## 代码块 16

```kotlin
成功
开
```

## 代码块 17

```kotlin
sealed class Result

data class Success(val data: String) : Result()

data class Failure(val reason: String) : Result()


fun render(result: Result): String = when (result) {

    is Success -> "成功：${result.data}"

    is Failure -> "失败：${result.reason}"

}


fun main() {

    println(render(Success("RUNOOB")))     // 成功：RUNOOB

    println(render(Failure("网络超时")))    // 失败：网络超时

}
```

## 代码块 18

```kotlin
成功：RUNOOB
失败：网络超时
```

## 代码块 19

```kotlin
sealed interface Response

data class Ok(val body: String) : Response

data class Error(val reason: String) : Response


fun handle(response: Response): String = when (response) {

    // 主条件成立后，再判断守卫条件

    is Ok if response.body.isNotEmpty() -> "成功：${response.body}"

    is Ok -> "成功但内容为空"

    is Error if response.reason.isNotBlank() -> "失败：${response.reason}"

    is Error -> "失败：原因未知"

}


fun main() {

    println(handle(Ok("RUNOOB")))    // 成功：RUNOOB

    println(handle(Ok("")))          // 成功但内容为空

    println(handle(Error("超时")))    // 失败：超时

    println(handle(Error("   ")))    // 失败：原因未知

}
```

## 代码块 20

```kotlin
成功：RUNOOB
成功但内容为空
失败：超时
失败：原因未知
```

## 代码块 21

```kotlin
sealed interface Animal {

    data class Cat(val mouseHunter: Boolean, val hungry: Boolean) : Animal

    data class Dog(val breed: String) : Animal

}


fun feed(animal: Animal): String = when (animal) {

    is Animal.Dog -> "喂狗"

    // 多个守卫条件用 && 组合

    is Animal.Cat if (!animal.mouseHunter && animal.hungry) -> "喂猫"

    is Animal.Cat -> "不喂猫"

}


fun main() {

    println(feed(Animal.Dog("Beagle")))                            // 喂狗

    println(feed(Animal.Cat(mouseHunter = false, hungry = true)))  // 喂猫

    println(feed(Animal.Cat(mouseHunter = true, hungry = true)))   // 不喂猫

}
```

## 代码块 22

```kotlin
喂狗
喂猫
不喂猫
```
