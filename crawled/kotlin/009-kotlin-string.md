# Kotlin 字符串与正则

> 来源: https://www.runoob.com/kotlin/kotlin-string.html

## 代码块 1

```kotlin
fun main() {

    val site = "Runoob"


    // 调用 uppercase 得到新字符串，原字符串不受影响

    val upper = site.uppercase()

    println(site)         // Runoob

    println(upper)        // RUNOOB


    // 用方括号按下标取字符，下标从 0 开始

    println(site[0])      // R

    println(site.length)  // 6


    // 用 for 遍历每一个字符

    for (c in site) {

        print(c)

    }

    println()             // 输出换行

}
```

## 代码块 2

```kotlin
Runoob
RUNOOB
R
6
Runoob
```

## 代码块 3

```kotlin
fun main() {

    val a = "runoob"

    val b = "runoob"

    val c = String(charArrayOf('r', 'u', 'n', 'o', 'o', 'b'))


    println(a == b)    // true，内容相同

    println(a == c)    // true，内容相同

    println(a === c)   // false，c 是运行时新建的对象

}
```

## 代码块 4

```kotlin
true
true
false
```

## 代码块 5

```kotlin
fun main() {

    // 转义字符串：\n 会被解释为换行

    val escaped = "第一行\n第二行"

    println(escaped)


    // 原始字符串：内容原样保留，包括换行

    val raw = """第一行

第二行"""

    println(raw)


    // 原始字符串里可以直接写反斜杠，不需要转义

    val path = """C:\Users\runoob\kotlin"""

    println(path)


    // 写 JSON 时特别方便

    val json = """{"site": "www.runoob.com"}"""

    println(json)


    // 原始字符串中 $ 仍然是模板起始符，输出字面量 $ 要写成 ${'$'}

    val price = """${'$'}9.99"""

    println(price)

}
```

## 代码块 6

```kotlin
第一行
第二行
第一行
第二行
C:\Users\runoob\kotlin
{"site": "www.runoob.com"}
$9.99
```

## 代码块 7

```kotlin
fun main() {

    // trimIndent：去掉公共缩进

    val text = """

        Runoob

        www.runoob.com

        RUNOOB

    """.trimIndent()

    println(text)


    // trimMargin：默认以 | 作为边界前缀

    val margin = """

        |Runoob

        |www.runoob.com

        |RUNOOB

    """.trimMargin()

    println(margin)


    // 也可以自定义边界前缀

    val custom = """

        >Runoob

        >RUNOOB

    """.trimMargin(">")

    println(custom)

}
```

## 代码块 8

```kotlin
Runoob
www.runoob.com
RUNOOB
Runoob
www.runoob.com
RUNOOB
Runoob
RUNOOB
```

## 代码块 9

```kotlin
fun main() {

    val siteName = "Runoob"

    val age = 10


    println("站点：$siteName")                    // 站点：Runoob

    println("$siteName 已上线 $age 年")           // Runoob 已上线 10 年


    // 复杂表达式用花括号包起来

    println("$siteName 长度是 ${siteName.length}")  // Runoob 长度是 6

    println("明年是第 ${age + 1} 年")               // 明年是第 11 年


    // 模板里也可以调用函数

    println("大写：${siteName.uppercase()}")        // 大写：RUNOOB


    // 输出字面量 $ 需要转义

    println("价格：\$9.99")                        // 价格：$9.99

}
```

## 代码块 10

```kotlin
站点：Runoob
Runoob 已上线 10 年
Runoob 长度是 6
明年是第 11 年
大写：RUNOOB
价格：$9.99
```

## 代码块 11

```kotlin
fun main() {

    val s = "  Runoob Kotlin  "


    println(s.length)                       // 17

    println(s.trim())                       // Runoob Kotlin

    println(s.trim().lowercase())           // runoob kotlin

    println(s.trim().uppercase())           // RUNOOB KOTLIN

    println(s.contains("runoob"))           // false，区分大小写

    println(s.trim().startsWith("Run"))     // true

    println(s.trim().endsWith("lin"))       // true

    println(s.trim().substring(0, 6))       // Runoob

    println(s.trim().replace("Kotlin", "RUNOOB"))  // Runoob RUNOOB

    println(s.trim().indexOf("Kotlin"))     // 7

    println("7".padStart(3, '0'))           // 007

    println("ab".repeat(3))                 // ababab

    println("a,b,c".split(","))             // [a, b, c]

    println("".isEmpty())                   // true

    println("   ".isBlank())                // true

}
```

## 代码块 12

```kotlin
17
Runoob Kotlin
runoob kotlin
RUNOOB KOTLIN
false
true
true
Runoob
Runoob RUNOOB
7
007
ababab
[a, b, c]
true
true
```

## 代码块 13

```kotlin
fun main() {

    // 多个分隔符

    println("a,b;c".split(",", ";"))          // [a, b, c]


    // 用正则作为分隔符

    println("a1b2c3".split(Regex("""\d""")))  // [a, b, c]


    // 限制返回元素个数，最后一个元素保留剩余内容

    println("a,b,c,d".split(",", limit = 3))  // [a, b, c,d]

}
```

## 代码块 14

```kotlin
[a, b, c]
[a, b, c]
[a, b, c,d]
```

## 代码块 15

```kotlin
fun main() {

    val name = "Runoob"

    val score = 95.5


    // String.format：占位符依次对应后面的参数

    val s1 = String.format("%s 的得分是 %.2f", name, score)

    println(s1)


    // 字符串的 format 扩展函数，写法更紧凑

    val s2 = "站点：%s，得分：%d".format(name, 96)

    println(s2)


    // %-10s 表示左对齐、宽度 10；%05d 表示不足 5 位左侧补 0

    println("%-10s|".format("runoob"))

    println("%05d".format(42))


    // %x 输出十六进制

    println("%x".format(255))

}
```

## 代码块 16

```kotlin
Runoob 的得分是 95.50
站点：Runoob，得分：96
runoob    |
00042
ff
```

## 代码块 17

```kotlin
fun main() {

    // 原始字符串中的 \d 就是正则的数字，不需要写 \\d

    val regex = Regex("""\d+""")


    // matches：整个字符串是否匹配

    println(regex.matches("12345"))             // true

    println(regex.matches("abc123"))            // false


    // containsMatchIn：是否包含任意一处匹配

    println(regex.containsMatchIn("订单号 abc123"))  // true


    // 等价写法：用 toRegex() 把字符串转成正则

    val same = """\d+""".toRegex()

    println(same.matches("2026"))               // true

}
```

## 代码块 18

```kotlin
true
false
true
true
```

## 代码块 19

```kotlin
fun main() {

    val regex = Regex("""\d+""")

    val text = "Runoob 2026 年 9 月 8 日"


    // find 返回 MatchResult?，可能为 null

    val first = regex.find(text)

    println(first?.value)                              // 2026

    println(first?.range)                              // 7..10


    // findAll 返回 Sequence<MatchResult>，用 map 取出内容

    val all = regex.findAll(text).map { it.value }.toList()

    println(all)                                       // [2026, 9, 8]


    // 也可以只取前两个

    val firstTwo = regex.findAll(text).take(2).map { it.value }.toList()

    println(firstTwo)                                  // [2026, 9]

}
```

## 代码块 20

```kotlin
2026
7..10
[2026, 9, 8]
[2026, 9]
```

## 代码块 21

```kotlin
fun main() {

    val regex = Regex("""\d+""")


    // 替换所有匹配

    println(regex.replace("a1b2c3", "#"))          // a#b#c#


    // 用 lambda 自定义替换内容，it 是匹配结果

    println(regex.replace("a1b2c3") { "<${it.value}>" })  // a<1>b<2>c<3>


    // 按匹配切分

    println("a1b2c3".split(regex))                 // [a, b, c]


    // 只替换第一个匹配

    println(regex.replaceFirst("a1b2", "#"))       // a#b2

}
```

## 代码块 22

```kotlin
a#b#c#
a<1>b<2>c<3>
[a, b, c]
a#b2
```

## 代码块 23

```kotlin
fun main() {

    // 三个捕获组：年、月、日

    val regex = Regex("""(\d{4})-(\d{2})-(\d{2})""")


    // matchEntire 要求整个字符串完全匹配

    val match = regex.matchEntire("2026-09-08")

    if (match != null) {

        println(match.groupValues)        // [2026-09-08, 2026, 09, 08]

        println(match.groupValues[1])     // 2026

        println(match.groupValues[2])     // 09

        println(match.groupValues[3])     // 08

    }


    // 命名捕获组写法：(?<名称>...)

    val named = Regex("""(?<year>\d{4})-(?<month>\d{2})""")

    val m = named.find("日期：2026-09")!!

    println(m.groups["year"]?.value)      // 2026

    println(m.groups["month"]?.value)     // 09

}
```

## 代码块 24

```kotlin
[2026-09-08, 2026, 09, 08]
2026
09
08
2026
09
```

## 代码块 25

```kotlin
fun main() {

    // IGNORE_CASE：忽略大小写

    val regex = Regex("runoob", RegexOption.IGNORE_CASE)

    println(regex.containsMatchIn("欢迎来到 RUNOOB"))   // true

    println(regex.matches("RUNOOB"))                    // true


    // 多个选项用 setOf 传入

    val multi = Regex("""^\d+""", setOf(RegexOption.MULTILINE))

    val text = "123\n456"

    println(multi.findAll(text).map { it.value }.toList())  // [123, 456]

}
```

## 代码块 26

```kotlin
true
true
[123, 456]
```
