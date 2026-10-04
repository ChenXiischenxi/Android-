# Kotlin 继承

> 来源: https://www.runoob.com/kotlin/kotlin-extend.html

## 代码块 1

```kotlin
// 文件路径：Main.kt

class Site(val name: String, val url: String) {

    // 重写 toString，让打印结果可读

    override fun toString(): String = "Site(name=$name, url=$url)"


    // 重写 equals，改为按内容比较

    override fun equals(other: Any?): Boolean {

        if (this === other) return true

        if (other !is Site) return false

        return name == other.name && url == other.url

    }


    // 重写 equals 后必须一起重写 hashCode，保证相等对象哈希码相同

    override fun hashCode(): Int = 31 * name.hashCode() + url.hashCode()

}


fun main() {

    val a = Site("RUNOOB", "www.runoob.com")

    val b = Site("RUNOOB", "www.runoob.com")


    println(a)

    println("a == b：${a == b}")                     // 内容相等

    println("a === b：${a === b}")                   // 不是同一个对象

    println("哈希码相同：${a.hashCode() == b.hashCode()}")

}
```

## 代码块 2

```kotlin
Site(name=RUNOOB, url=www.runoob.com)
a == b：true
a === b：false
哈希码相同：true
```

## 代码块 3

```kotlin
// 文件路径：Main.kt


// 加 open 之后才能被继承

open class Animal(val name: String) {

    // 加 open 之后才能被重写

    open fun sound(): String = "..."


    // 没有 open，默认 final，子类不能重写

    fun eat(): String = "$name 在吃东西"

}


class Dog(name: String) : Animal(name) {

    override fun sound(): String = "汪汪"

}


fun main() {

    val dog = Dog("旺财")

    println(dog.sound())

    println(dog.eat())

    println("dog 是 Animal：${dog is Animal}")

}
```

## 代码块 4

```kotlin
汪汪
旺财 在吃东西
dog 是 Animal：true
```

## 代码块 5

```kotlin
// 文件路径：Main.kt

open class Site(val name: String) {

    init {

        println("基类 init：$name")

    }


    open fun show(): String = "站点：$name"

}


// 子类主构造器把 name 传给父类构造器

class SubSite(name: String, val url: String) : Site(name) {

    init {

        println("子类 init：$url")

    }


    override fun show(): String = "${super.show()}，地址：$url"

}


fun main() {

    val s = SubSite("RUNOOB", "www.runoob.com")

    println(s.show())

}
```

## 代码块 6

```kotlin
基类 init：RUNOOB
子类 init：www.runoob.com
站点：RUNOOB，地址：www.runoob.com
```

## 代码块 7

```kotlin
// 文件路径：Main.kt

open class Person {

    open val role: String = "普通人"


    constructor(name: String) {

        println("Person 次构造器：$name")

    }


    // 委托给上一个次构造器，避免重复初始化

    constructor(name: String, age: Int) : this(name) {

        println("Person 次构造器（带年龄）：$name，$age")

    }

}


class Student : Person {

    constructor(name: String) : super(name) {

        println("Student 次构造器：$name")

    }


    constructor(name: String, age: Int) : super(name, age) {

        println("Student 次构造器（带年龄）：$name，$age")

    }


    override val role: String = "学生"

}


fun main() {

    val s = Student("小明", 18)

    println("角色：${s.role}")

}
```

## 代码块 8

```kotlin
Person 次构造器：小明
Person 次构造器（带年龄）：小明，18
Student 次构造器（带年龄）：小明，18
角色：学生
```

## 代码块 9

```kotlin
// 文件路径：Main.kt

open class Base {

    open fun foo(): String = "Base.foo"

    open fun bar(): String = "Base.bar"

}


open class Middle : Base() {

    // override 之后默认仍是 open，子类可以继续重写

    override fun foo(): String = "Middle.foo"


    // 加 final 之后，后面的子类不能再重写

    final override fun bar(): String = "Middle.bar"

}


class Leaf : Middle() {

    override fun foo(): String = "Leaf.foo"


    // override fun bar(): String = "Leaf.bar"   // 编译错误：bar 已被 final 锁定

}


fun main() {

    val leaf = Leaf()

    println(leaf.foo())

    println(leaf.bar())

}
```

## 代码块 10

```kotlin
Leaf.foo
Middle.bar
```

## 代码块 11

```kotlin
// 文件路径：Main.kt

open class Site {

    open val name: String = "RUNOOB"


    // 只有 getter，没有幕后字段

    open val url: String

        get() = "www.runoob.com"

}


class SubSite(

    override val name: String,     // 在主构造器里重写 val 属性

    private val rawUrl: String

) : Site() {

    // val 可以重写为 var，反过来不行

    override var url: String = rawUrl

        get() = field

        set(value) {

            field = value

        }

}


fun main() {

    val s = SubSite("Runoob", "www.runoob.com")

    println(s.name)

    println(s.url)


    // 因为子类把它重写成了 var，所以可以修改

    s.url = "https://www.runoob.com"

    println(s.url)

}
```

## 代码块 12

```kotlin
Runoob
www.runoob.com
https://www.runoob.com
```

## 代码块 13

```kotlin
// 文件路径：Main.kt

interface A {

    fun foo(): String = "A.foo"

}


interface B {

    fun foo(): String = "B.foo"

}


class C : A, B {

    // 两个接口都有默认实现，必须重写，并分别调用

    override fun foo(): String = super<A>.foo() + " | " + super<B>.foo()

}


fun main() {

    println(C().foo())

}
```

## 代码块 14

```kotlin
A.foo | B.foo
```

## 代码块 15

```kotlin
open class Person(var name: String, var age: Int) {
    open var sex: String = "unknow"
    init {
        println("基类初始化")
    }
}
// 子类的主构造方法的 name 前边也加了 var，这是不允许的，会报'name' hides member of supertype and needs 'override' modifier
class Student(var name: String, age: Int, var no: String, var score: Int) : Person(name, age) {
    override var sex: String = "male"
}
```

## 代码块 16

```kotlin
open class A {
    open fun f() {
        println("A")
    }
    fun a() {
        println("a")
    }
}
interface B {
    fun f() {
        println("B")
    }
    fun b() {
        println("b")
    }
}
class C : A(), B {
    override fun f() {
        // super<A>.f()
        // super<B>.f()
        println("C")
    }
}
```

## 代码块 17

```kotlin
var aaa: Int = 0
get() {
    field // 这里必须出现一下field关键字，否则 var aaa: Int = 0 会报错，除非你去掉 = 0这部分，不要给它赋初始化值
    return 0
}
set(value) {}
```
