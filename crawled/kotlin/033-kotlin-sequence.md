# Kotlin 序列

> 来源: https://www.runoob.com/kotlin/kotlin-sequence.html

## 代码块 1

```kotlin
fun main() {

    // 一个普通的列表

    val list = listOf("runoob", "RUNOOB", "kotlin")


    // asSequence() 把列表包装成序列，此时不会做任何计算

    val sequence = list.asSequence()


    // 只有调用末端操作时，元素才会真正被处理

    println(sequence.first())

    println(sequence.count())

}
```

## 代码块 2

```kotlin
runoob
3
```

## 代码块 3

```kotlin
fun main() {

    val data = (1..10).toList()


    var listSteps = 0

    // 集合：filter 先把 10 个元素全部走一遍，map 再把得到的 5 个偶数走一遍

    val listResult = data

        .filter { listSteps++; it % 2 == 0 }

        .map { listSteps++; it * it }

        .first { it > 20 }


    var seqSteps = 0

    // 序列：每个元素依次穿过 filter 和 map，找到第一个满足条件的元素就立刻停止

    val seqResult = data.asSequence()

        .filter { seqSteps++; it % 2 == 0 }

        .map { seqSteps++; it * it }

        .first { it > 20 }


    println("集合结果：$listResult，lambda 执行次数：$listSteps")

    println("序列结果：$seqResult，lambda 执行次数：$seqSteps")

}
```

## 代码块 4

```kotlin
集合结果：36，lambda 执行次数：15
序列结果：36，lambda 执行次数：9
```

## 代码块 5

```kotlin
fun main() {

    // 1. sequenceOf：元素已知时最直接

    println(sequenceOf("runoob", "RUNOOB", "kotlin").toList())


    // 2. generateSequence：种子 1，每次乘 2，这是一个无限序列

    val powers = generateSequence(1) { it * 2 }

    println(powers.take(5).toList())


    // 加上 takeWhile 就能在满足条件时停下来

    println(generateSequence(1) { it * 2 }.takeWhile { it <= 100 }.toList())


    // 3. sequence { }：用 yield 逐个产出，适合有状态的逻辑

    val fib = sequence {

        var a = 0

        var b = 1

        while (true) {          // 无限循环，靠外部 take 控制取多少

            yield(a)            // 产出一个值并暂停，等下次迭代再继续

            val next = a + b

            a = b

            b = next

        }

    }

    println(fib.take(8).toList())

}
```

## 代码块 6

```kotlin
[runoob, RUNOOB, kotlin]
[1, 2, 4, 8, 16]
[1, 2, 4, 8, 16, 32, 64]
[0, 1, 1, 2, 3, 5, 8, 13]
```

## 代码块 7

```kotlin
fun main() {

    // 这条链只是被"描述"出来，还没有任何元素被处理

    val pipeline = sequenceOf(1, 2, 3, 4, 5, 6)

        .filter { println("filter $it"); it % 2 == 0 }

        .map { println("map $it"); it * 10 }


    println("--- 到这里还没有输出 ---")


    // toList() 是末端操作，此时元素才逐个流过 filter 和 map

    val result = pipeline.toList()

    println(result)

}
```

## 代码块 8

```kotlin
--- 到这里还没有输出 ---
filter 1
filter 2
map 2
filter 3
filter 4
map 4
filter 5
filter 6
map 6
[20, 40, 60]
```

## 代码块 9

```kotlin
import kotlin.system.measureTimeMillis


fun main() {

    val data = (1..5_000_000).toList()


    // 集合：filter 和 map 各自生成一个约 167 万元素的中间列表

    val listTime = measureTimeMillis {

        data.filter { it % 3 == 0 }

            .map { it * 2 }

            .first { it > 1_000 }

    }


    // 序列：找到第一个满足条件的元素后立即停止，几乎不分配额外内存

    val seqTime = measureTimeMillis {

        data.asSequence()

            .filter { it % 3 == 0 }

            .map { it * 2 }

            .first { it > 1_000 }

    }


    println("集合耗时：${listTime}ms")

    println("序列耗时：${seqTime}ms")

}
```

## 代码块 10

```kotlin
集合耗时：96ms
序列耗时：2ms
```
