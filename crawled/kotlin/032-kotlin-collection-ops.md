# Kotlin 集合操作

> 来源: https://www.runoob.com/kotlin/kotlin-collection-ops.html

## 代码块 1

```kotlin
fun main() {

    val numbers = listOf(1, 2, 3, 4, 5, 6)


    // filter：只保留偶数

    val evens = numbers.filter { it % 2 == 0 }

    println("偶数：$evens")


    // filterNot：保留不满足条件的元素，等价于 filter { !... }

    val odds = numbers.filterNot { it % 2 == 0 }

    println("奇数：$odds")


    // filterNotNull：去掉 null，结果类型自动变成 List<String>

    val raw = listOf("runoob", null, "RUNOOB", null, "kotlin")

    val clean: List<String> = raw.filterNotNull()

    println("去空后：$clean")


    // partition：一次得到两组结果，用解构声明分别接收

    val (big, small) = numbers.partition { it > 3 }

    println("大于 3：$big")

    println("小于等于 3：$small")

}
```

## 代码块 2

```kotlin
偶数：[2, 4, 6]
奇数：[1, 3, 5]
去空后：[runoob, RUNOOB, kotlin]
大于 3：[4, 5, 6]
小于等于 3：[1, 2, 3]
```

## 代码块 3

```kotlin
fun main() {

    val words = listOf("runoob", "kotlin")


    // map：把每个字符串变成它的长度

    println(words.map { it.length })


    // map：把每个字符串变成大写

    println(words.map { it.uppercase() })


    // mapNotNull：转换失败时返回 null，这些 null 会被自动丢掉

    val mixed = listOf("1", "x", "3")

    println(mixed.mapNotNull { it.toIntOrNull() })


    // mapIndexed：同时拿到下标和元素

    println(words.mapIndexed { index, word -> "$index:$word" })


    val nested = listOf(listOf(1, 2), listOf(3, 4))


    // flatten：把「列表的列表」拍平一层

    println(nested.flatten())


    // flatMap：先变换再拍平，一步完成

    println(nested.flatMap { inner -> inner.map { it * 10 } })

}
```

## 代码块 4

```kotlin
[6, 6]
[RUNOOB, KOTLIN]
[1, 3]
[0:runoob, 1:kotlin]
[1, 2, 3, 4]
[10, 20, 30, 40]
```

## 代码块 5

```kotlin
fun main() {

    val numbers = listOf(1, 2, 3, 4)


    // fold：累加器从初始值 10 开始，依次加上每个元素

    println("fold：${numbers.fold(10) { acc, n -> acc + n }}")


    // reduce：没有初始值，用第一个元素 1 作起点连乘

    println("reduce：${numbers.reduce { acc, n -> acc * n }}")


    println("sum：${numbers.sum()}")


    // sumOf：先对每个元素取长度，再求和

    println("sumOf 长度：${listOf("runoob", "kotlin").sumOf { it.length }}")


    println("average：${numbers.average()}")

    println("max：${numbers.maxOrNull()}")

    println("min：${numbers.minOrNull()}")


    // 空集合上 fold 安全，maxOrNull 返回 null，而 reduce、average 会抛异常

    val empty = emptyList<Int>()

    println("空集合 fold：${empty.fold(0) { acc, n -> acc + n }}")

    println("空集合 max：${empty.maxOrNull()}")

}
```

## 代码块 6

```kotlin
fold：20
reduce：24
sum：10
sumOf 长度：12
average：2.5
max：4
min：1
空集合 fold：0
空集合 max：null
```

## 代码块 7

```kotlin
// 用于排序的数据类，定义在顶层

data class Site(val name: String, val age: Int)


fun main() {

    val sites = listOf(

        Site("runoob", 12),

        Site("kotlin", 9),

        Site("RUNOOB", 20)

    )


    // sortedBy：按选择器升序

    println(sites.sortedBy { it.age }.map { it.name })


    // sortedByDescending：按选择器降序

    println(sites.sortedByDescending { it.age }.map { it.name })


    // sortedWith：自定义比较器，先按名字再按年龄

    println(sites.sortedWith(compareBy<Site> { it.name }.thenBy { it.age }).map { it.name })


    // sorted：对元素自身做自然排序，仅适用于 Comparable 类型

    println(listOf(3, 1, 4).sorted())


    // reversed：只是把顺序倒过来，不做任何比较

    println(listOf(3, 1, 4).reversed())


    // shuffled：随机打乱，元素集合不变，每次运行顺序都可能不同

    val shuffled = listOf(1, 2, 3, 4, 5).shuffled()

    println("shuffled 后排序还原：${shuffled.sorted()}")

}
```

## 代码块 8

```kotlin
[kotlin, runoob, RUNOOB]
[RUNOOB, runoob, kotlin]
[RUNOOB, kotlin, runoob]
[1, 3, 4]
[4, 1, 3]
shuffled 后排序还原：[1, 2, 3, 4, 5]
```

## 代码块 9

```kotlin
// 用于分组的数据类，定义在顶层

data class Site(val name: String, val country: String)


fun main() {

    val sites = listOf(

        Site("runoob", "CN"),

        Site("kotlin", "US"),

        Site("RUNOOB", "CN")

    )


    // groupBy：键是 country，值是该国家的站点列表

    val byCountry = sites.groupBy { it.country }

    println(byCountry.mapValues { (_, list) -> list.map { it.name } })


    // associateBy：把 name 当键，直接拿到 Site 对象

    println(sites.associateBy { it.name }.keys)


    val numbers = listOf(1, 2, 3, 4, 5)


    // chunked：每 2 个一组，最后不足 2 个也保留

    println(numbers.chunked(2))


    // windowed：长度 3 的滑动窗口，默认 step = 1

    println(numbers.windowed(3))


    // step = 2 且允许不足长度的尾窗

    println(numbers.windowed(3, step = 2, partialWindows = true))

}
```

## 代码块 10

```kotlin
{CN=[runoob, RUNOOB], US=[kotlin]}
[runoob, kotlin, RUNOOB]
[[1, 2], [3, 4], [5]]
[[1, 2, 3], [2, 3, 4], [3, 4, 5]]
[[1, 2, 3], [3, 4, 5], [5]]
```

## 代码块 11

```kotlin
fun main() {

    val numbers = listOf(2, 4, 6, 7, 8)


    // find：第一个奇数，找不到返回 null

    println(numbers.find { it % 2 == 1 })

    println(numbers.find { it > 100 })


    println(numbers.first())

    println(numbers.first { it > 5 })

    println(numbers.last())

    println(numbers.last { it < 6 })


    // any / all / none 都是短路求值，一旦能确定结果就停止遍历

    println(numbers.any { it > 7 })

    println(numbers.all { it % 2 == 0 })

    println(numbers.none { it < 0 })

    println(numbers.count { it % 2 == 0 })

}
```

## 代码块 12

```kotlin
7
null
2
6
8
4
true
false
true
4
```

## 代码块 13

```kotlin
fun main() {

    val numbers = listOf(2, 4, 6, 7, 8)


    // 默认分隔符是 ", "

    println(numbers.joinToString())


    // 自定义前后缀和分隔符

    println(numbers.joinToString(separator = "-", prefix = "[", postfix = "]"))


    // 只拼前 3 个，剩下的用省略号表示

    println(numbers.joinToString(limit = 3, truncated = "..."))


    // transform：拼接前先把每个元素加工成想要的样子

    println(numbers.joinToString { "n=$it" })

}
```

## 代码块 14

```kotlin
2, 4, 6, 7, 8
[2-4-6-7-8]
2, 4, 6, ...
n=2, n=4, n=6, n=7, n=8
```
