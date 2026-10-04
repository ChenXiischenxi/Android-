# Kotlin 循环控制

> 来源: https://www.runoob.com/kotlin/kotlin-loop-control.html

## 代码块 1

```kotlin
// 文件路径：LoopFor.kt

fun main() {

    // listOf 创建一个只读列表

    val sites = listOf("Runoob", "www.runoob.com", "RUNOOB")


    // 依次取出每个元素，变量 site 的类型自动推断为 String

    for (site in sites) {

        println(site)

    }

}
```

## 代码块 2

```kotlin
Runoob
www.runoob.com
RUNOOB
```

## 代码块 3

```kotlin
fun main() {

    // intArrayOf 创建 Int 数组，避免装箱开销

    val numbers = intArrayOf(10, 20, 30)


    for (number in numbers) {

        println("当前元素：$number")

    }

}
```

## 代码块 4

```kotlin
当前元素：10
当前元素：20
当前元素：30
```

## 代码块 5

```kotlin
fun main() {

    // 闭区间 1..3：包含左右两端

    for (i in 1..3) print("$i")

    println("  => 1..3")


    // until：包含左端，不包含右端

    for (i in 1 until 3) print("$i")

    println("  => 1 until 3")


    // downTo：从大到小递减

    for (i in 3 downTo 1) print("$i")

    println("  => 3 downTo 1")


    // step：指定步长，步长必须为正数

    for (i in 1..6 step 2) print("$i")

    println("  => 1..6 step 2")


    // ..< 半开区间，Kotlin 1.9 起稳定

    for (i in 1..<3) print("$i")

    println("  => 半开区间")

}
```

## 代码块 6

```kotlin
123  => 1..3
12  => 1 until 3
321  => 3 downTo 1
135  => 1..6 step 2
12  => 半开区间
```

## 代码块 7

```kotlin
fun main() {

    val sites = listOf("Runoob", "www.runoob.com", "RUNOOB")


    // indices 返回下标区间 0..2，适合需要按下标再取值的场景

    for (i in sites.indices) {

        println("下标 $i -> ${sites[i]}")

    }


    println("---")


    // withIndex() 同时给出下标和值，(index, value) 是解构声明

    for ((index, value) in sites.withIndex()) {

        println("$index: $value")

    }

}
```

## 代码块 8

```kotlin
下标 0 -> Runoob
下标 1 -> www.runoob.com
下标 2 -> RUNOOB
---
0: Runoob
1: www.runoob.com
2: RUNOOB
```

## 代码块 9

```kotlin
fun main() {

    // mapOf 返回保持插入顺序的 Map

    val info = mapOf("name" to "Runoob", "site" to "www.runoob.com")


    for ((key, value) in info) {

        println("$key = $value")

    }

}
```

## 代码块 10

```kotlin
name = Runoob
site = www.runoob.com
```

## 代码块 11

```kotlin
fun main() {

    var count = 3


    while (count > 0) {

        println("倒计时 $count")

        count--            // 必须改变循环变量，否则会死循环

    }


    println("循环结束")

}
```

## 代码块 12

```kotlin
倒计时 3
倒计时 2
倒计时 1
循环结束
```

## 代码块 13

```kotlin
fun main() {

    var count = 0


    while (count > 0) {

        println("这一行永远不会输出")

        count--

    }


    println("循环结束，count = $count")

}
```

## 代码块 14

```kotlin
循环结束，count = 0
```

## 代码块 15

```kotlin
fun main() {

    var count = 0


    do {

        println("循环体执行：count = $count")

        count++

    } while (count < 0)    // 条件一开始就为 false，但循环体已经执行过一次


    println("循环结束")

}
```

## 代码块 16

```kotlin
循环体执行：count = 0
循环结束
```

## 代码块 17

```kotlin
fun main() {

    for (i in 1..10) {

        if (i == 3) continue   // i 为 3 时跳过，不执行下面的 println

        if (i > 5) break       // i 为 6 时结束整个循环

        println(i)

    }

}
```

## 代码块 18

```kotlin
1
2
4
5
```

## 代码块 19

```kotlin
fun main() {

    // loop@ 是外层循环的标签

    loop@ for (i in 1..3) {

        for (j in 1..3) {

            if (j == 2) continue@loop   // 跳过外层循环的本次迭代

            if (i == 3) break@loop      // 直接结束外层循环

            println("i = $i, j = $j")

        }

    }

    println("循环结束")

}
```

## 代码块 20

```kotlin
i = 1, j = 1
i = 2, j = 1
循环结束
```

## 代码块 21

```kotlin
fun main() {

    // 给 lambda 起一个显式标签 check

    val check = check@{ value: Int ->

        if (value < 0) return@check "负数"

        "非负数"

    }


    println(check(5))

    println(check(-1))

}
```

## 代码块 22

```kotlin
非负数
负数
```

## 代码块 23

```kotlin
fun main() {

    val numbers = listOf(1, null, 3, null, 5)


    for (number in numbers) {

        // run 是内联函数，它 lambda 里的 continue 作用于外层的 for 循环

        val value = number ?: run {

            println("遇到 null，跳过本次循环")

            continue

        }

        println("处理数字：$value")

    }

    println("循环结束")

}
```

## 代码块 24

```kotlin
处理数字：1
遇到 null，跳过本次循环
处理数字：3
遇到 null，跳过本次循环
处理数字：5
循环结束
```

## 代码块 25

```kotlin
fun main() {

    val numbers = listOf(1, 2, 3, 4, 5)


    for (number in numbers) {

        run {

            if (number == 4) break   // 非局部 break：结束外层的 for 循环

        }

        println("当前数字：$number")

    }

    println("循环结束")

}
```

## 代码块 26

```kotlin
当前数字：1
当前数字：2
当前数字：3
循环结束
```

## 代码块 27

```kotlin
fun main() {

    val numbers = listOf(1, 2, 0, 4)


    // return@forEach 只结束本次 lambda 调用，等价于跳过 0

    numbers.forEach {

        if (it == 0) return@forEach

        println("forEach：$it")

    }


    println("---")


    // 用 for 循环加 continue 也能达到同样效果

    for (number in numbers) {

        if (number == 0) continue

        println("for：$number")

    }

}
```

## 代码块 28

```kotlin
forEach：1
forEach：2
forEach：4
---
for：1
for：2
for：4
```

## 代码块 29

```kotlin
for (i in 1..4) print(i) // 打印结果为: "1234"
```

## 代码块 30

```kotlin
for (i in 4 downTo 1) print(i) // 打印结果为: "4321"
```

## 代码块 31

```kotlin
for (i in 1..4 step 2) print(i) // 打印结果为: "13"

for (i in 4 downTo 1 step 2) print(i) // 打印结果为: "42"
```

## 代码块 32

```kotlin
for (i in 1 until 10) { // i in [1, 10), 不包含 10
     println(i)
}
```
