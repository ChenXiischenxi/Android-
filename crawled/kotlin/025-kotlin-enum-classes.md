# Kotlin 枚举类

> 来源: https://www.runoob.com/kotlin/kotlin-enum-classes.html

## 代码块 1

```kotlin
enum class RunoobColor {

    RED, GREEN, BLUE

}


fun main() {

    val color = RunoobColor.RED

    println(color)                    // 直接打印就是常量名

    println(RunoobColor.RED.name)     // name 属性

    println(RunoobColor.RED.ordinal)  // ordinal 从 0 开始

}
```

## 代码块 2

```kotlin
RED
RED
0
```

## 代码块 3

```kotlin
// 主构造器带两个参数，每个常量各自传入不同的值

enum class RunoobColor(val rgb: Int, val hex: String) {

    RED(0xFF0000, "#FF0000"),

    GREEN(0x00FF00, "#00FF00"),

    BLUE(0x0000FF, "#0000FF")

}


fun main() {

    // entries 是 Kotlin 1.9 起推荐的遍历方式，后面会详细讲

    for (color in RunoobColor.entries) {

        println("${color.name} 的十进制值 ${color.rgb}，十六进制 ${color.hex}")

    }

}
```

## 代码块 4

```kotlin
RED 的十进制值 16711680，十六进制 #FF0000
GREEN 的十进制值 65280，十六进制 #00FF00
BLUE 的十进制值 255，十六进制 #0000FF
```

## 代码块 5

```kotlin
enum class RunoobState {

    WAITING {

        override fun signal(): RunoobState = RUNNING

        override fun describe(): String = "等待中"

    },

    RUNNING {

        override fun signal(): RunoobState = WAITING

        override fun describe(): String = "运行中"

    };   // 有成员时，常量列表要用分号结束


    // 抽象方法：每个常量都必须实现

    abstract fun signal(): RunoobState


    // 带默认实现的方法：常量可以选择重写

    open fun describe(): String = "未知状态"

}


fun main() {

    println(RunoobState.WAITING.describe())

    println(RunoobState.WAITING.signal().describe())

}
```

## 代码块 6

```kotlin
等待中
运行中
```

## 代码块 7

```kotlin
enum class RunoobLevel(val score: Int) {

    LOW(1), MID(5), HIGH(10);   // 分号把常量列表和成员分隔开


    // 普通成员函数

    fun isPass(): Boolean = score >= 5


    // 伴生对象也是成员，同样要写在分号之后

    companion object {

        fun fromScore(score: Int): RunoobLevel =

            entries.firstOrNull { it.score == score } ?: LOW

    }

}


fun main() {

    println(RunoobLevel.HIGH.isPass())

    println(RunoobLevel.LOW.isPass())

    println(RunoobLevel.fromScore(5))

}
```

## 代码块 8

```kotlin
true
false
MID
```

## 代码块 9

```kotlin
enum class RunoobColor { RED, GREEN, BLUE }


fun main() {

    // Kotlin 1.9 起推荐：entries 返回只读的 EnumEntries

    println(RunoobColor.entries.joinToString())

    println(RunoobColor.entries.size)

    println(RunoobColor.entries[1])


    // 遍历并格式化输出

    println(RunoobColor.entries.joinToString(" ") { "${it.ordinal}-${it.name}" })

}
```

## 代码块 10

```kotlin
RED, GREEN, BLUE
3
GREEN
0-RED 1-GREEN 2-BLUE
```

## 代码块 11

```kotlin
enum class RunoobColor { RED, GREEN, BLUE }


fun main() {

    // 旧写法：values() 每次调用都会创建一个新数组

    println(RunoobColor.values().joinToString())


    // 新写法（Kotlin 1.9 起）：entries 是只读列表视图，不分配数组

    println(RunoobColor.entries.joinToString())


    // 确实需要数组时，从 entries 转换

    val array: Array<RunoobColor> = RunoobColor.entries.toTypedArray()

    println(array.size)


    // Kotlin 1.9.20 起 enumValues() 已弃用，不要再使用

    // println(enumValues<RunoobColor>().joinToString())

}
```

## 代码块 12

```kotlin
RED, GREEN, BLUE
RED, GREEN, BLUE
3
```

## 代码块 13

```kotlin
enum class RunoobColor { RED, GREEN, BLUE }


fun main() {

    val color = RunoobColor.GREEN

    println(color.name)      // 常量名

    println(color.ordinal)   // 从 0 开始的位置索引


    for (item in RunoobColor.entries) {

        println("${item.ordinal} -> ${item.name}")

    }

}
```

## 代码块 14

```kotlin
GREEN
1
0 -> RED
1 -> GREEN
2 -> BLUE
```

## 代码块 15

```kotlin
enum class RunoobColor { RED, GREEN, BLUE }


fun main() {

    // valueOf：按名字取常量

    val red = RunoobColor.valueOf("RED")

    println(red == RunoobColor.RED)


    // enumValueOf：泛型版本，写法更通用

    val blue = enumValueOf<RunoobColor>("BLUE")

    println(blue.ordinal)


    // 安全查找：名字不存在时返回 null，避免抛异常

    val safe = RunoobColor.entries.firstOrNull { it.name == "PURPLE" }

    println(safe ?: "没有 PURPLE")

}
```

## 代码块 16

```kotlin
true
2
没有 PURPLE
```

## 代码块 17

```kotlin
enum class RunoobColor { RED, GREEN, BLUE }


// 覆盖了所有常量，作为表达式时不需要 else

fun hex(color: RunoobColor): String = when (color) {

    RunoobColor.RED -> "#FF0000"

    RunoobColor.GREEN -> "#00FF00"

    RunoobColor.BLUE -> "#0000FF"

}


fun main() {

    println(hex(RunoobColor.RED))

    println(hex(RunoobColor.BLUE))

}
```

## 代码块 18

```kotlin
#FF0000
#0000FF
```
