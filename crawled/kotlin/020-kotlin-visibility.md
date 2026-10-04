# Kotlin 可见性修饰符

> 来源: https://www.runoob.com/kotlin/kotlin-visibility.html

## 代码块 1

```kotlin
// 文件：RunoobFile.kt

private const val SITE: String = "www.runoob.com"   // 顶层 private：仅本文件可见


fun printSite() {

    println(SITE)   // 同一个文件内可以访问

}


// 文件：Main.kt（与 RunoobFile.kt 一起编译）

fun main() {

    printSite()      // 可以调用，printSite 是 public

    // println(SITE) // 编译错误：Cannot access 'SITE': it is private in file

}
```

## 代码块 2

```kotlin
www.runoob.com
```

## 代码块 3

```kotlin
class RunoobAccount {

    private var balance: Double = 0.0   // 仅本类可见


    fun deposit(amount: Double) {

        // 内部可以自由读写 private 属性

        require(amount > 0) { "金额必须大于 0" }

        balance += amount

    }


    fun showBalance(): String = "余额：$balance 元"

}


fun main() {

    val account = RunoobAccount()

    account.deposit(100.0)

    println(account.showBalance())

    // println(account.balance)   // 编译错误：balance 是 private

}
```

## 代码块 4

```kotlin
余额：100.0 元
```

## 代码块 5

```kotlin
open class RunoobAnimal {

    protected var name: String = "Runoob 猫"   // 子类内部可见


    protected fun showName(): String = "动物名称：$name"

}


class RunoobCat : RunoobAnimal() {

    fun introduce() {

        name = "Runoob 小猫"   // 子类内部可以访问 protected 属性

        println(showName())    // 子类内部可以调用 protected 方法

    }

}


fun main() {

    val cat = RunoobCat()

    cat.introduce()

    // println(cat.name)   // 编译错误：protected 成员在类外不可见

    // cat.showName()      // 编译错误：同上

}
```

## 代码块 6

```kotlin
动物名称：Runoob 小猫
```

## 代码块 7

```kotlin
// 编译错误：Modifier 'protected' is not applicable to top-level declarations

// protected fun runoobHelp(): String = "帮助中心"


// 正确写法：顶层要么 public，要么 private / internal

fun runoobHelp(): String = "帮助中心"


fun main() {

    println(runoobHelp())

}
```

## 代码块 8

```kotlin
帮助中心
```

## 代码块 9

```kotlin
// 文件：Logger.kt

internal fun log(message: String) {

    println("[RUNOOB] $message")

}


internal class RunoobLogger {

    internal val tag: String = "RUNOOB"

}


// 文件：Main.kt（与 Logger.kt 属于同一个模块）

fun main() {

    log("模块内可以直接调用")

    val logger = RunoobLogger()

    println(logger.tag)

}
```

## 代码块 10

```kotlin
[RUNOOB] 模块内可以直接调用
RUNOOB
```

## 代码块 11

```kotlin
public class RunoobSite          // 显式写 public

class RunoobMirror               // 省略修饰符，默认就是 public


public fun runoobHello(): String = "Hello RUNOOB"

fun runoobHi(): String = "Hi www.runoob.com"


public val siteName: String = "RUNOOB"

val siteUrl: String = "www.runoob.com"


fun main() {

    println(runoobHello())

    println(runoobHi())

    println("$siteName - $siteUrl")

}
```

## 代码块 12

```kotlin
Hello RUNOOB
Hi www.runoob.com
RUNOOB - www.runoob.com
```

## 代码块 13

```kotlin
// 主构造器设为 private：外部不能直接创建实例

class RunoobSingleton private constructor() {

    companion object {

        private val instance = RunoobSingleton()

        fun getInstance(): RunoobSingleton = instance

    }

}


// 主构造器设为 internal：只有同一模块内能创建

class RunoobConfig internal constructor(val host: String, val port: Int)


fun main() {

    val config = RunoobConfig("www.runoob.com", 80)

    println("${config.host}:${config.port}")


    // RunoobSingleton()   // 编译错误：主构造器是 private


    val single = RunoobSingleton.getInstance()

    println(single.javaClass.simpleName)

}
```

## 代码块 14

```kotlin
www.runoob.com:80
RunoobSingleton
```

## 代码块 15

```kotlin
class RunoobUser {

    var name: String = "runoob"

        private set      // setter 仅本类可见，外部只能读不能改


    fun rename(newName: String) {

        name = newName    // 本类内部仍然可以修改

    }

}


fun main() {

    val user = RunoobUser()

    println(user.name)

    user.rename("RUNOOB")

    println(user.name)

    // user.name = "菜鸟教程"   // 编译错误：setter 是 private

}
```

## 代码块 16

```kotlin
runoob
RUNOOB
```

## 代码块 17

```kotlin
open class RunoobBase {

    protected open fun runoobTip(): String = "来自基类的提示"

}


class RunoobChild : RunoobBase() {

    // 允许把 protected 放宽为 public

    public override fun runoobTip(): String = "来自子类的提示"

}


fun main() {

    println(RunoobChild().runoobTip())   // 现在是 public，类外可调用

}
```

## 代码块 18

```kotlin
来自子类的提示
```

## 代码块 19

```kotlin
open class RunoobBase2 {

    open fun runoobInfo(): String = "info"

}


class RunoobChild2 : RunoobBase2() {

    // 编译错误：'runoobInfo' has a weaker access privilege than the overridden declaration

    // private override fun runoobInfo(): String = "info"

}
```
