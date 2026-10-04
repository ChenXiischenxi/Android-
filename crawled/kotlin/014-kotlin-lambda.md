# Kotlin Lambda 高阶函数

> 来源: https://www.runoob.com/kotlin/kotlin-lambda.html

## 代码块 1

```kotlin
// 文件路径：LambdaType.kt


// 接收两个 Int，返回 Int

val sum: (Int, Int) -> Int = { a, b -> a + b }


// 接收一个 String，返回 String

val greet: (String) -> String = { name -> "你好，$name" }


// 不接收参数，不返回有意义的值

val log: () -> Unit = { println("RUNOOB") }


// 整个函数类型的值可以为 null，要加一层括号

var callback: ((Int) -> Int)? = null


fun main() {

    println(sum(1, 2))

    println(greet("Runoob"))

    log()


    callback = { it * 2 }

    // callback 可能为 null，用安全调用 ?.invoke

    println(callback?.invoke(21))

}
```

## 代码块 2

```kotlin
3
你好，Runoob
RUNOOB
42
```

## 代码块 3

```kotlin
// 带接收者的函数类型：接收者是 String，参数是 Int，返回 String

val repeatFun: String.(Int) -> String = { times -> this.repeat(times) }


fun main() {

    // 既可以像扩展函数一样调用

    println("Run".repeatFun(2))


    // 也可以当作普通函数类型使用，此时接收者变成第一个参数

    val plain: (String, Int) -> String = repeatFun

    println(plain("RUNOOB", 2))

}
```

## 代码块 4

```kotlin
RunRun
RUNOOBRUNOOB
```

## 代码块 5

```kotlin
fun main() {

    // 完整写法：参数需要标类型时，类型写在参数名后面

    val sum = { a: Int, b: Int -> a + b }

    println(sum(3, 4))


    // 只有一个参数时可以省略参数声明，用隐式参数 it

    val double: (Int) -> Int = { it * 2 }

    println(double(5))


    // 没有参数的 Lambda

    val hello = { println("Hello, Runoob") }

    hello()


    // 多行 Lambda：最后一个表达式作为返回值

    val describe = { value: Int ->

        val text = if (value > 0) "正数" else "非正数"

        "结果是 $text"

    }

    println(describe(1))


    // 用不到的参数可以用下划线占位，Kotlin 1.1 起支持

    val second = { _: Int, value: Int -> value }

    println(second(1, 2))

}
```

## 代码块 6

```kotlin
7
10
Hello, Runoob
结果是 正数
2
```

## 代码块 7

```kotlin
// 接收函数作为参数

fun calculate(a: Int, b: Int, operation: (Int, Int) -> Int): Int {

    return operation(a, b)

}


// 返回一个函数：返回类型是 (Int) -> Int

fun multiplier(factor: Int): (Int) -> Int {

    return { value -> value * factor }

}


fun main() {

    // 尾随 Lambda 写法：Lambda 写在括号外面

    println(calculate(6, 3) { a, b -> a + b })

    println(calculate(6, 3) { a, b -> a * b })


    // 先拿到函数，再调用

    val triple = multiplier(3)

    println(triple(5))


    // 直接调用返回的函数

    println(multiplier(10)(4))

}
```

## 代码块 8

```kotlin
9
18
15
40
```

## 代码块 9

```kotlin
fun main() {

    val sites = listOf("runoob", "RUNOOB", "java", "kotlin")


    // forEach：对每个元素执行一段代码，返回 Unit

    sites.forEach { println(it) }


    println("---")


    // filter：保留让 Lambda 返回 true 的元素，得到新列表

    val upper = sites.filter { it == it.uppercase() }

    println(upper)


    // map：把每个元素转换成另一个值，得到新列表

    val lengths = sites.map { it.length }

    println(lengths)


    // 链式调用：先过滤再转换

    val result = sites

        .filter { it.startsWith("r", ignoreCase = true) }

        .map { it.uppercase() }

    println(result)

}
```

## 代码块 10

```kotlin
runoob
RUNOOB
java
kotlin
---
[RUNOOB]
[6, 6, 4, 6]
[RUNOOB, RUNOOB]
```

## 代码块 11

```kotlin
fun main() {

    val sites = listOf("Runoob", "www.runoob.com")


    // forEachIndexed 的 Lambda 接收 (index, value)

    sites.forEachIndexed { index, value ->

        println("$index -> $value")

    }


    // Map 的 forEach 可以直接解构出键和值

    val info = mapOf("name" to "Runoob", "site" to "www.runoob.com")

    info.forEach { (key, value) ->

        println("$key = $value")

    }

}
```

## 代码块 12

```kotlin
0 -> Runoob
1 -> www.runoob.com
name = Runoob
site = www.runoob.com
```

## 代码块 13

```kotlin
fun main() {

    var counter = 0


    // 捕获外部的局部变量 counter，并且修改它

    val increment = { counter++ }


    increment()

    increment()

    println("counter = $counter")


    // 每次调用 makeCounter 都会创建一个独立的闭包

    val c1 = makeCounter()

    val c2 = makeCounter()


    c1()

    c1()

    c2()

    println("c1 = ${c1()}, c2 = ${c2()}")

}


// 返回一个函数，函数内部持有自己的 count

fun makeCounter(): () -> Int {

    var count = 0

    return {

        count++

        count      // 最后一个表达式的值作为返回值

    }

}
```

## 代码块 14

```kotlin
counter = 2
c1 = 3, c2 = 2
```

## 代码块 15

```kotlin
fun main() {

    // 匿名函数：有参数类型和返回类型，用 fun 开头

    val sum = fun(a: Int, b: Int): Int {

        return a + b        // 从匿名函数自身返回

    }

    println(sum(2, 3))


    // 匿名函数也可以用表达式体

    val square = fun(x: Int) = x * x

    println(square(6))


    // 传给高阶函数时，匿名函数里的 return 不会从 main 返回

    listOf(1, 2, 3, 4).forEach(fun(value) {

        if (value == 3) return   // 只结束这一次匿名函数调用

        println(value)

    })

    println("结束")

}
```

## 代码块 16

```kotlin
5
36
1
2
4
结束
```

## 代码块 17

```kotlin
// 顶层函数

fun isEven(value: Int) = value % 2 == 0


class Site(val name: String) {

    fun hello() = "你好，$name"

}


fun main() {

    val numbers = listOf(1, 2, 3, 4)


    // ::isEven 等价于 { value -> isEven(value) }

    println(numbers.filter(::isEven))


    val site = Site("Runoob")


    // 绑定引用：已经绑定到 site 实例，调用时不用再传接收者

    val bound = site::hello

    println(bound())


    // 未绑定引用：调用时需要把接收者作为第一个参数传入

    val unbound: (Site) -> String = Site::hello

    println(unbound(site))

}
```

## 代码块 18

```kotlin
[2, 4]
你好，Runoob
你好，Runoob
```

## 代码块 19

```kotlin
class Site(val name: String, val url: String)


fun main() {

    // 构造器引用 ::Site 相当于一个 (String, String) -> Site 的函数

    val create: (String, String) -> Site = ::Site

    val runoob = create("Runoob", "www.runoob.com")

    println("${runoob.name} - ${runoob.url}")


    // 在需要函数的地方直接使用构造器引用

    val pairs = listOf("Runoob" to "www.runoob.com", "RUNOOB" to "kotlin.runoob.com")

    val sites = pairs.map { (name, url) -> create(name, url) }

    println(sites.map { it.name })

}
```

## 代码块 20

```kotlin
Runoob - www.runoob.com
[Runoob, RUNOOB]
```

## 代码块 21

```kotlin
// Kotlin 的函数式接口：用 fun interface 声明，Kotlin 1.4 起稳定

fun interface StringChecker {

    fun check(value: String): Boolean

}


fun main() {

    // Lambda 自动转换为函数式接口的实例

    val notEmpty = StringChecker { it.isNotEmpty() }

    println(notEmpty.check("Runoob"))

    println(notEmpty.check(""))


    // 与 Java 函数式接口互操作：Runnable 只有一个抽象方法 run()

    val task = Runnable { println("在 Java 线程接口里运行 RUNOOB") }

    task.run()

}
```

## 代码块 22

```kotlin
true
false
在 Java 线程接口里运行 RUNOOB
```
