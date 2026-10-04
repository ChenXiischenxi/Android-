# Kotlin 扩展

> 来源: https://www.runoob.com/kotlin/kotlin-extensions.html

## 代码块 1

```kotlin
class User(var name: String)


// 给 User 类扩展一个 printInfo 函数

fun User.printInfo() {

    println("用户名 $name")

}


fun main() {

    val user = User("Runoob")

    user.printInfo()   // 像调用成员函数一样调用扩展函数

}
```

## 代码块 2

```kotlin
用户名 Runoob
```

## 代码块 3

```kotlin
// 给 MutableList<Int> 扩展一个交换函数

fun MutableList<Int>.swap(index1: Int, index2: Int) {

    val tmp = this[index1]        // this 指向调用 swap 的那个列表

    this[index1] = this[index2]

    this[index2] = tmp

}


fun main() {

    val list = mutableListOf(1, 2, 3)

    list.swap(0, 2)               // 交换下标 0 和 2 的元素

    println(list)

}
```

## 代码块 4

```kotlin
[3, 2, 1]
```

## 代码块 5

```kotlin
open class C

class D : C()


fun C.foo() = "c"

fun D.foo() = "d"


// 参数 c 的声明类型是 C，所以编译期就绑定到 C.foo()

fun printFoo(c: C) {

    println(c.foo())

}


fun main() {

    printFoo(D())   // 传入 D 的实例，输出的仍然是 c

}
```

## 代码块 6

```kotlin
c
```

## 代码块 7

```kotlin
class C {

    fun foo() = "成员函数"

}


fun C.foo() = "扩展函数"


fun main() {

    println(C().foo())   // 成员函数胜出

}
```

## 代码块 8

```kotlin
成员函数
```

## 代码块 9

```kotlin
// 接收者是 Any?，所以 null 也能调用这个扩展

fun Any?.describe(): String {

    if (this == null) return "空值"

    // 判空之后 this 已经是非空类型

    return "非空：$this"

}


fun main() {

    val text: String? = null

    println(text.describe())

    println("RUNOOB".describe())

}
```

## 代码块 10

```kotlin
空值
非空：RUNOOB
```

## 代码块 11

```kotlin
class Site(val name: String, val url: String)


// 只读扩展属性：只提供 getter

val Site.info: String

    get() = "$name ($url)"


fun main() {

    val site = Site("菜鸟教程", "www.runoob.com")

    println(site.info)

}
```

## 代码块 12

```kotlin
菜鸟教程 (www.runoob.com)
```

## 代码块 13

```kotlin
// var 扩展属性：getter 和 setter 都必须显式写出

var StringBuilder.lastChar: Char

    get() = get(length - 1)              // 读取最后一个字符

    set(value: Char) {

        setCharAt(length - 1, value)     // 修改最后一个字符

    }


fun main() {

    val sb = StringBuilder("RUNOOB")

    println(sb.lastChar)

    sb.lastChar = '!'

    println(sb)

}
```

## 代码块 14

```kotlin
B
RUNOO!
```

## 代码块 15

```kotlin
class Foo


// 错误：扩展属性不能有初始化器，它没有 backing field

val Foo.bar = 1


// 正确写法：提供显式的 getter

val Foo.bar: Int

    get() = 1
```

## 代码块 16

```kotlin
class MyClass {

    companion object   // 将被称为 Companion

}


// 给伴生对象扩展函数

fun MyClass.Companion.create(): MyClass = MyClass()


// 给伴生对象扩展属性

val MyClass.Companion.siteName: String

    get() = "菜鸟教程"


fun main() {

    println(MyClass.siteName)        // 用类名访问扩展属性

    println(MyClass.create() is MyClass)

}
```

## 代码块 17

```kotlin
菜鸟教程
true
```

## 代码块 18

```kotlin
// 文件路径：com/runoob/extensions/SiteExtensions.kt

package com.runoob.extensions


class Site(val name: String, val url: String)


// 顶层扩展函数，属于包 com.runoob.extensions

fun Site.describe(): String = "$name -> $url"
```

## 代码块 19

```kotlin
// 文件路径：com/runoob/app/Main.kt

package com.runoob.app


import com.runoob.extensions.Site

import com.runoob.extensions.describe   // 导入扩展函数


// 也可以写 import com.runoob.extensions.* 导入整个包


fun main() {

    val site = Site("菜鸟教程", "www.runoob.com")

    println(site.describe())

}
```

## 代码块 20

```kotlin
菜鸟教程 -> www.runoob.com
```

## 代码块 21

```kotlin
class D {

    fun bar() = "D.bar"

}


class C {

    fun baz() = "C.baz"


    // 在 C 内部给 D 定义扩展函数

    fun D.foo(): String {

        val fromExtension = bar()   // 扩展接收者 D 的成员

        val fromDispatch = baz()    // 分发接收者 C 的成员

        return "$fromExtension / $fromDispatch"

    }


    fun caller(d: D) = d.foo()

}


fun main() {

    println(C().caller(D()))

}
```

## 代码块 22

```kotlin
D.bar / C.baz
```

## 代码块 23

```kotlin
class D {

    fun bar() = "D.bar"

}


class C {

    fun bar() = "C.bar"     // 与 D 的 bar 同名


    fun D.foo(): String {

        val first = bar()         // 扩展接收者优先，调用 D.bar()

        val second = this@C.bar() // 显式指定分发接收者，调用 C.bar()

        return "$first / $second"

    }


    fun caller(d: D) = d.foo()

}


fun main() {

    println(C().caller(D()))

}
```

## 代码块 24

```kotlin
D.bar / C.bar
```

## 代码块 25

```kotlin
open class D

class D1 : D()


open class C {

    open fun D.foo() = "D.foo in C"

    open fun D1.foo() = "D1.foo in C"


    fun caller(d: D) = d.foo()   // 参数声明类型是 D

}


class C1 : C() {

    override fun D.foo() = "D.foo in C1"

    override fun D1.foo() = "D1.foo in C1"

}


fun main() {

    println(C().caller(D()))    // 分发接收者是 C

    println(C1().caller(D()))   // 分发接收者是 C1，虚拟解析

    println(C().caller(D1()))   // 扩展接收者按声明类型 D 静态解析

}
```

## 代码块 26

```kotlin
D.foo in C
D.foo in C1
D.foo in C
```

## 代码块 27

```kotlin
class MyClass {
    companion object {
        val myClassField1: Int = 1
        var myClassField2 = "this is myClassField2"
        fun companionFun1() {
            println("this is 1st companion function.")
            foo()
        }
        fun companionFun2() {
            println("this is 2st companion function.")
            companionFun1()
        }
    }
    fun MyClass.Companion.foo() {
        println("伴随对象的扩展函数（内部）")
    }
    fun test2() {
        MyClass.foo()
    }
    init {
        test2()
    }
}
val MyClass.Companion.no: Int
    get() = 10
fun MyClass.Companion.foo() {
    println("foo 伴随对象外部扩展函数")
}
fun main(args: Array<String>) {
    println("no:${MyClass.no}")
    println("field1:${MyClass.myClassField1}")
    println("field2:${MyClass.myClassField2}")
    MyClass.foo()
    MyClass.companionFun2()
}
```

## 代码块 28

```kotlin
no:10
field1:1
field2:this is myClassField2
foo 伴随对象外部扩展函数
this is 2st companion function.
this is 1st companion function.
foo 伴随对象外部扩展函数
```
