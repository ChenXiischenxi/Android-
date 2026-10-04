# Kotlin 接口

> 来源: https://www.runoob.com/kotlin/kotlin-interface.html

## 代码块 1

```kotlin
// 文件路径：Main.kt

interface Site {

    // 抽象方法：没有方法体，实现类必须重写

    fun name(): String


    // 带默认实现的方法：实现类可以直接用，也可以重写

    fun url(): String = "www.runoob.com"


    // 默认实现可以调用其他成员，包括抽象的 name()

    fun info(): String = "站点：${name()}，地址：${url()}"

}


// 全部重写

class RunoobSite : Site {

    override fun name(): String = "RUNOOB"


    override fun url(): String = "https://www.runoob.com"

}


// 只重写抽象方法，url() 和 info() 使用接口的默认实现

class SimpleSite : Site {

    override fun name(): String = "Runoob"

}


fun main() {

    println(RunoobSite().info())

    println(SimpleSite().info())

}
```

## 代码块 2

```kotlin
站点：RUNOOB，地址：https://www.runoob.com
站点：Runoob，地址：www.runoob.com
```

## 代码块 3

```kotlin
// 文件路径：Main.kt

interface Named {

    fun label(): String

}


// 没有主构造器的实现

class Simple : Named {

    override fun label(): String = "Simple"

}


// 有主构造器的实现：构造器参数写在接口名前面

class Site(val name: String) : Named {

    override fun label(): String = "Site($name)"

}


fun main() {

    // 接口可以作为集合的元素类型，存放不同实现

    val list: List<Named> = listOf(Simple(), Site("RUNOOB"))


    for (item in list) {

        println(item.label())

    }

}
```

## 代码块 4

```kotlin
Simple
Site(RUNOOB)
```

## 代码块 5

```kotlin
// 文件路径：Main.kt

interface Named {

    val name: String              // 抽象属性：实现类必须提供


    // 带默认 getter 的属性：实现类不用重写就能用

    val displayName: String

        get() = "[$name]"


    // 接口里也可以声明 var，但 setter 由实现类负责

    var visits: Int

}


class Site(override val name: String) : Named {

    // var 属性在实现类里补上存储与 setter

    override var visits: Int = 0

}


fun main() {

    val site = Site("RUNOOB")

    println(site.displayName)


    site.visits = 100

    println("${site.name} 访问量：${site.visits}")

}
```

## 代码块 6

```kotlin
[RUNOOB]
RUNOOB 访问量：100
```

## 代码块 7

```kotlin
// 文件路径：Main.kt

interface A {

    fun foo(): String = "A.foo"

    val label: String

        get() = "A.label"

}


interface B {

    fun foo(): String = "B.foo"

    val label: String

        get() = "B.label"

}


class C : A, B {

    // 两个接口的默认实现冲突，必须显式重写

    override fun foo(): String = super<A>.foo() + " | " + super<B>.foo()


    override val label: String

        get() = super<A>.label + " | " + super<B>.label

}


fun main() {

    val c = C()

    println(c.foo())

    println(c.label)

}
```

## 代码块 8

```kotlin
A.foo | B.foo
A.label | B.label
```

## 代码块 9

```kotlin
// 文件路径：Main.kt

interface Base {

    fun base(): String = "Base"

}


interface Left : Base {

    fun left(): String = "Left"

}


interface Right : Base {

    // 子接口重写了 Base 的默认实现

    override fun base(): String = "Right 重写了 Base"


    fun right(): String = "Right"

}


// Left 和 Right 都继承自 Base，Impl 只需要处理一次

class Impl : Left, Right {

    override fun base(): String = super<Right>.base()

}


fun main() {

    val impl = Impl()

    println(impl.base())

    println(impl.left())

    println(impl.right())

}
```

## 代码块 10

```kotlin
Right 重写了 Base
Left
Right
```

## 代码块 11

```kotlin
// 文件路径：Main.kt

fun interface Validator {

    // 唯一的抽象方法

    fun validate(text: String): Boolean


    // 非抽象成员不影响函数式接口的判定

    fun describe(): String = "校验器"

}


fun check(text: String, validator: Validator): String =

    if (validator.validate(text)) "「$text」通过校验" else "「$text」未通过校验"


fun main() {

    // 用 lambda 直接构造 fun interface 的实例

    val notEmpty = Validator { it.isNotEmpty() }

    println(check("RUNOOB", notEmpty))

    println(check("", notEmpty))


    val shorter = Validator { it.length <= 10 }

    println(check("www.runoob.com", shorter))

    println(shorter.describe())

}
```

## 代码块 12

```kotlin
「RUNOOB」通过校验
「」未通过校验
「www.runoob.com」未通过校验
校验器
```
