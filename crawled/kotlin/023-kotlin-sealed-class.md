# Kotlin 数据类与密封类

> 来源: https://www.runoob.com/kotlin/kotlin-sealed-class.html

## 代码块 1

```kotlin
// 文件：RunoobResult.kt

sealed class RunoobResult


// 子类与密封类写在同一个文件中

data class Success(val data: String) : RunoobResult()

data class Failure(val message: String) : RunoobResult()

object Loading : RunoobResult()


fun main() {

    val result: RunoobResult = Success("www.runoob.com")

    println(result)


    // RunoobResult()   // 编译错误：密封类不能直接实例化

}
```

## 代码块 2

```kotlin
Success(data=www.runoob.com)
```

## 代码块 3

```kotlin
// 文件：RunoobResult.kt


// 推荐写法：子类与密封类在同一个文件，平级声明，不必嵌套

sealed class RunoobResult


class Success(val data: String) : RunoobResult()

class Failure(val message: String) : RunoobResult()


// 下面这种「必须内嵌」的写法是 Kotlin 1.0 的旧限制，现在不再需要

sealed class OldStyleResult {

    class Success(val data: String) : OldStyleResult()

    class Failure(val message: String) : OldStyleResult()

}


fun main() {

    val a: RunoobResult = Success("runoob")

    val b: OldStyleResult = OldStyleResult.Success("RUNOOB")

    println(a.javaClass.simpleName)

    println(b.javaClass.simpleName)

}
```

## 代码块 4

```kotlin
Success
Success
```

## 代码块 5

```kotlin
// 文件：RunoobEvent.kt

// Kotlin 1.4 起，接口也可以声明为 sealed

sealed interface RunoobEvent


data class Click(val x: Int, val y: Int) : RunoobEvent

data class Scroll(val delta: Int) : RunoobEvent

data object Refresh : RunoobEvent   // data object 需要 Kotlin 1.9 起


fun handle(event: RunoobEvent): String = when (event) {

    is Click -> "点击坐标：(${event.x}, ${event.y})"

    is Scroll -> "滚动：${event.delta}"

    Refresh -> "刷新"

}


fun main() {

    println(handle(Click(10, 20)))

    println(handle(Scroll(-5)))

    println(handle(Refresh))

}
```

## 代码块 6

```kotlin
点击坐标：(10, 20)
滚动：-5
刷新
```

## 代码块 7

```kotlin
sealed interface RunoobClickable

sealed interface RunoobHoverable


// 一个类可以同时实现多个密封接口

class RunoobButton : RunoobClickable, RunoobHoverable


fun main() {

    val button = RunoobButton()

    println(button is RunoobClickable)

    println(button is RunoobHoverable)

}
```

## 代码块 8

```kotlin
true
true
```

## 代码块 9

```kotlin
sealed class RunoobState {

    object Idle : RunoobState()

    object Running : RunoobState()

    data class Error(val code: Int) : RunoobState()

}


// 作为表达式：必须覆盖所有分支，漏掉任何一个都编译不通过

fun label(state: RunoobState): String = when (state) {

    RunoobState.Idle -> "空闲"

    RunoobState.Running -> "运行中"

    is RunoobState.Error -> "错误码 ${state.code}"

}


fun main() {

    println(label(RunoobState.Idle))

    println(label(RunoobState.Running))

    println(label(RunoobState.Error(404)))

}
```

## 代码块 10

```kotlin
空闲
运行中
错误码 404
```

## 代码块 11

```kotlin
// 枚举：所有常量共享同一组属性，无法表达「每个分支携带不同数据」

enum class RunoobStatus(val code: Int) {

    OK(200), NOT_FOUND(404), TIMEOUT(0)

}


// 密封类：每个子类可以带自己的数据

sealed class RunoobResponse {

    data class Ok(val body: String) : RunoobResponse()

    data class NotFound(val path: String) : RunoobResponse()

    data object Timeout : RunoobResponse()

}


fun describe(response: RunoobResponse): String = when (response) {

    is RunoobResponse.Ok -> "返回内容：${response.body}"

    is RunoobResponse.NotFound -> "找不到路径：${response.path}"

    RunoobResponse.Timeout -> "请求超时"

}


fun main() {

    println(RunoobStatus.OK.code)

    println(describe(RunoobResponse.Ok("RUNOOB")))

    println(describe(RunoobResponse.NotFound("/runoob")))

    println(describe(RunoobResponse.Timeout))

}
```

## 代码块 12

```kotlin
200
返回内容：RUNOOB
找不到路径：/runoob
请求超时
```

## 代码块 13

```kotlin
sealed class UiOp {
    object Show: UiOp()
    object Hide: UiOp()
}
fun execute(view: View, op: UiOp) = when (op) {
    UiOp.Show -> view.visibility = View.VISIBLE
    UiOp.Hide -> view.visibility = View.GONE
}
```

## 代码块 14

```kotlin
sealed class UiOp {
    object Show: UiOp()
    object Hide: UiOp()
    class TranslateX(val px: Float): UiOp()
    class TranslateY(val px: Float): UiOp()
}


fun execute(view: View, op: UiOp) = when (op) {
    UiOp.Show -> view.visibility = View.VISIBLE
    UiOp.Hide -> view.visibility = View.GONE
    is UiOp.TranslateX -> view.translationX = op.px // 这个 when 语句分支不仅告诉 view 要水平移动，还告诉 view 需要移动多少距离，这是枚举等 Java 传统思想不容易实现的
    is UiOp.TranslateY -> view.translationY = op.px
}
```

## 代码块 15

```kotlin
// 先封装一个UI操作列表
class Ui(val uiOps: List = emptyList()) {
    operator fun plus(uiOp: UiOp) = Ui(uiOps + uiOp)
}

// 定义一组操作
val ui = Ui() +
        UiOp.Show +
        UiOp.TranslateX(20f) +
        UiOp.TranslateY(40f) +
        UiOp.Hide
// 定义调用的函数
fun run(view: View, ui: Ui) {
    ui.uiOps.forEach { execute(view, it) }
}

run(view, ui) // 最终调用
```
