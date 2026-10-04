# Kotlin 运算符重载

> 来源: https://www.runoob.com/kotlin/kotlin-operator.html

## 代码块 1

```kotlin
class Point(val x: Int, val y: Int) {

    // 函数名必须叫 plus，并且用 operator 修饰

    operator fun plus(other: Point): Point = Point(x + other.x, y + other.y)


    override fun toString(): String = "($x, $y)"

}


fun main() {

    val a = Point(1, 2)

    val b = Point(3, 4)


    // a + b 会被编译器翻译成 a.plus(b)

    println(a + b)

    println(a.plus(b))

}
```

## 代码块 2

```kotlin
(4, 6)
(4, 6)
```

## 代码块 3

```kotlin
data class Counter(val value: Int) {

    // -counter

    operator fun unaryMinus() = Counter(-value)


    // counter++

    operator fun inc() = Counter(value + 1)


    // counter--

    operator fun dec() = Counter(value - 1)

}


fun main() {

    val c = Counter(10)

    println(-c)


    // ++ 与 -- 会重新赋值给变量，因此变量必须声明为 var

    var n = Counter(0)

    n++

    println(n)

    n--

    println(n)

}
```

## 代码块 4

```kotlin
Counter(value=-10)
Counter(value=1)
Counter(value=0)
```

## 代码块 5

```kotlin
class Basket {

    private val items = mutableListOf<String>()


    // plusAssign 返回 Unit，修改的是对象自身状态

    // 因此 basket 声明为 val 也可以使用 +=

    operator fun plusAssign(item: String) {

        items += item

    }


    override fun toString(): String = items.toString()

}


fun main() {

    val basket = Basket()

    basket += "苹果"

    basket += "香蕉"

    basket += "RUNOOB 周边"

    println(basket)

}
```

## 代码块 6

```kotlin
[苹果, 香蕉, RUNOOB 周边]
```

## 代码块 7

```kotlin
data class Version(val major: Int, val minor: Int) : Comparable<Version> {

    // 实现 Comparable 接口后，> < >= <= 都能直接用

    override fun compareTo(other: Version): Int {

        if (major != other.major) return major - other.major

        return minor - other.minor

    }

}


fun main() {

    val current = Version(2, 2)

    val old = Version(1, 9)


    println(current > old)

    println(current < old)

    println(current >= Version(2, 2))

    println(current == Version(2, 2))

    println(current != old)

}
```

## 代码块 8

```kotlin
true
false
true
true
true
```

## 代码块 9

```kotlin
class Playlist {

    private val songs = mutableListOf<String>()


    // list[0] -> list.get(0)

    operator fun get(index: Int): String = songs[index]


    // list[0] = "x" -> list.set(0, "x")

    operator fun set(index: Int, value: String) {

        songs[index] = value

    }


    // "x" in list -> list.contains("x")

    operator fun contains(title: String): Boolean = songs.any { it.contains(title) }


    operator fun plusAssign(song: String) {

        songs += song

    }

}


fun main() {

    val list = Playlist()

    list += "Runoob 教程"

    list += "Kotlin 入门"

    list += "RUNOOB 实战"


    println(list[0])

    list[1] = "Kotlin 值类"

    println(list[1])

    println("值类" in list)

    println("Java" in list)

}
```

## 代码块 10

```kotlin
Runoob 教程
Kotlin 值类
true
false
```

## 代码块 11

```kotlin
class Formatter(val prefix: String) {

    // f("x") -> f.invoke("x")

    operator fun invoke(text: String): String = "$prefix$text"


    // f("x", "y") -> f.invoke("x", "y")

    operator fun invoke(vararg texts: String): String =

        texts.joinToString(", ") { "$prefix$it" }

}


fun main() {

    val f = Formatter("[RUNOOB] ")

    println(f("第一条"))

    println(f("第一条", "第二条", "第三条"))

}
```

## 代码块 12

```kotlin
[RUNOOB] 第一条
[RUNOOB] 第一条, [RUNOOB] 第二条, [RUNOOB] 第三条
```

## 代码块 13

```kotlin
data class Vector(val x: Double, val y: Double) {

    operator fun plus(other: Vector) = Vector(x + other.x, y + other.y)


    operator fun minus(other: Vector) = Vector(x - other.x, y - other.y)


    // 数乘：向量 * 标量

    operator fun times(scale: Double) = Vector(x * scale, y * scale)


    operator fun unaryMinus() = Vector(-x, -y)


    // v[0] 取 x，v[1] 取 y

    operator fun get(index: Int): Double = when (index) {

        0 -> x

        1 -> y

        else -> throw IndexOutOfBoundsException("向量只有两个分量，索引为 $index")

    }


    override fun toString(): String = "($x, $y)"

}


fun main() {

    val a = Vector(1.0, 2.0)

    val b = Vector(3.0, 4.0)


    println(a + b)

    println(a - b)

    println(a * 2.0)

    println(-a)

    println(a[0])

    println(a[1])

}
```

## 代码块 14

```kotlin
(4.0, 6.0)
(-2.0, -2.0)
(2.0, 4.0)
(-1.0, -2.0)
1.0
2.0
```

## 代码块 15

```kotlin
import kotlin.math.abs


@JvmInline

value class Money(val cents: Long) {

    operator fun plus(other: Money) = Money(cents + other.cents)


    operator fun minus(other: Money) = Money(cents - other.cents)


    // 数量倍乘

    operator fun times(quantity: Int) = Money(cents * quantity)


    operator fun compareTo(other: Money): Int = cents.compareTo(other.cents)


    // 输出成 19.99 这样的金额格式

    override fun toString(): String {

        val sign = if (cents < 0) "-" else ""

        val absCents = abs(cents)

        return "$sign${absCents / 100}.${(absCents % 100).toString().padStart(2, '0')}"

    }

}


fun main() {

    val price = Money(1999)             // 19.99

    val total = price * 3 + Money(500)  // 19.99 * 3 + 5.00


    println("单价：$price")

    println("总价：$total")

    println("总价大于单价：${total > price}")

    println("差额：${total - price}")

}
```

## 代码块 16

```kotlin
单价：19.99
总价：64.97
总价大于单价：true
差额：44.98
```
