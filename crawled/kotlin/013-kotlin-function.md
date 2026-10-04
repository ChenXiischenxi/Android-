# Kotlin 函数

> 来源: https://www.runoob.com/kotlin/kotlin-function.html

## 代码块 1

```kotlin
// 文件路径：FunctionBasic.kt


// 块体：有花括号和 return，返回类型必须显式写出

fun add(a: Int, b: Int): Int {

    return a + b

}


// 表达式体：用 = 直接给出结果，返回类型可以推断为 Int

fun sub(a: Int, b: Int) = a - b


// 块体但没有返回值：默认返回 Unit，可以省略 : Unit

fun printSum(a: Int, b: Int) {

    println("$a + $b = ${a + b}")

}


fun main() {

    println(add(1, 2))       // 调用块体函数

    println(sub(5, 3))       // 调用表达式体函数

    printSum(2, 3)

}
```

## 代码块 2

```kotlin
3
2
2 + 3 = 5
```

## 代码块 3

```kotlin
// 显式写出返回类型，可读性更好

fun double(x: Int): Int = x * 2


// 返回类型也可以省略，由编译器推断为 Int

fun square(x: Int) = x * x


// 配合 when 表达式，替代一长串 if-else

fun describe(value: Int) = when {

    value < 0 -> "负数"

    value == 0 -> "零"

    else -> "正数"

}


fun main() {

    println(double(4))

    println(square(4))

    println(describe(-1))

    println(describe(0))

    println(describe(7))

}
```

## 代码块 4

```kotlin
8
16
负数
零
正数
```

## 代码块 5

```kotlin
// 两个参数都有默认值

fun greet(name: String = "Runoob", site: String = "www.runoob.com"): String {

    return "欢迎 $name 访问 $site"

}


fun main() {

    println(greet())                            // 两个参数都用默认值

    println(greet("RUNOOB"))                    // 只覆盖第一个参数

    println(greet(site = "kotlin.runoob.com"))  // 只覆盖第二个参数，用命名参数

}
```

## 代码块 6

```kotlin
欢迎 Runoob 访问 www.runoob.com
欢迎 RUNOOB 访问 www.runoob.com
欢迎 Runoob 访问 kotlin.runoob.com
```

## 代码块 7

```kotlin
// value 有默认值，却写在 unit 前面

fun format(value: Int = 0, unit: String): String = "$value$unit"


fun main() {

    // 不能写 format("px")，那样会把字符串传给 value 导致类型不匹配

    println(format(unit = "px"))

    println(format(12, "px"))

}
```

## 代码块 8

```kotlin
0px
12px
```

## 代码块 9

```kotlin
fun createSite(name: String, url: String, port: Int = 80): String {

    return "$name -> $url:$port"

}


fun main() {

    // 顺序打乱也能正确匹配

    println(createSite(url = "www.runoob.com", name = "Runoob"))


    // 位置参数和命名参数混用：位置参数必须写在命名参数前面

    println(createSite("RUNOOB", url = "www.runoob.com", port = 443))

}
```

## 代码块 10

```kotlin
Runoob -> www.runoob.com:80
RUNOOB -> www.runoob.com:443
```

## 代码块 11

```kotlin
// vararg numbers 在函数内部是 IntArray 类型

fun total(vararg numbers: Int): Int {

    var sum = 0

    for (number in numbers) {

        sum += number

    }

    return sum

}


fun main() {

    println(total(1, 2, 3))       // 传三个值

    println(total())              // 一个都不传，数组为空

    println(total(10, 20, 30, 40))


    // 已经有数组时，用展开运算符 * 把数组拆成独立参数

    val values = intArrayOf(100, 200)

    println(total(*values))

}
```

## 代码块 12

```kotlin
6
0
100
300
```

## 代码块 13

```kotlin
fun total(vararg numbers: Int): Int = numbers.sum()


fun main() {

    val list = listOf(1, 2, 3)


    // 错误写法：total(*list) 编译不通过

    // 正确做法是先转成数组再展开

    println(total(*list.toIntArray()))

}
```

## 代码块 14

```kotlin
6
```

## 代码块 15

```kotlin
// 显式写出 : Unit，与省略时完全等价

fun sayHello(): Unit {

    println("Hello, Runoob!")

}


// 下面两个函数返回类型都是 Unit

fun log1() {

    println("RUNOOB")

}


fun log2(): Unit = println("RUNOOB")


fun main() {

    sayHello()

    log1()


    // Unit 是类型，所以可以用变量接收它

    val result: Unit = log2()

    println(result)

}
```

## 代码块 16

```kotlin
Hello, Runoob!
RUNOOB
RUNOOB
kotlin.Unit
```

## 代码块 17

```kotlin
// 顶层函数：直接写在文件里

fun factorial(n: Int): Long {

    // 局部函数：定义在 factorial 内部，可以访问外层的 n

    fun multiply(current: Int, acc: Long): Long {

        return if (current == 1) acc else multiply(current - 1, acc * current)

    }


    // 局部函数也可以写成表达式体，返回类型同样能推断

    fun describe() = "计算 $n 的阶乘"


    println(describe())

    return multiply(n, 1L)

}


fun main() {

    println(factorial(5))

}
```

## 代码块 18

```kotlin
计算 5 的阶乘
120
```

## 代码块 19

```kotlin
// 递归调用是最后一步操作，可以享受 tailrec 优化

tailrec fun gcd(a: Int, b: Int): Int {

    return if (b == 0) a else gcd(b, a % b)

}


// 普通递归：最后一步是乘法而不是自身调用，不能用 tailrec

fun factorial(n: Int): Long {

    return if (n <= 1) 1L else n * factorial(n - 1)

}


fun main() {

    println(gcd(48, 18))

    println(factorial(5))

}
```

## 代码块 20

```kotlin
6
120
```

## 代码块 21

```kotlin
// 顶层函数：不属于任何类

fun topLevel(): String = "我是顶层函数"


class Site(val name: String) {

    // 成员函数：需要通过实例访问

    fun describe(): String = "站点：$name"


    // 成员函数内部可以直接调用顶层函数

    fun info() = "${describe()} / ${topLevel()}"

}


fun main() {

    println(topLevel())


    val runoob = Site("Runoob")

    println(runoob.describe())

    println(runoob.info())

}
```

## 代码块 22

```kotlin
我是顶层函数
站点：Runoob
站点：Runoob / 我是顶层函数
```

## 代码块 23

```kotlin
// 参数类型不同

fun format(value: Int) = "整数：$value"

fun format(value: Double) = "小数：$value"


// 参数个数不同

fun format(value: String, upper: Boolean) = if (upper) value.uppercase() else value


fun main() {

    println(format(42))

    println(format(3.14))

    println(format("runoob", true))

    println(format("runoob", false))

}
```

## 代码块 24

```kotlin
整数：42
小数：3.14
RUNOOB
runoob
```

## 代码块 25

```kotlin
// 错误示例：只有返回类型不同，编译不通过

// fun value(): Int = 1

// fun value(): String = "1"
```

## 代码块 26

```kotlin
class Site(val name: String) {

    // 成员中缀函数：只能有一个参数

    infix fun hostedAt(domain: String): String = "$name 托管在 $domain"

}


// 扩展中缀函数：给已有类型添加中缀调用能力

infix fun Int.biggerThan(other: Int): Boolean = this > other


fun main() {

    val runoob = Site("Runoob")


    // 下面两种写法完全等价

    println(runoob.hostedAt("www.runoob.com"))

    println(runoob hostedAt "www.runoob.com")


    // 等价于 10.biggerThan(3)

    println(10 biggerThan 3)

}
```

## 代码块 27

```kotlin
Runoob 托管在 www.runoob.com
Runoob 托管在 www.runoob.com
true
```
