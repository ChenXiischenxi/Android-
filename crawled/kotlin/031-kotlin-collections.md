# Kotlin 集合

> 来源: https://www.runoob.com/kotlin/kotlin-collections.html

## 代码块 1

```kotlin
fun main() {

    val mutable = mutableListOf("Runoob", "RUNOOB")


    // 同一个对象，用只读接口引用它

    val readOnly: List<String> = mutable


    // readOnly.add("Kotlin")  // 编译错误：List 接口没有 add 方法


    // 通过可变引用依然可以修改

    mutable.add("Kotlin")


    // 只读引用看到的是同一个对象，因此也能看到变化

    println(readOnly)

}
```

## 代码块 2

```kotlin
[Runoob, RUNOOB, Kotlin]
```

## 代码块 3

```kotlin
fun main() {

    // 外层列表是只读的，但元素本身是 MutableList

    val users = listOf(mutableListOf("Runoob"))


    // users.add(...) 不行，但修改元素可以

    users[0].add("RUNOOB")


    println(users)

}
```

## 代码块 4

```kotlin
[[Runoob, RUNOOB]]
```

## 代码块 5

```kotlin
fun main() {

    val readOnly = listOf("Runoob", "RUNOOB", "Kotlin")

    val mutable = mutableListOf("Runoob", "RUNOOB")

    val arrayBacked = arrayListOf("Runoob", "RUNOOB")


    mutable.add("Kotlin")

    arrayBacked.add("Kotlin")


    println(readOnly)

    println(mutable)

    println(arrayBacked)


    // 下标访问与几个常用查询方法

    println(readOnly[0])

    println(readOnly.getOrNull(10))     // 越界返回 null，不抛异常

    println(readOnly.indexOf("Kotlin"))

    println(readOnly.contains("RUNOOB"))

}
```

## 代码块 6

```kotlin
[Runoob, RUNOOB, Kotlin]
[Runoob, RUNOOB, Kotlin]
[Runoob, RUNOOB, Kotlin]
Runoob
null
2
true
```

## 代码块 7

```kotlin
fun main() {

    // 重复的 "Runoob" 会被自动忽略

    val readOnly = setOf("Runoob", "RUNOOB", "Runoob")

    val mutable = mutableSetOf("Runoob", "RUNOOB")

    val hash = hashSetOf("Runoob", "RUNOOB")


    mutable.add("Kotlin")

    mutable.add("Runoob")   // 已存在，不会重复添加

    hash.add("Kotlin")


    println(readOnly)

    println(mutable)

    println(hash.sorted())  // HashSet 顺序不确定，排序后再输出

    println(readOnly.size)

    println("RUNOOB" in readOnly)

}
```

## 代码块 8

```kotlin
[Runoob, RUNOOB]
[Runoob, RUNOOB, Kotlin]
[Kotlin, RUNOOB, Runoob]
2
true
```

## 代码块 9

```kotlin
fun main() {

    // to 是中缀函数，用来构造键值对

    val readOnly = mapOf("Runoob" to 1, "RUNOOB" to 2)

    val mutable = mutableMapOf("Runoob" to 1)

    val hash = hashMapOf("Runoob" to 1)


    mutable["RUNOOB"] = 2

    hash["RUNOOB"] = 2


    println(readOnly)

    println(mutable)

    println(readOnly["Runoob"])

    println(readOnly["Kotlin"])                 // 键不存在返回 null

    println(readOnly.getOrDefault("Kotlin", 0)) // 提供默认值

    println(readOnly.keys)

    println(readOnly.values)

}
```

## 代码块 10

```kotlin
{Runoob=1, RUNOOB=2}
{Runoob=1, RUNOOB=2}
1
null
0
[Runoob, RUNOOB]
[1, 2]
```

## 代码块 11

```kotlin
fun main() {

    // it 是下标，生成 0 到 4 的平方

    val squares = List(5) { it * it }

    val zeros = MutableList(3) { 0 }

    println(squares)

    println(zeros)


    // buildList 内部可以写任意逻辑，最后返回只读列表

    val built = buildList {

        add("Runoob")

        add("RUNOOB")

        if (size > 1) add("Kotlin")

    }

    println(built)


    val map = buildMap {

        put("Runoob", 1)

        put("RUNOOB", 2)

    }

    println(map)

}
```

## 代码块 12

```kotlin
[0, 1, 4, 9, 16]
[0, 0, 0]
[Runoob, RUNOOB, Kotlin]
{Runoob=1, RUNOOB=2}
```

## 代码块 13

```kotlin
fun main() {

    val numbers = listOf(3, 1, 2, 1)


    val set: Set<Int> = numbers.toSet()            // 去重，保持首次出现顺序

    val sortedList: List<Int> = numbers.sorted()   // 排序，返回新列表

    val mutableCopy: MutableList<Int> = numbers.toMutableList()


    // 修改副本不影响原列表

    mutableCopy.add(99)


    println(numbers)

    println(set)

    println(sortedList)

    println(mutableCopy)


    // List<Pair> 转 Map，键重复时保留最后一个值

    val pairs = listOf("Runoob" to 1, "RUNOOB" to 2)

    val map: Map<String, Int> = pairs.toMap()

    println(map)


    // associate 用 lambda 自定义键和值

    val byLength = listOf("Runoob", "Kotlin").associate { it to it.length }

    println(byLength)

}
```

## 代码块 14

```kotlin
[3, 1, 2, 1]
[3, 1, 2]
[1, 1, 2, 3]
[3, 1, 2, 1, 99]
{Runoob=1, RUNOOB=2}
{Runoob=6, Kotlin=6}
```
