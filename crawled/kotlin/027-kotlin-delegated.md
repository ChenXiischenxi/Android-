# kotlin 委托

> 来源: https://www.runoob.com/kotlin/kotlin-delegated.html

## 代码块 1

```kotlin
interface Base {

    fun print()

}


// 被委托的类

class BaseImpl(private val x: Int) : Base {

    override fun print() {

        println("BaseImpl: $x")

    }

}


// Derived 把 Base 接口的实现委托给构造参数 b

class Derived(b: Base) : Base by b


fun main() {

    val b = BaseImpl(10)

    Derived(b).print()   // 实际调用的是 b.print()

}
```

## 代码块 2

```kotlin
BaseImpl: 10
```

## 代码块 3

```kotlin
interface Base {

    fun print()

    fun name(): String

}


class BaseImpl(private val x: Int) : Base {

    override fun print() = println("BaseImpl: $x")

    override fun name() = "BaseImpl"

}


class Derived(b: Base) : Base by b {

    // 只重写 name()，print() 仍然转发给 b

    override fun name() = "Derived"

}


fun main() {

    val d = Derived(BaseImpl(10))

    d.print()

    println(d.name())

}
```

## 代码块 4

```kotlin
BaseImpl: 10
Derived
```

## 代码块 5

```kotlin
import kotlin.reflect.KProperty


class Example {

    // 属性的读写都委托给 Delegate 实例

    var p: String by Delegate()


    override fun toString() = "Example"

}


class Delegate {

    // thisRef 是属性所属的对象，property 描述属性本身

    operator fun getValue(thisRef: Any?, property: KProperty<*>): String {

        return "$thisRef 读取了属性 ${property.name}"

    }


    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: String) {

        println("$thisRef 的 ${property.name} 被赋值为 $value")

    }

}


fun main() {

    val e = Example()

    println(e.p)        // 访问属性，调用 getValue()

    e.p = "RUNOOB"      // 赋值，调用 setValue()

}
```

## 代码块 6

```kotlin
Example 读取了属性 p
Example 的 p 被赋值为 RUNOOB
```

## 代码块 7

```kotlin
val lazyValue: String by lazy {

    println("computed!")   // 只在第一次访问时输出

    "Hello"

}


fun main() {

    println(lazyValue)   // 第一次访问，触发初始化

    println(lazyValue)   // 第二次访问，直接返回缓存

}
```

## 代码块 8

```kotlin
computed!
Hello
Hello
```

## 代码块 9

```kotlin
import kotlin.LazyThreadSafetyMode


fun main() {

    // 显式指定线程安全模式

    val config: String by lazy(LazyThreadSafetyMode.PUBLICATION) {

        println("执行初始化")

        "www.runoob.com"

    }

    println(config)

    println(config)

}
```

## 代码块 10

```kotlin
执行初始化
www.runoob.com
www.runoob.com
```

## 代码块 11

```kotlin
import kotlin.properties.Delegates


class User {

    // 每次赋值后都会执行回调

    var name: String by Delegates.observable("初始值") { prop, old, new ->

        println("${prop.name}：$old -> $new")

    }

}


fun main() {

    val user = User()

    user.name = "第一次赋值"

    user.name = "第二次赋值"

}
```

## 代码块 12

```kotlin
name：初始值 -> 第一次赋值
name：第一次赋值 -> 第二次赋值
```

## 代码块 13

```kotlin
import kotlin.properties.Delegates


class User {

    // 只有取值在 0 到 150 之间才允许写入

    var age: Int by Delegates.vetoable(0) { _, _, new ->

        new in 0..150

    }

}


fun main() {

    val user = User()

    user.age = 25

    println(user.age)

    user.age = -1        // 被拒绝，保持 25

    println(user.age)

    user.age = 200       // 被拒绝，保持 25

    println(user.age)

}
```

## 代码块 14

```kotlin
25
25
25
```

## 代码块 15

```kotlin
class Site(val map: Map<String, Any?>) {

    // 属性名 name 对应 map 里的 "name" 键

    val name: String by map

    val url: String by map

}


fun main() {

    val site = Site(mapOf(

        "name" to "菜鸟教程",

        "url" to "www.runoob.com"

    ))

    println(site.name)

    println(site.url)

}
```

## 代码块 16

```kotlin
菜鸟教程
www.runoob.com
```

## 代码块 17

```kotlin
class Site(val map: MutableMap<String, Any?>) {

    var name: String by map

    var url: String by map

}


fun main() {

    val map = mutableMapOf<String, Any?>(

        "name" to "菜鸟教程",

        "url" to "www.runoob.com"

    )

    val site = Site(map)


    println(site.name)

    site.name = "RUNOOB"       // 写回映射

    println(site.name)

    println(map["name"])       // 映射本身也被修改了

}
```

## 代码块 18

```kotlin
菜鸟教程
RUNOOB
RUNOOB
```

## 代码块 19

```kotlin
import kotlin.properties.Delegates


class Foo {

    // 声明时不赋值，等运行时再赋值

    var notNullBar: String by Delegates.notNull<String>()

}


fun main() {

    val foo = Foo()             // 必须先创建实例

    foo.notNullBar = "bar"      // 赋值之后才能读取

    println(foo.notNullBar)

}
```

## 代码块 20

```kotlin
bar
```

## 代码块 21

```kotlin
import kotlin.properties.Delegates


class Foo {

    var notNullBar: String by Delegates.notNull<String>()

}


fun main() {

    val foo = Foo()

    println(foo.notNullBar)   // 赋值前读取，抛异常

}
```

## 代码块 22

```kotlin
Exception in thread "main" java.lang.IllegalStateException: Property notNullBar should be initialized before get.
```

## 代码块 23

```kotlin
fun process(input: String?) {

    // 局部变量委托给 lazy，第一次访问时才计算

    val normalized: String by lazy {

        println("执行规范化")

        input?.trim()?.uppercase() ?: ""

    }


    if (normalized.isNotEmpty()) {   // 这里才触发初始化

        println("结果：$normalized")

    }

}


fun main() {

    process(" runoob ")

    process(null)   // 虽然也会触发初始化，但结果为空，不会打印结果行

}
```

## 代码块 24

```kotlin
执行规范化
结果：RUNOOB
执行规范化
```

## 代码块 25

```kotlin
import kotlin.properties.ReadOnlyProperty

import kotlin.reflect.KProperty


// 委托提供者：在绑定属性时校验属性名

class ValidatedDelegate<T>(

    private val value: T,

    private val allowedName: String

) {

    operator fun provideDelegate(

        thisRef: Any?,

        prop: KProperty<*>

    ): ReadOnlyProperty<Any?, T> {

        // 属性创建阶段立即校验，名字不对就直接失败

        require(prop.name == allowedName) {

            "属性名必须是 $allowedName，实际是 ${prop.name}"

        }

        return object : ReadOnlyProperty<Any?, T> {

            override fun getValue(thisRef: Any?, property: KProperty<*>): T = value

        }

    }

}


class MyUI {

    val name by ValidatedDelegate("菜鸟教程", "name")

}


fun main() {

    println(MyUI().name)

}
```

## 代码块 26

```kotlin
菜鸟教程
```

## 代码块 27

```kotlin
import kotlin.properties.ReadOnlyProperty

import kotlin.reflect.KProperty


class ValidatedDelegate<T>(

    private val value: T,

    private val allowedName: String

) {

    operator fun provideDelegate(

        thisRef: Any?,

        prop: KProperty<*>

    ): ReadOnlyProperty<Any?, T> {

        require(prop.name == allowedName) {

            "属性名必须是 $allowedName，实际是 ${prop.name}"

        }

        return object : ReadOnlyProperty<Any?, T> {

            override fun getValue(thisRef: Any?, property: KProperty<*>): T = value

        }

    }

}


class MyUI {

    // 属性名是 siteName，与 allowedName 不一致，构造 MyUI 时立即报错

    val siteName by ValidatedDelegate("菜鸟教程", "name")

}
```

## 代码块 28

```kotlin
Exception in thread "main" java.lang.IllegalArgumentException: 属性名必须是 name，实际是 siteName
```

## 代码块 29

```kotlin
class MyDelegate {

    operator fun getValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>): String = "value"

    operator fun setValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>, value: String) {}

}


class C {

    var prop: String by MyDelegate()

}


// 上面这段代码大致等价于编译器生成的下面这段：

class CGenerated {

    private val prop$delegate = MyDelegate()


    var prop: String

        get() = prop$delegate.getValue(this, this::prop)

        set(value: String) = prop$delegate.setValue(this, this::prop, value)

}
```

## 代码块 30

```kotlin
import kotlin.properties.ReadOnlyProperty

import kotlin.reflect.KProperty


class MyDelegate {

    // 定义 provideDelegate 后，编译器改为调用它来创建委托对象

    operator fun provideDelegate(thisRef: Any?, prop: KProperty<*>): ReadOnlyProperty<Any?, String> {

        println("绑定属性 ${prop.name}")

        return object : ReadOnlyProperty<Any?, String> {

            override fun getValue(thisRef: Any?, property: KProperty<*>): String = "value"

        }

    }

}


class C {

    val prop: String by MyDelegate()

}


// 当 provideDelegate 存在时，生成的辅助属性变成：

class CGenerated {

    // 调用 provideDelegate 创建真正的委托对象

    private val prop$delegate = MyDelegate().provideDelegate(this, this::prop)


    val prop: String

        get() = prop$delegate.getValue(this, this::prop)

}
```

## 代码块 31

```kotlin
class ResourceID() {
    val image_id: String = "101"
    val text_id: String = "102"
}

class ResourceLoader(id: ResourceID) {
    val d: ResourceID = id
    operator fun provideDelegate( thisRef: MyUI, prop: KProperty ): ReadOnlyProperty {
        if(checkProperty(thisRef, prop.name)){
            return DellImpl(d)
        }else{
            throw Exception("Error ${prop.name}")
        }
    }

    private fun checkProperty(thisRef: MyUI, name: String):Boolean {
        if(name.equals("image") || name.equals("text")){
            return true
        }else{
            return false
        }
    }
}

class DellImpl(d: ResourceID) : ReadOnlyProperty {
    val id: ResourceID = d
    override fun getValue(thisRef: MyUI, property: KProperty): String {
        if(property.name.equals("image"))
            return property.name+"  "+id.image_id
        else
            return property.name+"  "+id.text_id
    }
}

fun  bindResource(id: ResourceID): ResourceLoader {
    var res = ResourceLoader(id);
    return res
}

class MyUI {
    val image by bindResource(ResourceID())
    val text by bindResource(ResourceID())
    //val webview by bindResource(ResourceID())
}

fun main(args: Array) {
    try{
        var ui = MyUI()
        println(ui.image)
        println(ui.text)
    }catch(e: Exception) {
        println(e.message)
    }
}
```

## 代码块 32

```kotlin
class MyReadOnlyPropertyImpl : ReadOnlyProperty<MyTestClass, String> {
    override fun getValue(thisRef: MyTestClass, property: KProperty<*>): String {
        val s  = "aaa"
        return s;
    }
}
class MyProvider {
    operator fun provideDelegate(thisRef: MyTestClass, prop: KProperty<*>): ReadOnlyProperty<MyTestClass, String> {
        println("do something") // 这行代码是在getValue方法之外调用的
        val myReadOnlyPropertyImpl = MyReadOnlyPropertyImpl() // 这里才是调用getValue方法的地方
        return myReadOnlyPropetyImpl
    }
}
class MyTestClass {
    val myProvider = MyProvider()
    val myField1: String by myProvider
}
// 测试
fun main(args: Array<String>) {
    val myTestClass = MyTestClass()
    println(myTestClass.myField1)
}
```

## 代码块 33

```kotlin
do something
aaa
```

## 代码块 34

```kotlin
class MyProvider {
    operator fun provideDelegate(thisRef: MyTestClass, prop: KProperty<*>): ReadOnlyProperty<MyTestClass, String> {
        println("do something") // 这行代码是在getValue方法之外调用的
        return object: ReadOnlyProperty<MyTestClass, String> {            // 这里才是调用getValue方法的地方
            override fun getValue(thisRef: MyTestClass, property: KProperty<*>): String {
                return "aaa"
            }
        }
    }
}
```

## 代码块 35

```kotlin
import kotlin.properties.ReadOnlyProperty
import kotlin.reflect.KProperty

class ResourceID() {
    val image_id: String = "101"
    val text_id: String = "102"
}
class ResourceLoader(id: ResourceID) {
    val d: ResourceID = id
    operator fun provideDelegate( thisRef: MyUI, prop: KProperty<*>): ReadOnlyProperty<MyUI, String> {
        if(checkProperty(thisRef, prop.name)){
            return DellImpl(d)
        }else{
            throw Exception("Error ${prop.name}")
        }
    }
    private fun checkProperty(thisRef: MyUI, name: String):Boolean {
        return name.equals("image") || name.equals("text")
    }
}
class DellImpl(d: ResourceID) : ReadOnlyProperty<MyUI, String> {
    val id: ResourceID = d
    override fun getValue(thisRef: MyUI, property: KProperty<*>): String {
        if(property.name.equals("image"))
            return property.name+"  "+id.image_id
        else
            return property.name+"  "+id.text_id
    }
}
fun  bindResource(id: ResourceID): ResourceLoader {
    var res = ResourceLoader(id);
    return res
}
class MyUI {
    val image by bindResource(ResourceID())
    val text by bindResource(ResourceID())
    //val webview by bindResource(ResourceID())
}
fun main(args: Array<String>) {
    try{
        var ui = MyUI()
        println(ui.image)
        println(ui.text)
    }catch(e: Exception) {
        println(e.message)
    }
}

// 输出
/**
* image  101
* text  102
*/
```

## 代码块 36

```kotlin
class ResourceID() {
    val image_id: String = "101"
    val text_id: String = "102"
}
class ResourceLoader(id: ResourceID) {
    val d: ResourceID = id
    //表明该函数返回的值是ReadOnlyProperty<MyUI, String>
    //在实例化MyUI的时候，立即做这里的检查
    operator fun provideDelegate( thisRef: MyUI, prop: KProperty<*>): ReadOnlyProperty<MyUI, String> {
        if(checkProperty(thisRef, prop.name)){
            //匹配则返回相应的委托
            return DellImpl(d)
        }else{
            //不匹配则抛出异常
            throw Exception("Error ${prop.name}")
        }
    }

    //检查名字是否匹配
    private fun checkProperty(thisRef: MyUI, name: String):Boolean {
        return name.equals("image") || name.equals("text")
    }
}

//ReadOnlyProperty<MyUI, String>泛型参数：第一个大概和thisRef一样，第二个参数是getValue()的返回值
class DellImpl(d: ResourceID) : ReadOnlyProperty<MyUI, String> {
    val id: ResourceID = d
    override fun getValue(thisRef: MyUI, property: KProperty<*>): String {
        //这里就是调用ui.image得到的值
        if(property.name.equals("image"))
            return property.name+"  "+id.image_id
        else
            return property.name+"  "+id.text_id
    }
}

fun  bindResource(id: ResourceID): ResourceLoader {
    var res = ResourceLoader(id);
    return res
}

class MyUI {
    //这里的bindResource(ResourceID())最终会返回一个委托或者抛出异常
    val image : String by bindResource(ResourceID())
    val text : String by bindResource(ResourceID())
    //val webview by bindResource(ResourceID())
}
fun main(args: Array<String>) {
    try{
        var ui = MyUI()
        println(ui.image)
        println(ui.text)
    }catch(e: Exception) {
        println(e.message)
    }
}

// 输出
/**
 * image  101
 * text  102
 */
```
