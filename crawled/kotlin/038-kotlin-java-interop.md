# Kotlin Java 互操作

> 来源: https://www.runoob.com/kotlin/kotlin-java-interop.html

## 代码块 1

```kotlin
// 文件路径：Person.java

public class Person {

    private String name;          // 私有字段

    private int age;


    public Person(String name, int age) {

        this.name = name;

        this.age = age;

    }


    // Java 的 getter / setter

    public String getName() { return name; }

    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }

    public void setAge(int age) { this.age = age; }


    // 静态方法

    public static String welcome(String site) {

        return "欢迎来到 " + site;

    }

}
```

## 代码块 2

```kotlin
// 文件路径：Main.kt

fun main() {

    val person = Person("RUNOOB", 10)


    // 调用 Java getter 时可以直接用属性语法

    println(person.name)              // 等价于 person.getName()

    println(person.age)               // 等价于 person.getAge()


    // 调用 Java setter 也可以直接用属性赋值

    person.age = 20                   // 等价于 person.setAge(20)

    println("修改后：${person.age}")


    // 静态方法按 Java 的写法调用

    println(Person.welcome("www.runoob.com"))

}
```

## 代码块 3

```kotlin
RUNOOB
10
修改后：20
欢迎来到 www.runoob.com
```

## 代码块 4

```kotlin
// 文件路径：Runoob.kt

class Runoob {

    companion object {

        // 没有 @JvmStatic，Java 必须写 Runoob.Companion.currentVersion()

        fun currentVersion(): String = "Kotlin 2.2"


        // 加了 @JvmStatic，Java 可以直接写 Runoob.staticVersion()

        @JvmStatic

        fun staticVersion(): String = "Kotlin 2.2"


        // const val 会生成静态常量字段

        const val SITE: String = "www.runoob.com"

    }

}


// 顶层函数会生成 RunoobKt 类（文件名 + Kt）

fun topLevelHello(): String = "来自顶层函数的问候"
```

## 代码块 5

```kotlin
// 文件路径：Main.java

public class Main {

    public static void main(String[] args) {

        System.out.println(Runoob.Companion.currentVersion()); // 伴生对象要经过 Companion

        System.out.println(Runoob.staticVersion());            // @JvmStatic 变成静态方法

        System.out.println(Runoob.SITE);                       // const val 是静态字段

        System.out.println(RunoobKt.topLevelHello());          // 顶层函数在 RunoobKt 中

    }

}
```

## 代码块 6

```kotlin
Kotlin 2.2
Kotlin 2.2
www.runoob.com
来自顶层函数的问候
```

## 代码块 7

```kotlin
// 文件路径：Utils.kt

@file:JvmName("RunoobUtils")        // 文件注解必须写在 package 之前


package com.runoob


fun version(): String = "Kotlin 2.2"
```

## 代码块 8

```kotlin
// 文件路径：MessageService.java

public class MessageService {

    // 没有标注 @Nullable / @NotNull，返回值是平台类型 String!

    public String getMessage() {

        return null;              // 运行时可能返回 null

    }

}
```

## 代码块 9

```kotlin
// 文件路径：Main.kt

fun main() {

    val service = MessageService()


    // 声明为可空类型，强制自己做判空，这是推荐写法

    val message: String? = service.message

    println("内容：$message")

    println("长度：${message?.length ?: 0}")

}
```

## 代码块 10

```kotlin
内容：null
长度：0
```

## 代码块 11

```kotlin
// 文件路径：Config.kt

import java.io.IOException


class Config {

    // @JvmField：Java 直接访问字段 config.timeout

    @JvmField

    val timeout: Int = 3000


    // 普通 val：Java 要通过 getPort() 访问

    val port: Int = 8080

}


class Formatter {

    // @JvmOverloads：为默认参数生成 1 个、2 个、3 个参数的重载

    @JvmOverloads

    fun format(text: String, prefix: String = "[RUNOOB] ", upper: Boolean = false): String {

        val result = prefix + text

        return if (upper) result.uppercase() else result

    }


    // @Throws：让 Java 看到受检异常，调用时必须 try/catch

    @Throws(IOException::class)

    fun readConfig(path: String): String {

        if (path.isEmpty()) throw IOException("路径不能为空")

        return "读取成功：$path"

    }

}


// @JvmName：修改生成的 JVM 方法名

@JvmName("greetFromKotlin")

fun greet(name: String): String = "你好，$name"
```

## 代码块 12

```kotlin
// 文件路径：Main.java

import java.io.IOException;


public class Main {

    public static void main(String[] args) throws IOException {

        Config config = new Config();

        System.out.println(config.timeout);      // @JvmField：直接访问字段

        System.out.println(config.getPort());    // 普通属性：走 getter


        Formatter formatter = new Formatter();

        System.out.println(formatter.format("hello"));                     // 1 个参数

        System.out.println(formatter.format("hello", "kotlin "));          // 2 个参数

        System.out.println(formatter.format("hello", "kotlin ", true));    // 3 个参数

        System.out.println(formatter.readConfig("runoob.conf"));

        System.out.println(ConfigKt.greetFromKotlin("RUNOOB"));            // @JvmName 后的名字

    }

}
```

## 代码块 13

```kotlin
3000
8080
[RUNOOB] hello
kotlin hello
KOTLIN HELLO
读取成功：runoob.conf
你好，RUNOOB
```

## 代码块 14

```kotlin
// 文件路径：Site.kt

class Site {

    // 只改 getter 的名字，Java 侧用 getSiteUrl()

    @get:JvmName("getSiteUrl")

    val url: String = "www.runoob.com"


    // 布尔属性，Java 侧是 isActive()

    val isActive: Boolean = true

}
```

## 代码块 15

```kotlin
// 文件路径：Greeter.kt

class Greeter {

    // 没有 @JvmOverloads：Java 只能写 greeter.greet("RUNOOB", "你好，")

    fun greet(name: String, prefix: String = "你好，"): String = "$prefix$name"


    // 有 @JvmOverloads：Java 可以只传 name

    @JvmOverloads

    fun greetShort(name: String, prefix: String = "你好，"): String = "$prefix$name"

}
```

## 代码块 16

```kotlin
// 文件路径：Main.java

public class Main {

    public static void main(String[] args) {

        Greeter greeter = new Greeter();

        System.out.println(greeter.greet("RUNOOB", "你好，"));

        System.out.println(greeter.greetShort("RUNOOB"));

        System.out.println(greeter.greetShort("RUNOOB", "欢迎，"));

    }

}
```

## 代码块 17

```kotlin
你好，RUNOOB
你好，RUNOOB
欢迎，RUNOOB
```

## 代码块 18

```kotlin
// 文件路径：Task.java

public interface Task {

    void run(String name);        // 只有一个抽象方法

}
```

## 代码块 19

```kotlin
// 文件路径：Main.kt


fun execute(task: Task) {

    task.run("RUNOOB")

}


// Kotlin 1.4 起可以用 fun interface 声明函数式接口

fun interface Printer {

    fun print(text: String)

}


fun main() {

    // Java 接口在 Kotlin 中直接传 lambda

    execute { name -> println("执行任务：$name") }


    // Kotlin 自己的 fun interface 同样支持 SAM 转换

    val printer = Printer { text -> println(text) }

    printer.print("www.runoob.com")

}
```

## 代码块 20

```kotlin
执行任务：RUNOOB
www.runoob.com
```

## 代码块 21

```kotlin
// 文件路径：Runner.kt

// Java 调用时只能传 Function0<Unit>，不太友好

fun runKotlinStyle(action: () -> Unit) {

    action()

}
```

## 代码块 22

```kotlin
// 文件路径：Main.java

import kotlin.Unit;

import kotlin.jvm.functions.Function0;


public class Main {

    public static void main(String[] args) {

        // Java 必须显式实现 Function0，还要 return Unit.INSTANCE

        RunnerKt.runKotlinStyle(new Function0<Unit>() {

            @Override

            public Unit invoke() {

                System.out.println("来自 Java 的调用");

                return Unit.INSTANCE;

            }

        });

    }

}
```

## 代码块 23

```kotlin
来自 Java 的调用
```
