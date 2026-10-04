# Kotlin 教程

> 来源: https://www.runoob.com/kotlin/kotlin-tutorial.html

## 代码块 1

```kotlin
package hello                      //  可选的包头

fun main(args: Array<String>) {    // 包级可见的函数，接受一个字符串数组作为参数
   println("Hello World!")         // 分号可以省略
}
```

## 代码块 2

```kotlin
class Greeter(val name: String) {
   fun greet() {
      println("Hello, $name")
   }
}

fun main(args: Array<String>) {
   Greeter("World!").greet()          // 创建一个对象不用 new 关键字
}
```
