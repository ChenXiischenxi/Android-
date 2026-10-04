# Kotlin 内联函数与 reified

> 来源: https://www.runoob.com/kotlin/kotlin-inline-function.html

## 代码块 1

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

## 代码块 2

```kotlin
普通调用：RUNOOB
内联调用：RUNOOB
```

## 代码块 3

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

## 代码块 4

```kotlin
Runoob
www.runoob.com
RUNOOB
```

## 代码块 5

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

## 代码块 6

```kotlin
1
2
```

## 代码块 7

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

## 代码块 8

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

## 代码块 9

```kotlin
任务执行：www.runoob.com
任务结束：RUNOOB
```

## 代码块 10

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

## 代码块 11

```kotlin
crossinline 中的代码：RUNOOB
```

## 代码块 12

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

## 代码块 13

```kotlin
true
false
String
Int
Site
```

## 代码块 14

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

## 代码块 15

```kotlin
[Runoob, RUNOOB]
```

## 代码块 16

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

## 代码块 17

```kotlin
true
false
```
