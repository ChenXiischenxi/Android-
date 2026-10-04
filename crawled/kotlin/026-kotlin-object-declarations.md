# Kotlin 对象表达式与对象声明

> 来源: https://www.runoob.com/kotlin/kotlin-object-declarations.html

## 代码块 1

```kotlin
// 定义一个接口

interface Greeter {

    fun greet(): String

}


fun main() {

    // object : Greeter 表示创建一个实现了 Greeter 接口的匿名对象

    val runoob = object : Greeter {

        override fun greet() = "Hello, RUNOOB"

    }

    println(runoob.greet())

}
```

## 代码块 2

```kotlin
Hello, RUNOOB
```

## 代码块 3

```kotlin
open class A(x: Int) {

    open val y: Int = x

}


interface B {

    fun hello(): String

}


fun main() {

    // 同时继承 A(1) 并实现 B，A 的构造参数 1 必须显式传入

    val ab = object : A(1), B {

        override val y = 15

        override fun hello() = "菜鸟教程"

    }

    println(ab.y)

    println(ab.hello())

}
```

## 代码块 4

```kotlin
15
菜鸟教程
```

## 代码块 5

```kotlin
fun main() {

    // 没有任何超类型，直接得到一个匿名对象

    val site = object {

        var name: String = "菜鸟教程"

        var url: String = "www.runoob.com"

    }

    println(site.name)

    println(site.url)

}
```

## 代码块 6

```kotlin
菜鸟教程
www.runoob.com
```

## 代码块 7

```kotlin
interface ClickListener {

    fun onClick()

}


fun countClicks(listener: ClickListener) {

    listener.onClick()

}


fun main() {

    var clickCount = 0

    // 匿名对象捕获了外层的 clickCount 变量

    val listener = object : ClickListener {

        override fun onClick() {

            clickCount++

            println("被点击了 $clickCount 次")

        }

    }

    countClicks(listener)

    countClicks(listener)

}
```

## 代码块 8

```kotlin
被点击了 1 次
被点击了 2 次
```

## 代码块 9

```kotlin
class C {

    // 私有函数：返回类型就是匿名对象的真实类型

    private fun foo() = object {

        val x: String = "RUNOOB"

    }


    // 公有函数：返回类型退化为 Any

    fun publicFoo() = object {

        val x: String = "RUNOOB"

    }


    fun bar() {

        val x1 = foo().x          // 可以访问

        println(x1)

        // val x2 = publicFoo().x // 编译错误：Any 上没有成员 x

    }

}


fun main() {

    C().bar()

}
```

## 代码块 10

```kotlin
RUNOOB
```

## 代码块 11

```kotlin
// 对象声明：全局唯一的单例

object Site {

    var url: String = ""

    val name: String = "菜鸟教程"

}


fun main() {

    val s1 = Site

    val s2 = Site

    s1.url = "www.runoob.com"

    println(s1.url)

    println(s2.url)

    println(s1 === s2)   // 两者是同一个实例

}
```

## 代码块 12

```kotlin
www.runoob.com
www.runoob.com
true
```

## 代码块 13

```kotlin
interface Formatter {

    fun format(value: String): String

}


// 对象声明实现接口，可以直接通过对象名使用

object UpperFormatter : Formatter {

    override fun format(value: String) = value.uppercase()

}


fun main() {

    println(UpperFormatter.format("runoob"))

}
```

## 代码块 14

```kotlin
RUNOOB
```

## 代码块 15

```kotlin
class Site {

    var name = "菜鸟教程"


    object DeskTop {

        var url = "www.runoob.com"

        // fun showName() = name  // 编译错误：不能访问外部类的实例成员

    }

}


fun main() {

    println(Site.DeskTop.url)   // 只能用类名访问

}
```

## 代码块 16

```kotlin
www.runoob.com
```

## 代码块 17

```kotlin
class MyClass {

    // 具名伴生对象，名字叫 Factory

    companion object Factory {

        fun create(): MyClass = MyClass()

    }

}


fun main() {

    val instance = MyClass.create()          // 直接用类名调用

    println(instance is MyClass)

    println(MyClass.Factory.create() is MyClass)   // 也可以用伴生对象的名字调用

}
```

## 代码块 18

```kotlin
true
true
```

## 代码块 19

```kotlin
class MyClass {

    companion object {

        const val SITE = "www.runoob.com"

    }

}


fun main() {

    val companion = MyClass.Companion

    println(companion.SITE)

    println(MyClass.SITE)

}
```

## 代码块 20

```kotlin
www.runoob.com
www.runoob.com
```

## 代码块 21

```kotlin
interface Factory<T> {

    fun create(): T

}


class MyClass {

    // 伴生对象实现 Factory 接口

    companion object : Factory<MyClass> {

        override fun create(): MyClass = MyClass()


        var count = 0

    }

}


fun main() {

    // 把伴生对象当作 Factory 实例使用

    val factory: Factory<MyClass> = MyClass.Companion

    val a = factory.create()

    MyClass.count = 3

    println(a is MyClass)

    println(MyClass.count)

}
```

## 代码块 22

```kotlin
true
3
```

## 代码块 23

```kotlin
// 对象声明：首次访问时才初始化

object Singleton {

    init {

        println("Singleton 初始化")

    }


    fun hello() = "hello"

}


// 伴生对象：随外部类初始化

class Holder {

    companion object {

        init {

            println("Holder 的伴生对象初始化")

        }

    }

}


fun main() {

    println("main 开始")

    val holder = Holder()            // 触发 Holder 类初始化，伴生对象随之初始化

    println("创建了 Holder 实例")

    println(Singleton.hello())       // 首次访问，Singleton 此时才初始化

    println("访问了 Singleton")

    println(holder is Holder)

}
```

## 代码块 24

```kotlin
main 开始
Holder 的伴生对象初始化
创建了 Holder 实例
Singleton 初始化
hello
访问了 Singleton
true
```
