# Kotlin 数据类与解构

> 来源: https://www.runoob.com/kotlin/kotlin-data-class.html

## 代码块 1

```kotlin
// data 关键字写在 class 之前

data class RunoobSite(val name: String, val url: String, val age: Int)


fun main() {

    val site = RunoobSite("菜鸟教程", "www.runoob.com", 12)


    println(site)      // 自动生成的 toString()

    println(site.name) // 属性照常访问


    val same = RunoobSite("菜鸟教程", "www.runoob.com", 12)

    println(site == same)                              // 自动生成的 equals()

    println(site.hashCode() == same.hashCode())        // 自动生成的 hashCode()

}
```

## 代码块 2

```kotlin
RunoobSite(name=菜鸟教程, url=www.runoob.com, age=12)
菜鸟教程
true
true
```

## 代码块 3

```kotlin
// 正确：主构造器至少一个参数，且都是 val / var

data class RunoobA(val id: Int)


// 错误：主构造器没有参数

// data class RunoobB()   // Data class must have at least one primary constructor parameter


// 错误：参数没有 val / var，只是一个普通形参

// data class RunoobC(name: String)


// 错误：不能是 abstract / open / sealed / inner

// abstract data class RunoobD(val id: Int)

// open data class RunoobE(val id: Int)


fun main() {

    println(RunoobA(1))

}
```

## 代码块 4

```kotlin
RunoobA(id=1)
```

## 代码块 5

```kotlin
data class RunoobSite(val name: String, val url: String, val age: Int)


fun main() {

    val site = RunoobSite("菜鸟教程", "www.runoob.com", 12)


    // 只改 url，其余字段保持原值

    val mirror = site.copy(url = "m.runoob.com")

    println(mirror)


    // 一次改多个字段

    val renamed = site.copy(name = "RUNOOB 教程", age = 13)

    println(renamed)


    // 不传任何参数 = 浅拷贝一个新对象

    val same = site.copy()

    println(same == site)    // 属性相同，结构相等

    println(same === site)   // 但不是同一个对象

}
```

## 代码块 6

```kotlin
RunoobSite(name=菜鸟教程, url=m.runoob.com, age=12)
RunoobSite(name=RUNOOB 教程, url=www.runoob.com, age=13)
true
false
```

## 代码块 7

```kotlin
data class RunoobSite(val name: String, val url: String, val age: Int)


fun main() {

    val site = RunoobSite("菜鸟教程", "www.runoob.com", 12)


    // 按主构造器参数顺序解构

    val (name, url, age) = site

    println("名称：$name，网址：$url，年龄：$age")


    // 只关心其中一个字段，其余用下划线占位（Kotlin 1.1 起）

    val (_, siteUrl, _) = site

    println("只要网址：$siteUrl")


    // 遍历 Map 时同样使用解构

    val scores = mapOf("runoob" to 95, "RUNOOB" to 88)

    for ((key, value) in scores) {

        println("$key -> $value")

    }

}
```

## 代码块 8

```kotlin
名称：菜鸟教程，网址：www.runoob.com，年龄：12
只要网址：www.runoob.com
runoob -> 95
RUNOOB -> 88
```

## 代码块 9

```kotlin
class RunoobPoint(val x: Int, val y: Int) {

    // 手动声明 componentN，让普通类也支持解构

    operator fun component1() = x

    operator fun component2() = y

}


fun main() {

    val (x, y) = RunoobPoint(3, 4)

    println("x=$x, y=$y")

}
```

## 代码块 10

```kotlin
x=3, y=4
```

## 代码块 11

```kotlin
data class RunoobUser(val name: String) {

    var city: String = "北京"   // 类体属性，不参与 equals / hashCode

}


fun main() {

    val a = RunoobUser("runoob")

    val b = RunoobUser("runoob")

    a.city = "上海"

    b.city = "广州"


    println(a == b)            // 只比较 name，所以是 true

    println(a.city == b.city)  // 类体属性单独比较，false

}
```

## 代码块 12

```kotlin
true
false
```

## 代码块 13

```kotlin
fun main() {

    // to 是中缀函数，等价于 Pair("runoob", 95)

    val score: Pair<String, Int> = "runoob" to 95

    println(score.first)    // 第一个值

    println(score.second)   // 第二个值


    // 解构 Pair

    val (name, value) = score

    println("$name 的分数是 $value")


    // Triple 表示三个值

    val info = Triple("RUNOOB", "www.runoob.com", 2026)

    val (site, url, year) = info

    println("$site - $url - $year")


    // Pair 也是数据类，同样有 copy

    println(score.copy(second = 100))

}
```

## 代码块 14

```kotlin
runoob
95
runoob 的分数是 95
RUNOOB - www.runoob.com - 2026
(runoob, 100)
```

## 代码块 15

```kotlin
// Kotlin 1.9 起：data object 自动生成 toString / equals / hashCode

data object RunoobConfig {

    val siteName: String = "RUNOOB"

}


fun main() {

    println(RunoobConfig)                    // 输出对象名，而不是地址

    println(RunoobConfig == RunoobConfig)    // 单例，永远相等

    println(RunoobConfig.siteName)

}
```

## 代码块 16

```kotlin
RunoobConfig
true
RUNOOB
```

## 代码块 17

```kotlin
sealed interface RunoobState {

    data object Loading : RunoobState                        // 无数据的单例分支

    data object Empty : RunoobState                          // 无数据的单例分支

    data class Success(val data: String) : RunoobState       // 带数据的分支

}


fun describe(state: RunoobState): String = when (state) {

    RunoobState.Loading -> "加载中"

    RunoobState.Empty -> "暂无数据"

    is RunoobState.Success -> "成功：${state.data}"

}


fun main() {

    println(describe(RunoobState.Loading))

    println(describe(RunoobState.Empty))

    println(describe(RunoobState.Success("www.runoob.com")))

}
```

## 代码块 18

```kotlin
加载中
暂无数据
成功：www.runoob.com
```
