# Kotlin 值类

> 来源: https://www.runoob.com/kotlin/kotlin-value-class.html

## 代码块 1

```kotlin
// 三个参数都是 String，编译器无法阻止调用者把顺序写反

fun transfer(fromAccount: String, toAccount: String, amount: Double) {

    println("从 $fromAccount 转账 $amount 到 $toAccount")

}


fun main() {

    val account = "6222021234567890"

    val password = "runoob-2026"

    // 参数顺序写反了，编译照样通过，运行时才暴露问题

    transfer(password, account, 100.0)

}
```

## 代码块 2

```kotlin
从 runoob-2026 转账 100.0 到 6222021234567890
```

## 代码块 3

```kotlin
@JvmInline

value class UserId(val value: Int)


@JvmInline

value class Email(val address: String)


// 两个参数类型不同，调用时传反顺序会直接编译报错

fun sendMail(to: Email, userId: UserId) {

    println("向 ${to.address} 的用户 ${userId.value} 发送邮件")

}


fun main() {

    val email = Email("[email protected]")

    val id = UserId(1001)

    sendMail(email, id)


    // 值类自动生成 equals / hashCode / toString

    println(id == UserId(1001))

    println(UserId(1001) == UserId(1002))

    println(id)

}
```

## 代码块 4

```kotlin
向 [email protected] 的用户 1001 发送邮件
true
false
UserId(value=1001)
```

## 代码块 5

```kotlin
@JvmInline

value class Percentage(val value: Int) {

    init {

        // 构造时校验，非法值根本创建不出来

        require(value in 0..100) { "百分比必须在 0 到 100 之间，当前为 $value" }

    }

}


fun main() {

    val progress = Percentage(80)

    println("进度：${progress.value}%")


    // 用 runCatching 捕获构造异常，方便展示错误信息

    val result = runCatching { Percentage(120) }

    println(result.exceptionOrNull()?.message)

}
```

## 代码块 6

```kotlin
进度：80%
百分比必须在 0 到 100 之间，当前为 120
```

## 代码块 7

```kotlin
@JvmInline

value class Email private constructor(val address: String) {

    companion object {

        // 工厂函数：统一做清洗与校验，外部无法绕过

        fun of(raw: String): Email {

            val normalized = raw.trim().lowercase()

            require(normalized.contains("@")) { "邮箱格式不正确：$raw" }

            return Email(normalized)

        }

    }

}


fun main() {

    val email = Email.of("  [email protected]  ")

    println(email.address)


    val bad = runCatching { Email.of("runoob.com") }

    println(bad.exceptionOrNull()?.message)

}
```

## 代码块 8

```kotlin
[email protected]
邮箱格式不正确：runoob.com
```

## 代码块 9

```kotlin
@JvmInline

value class Temperature(val celsius: Double) {

    // 计算属性：不占额外内存，getter 每次现算

    val fahrenheit: Double

        get() = celsius * 9 / 5 + 32

}


fun main() {

    val t = Temperature(25.0)

    println("摄氏 ${t.celsius} 度")

    println("华氏 ${t.fahrenheit} 度")

}
```

## 代码块 10

```kotlin
摄氏 25.0 度
华氏 77.0 度
```

## 代码块 11

```kotlin
interface Displayable {

    fun display(): String

}


@JvmInline

value class Meter(val value: Double) : Displayable {

    override fun display(): String = "$value m"

}


// 参数是具体类型 Meter，底层就是一个 double

fun half(m: Meter): Meter = Meter(m.value / 2)


// 参数是接口类型，传入的 Meter 会被装箱成对象

fun show(d: Displayable): String = d.display()


fun main() {

    val m = Meter(10.0)

    println(half(m).value)

    println(show(m))

    println(m.display())

}
```

## 代码块 12

```kotlin
5.0
10.0 m
10.0 m
```
