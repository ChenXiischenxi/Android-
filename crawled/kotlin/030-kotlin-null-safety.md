# Kotlin 空安全

> 来源: https://www.runoob.com/kotlin/kotlin-null-safety.html

## 代码块 1

```kotlin
fun main() {

    val name: String = "Runoob"           // 非空，永远不可能是 null

    var site: String? = "www.runoob.com"  // 可空，可以赋值为 null


    // 非空类型直接访问成员，编译器保证安全

    println(name.length)


    // 可空类型必须用安全调用，直接写 site.length 会编译报错

    println(site?.length)


    site = null

    println(site?.length)

}
```

## 代码块 2

```kotlin
6
14
null
```

## 代码块 3

```kotlin
data class Address(val city: String, val zip: String?)

data class User(val name: String, val address: Address?)


fun main() {

    val user = User("Runoob", Address("北京", null))

    val noAddress = User("RUNOOB", null)


    println(user.address?.city)      // address 非空，输出城市

    println(noAddress.address?.city) // address 为 null，输出 null

    println(user.address?.zip?.length) // zip 为 null，输出 null

}
```

## 代码块 4

```kotlin
北京
null
null
```

## 代码块 5

```kotlin
// 为 null 或解析失败时抛出异常，右侧只在左侧为 null 时求值

fun parsePort(text: String?): Int {

    return text?.toIntOrNull() ?: throw IllegalArgumentException("端口不合法：$text")

}


fun main() {

    val nickname: String? = null

    val display = nickname ?: "游客"

    println(display)


    println(parsePort("8080"))

    println(runCatching { parsePort("abc") }.exceptionOrNull()?.message)

}
```

## 代码块 6

```kotlin
游客
8080
端口不合法：abc
```

## 代码块 7

```kotlin
fun welcome(name: String?): String {

    // name 为 null 时函数直接返回，后面的代码不会执行

    val safeName = name ?: return "名字不能为空"

    return "欢迎 $safeName"

}


fun main() {

    println(welcome("Runoob"))

    println(welcome(null))

}
```

## 代码块 8

```kotlin
欢迎 Runoob
名字不能为空
```

## 代码块 9

```kotlin
fun main() {

    val value: String? = "RUNOOB"

    // 确定非空时可以直接用，此处输出 6

    println(value!!.length)


    val empty: String? = null

    // 实际为 null，断言失败抛出 NullPointerException

    val result = runCatching { empty!!.length }

    println(result.exceptionOrNull()?.javaClass?.name)

}
```

## 代码块 10

```kotlin
6
java.lang.NullPointerException
```

## 代码块 11

```kotlin
fun main() {

    val email: String? = "[email protected]"

    val missing: String? = null


    // 非空才执行，it 已经是 String 而不是 String?

    email?.let { println("发送邮件到 $it") }

    missing?.let { println("发送邮件到 $it") }


    // 等价的 if 判空写法，Kotlin 会自动智能转换

    if (email != null) {

        println("长度：${email.length}")

    }

}
```

## 代码块 12

```kotlin
发送邮件到 [email protected]
长度：21
```

## 代码块 13

```kotlin
fun describe(value: Any): String {

    // 转换失败返回 null，不会抛异常

    val text = value as? String

    val number = value as? Int

    return "String=$text, Int=$number"

}


fun main() {

    println(describe("RUNOOB"))

    println(describe(42))

    println(describe(3.14))

}
```

## 代码块 14

```kotlin
String=RUNOOB, Int=null
String=null, Int=42
String=null, Int=null
```

## 代码块 15

```kotlin
fun lengthOf(value: Any): Int {

    // is 判断之后，value 在本分支内被智能转换为 String

    return if (value is String) value.length else -1

}


fun main() {

    println(lengthOf("Runoob"))

    println(lengthOf(100))

}
```

## 代码块 16

```kotlin
6
-1
```

## 代码块 17

```kotlin
// 文件路径：Site.java

public class Site {

    // 没有 @Nullable / @NotNull 注解，Kotlin 无法判断返回值是否可空

    public static String getName() {

        return null;

    }

}
```

## 代码块 18

```kotlin
fun main() {

    val result = runCatching {

        // Site.getName() 是平台类型 String!，编译通过

        val name: String = Site.getName()

        name.length

    }

    println("捕获到异常：${result.exceptionOrNull()?.javaClass?.name}")

    println("异常信息：${result.exceptionOrNull()?.message}")

}
```

## 代码块 19

```kotlin
捕获到异常：java.lang.NullPointerException
异常信息：getName(...) must not be null
```

## 代码块 20

```kotlin
fun main() {

    // 主动声明为 String?，把判断权交回给编译器

    val name: String? = Site.getName()

    println("站点名称：${name ?: "未命名"}")


    // 也可以交给安全调用与 Elvis 处理

    println("名称长度：${name?.length ?: 0}")

}
```

## 代码块 21

```kotlin
站点名称：未命名
名称长度：0
```

## 代码块 22

```kotlin
class UserService {

    // lateinit 只能修饰 var，不能修饰基本类型，也不能是可空类型

    lateinit var siteName: String


    fun init(name: String) {

        siteName = name

    }


    fun printInfo() {

        // 用 ::属性名.isInitialized 判断是否已初始化

        if (::siteName.isInitialized) {

            println("站点：$siteName")

        } else {

            println("站点尚未初始化")

        }

    }

}


fun main() {

    val service = UserService()

    service.printInfo()

    service.init("www.runoob.com")

    service.printInfo()

}
```

## 代码块 23

```kotlin
站点尚未初始化
站点：www.runoob.com
```

## 代码块 24

```kotlin
fun main() {

    val names: List<String> = listOf("Runoob", "RUNOOB")

    val maybeNames: List<String>? = null

    val namesWithNull: List<String?> = listOf("Runoob", null, "RUNOOB")


    println(names.size)

    println(maybeNames?.size)

    println(namesWithNull.size)

    println(namesWithNull[1])          // 元素是 String?，输出 null


    // Map 取值返回可空类型，键不存在时就是 null

    val scores = mapOf("Runoob" to 90)

    println(scores["RUNOOB"])

    println(scores["RUNOOB"] ?: 0)


    // filterNotNull 过滤掉 null 元素，返回 List<String>

    val cleaned: List<String> = namesWithNull.filterNotNull()

    println(cleaned)

}
```

## 代码块 25

```kotlin
2
null
3
null
null
0
[Runoob, RUNOOB]
```
