# Kotlin 运算符与位运算

> 来源: https://www.runoob.com/kotlin/kotlin-operators.html

## 代码块 1

```kotlin
fun main() {

    println(7 + 3)      // 10

    println(7 - 3)      // 4

    println(7 * 3)      // 21

    println(7 / 3)      // 2，整数除法直接截断小数部分

    println(7 % 3)      // 1，取余

    println(7.0 / 3)    // 2.3333333333333335，有一个是浮点结果就是浮点

    println(-7 % 3)     // -1，余数的符号与被除数一致


    // 整数除以零会抛异常

    // println(1 / 0)   // 抛出 ArithmeticException: / by zero

    // 浮点除以零不会抛异常

    println(1.0 / 0.0)  // Infinity

    println(0.0 / 0.0)  // NaN


    // 一元运算符

    println(-5)         // -5

    println(+5)         // 5


    // 自增自减

    var i = 1

    println(i++)        // 1，先取值再加 1

    println(i)          // 2

    println(++i)        // 3，先加 1 再取值

    println(i--)        // 3

    println(i)          // 2

}
```

## 代码块 2

```kotlin
10
4
21
2
1
2.3333333333333335
-1
Infinity
NaN
-5
5
1
2
3
3
2
```

## 代码块 3

```kotlin
fun main() {

    val done = 3

    val total = 4


    // 两个 Int 相除，结果被截断成 0

    println(done / total)                    // 0


    // 先转成 Double 再做除法

    println(done.toDouble() / total)         // 0.75


    // 或者用乘法先放大

    println(done * 100 / total)              // 75

}
```

## 代码块 4

```kotlin
0
0.75
75
```

## 代码块 5

```kotlin
fun main() {

    var a = 10


    a += 5      // 等价于 a = a + 5

    println(a)  // 15


    a -= 3

    println(a)  // 12


    a *= 2

    println(a)  // 24


    a /= 5

    println(a)  // 4


    a %= 3

    println(a)  // 1

}
```

## 代码块 6

```kotlin
15
12
24
4
1
```

## 代码块 7

```kotlin
fun main() {

    println(3 == 3)           // true

    println(3 != 4)           // true

    println(3 < 4)            // true

    println(3 > 4)            // false

    println(3 <= 3)           // true

    println(3 >= 4)           // false


    // 字符串按字典序比较

    println("abc" < "abd")    // true


    // 不同类型可以用大小比较，走的是 compareTo 重载

    println(3 < 3.5)          // true

}
```

## 代码块 8

```kotlin
true
true
true
false
true
false
true
true
```

## 代码块 9

```kotlin
fun check(): Boolean {

    println("check 被调用")

    return true

}


fun main() {

    val t = true

    val f = false


    println(t && f)          // false

    println(t || f)          // true

    println(!t)              // false


    // 短路演示

    println(f && check())    // false，左侧已为 false，右侧不求值

    println(t || check())    // true，左侧已为 true，右侧不求值

    println(t && check())    // true，右侧必须求值

}
```

## 代码块 10

```kotlin
false
true
false
false
true
check 被调用
true
```

## 代码块 11

```kotlin
fun main() {

    val name: String? = null


    // 左侧为 false 时，右侧的 name.length 不会执行

    if (name != null && name.length > 0) {

        println("名字长度：${name.length}")

    } else {

        println("名字为空")   // 名字为空

    }

}
```

## 代码块 12

```kotlin
名字为空
```

## 代码块 13

```kotlin
fun main() {

    val a = 0b1100    // 十进制 12

    val b = 0b1010    // 十进制 10


    println(a and b)     // 8，0b1000

    println(a or b)      // 14，0b1110

    println(a xor b)     // 6，0b0110

    println(a.inv())     // -13，按位取反


    println(a shl 1)     // 24，左移一位等于乘 2

    println(a shr 1)     // 6，右移一位等于除以 2

    println(-8 shr 1)    // -4，有符号右移保留符号位

    println(-8 ushr 1)   // 2147483644，无符号右移高位补 0


    // 中缀函数优先级低于算术运算符

    println(1 + 2 shl 3) // 24，先算 1 + 2 再左移 3 位

}
```

## 代码块 14

```kotlin
8
14
6
-13
24
6
-4
2147483644
24
```

## 代码块 15

```kotlin
fun main() {

    val color = 0xFFCC00   // 一个 24 位的 RGB 颜色


    // 右移 16 位再取低 8 位，得到红色分量

    val red = (color shr 16) and 0xFF

    val green = (color shr 8) and 0xFF

    val blue = color and 0xFF


    println("R=$red G=$green B=$blue")   // R=255 G=204 B=0


    // 用位掩码表示多个开关

    val READ = 0b001

    val WRITE = 0b010

    val EXEC = 0b100


    var permission = READ or WRITE        // 拥有读和写权限

    println(permission)                   // 3

    println((permission and READ) != 0)   // true，有读权限

    println((permission and EXEC) != 0)   // false，没有执行权限

}
```

## 代码块 16

```kotlin
R=255 G=204 B=0
3
true
false
```

## 代码块 17

```kotlin
fun main() {

    val closed = 1..5

    println(closed)                    // 1..5

    println(5 in closed)               // true

    println(closed.toList())           // [1, 2, 3, 4, 5]


    val open = 1..<5

    println(open)                      // 1..4

    println(5 in open)                 // false

    println(open.toList())             // [1, 2, 3, 4]


    println((1 until 5).toList())      // [1, 2, 3, 4]

    println((5 downTo 1).toList())     // [5, 4, 3, 2, 1]

    println((1..10 step 3).toList())   // [1, 4, 7, 10]

    println((10 downTo 1 step 3).toList())  // [10, 7, 4, 1]


    // 字符也可以构成区间

    println(('a'..'e').toList())       // [a, b, c, d, e]

}
```

## 代码块 18

```kotlin
1..5
true
[1, 2, 3, 4, 5]
1..4
false
[1, 2, 3, 4]
[1, 2, 3, 4]
[5, 4, 3, 2, 1]
[1, 4, 7, 10]
[10, 7, 4, 1]
[a, b, c, d, e]
```

## 代码块 19

```kotlin
fun main() {

    // 判断数字是否在区间内

    println(3 in 1..5)                  // true

    println(9 !in 1..5)                 // true


    // 判断字符是否在字符区间内

    println('c' in 'a'..'z')            // true

    println('C' in 'a'..'z')            // false


    // 判断子串是否出现在字符串中

    val site = "www.runoob.com"

    println("runoob" in site)           // true

    println("RUNOOB" in site)           // false，区分大小写

    println('r' in site)                // true


    // 判断元素是否在集合中

    val names = listOf("Runoob", "Kotlin")

    println("Runoob" in names)          // true

    println("Java" !in names)           // true

}
```

## 代码块 20

```kotlin
true
true
true
false
true
false
true
true
true
```

## 代码块 21

```kotlin
fun main() {

    // && 的优先级高于 ||

    println(true || false && false)     // true，等价于 true || (false && false)


    // 区间运算符的优先级高于中缀函数

    println(1..5 step 2)                // 1..5 step 2


    // 中缀函数优先级低于算术运算符

    println(1 + 2 shl 3)                // 24，等价于 (1 + 2) shl 3


    // 加括号让意图更清晰

    println((true || false) && false)   // false

}
```

## 代码块 22

```kotlin
true
1..5 step 2
24
false
```
