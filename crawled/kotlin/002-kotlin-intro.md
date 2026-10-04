# Kotlin 简介

> 来源: https://www.runoob.com/kotlin/kotlin-intro.html

## 代码块 1

```kotlin
// 文件路径：hello.kt

// 第一个 Kotlin 程序

fun main() {

    println("Hello, Runoob!")            // 打印一行文本并换行

    println("欢迎来到 www.runoob.com")     // 中文同样可以直接输出

}
```

## 代码块 2

```kotlin
Hello, Runoob!
欢迎来到 www.runoob.com
```

## 代码块 3

```kotlin
// 文件路径：Site.kt

// 用类描述一个网站，主构造器直接声明属性

class Site(val name: String, val url: String) {


    // 表达式体函数，返回值类型由编译器推断为 String

    fun introduce(): String = "欢迎访问 $name（$url）"

}


fun main() {

    // 创建对象，参数按顺序传入

    val runoob = Site("菜鸟教程", "www.runoob.com")


    println(runoob.introduce())                    // 调用成员函数

    println("站点名称长度：${runoob.name.length}")   // 字符串模板里可以放表达式

}
```

## 代码块 4

```kotlin
欢迎访问 菜鸟教程（www.runoob.com）
站点名称长度：4
```
