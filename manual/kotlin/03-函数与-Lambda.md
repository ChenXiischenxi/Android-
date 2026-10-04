# 函数与 Lambda

> 本章归并自 4 页教程代码块，来源见各节。

## Kotlin 函数

> 来源: https://www.runoob.com/kotlin/kotlin-function.html

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

```kotlin
3
2
2 + 3 = 5
```

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

```kotlin
8
16
负数
零
正数
```

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

```kotlin
欢迎 Runoob 访问 www.runoob.com
欢迎 RUNOOB 访问 www.runoob.com
欢迎 Runoob 访问 kotlin.runoob.com
```

```kotlin
// value 有默认值，却写在 unit 前面

fun format(value: Int = 0, unit: String): String = "$value$unit"


fun main() {

    // 不能写 format("px")，那样会把字符串传给 value 导致类型不匹配

    println(format(unit = "px"))

    println(format(12, "px"))

}
```

```kotlin
0px
12px
```

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

```kotlin
Runoob -> www.runoob.com:80
RUNOOB -> www.runoob.com:443
```

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

```kotlin
6
0
100
300
```

```kotlin
fun total(vararg numbers: Int): Int = numbers.sum()


fun main() {

    val list = listOf(1, 2, 3)


    // 错误写法：total(*list) 编译不通过

    // 正确做法是先转成数组再展开

    println(total(*list.toIntArray()))

}
```

```kotlin
6
```

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

```kotlin
Hello, Runoob!
RUNOOB
RUNOOB
kotlin.Unit
```

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

```kotlin
计算 5 的阶乘
120
```

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

```kotlin
6
120
```

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

```kotlin
我是顶层函数
站点：Runoob
站点：Runoob / 我是顶层函数
```

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

```kotlin
整数：42
小数：3.14
RUNOOB
runoob
```

```kotlin
// 错误示例：只有返回类型不同，编译不通过

// fun value(): Int = 1

// fun value(): String = "1"
```

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

```kotlin
Runoob 托管在 www.runoob.com
Runoob 托管在 www.runoob.com
true
```

## Kotlin Lambda 高阶函数

> 来源: https://www.runoob.com/kotlin/kotlin-lambda.html

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

```kotlin
3
你好，Runoob
RUNOOB
42
```

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

```kotlin
RunRun
RUNOOBRUNOOB
```

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

```kotlin
7
10
Hello, Runoob
结果是 正数
2
```

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

```kotlin
9
18
15
40
```

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

```kotlin
0 -> Runoob
1 -> www.runoob.com
name = Runoob
site = www.runoob.com
```

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

```kotlin
counter = 2
c1 = 3, c2 = 2
```

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

```kotlin
5
36
1
2
4
结束
```

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

```kotlin
[2, 4]
你好，Runoob
你好，Runoob
```

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

```kotlin
Runoob - www.runoob.com
[Runoob, RUNOOB]
```

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

```kotlin
true
false
在 Java 线程接口里运行 RUNOOB
```

## Kotlin 内联函数与 reified

> 来源: https://www.runoob.com/kotlin/kotlin-inline-function.html

```kotlin
// 文件路径：InlineBasic.kt


// 普通高阶函数：Lambda 会被编译成一个函数对象

fun runTask(action: () -> Unit) {

    action()

}


// 内联函数：编译器把函数体和 Lambda 体复制到调用处

inline fun runTaskInline(action: () -> Unit) {

    action()

}


fun main() {

    runTask { println("普通调用：RUNOOB") }

    runTaskInline { println("内联调用：RUNOOB") }

}
```

```kotlin
普通调用：RUNOOB
内联调用：RUNOOB
```

```kotlin
// 给 List 增加一个内联的遍历扩展

inline fun <T> List<T>.forEachRunoob(action: (T) -> Unit) {

    for (element in this) {

        action(element)      // 内联后这里直接展开成 Lambda 的代码

    }

}


fun main() {

    val sites = listOf("Runoob", "www.runoob.com", "RUNOOB")


    sites.forEachRunoob {

        println(it)

    }

}
```

```kotlin
Runoob
www.runoob.com
RUNOOB
```

```kotlin
inline fun <T> List<T>.forEachRunoob(action: (T) -> Unit) {

    for (element in this) {

        action(element)

    }

}


fun main() {

    listOf(1, 2, 3, 4, 5).forEachRunoob {

        if (it == 3) return          // 非局部返回：直接从 main 返回

        println(it)

    }

    println("这一行不会执行")

}
```

```kotlin
1
2
```

```kotlin
// 非内联函数：下面的写法会编译失败

fun runTask(action: () -> Unit) {

    action()

}


fun main() {

    runTask {

        // 编译错误：'return' is not allowed here

        // return

        println("只能正常返回，不能跳出 main")

    }

}
```

```kotlin
// onFinish 需要当作值使用，所以标记为 noinline；action 保持内联

inline fun runTask(noinline onFinish: () -> Unit, action: () -> Unit) {

    action()


    // noinline 的 Lambda 可以赋给变量，也可以再传给其他函数

    val handler: () -> Unit = onFinish

    handler()

}


fun main() {

    runTask(

        onFinish = { println("任务结束：RUNOOB") },

        action = { println("任务执行：www.runoob.com") }

    )

}
```

```kotlin
任务执行：www.runoob.com
任务结束：RUNOOB
```

```kotlin
// crossinline：block 仍然内联，但不允许非局部返回

inline fun runCrossInline(crossinline block: () -> Unit) {

    // block 被放进 Runnable 的 Lambda 里，属于另一个执行上下文

    val task = Runnable { block() }

    task.run()

}


fun main() {

    runCrossInline {

        println("crossinline 中的代码：RUNOOB")

        // 编译错误：'return' is not allowed here

        // return

    }

}
```

```kotlin
crossinline 中的代码：RUNOOB
```

```kotlin
// reified 必须搭配 inline 使用

inline fun <reified T> Any?.isInstanceOf(): Boolean = this is T


// 运行时获取类型名

inline fun <reified T> typeName(): String = T::class.simpleName ?: "未知类型"


class Site(val name: String)


fun main() {

    val value: Any = "RUNOOB"


    println(value.isInstanceOf<String>())

    println(value.isInstanceOf<Int>())


    println(typeName<String>())

    println(typeName<Int>())

    println(typeName<Site>())

}
```

```kotlin
true
false
String
Int
Site
```

```kotlin
inline fun <reified T> List<*>.filterIsInstanceRunoob(): List<T> {

    val result = mutableListOf<T>()

    for (element in this) {

        if (element is T) {      // 因为 reified，这里才能对 T 做类型判断

            result.add(element)

        }

    }

    return result

}


fun main() {

    val mixed: List<Any> = listOf(1, "Runoob", 2, "RUNOOB", 3.14)


    val strings = mixed.filterIsInstanceRunoob<String>()

    println(strings)

}
```

```kotlin
[Runoob, RUNOOB]
```

```kotlin
class SiteValidator {

    // 被 public 内联函数调用的 internal 成员，需要 @PublishedApi

    @PublishedApi

    internal fun checkName(name: String): Boolean = name.isNotEmpty()


    inline fun validate(name: String): Boolean = checkName(name)

}


fun main() {

    val validator = SiteValidator()


    println(validator.validate("Runoob"))

    println(validator.validate(""))

}
```

```kotlin
true
false
```

## Kotlin 作用域函数

> 来源: https://www.runoob.com/kotlin/kotlin-scope-functions.html

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

```kotlin
站点：www.runoob.com
长度：14
空对象兜底长度：0
```

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

```kotlin
RUNOOB - www.runoob.com
```

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

```kotlin
RUNOOB -> www.runoob.com
对象本身也被修改：RUNOOB
```

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

```kotlin
计算 10 + 20
结果：30
```

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

```kotlin
是否成功：false
是否失败：true
异常类型：NumberFormatException
安全取值：null
兜底取值：0
onFailure 收到：NumberFormatException
onSuccess 收到：100
```

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

```kotlin
Runoob - www.runoob.com
builder 也被修改：Runoob - www.runoob.com
```

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

```kotlin
Site(name=RUNOOB, url=www.runoob.com, visits=100)
类型仍是 Site：Site
```

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

```kotlin
创建完成，元素个数：2
[Runoob, RUNOOB, www.runoob.com]
```

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

```kotlin
runoob
RUNOOB
```

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

```kotlin
[RUNOOB, KOTLIN]
[runoob], [kotlin]
```

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

```kotlin
执行了：RUNOOB
also 也能配合安全调用：RUNOOB
```
