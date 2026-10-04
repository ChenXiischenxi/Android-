# Kotlin 类和对象

> 来源: https://www.runoob.com/kotlin/kotlin-class-object.html

## 代码块 1

```kotlin
// 文件路径：Main.kt


// 空类：没有类体，大括号可以省略

class Runoob


// 带空主构造器的类，与上面写法等价

class RunoobSite()


fun main() {

    // 不需要 new，直接调用类名创建对象

    val a = Runoob()

    val b = RunoobSite()


    println("a 的类型：${a::class.simpleName}")

    println("b 的类型：${b::class.simpleName}")

}
```

## 代码块 2

```kotlin
a 的类型：Runoob
b 的类型：RunoobSite
```

## 代码块 3

```kotlin
// 文件路径：Main.kt

class Site {

    var name: String = "RUNOOB"           // var 属性：有 getter 和 setter

    val url: String = "www.runoob.com"    // val 属性：只有 getter


    // 自定义 getter：每次访问都重新计算，没有幕后字段

    val info: String

        get() = "$name - $url"


    // 自定义 setter：value 是约定俗成的参数名

    var visits: Int = 0

        set(value) {

            if (value < 0) {

                println("访问量不能为负，已忽略")

            } else {

                field = value

            }

        }

}


fun main() {

    val site = Site()


    println(site.info)


    site.visits = 100

    println("访问量：${site.visits}")


    site.visits = -1

    println("访问量：${site.visits}")

}
```

## 代码块 4

```kotlin
RUNOOB - www.runoob.com
访问量：100
访问量不能为负，已忽略
访问量：100
```

## 代码块 5

```kotlin
// 文件路径：Main.kt

class Counter {

    var count: Int = 0

        get() = field        // field 就是幕后字段

        set(value) {

            field = value

        }


    // 只读计算属性：没有幕后字段，每次访问都重新计算

    val doubleCount: Int

        get() = count * 2

}


fun main() {

    val c = Counter()

    c.count = 21


    println("count：${c.count}")

    println("doubleCount：${c.doubleCount}")

}
```

## 代码块 6

```kotlin
count：21
doubleCount：42
```

## 代码块 7

```kotlin
// 文件路径：Main.kt


// 主构造器直接声明属性：val 只读，var 可变

class Site(val name: String, var visits: Int) {

    // 没写 constructor，因为既没有注解也没有可见性修饰符

    init {

        println("创建站点：$name，初始访问量：$visits")

    }

}


fun main() {

    val site = Site("RUNOOB", 0)

    site.visits = 10

    println("${site.name} 访问量：${site.visits}")

}
```

## 代码块 8

```kotlin
创建站点：RUNOOB，初始访问量：0
RUNOOB 访问量：10
```

## 代码块 9

```kotlin
// 文件路径：Main.kt

class Demo(val name: String) {

    // 属性初始化器与 init 块按书写顺序执行

    private val first = "第一个属性：$name".also { println(it) }


    init {

        println("init 块：$name")

    }


    private val second = "第二个属性：$name".also { println(it) }

}


fun main() {

    Demo("RUNOOB")

}
```

## 代码块 10

```kotlin
第一个属性：RUNOOB
init 块：RUNOOB
第二个属性：RUNOOB
```

## 代码块 11

```kotlin
// 文件路径：Main.kt

class Site(val name: String, val url: String) {

    var visits: Int = 0


    // 次构造器必须委托给主构造器，这里补上默认地址

    constructor(name: String) : this(name, "www.runoob.com") {

        println("使用次构造器创建：$name")

    }

}


fun main() {

    val a = Site("RUNOOB", "www.runoob.com")

    println("${a.name} -> ${a.url}")


    val b = Site("Runoob")

    println("${b.name} -> ${b.url}")

}
```

## 代码块 12

```kotlin
RUNOOB -> www.runoob.com
使用次构造器创建：Runoob
Runoob -> www.runoob.com
```

## 代码块 13

```kotlin
// 文件路径：Main.kt

class Token private constructor(val value: String) {

    // 外部无法调用 Token("...")，只能通过这个工厂方法

    companion object {

        fun create(): Token = Token("runoob-token")

    }


    fun describe(): String = "Token($value)"

}


fun main() {

    // val t = Token("abc")   // 编译错误：构造函数是私有的

    val token = Token.create()

    println(token.describe())

}
```

## 代码块 14

```kotlin
Token(runoob-token)
```

## 代码块 15

```kotlin
// 文件路径：Main.kt

abstract class Shape {

    // 抽象成员没有实现，子类必须重写

    abstract fun area(): Double


    // 普通成员默认是 final，加 open 才能被重写

    open fun describe(): String = "面积是 ${area()}"

}


class Circle(val radius: Double) : Shape() {

    override fun area(): Double = 3.14 * radius * radius

}


class Square(val side: Double) : Shape() {

    override fun area(): Double = side * side


    override fun describe(): String = "正方形" + super.describe()

}


fun main() {

    // val s = Shape()   // 编译错误：抽象类不能实例化


    val shapes: List<Shape> = listOf(Circle(2.0), Square(3.0))

    for (shape in shapes) {

        println(shape.describe())

    }

}
```

## 代码块 16

```kotlin
面积是 12.56
正方形面积是 9.0
```

## 代码块 17

```kotlin
// 文件路径：Main.kt

class Outer(val name: String = "OUTER") {

    private val secret = "runoob"


    // 嵌套类：不持有外部类实例引用，访问不了 name 和 secret

    class Nested {

        fun hello(): String = "我是嵌套类，拿不到外部类的成员"

    }


    // 内部类：持有外部类实例引用，可以访问外部类成员

    inner class Inner {

        fun hello(): String = "我是内部类，name=$name，secret=$secret"


        // this@Outer 明确指向外部类实例

        fun outerName(): String = this@Outer.name

    }

}


fun main() {

    // 嵌套类直接用外部类名访问，不需要外部类对象

    val nested = Outer.Nested()

    println(nested.hello())


    // 内部类必须依赖外部类实例

    val outer = Outer()

    val inner = outer.Inner()

    println(inner.hello())

    println("this@Outer 拿到：${inner.outerName()}")

}
```

## 代码块 18

```kotlin
我是嵌套类，拿不到外部类的成员
我是内部类，name=OUTER，secret=runoob
this@Outer 拿到：OUTER
```

## 代码块 19

```kotlin
// 文件路径：Main.kt

interface ClickListener {

    fun onClick(name: String)

}


fun main() {

    // 对象表达式：临时实现 ClickListener 接口

    val listener = object : ClickListener {

        override fun onClick(name: String) {

            println("点击了：$name")

        }

    }

    listener.onClick("RUNOOB")


    // 不实现任何接口时，也可以直接写一个匿名对象

    val config = object {

        val url = "www.runoob.com"

        val timeout = 3000

    }

    println("${config.url} -> ${config.timeout}ms")

}
```

## 代码块 20

```kotlin
点击了：RUNOOB
www.runoob.com -> 3000ms
```

## 代码块 21

```kotlin
// 文件路径：Main.kt

open class Base {

    private val a = "private：仅本类内部可见"

    protected val b = "protected：仅本类及其子类内部可见"

    internal val c = "internal：同一模块内可见"

    val d = "public：默认，任何位置可见"


    fun showBase() {

        println(a)

        println(b)

    }

}


class Derived : Base() {

    fun showDerived() {

        // println(a)   // 编译错误：private 成员连子类也看不到

        println(b)      // 可以：protected 在子类内部可见

        println(c)

        println(d)

    }

}


fun main() {

    val base = Base()

    base.showBase()


    // println(base.b)  // 编译错误：外部无法访问 protected 成员


    val derived = Derived()

    derived.showDerived()

}
```

## 代码块 22

```kotlin
private：仅本类内部可见
protected：仅本类及其子类内部可见
protected：仅本类及其子类内部可见
internal：同一模块内可见
public：默认，任何位置可见
```

## 代码块 23

```kotlin
var no: Int = 100
    get() = field                // 后端变量
    set(value) {
        if (value < 10) {       // 如果传入的值小于 10 返回该值
            field = value
        } else {
            field = -1         // 如果传入的值大于等于 10 返回 -1
        }
    }
```

## 代码块 24

```kotlin
var no: Int = 100
    get() = no
    set(value) {
        if (value < 10) {       // 如果传入的值小于 10 返回该值
            no = value
        } else {
            no = -1         // 如果传入的值大于等于 10 返回 -1
        }
    }
```

## 代码块 25

```kotlin
int no = 100;
public int getNo() {
    return getNo();// Kotlin中的get() = no语句中出来了变量no，直接被编译器理解成“调用getter方法”
}

public void setNo(int value) {
    if (value < 10) {
        setNo(value);// Kotlin中出现“no =”这样的字样，直接被编译器理解成“这里要调用setter方法”
    } else {
        setNo(-1);// 在setter方法中调用setter方法，这是不正确的
    }
}
```

## 代码块 26

```kotlin
var demo = Outter.Nested()// 嵌套类，Outter后边没有括号
var demo = Outter().Inner();// 内部类，Outter后边有括号
```

## 代码块 27

```kotlin
class Outer {                  // 外部类
    private val bar: Int = 1
    class Nested {             // 嵌套类
        var ot: Outer = Outer()
        println(ot.bar) // 嵌套类可以引用外部类私有变量，但要先创建外部类的实例，不能直接引用
        fun foo() = 2
    }
}
```

## 代码块 28

```kotlin
class Outer {
    private val bar: Int = 1
    var v = "成员属性"
    /**嵌套内部类**/
    inner class Inner {
        fun foo() = bar  // 访问外部类成员
        fun innerTest() {
            var o = this@Outer //获取外部类的成员变量
            println("内部类可以引用外部类的成员，例如：" + o.v)
        }
    }
}
```

## 代码块 29

```kotlin
fun main(args: Array<String>) {
    var test = Test()

    /**
     * 采用对象表达式来创建接口对象，即匿名内部类的实例。
     */
    test.setInterFace(object : TestInterFace {
        override fun test() {
            println("对象表达式创建匿名内部类的实例")
        }
    })
}
```

## 代码块 30

```kotlin
// 还是 JAVA 代码
int no = 100;
private int _no = 100;
public int getNo() {
    return _no;//
}

public void setNo(int value) {
    if (value < 10) {
        _no = value;// Kotlin中出现“no =”这样的字样，直接被编译器理解成“这里要调用setter方法”
    } else {
        _no = -1;// 在setter方法中调用setter方法，这是不正确的
    }
}
```

## 代码块 31

```kotlin
class Runoob {
    var name: String = ……
    var url: String = ……
    var city: String = ……
}

var entity = Runoob()
entity.javaClass.getDeclaredFields().forEach { field -> println(field.name) }
```
