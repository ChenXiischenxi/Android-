# Kotlin 泛型

> 来源: https://www.runoob.com/kotlin/kotlin-generics.html

## 代码块 1

```kotlin
// T 是类型参数，创建实例时再确定它具体是什么类型

class Box<T>(t: T) {

    var value = t

}


fun main() {

    val boxInt = Box<Int>(10)          // 显式指定 T 为 Int

    val boxString = Box("RUNOOB")      // 省略类型参数，编译器推断为 Box<String>

    println(boxInt.value)

    println(boxString.value)

}
```

## 代码块 2

```kotlin
10
RUNOOB
```

## 代码块 3

```kotlin
class Box<T>(t: T) {

    var value = t

}


// 类型参数 T 放在 fun 和函数名之间

fun <T> boxIn(value: T) = Box(value)


fun main() {

    val box1 = boxIn<Int>(1)        // 显式指定类型参数

    val box2 = boxIn("runoob")      // 编译器推断类型参数

    println(box1.value)

    println(box2.value)

}
```

## 代码块 4

```kotlin
1
runoob
```

## 代码块 5

```kotlin
fun main() {

    val age = 23

    val name = "runoob"

    val bool = true


    doPrintln(age)      // 推断为 doPrintln<Int>

    doPrintln(name)     // 推断为 doPrintln<String>

    doPrintln(bool)     // 推断为 doPrintln<Boolean>

}


fun <T> doPrintln(content: T) {

    when (content) {

        is Int -> println("整型数字为 $content")

        // uppercase() 在 Kotlin 1.5 起取代了已弃用的 toUpperCase()

        is String -> println("字符串转换为大写：${content.uppercase()}")

        else -> println("T 不是整型，也不是字符串")

    }

}
```

## 代码块 6

```kotlin
整型数字为 23
字符串转换为大写：RUNOOB
T 不是整型，也不是字符串
```

## 代码块 7

```kotlin
// 没有参数可以推断 T，只能靠赋值目标或显式指定来确定

fun <T> nothing(): T? = null


fun main() {

    val inferred = listOf("runoob", "kotlin")        // 推断为 List<String>

    val explicit: List<Any> = listOf("runoob", 42)   // 由声明类型推断为 List<Any>

    val empty: String? = nothing()                   // 由赋值目标推断 T 为 String

    println(inferred)

    println(explicit)

    println(empty)

}
```

## 代码块 8

```kotlin
[runoob, kotlin]
[runoob, 42]
null
```

## 代码块 9

```kotlin
// T 必须是 Comparable<T> 的子类型，这样才能比较大小

fun <T : Comparable<T>> sort(list: List<T>): List<T> = list.sorted()


fun main() {

    println(sort(listOf(3, 1, 2)))

    println(sort(listOf("runoob", "kotlin", "www.runoob.com")))

}
```

## 代码块 10

```kotlin
[1, 2, 3]
[kotlin, runoob, www.runoob.com]
```

## 代码块 11

```kotlin
// 没有写约束，上界默认为 Any?，因此 T 可以取可空类型

fun <T> echo(value: T): String = "收到：$value"


fun main() {

    println(echo("runoob"))

    println(echo(42))

    println(echo<String?>(null))   // 显式指定 T 为 String?

}
```

## 代码块 12

```kotlin
收到：runoob
收到：42
收到：null
```

## 代码块 13

```kotlin
// T 同时满足两个约束：是 CharSequence 的子类型，且可比较

fun <T> copyWhenGreater(list: List<T>, threshold: T): List<String>

        where T : CharSequence,

              T : Comparable<T> {

    return list.filter { it > threshold }.map { it.toString() }

}


fun main() {

    val list = listOf("runoob", "kotlin", "www.runoob.com")

    println(copyWhenGreater(list, "kotlin"))

}
```

## 代码块 14

```kotlin
[runoob, www.runoob.com]
```

## 代码块 15

```kotlin
// out A：A 只作为返回值出现，因此 Producer<String> 可以赋给 Producer<Any>

class Producer<out A>(private val value: A) {

    fun get(): A = value

}


fun main() {

    val strProducer: Producer<String> = Producer("RUNOOB")

    val anyProducer: Producer<Any> = strProducer   // 协变：子类型赋给父类型

    println(anyProducer.get())

}
```

## 代码块 16

```kotlin
RUNOOB
```

## 代码块 17

```kotlin
// in A：A 只作为参数出现，因此 Consumer<Any> 可以赋给 Consumer<String>

class Consumer<in A> {

    fun consume(value: A) {

        println("消费：$value")

    }

}


fun main() {

    val anyConsumer: Consumer<Any> = Consumer<Any>()

    val strConsumer: Consumer<String> = anyConsumer   // 逆变：父类型赋给子类型

    strConsumer.consume("runoob")

}
```

## 代码块 18

```kotlin
消费：runoob
```

## 代码块 19

```kotlin
// Array 是不变的，Array<String> 不能直接当作 Array<Any>

// 参数写成 Array<out Any> 后就可以接收任意元素为 Any 子类型的数组

fun copy(from: Array<out Any>, to: Array<Any>) {

    for (i in from.indices) {

        to[i] = from[i]

    }

}


fun main() {

    val src = arrayOf("runoob", "kotlin")   // Array<String>

    val dst = Array<Any>(2) { "" }          // Array<Any>

    copy(src, dst)

    println(dst.joinToString())

}
```

## 代码块 20

```kotlin
runoob, kotlin
```

## 代码块 21

```kotlin
// 接收任意元素类型的只读列表

fun printAll(list: List<*>) {

    for (item in list) {

        println(item)

    }

}


fun main() {

    printAll(listOf(1, 2, 3))

    printAll(listOf("runoob", "kotlin"))

}
```

## 代码块 22

```kotlin
1
2
3
runoob
kotlin
```

## 代码块 23

```kotlin
// reified 只能用在 inline 函数的类型参数上

inline fun <reified T> typeName(): String = T::class.simpleName ?: "未知"


inline fun <reified T> isType(value: Any): Boolean = value is T


fun main() {

    println(typeName<String>())

    println(typeName<Int>())

    println(isType<String>("RUNOOB"))

    println(isType<Int>("RUNOOB"))

}
```

## 代码块 24

```kotlin
String
Int
true
false
```

## 代码块 25

```kotlin
fun main() {

    val mixed: List<Any> = listOf("runoob", 42, "kotlin", 3.14)

    val strings = mixed.filterIsInstance<String>()

    println(strings)

}
```

## 代码块 26

```kotlin
[runoob, kotlin]
```

## 代码块 27

```kotlin
class A<T>(val t: T, val t2 : T, val t3 : T)
class Apple(var name : String)
fun main(args: Array<String>) {
    //使用类
    val a1: A<*> = A(12, "String", Apple("苹果"))
    val a2: A<Any?> = A(12, "String", Apple("苹果"))   //和a1是一样的
    val apple = a1.t3    //参数类型为Any
    println(apple)
    val apple2 = apple as Apple   //强转成Apple类
    println(apple2.name)
    //使用数组
    val l:ArrayList<*> = arrayListOf("String",1,1.2f,Apple("苹果"))
    for (item in l){
        println(item)
    }
}
```
