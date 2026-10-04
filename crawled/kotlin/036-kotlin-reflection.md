# Kotlin 反射

> 来源: https://www.runoob.com/kotlin/kotlin-reflection.html

## 代码块 1

```kotlin
package com.runoob


import kotlin.reflect.KClass


// 定义一个示例类

class Runoob(val name: String, var age: Int)


fun main() {

    // 类名 ::class 得到 KClass 对象

    val kClass: KClass<Runoob> = Runoob::class

    println("简单名: ${kClass.simpleName}")

    println("限定名: ${kClass.qualifiedName}")


    // 通过实例也能拿到 KClass，类型和上面完全一样

    val site = Runoob("RUNOOB", 10)

    println("实例的类: ${site::class.simpleName}")

    println("是同一个对象: ${site::class == Runoob::class}")

}
```

## 代码块 2

```kotlin
简单名: Runoob
限定名: com.runoob.Runoob
实例的类: Runoob
是同一个对象: true
```

## 代码块 3

```kotlin
package com.runoob


class Runoob(val name: String)


fun main() {

    // KClass -> Class

    val javaClass: Class<Runoob> = Runoob::class.java

    println("Java 类名: ${javaClass.name}")


    // Class -> KClass

    val back = javaClass.kotlin

    println("转回 KClass: ${back.simpleName}")

}
```

## 代码块 4

```kotlin
Java 类名: com.runoob.Runoob
转回 KClass: Runoob
```

## 代码块 5

```kotlin
package com.runoob


import kotlin.reflect.KFunction2


// 顶层函数

fun add(a: Int, b: Int): Int = a + b


class Calculator {

    fun multiply(a: Int, b: Int): Int = a * b

}


fun main() {

    // 顶层函数的引用，类型是 KFunction2<Int, Int, Int>

    val f: KFunction2<Int, Int, Int> = ::add

    println("函数名: ${f.name}")

    println("参数个数: ${f.parameters.size}")


    // 直接调用是编译期绑定的，不经过反射，性能接近普通函数调用

    println("直接调用: ${f(3, 4)}")


    // call 才是真正的反射调用，参数按位置依次传入

    println("call 调用: ${f.call(3, 4)}")


    // 成员函数引用要先有实例

    val calc = Calculator()

    val m = calc::multiply

    println("成员函数名: ${m.name}")

    println("call 调用: ${m.call(5, 6)}")

}
```

## 代码块 6

```kotlin
函数名: add
参数个数: 2
直接调用: 7
call 调用: 7
成员函数名: multiply
call 调用: 30
```

## 代码块 7

```kotlin
package com.runoob


fun add(a: Int, b: Int): Int = a + b


fun main() {

    val f = ::add

    // 用参数名传值，顺序可以打乱

    val args = mapOf(f.parameters[1] to 4, f.parameters[0] to 3)

    println("callBy: ${f.callBy(args)}")

}
```

## 代码块 8

```kotlin
callBy: 7
```

## 代码块 9

```kotlin
package com.runoob


import kotlin.reflect.KMutableProperty1

import kotlin.reflect.KProperty1


class User(val name: String, var age: Int)


fun main() {

    val user = User("RUNOOB", 10)


    // val 属性得到 KProperty1，只能读

    val nameProp: KProperty1<User, String> = User::name

    println("属性名: ${nameProp.name}")

    println("读取 name: ${nameProp.get(user)}")


    // var 属性得到 KMutableProperty1，可以读也可以写

    val ageProp: KMutableProperty1<User, Int> = User::age

    println("读取 age: ${ageProp.get(user)}")

    ageProp.set(user, 20)

    println("写入后 age: ${user.age}")

}
```

## 代码块 10

```kotlin
属性名: name
读取 name: RUNOOB
读取 age: 10
写入后 age: 20
```

## 代码块 11

```kotlin
package com.runoob


import kotlin.reflect.KProperty0


// 顶层属性

val siteName: String = "www.runoob.com"


object Config {

    val version: String = "Kotlin 2.2"

}


fun main() {

    val p1: KProperty0<String> = ::siteName

    println("${p1.name} = ${p1.get()}")


    val p2: KProperty0<String> = Config::version

    println("${p2.name} = ${p2.get()}")

}
```

## 代码块 12

```kotlin
siteName = www.runoob.com
version = Kotlin 2.2
```

## 代码块 13

```kotlin
package com.runoob


import kotlin.reflect.KProperty1

import kotlin.reflect.full.declaredMemberFunctions

import kotlin.reflect.full.memberProperties


class Runoob(val name: String, var age: Int) {

    fun greet(): String = "欢迎来到 $name"

}


fun main() {

    val site = Runoob("RUNOOB", 10)

    val kClass = site::class


    // memberProperties 包含父类属性，Any 本身没有属性，所以就是这两个

    println("成员属性：")

    for (prop in kClass.memberProperties.sortedBy { it.name }) {

        // memberProperties 的元素类型带 out 投影，直接调用 get 会被禁止，需要先转成具体类型

        @Suppress("UNCHECKED_CAST")

        val p = prop as KProperty1<Runoob, *>

        println("  ${p.name} = ${p.get(site)}")

    }


    // declaredMemberFunctions 只包含本类声明的函数

    println("本类声明的函数：")

    for (func in kClass.declaredMemberFunctions.sortedBy { it.name }) {

        println("  ${func.name}")

    }


    // 按名字找到函数并调用

    val greet = kClass.declaredMemberFunctions.first { it.name == "greet" }

    println("调用 greet(): ${greet.call(site)}")

}
```

## 代码块 14

```kotlin
成员属性：
  age = 10
  name = RUNOOB
本类声明的函数：
  greet
调用 greet(): 欢迎来到 RUNOOB
```

## 代码块 15

```kotlin
package com.runoob


import kotlin.reflect.full.createInstance


class Runoob {

    val siteName: String = "RUNOOB"

    override fun toString(): String = "Runoob 实例"

}


fun main() {

    val instance = Runoob::class.createInstance()

    println(instance)

    println(instance.siteName)

}
```

## 代码块 16

```kotlin
Runoob 实例
RUNOOB
```

## 代码块 17

```kotlin
package com.runoob


import kotlin.reflect.full.primaryConstructor


class Site(val name: String, val url: String)


fun main() {

    // 拿到主构造器，再按顺序传参调用

    val ctor = Site::class.primaryConstructor!!

    val site = ctor.call("RUNOOB", "www.runoob.com")

    println("${site.name} -> ${site.url}")

}
```

## 代码块 18

```kotlin
RUNOOB -> www.runoob.com
```

## 代码块 19

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("jvm") version "2.2.0"

}


dependencies {

    // kotlin("reflect") 会自动使用与 Kotlin 插件一致的版本

    implementation(kotlin("reflect"))


    // 也可以写死坐标，注意版本要和 Kotlin 编译器保持一致

    // implementation("org.jetbrains.kotlin:kotlin-reflect:2.2.0")

}
```

## 代码块 20

```xml
<!-- 文件路径：pom.xml -->

<dependency>

    <groupId>org.jetbrains.kotlin</groupId>

    <artifactId>kotlin-reflect</artifactId>

    <version>2.2.0</version>

</dependency>
```

## 代码块 21

```kotlin
package com.runoob


import java.lang.reflect.Method


class Runoob(val name: String) {

    fun greet(): String = "欢迎来到 $name"

}


fun main() {

    // Java 风格：用字符串加载类，写错要到运行时才发现

    val clazz = Class.forName("com.runoob.Runoob")

    val ctor = clazz.getConstructor(String::class.java)

    val instance = ctor.newInstance("RUNOOB")


    // 按方法名和参数类型查找

    val method: Method = clazz.getMethod("greet")

    println(method.invoke(instance))

}
```

## 代码块 22

```kotlin
欢迎来到 RUNOOB
```

## 代码块 23

```kotlin
package com.runoob


import kotlin.reflect.full.memberProperties


class Profile(val name: String, val nickname: String?)


fun main() {

    for (prop in Profile::class.memberProperties.sortedBy { it.name }) {

        val type = prop.returnType

        println("${prop.name}: ${type}，可空 = ${type.isMarkedNullable}")

    }

}
```

## 代码块 24

```kotlin
name: kotlin.String，可空 = false
nickname: kotlin.String?，可空 = true
```
