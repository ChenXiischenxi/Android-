# Kotlin 基本数据类型

> 来源: https://www.runoob.com/kotlin/kotlin-basic-types.html

## 代码块 1

```kotlin
fun main() {

    val max = Int.MAX_VALUE      // Int 的最大值

    println(max)                 // 2147483647

    println(max + 1)             // -2147483648，溢出后绕回最小值


    val min = Int.MIN_VALUE      // Int 的最小值

    println(min)                 // -2147483648

    println(min - 1)             // 2147483647，向另一个方向溢出


    // 需要更大范围时使用 Long，注意先把 Int 转成 Long 再相加

    val big = Int.MAX_VALUE.toLong() + 1

    println(big)                 // 2147483648

}
```

## 代码块 2

```kotlin
2147483647
-2147483648
-2147483648
2147483647
2147483648
```

## 代码块 3

```kotlin
fun main() {

    val dec = 123                  // 十进制

    val hex = 0x0F                 // 十六进制，等于十进制的 15

    val bin = 0b00001011           // 二进制，等于十进制的 11

    val long = 123L                // Long 字面量

    val oneMillion = 1_000_000     // 下划线分隔，方便阅读


    // 十六进制和二进制同样可以用下划线分组

    val hexBytes = 0xFF_EC_DE

    val bytes = 0b1101_0010


    // 浮点字面量默认是 Double，加 f 后缀才是 Float

    val pi = 3.14

    val piFloat = 3.14f

    val sci = 123.5e10             // 科学计数法，等于 1.235E12


    println(dec)

    println(hex)

    println(bin)

    println(long)

    println(oneMillion)

    println(hexBytes)

    println(bytes)

    println(pi)

    println(piFloat)

    println(sci)

}
```

## 代码块 4

```kotlin
123
15
11
123
1000000
16772318
210
3.14
3.14
1.235E12
```

## 代码块 5

```kotlin
fun main() {

    val b: Byte = 1

    // val i: Int = b        // 编译错误：Kotlin 不会把 Byte 隐式转换为 Int

    val i: Int = b.toInt()   // 必须显式调用转换函数

    println(i)               // 1


    // 字面量是例外：编译器在编译期就能确认 100 在 Byte 范围内

    val b2: Byte = 100

    println(b2)              // 100


    // 算术运算可以混合类型，结果类型由操作数决定

    val l = 1L + 3           // Long + Int 得到 Long

    println(l)               // 4

}
```

## 代码块 6

```kotlin
1
100
4
```

## 代码块 7

```kotlin
fun main() {

    val i: Int = 65


    println(i.toByte())      // 65

    println(i.toShort())     // 65

    println(i.toLong())      // 65

    println(i.toFloat())     // 65.0

    println(i.toDouble())    // 65.0

    println(i.toChar())      // A，65 是字符 A 的码点


    // 浮点转整数会直接丢弃小数部分，而不是四舍五入

    val d: Double = 3.99

    println(d.toInt())       // 3

    println(d.toLong())      // 3


    // 超出目标类型范围时按位截断

    val big: Int = 300

    println(big.toByte())    // 44，300 超出 Byte 范围，保留低 8 位

}
```

## 代码块 8

```kotlin
65
65
65
65.0
65.0
A
3
3
44
```

## 代码块 9

```kotlin
fun main() {

    val u: UInt = 42u           // u 后缀，配合期望类型得到 UInt

    val ul: ULong = 1u          // 期望类型是 ULong，所以 1u 也按 ULong 处理

    val explicit: ULong = 1uL   // uL 后缀显式指定 ULong

    val byte: UByte = 0xFFu     // 期望类型是 UByte，255 在范围内

    val us: UShort = 1u         // 期望类型是 UShort


    println(u)                  // 42

    println(ul)                 // 1

    println(explicit)           // 1

    println(byte)               // 255

    println(us)                 // 1

    println(UInt.MAX_VALUE)     // 4294967295

    println(UByte.MIN_VALUE)    // 0

    println(u + 1u)             // 43，无符号运算

    println(u.toInt())          // 42，转回有符号 Int

}
```

## 代码块 10

```kotlin
42
1
1
255
1
4294967295
0
43
42
```

## 代码块 11

```kotlin
fun main() {

    val a: Int = 5

    val b: Int = 10


    println(a == b)      // false，结构相等比较的是值

    println(a != b)      // true

    println(a < b)       // true

    println(a > b)       // false

    println(a <= b)      // true

    println(a >= b)      // false


    // Int 是基本类型，=== 退化为和 == 相同

    val x: Int = 1000

    val y: Int = 1000

    println(x == y)      // true

    println(x === y)     // true，对基本类型 === 等价于 ==


    // 要观察引用相等，必须使用装箱类型 Int?

    val p: Int? = 1000

    val q: Int? = 1000

    println(p == q)      // true，值相等

    println(p === q)     // false，1000 超出缓存区间，两个不同的装箱对象


    val m: Int? = 100

    val n: Int? = 100

    println(m === n)     // true，命中 JVM Integer 缓存 -128..127

}
```

## 代码块 12

```kotlin
false
true
true
false
true
false
true
true
true
false
true
```

## 代码块 13

```kotlin
fun main() {

    val i: Int = 5

    val d: Double = 5.0


    // val bad = (i == d)      // 编译错误：Int 与 Double 不能直接用 == 比较


    // 大小比较可以跨类型，走的是 Int.compareTo(Double) 重载

    println(i < d)             // false

    println(i > 4.9)           // true

    println(i.compareTo(d))    // 0，相等时返回 0

}
```

## 代码块 14

```kotlin
false
true
0
```

## 代码块 15

```kotlin
fun main() {

    val t: Boolean = true

    val f: Boolean = false


    println(t && f)      // false

    println(t || f)      // true

    println(!t)          // false


    // 也可以使用函数形式

    println(t.and(f))    // false

    println(t.or(f))     // true

    println(t.xor(f))    // true，异或：两个值不同时为 true

    println(t.not())     // false

}
```

## 代码块 16

```kotlin
false
true
false
false
true
true
false
```

## 代码块 17

```kotlin
fun check(): Boolean {

    println("check 被调用")

    return true

}


fun main() {

    val f = false


    println(f && check())     // false，左侧已为 false，右侧不求值

    println(true || check())  // true，左侧已为 true，右侧不求值

    println(true && check())  // true，右侧必须求值

}
```

## 代码块 18

```kotlin
false
true
check 被调用
true
```

## 代码块 19

```kotlin
fun main() {

    val c: Char = 'A'


    println(c)                  // A

    println(c.code)             // 65，字符的 Unicode 码点

    println(c + 1)              // B，Char + Int 得到新的 Char

    println(c - 'A')            // 0，两个 Char 相减得到 Int

    println('5'.digitToInt())   // 5，把数字字符转换成数字


    // val n: Int = c           // 编译错误：Char 不能直接赋给 Int

    val n: Int = c.code

    println(n)                  // 65

}
```

## 代码块 20

```kotlin
A
65
B
0
5
65
```

## 代码块 21

```kotlin
fun main() {

    println("换行符：\n第二行")        // 输出两行

    println("反斜杠：\\")              // 反斜杠：\

    println("双引号：\"")              // 双引号："

    println("美元符号：\$")            // 美元符号：$

    println("Unicode 转义：\u0041")    // Unicode 转义：A

}
```

## 代码块 22

```kotlin
换行符：
第二行
反斜杠：\
双引号："
美元符号：$
Unicode 转义：A
```

## 代码块 23

```kotlin
fun main() {

    // arrayOf 根据元素推断类型，得到 Array<Int>

    val a = arrayOf(1, 2, 3)


    // Array(3) { ... } 是工厂函数：it 是下标，从 0 开始

    val b = Array(3) { it * 2 }        // [0, 2, 4]


    println(a[0])                      // 1

    println(b[1])                      // 2

    println(a.size)                    // 3

    println(b.contentToString())       // [0, 2, 4]


    // 方括号等价于调用 get 和 set

    a[0] = 100

    println(a[0])                      // 100

    println(a.contentToString())       // [100, 2, 3]


    // 基本类型数组避免装箱，性能更好

    val ints: IntArray = intArrayOf(1, 2, 3)

    ints[0] = ints[1] + ints[2]

    println(ints.contentToString())    // [5, 2, 3]

}
```

## 代码块 24

```kotlin
1
2
3
[0, 2, 4]
100
[100, 2, 3]
[5, 2, 3]
```

## 代码块 25

```kotlin
fun main() {

    val zeros = IntArray(3) { 0 }           // 指定长度和初始化函数

    val squares = IntArray(5) { it * it }   // it 是下标

    val names = Array(3) { "RUNOOB" }       // 每个元素都用同一个表达式初始化

    val nulls = arrayOfNulls<String>(2)     // 元素全部为 null


    println(zeros.contentToString())        // [0, 0, 0]

    println(squares.contentToString())      // [0, 1, 4, 9, 16]

    println(names.contentToString())        // [RUNOOB, RUNOOB, RUNOOB]

    println(nulls.contentToString())        // [null, null]


    // 二维数组：元素本身还是数组

    val grid = Array(2) { IntArray(3) { 0 } }

    grid[1][2] = 9

    println(grid[1].contentToString())      // [0, 0, 9]

}
```

## 代码块 26

```kotlin
[0, 0, 0]
[0, 1, 4, 9, 16]
[RUNOOB, RUNOOB, RUNOOB]
[null, null]
[0, 0, 9]
```

## 代码块 27

```kotlin
fun main() {

    val strings = arrayOf("Runoob", "www.runoob.com")


    // val anys: Array<Any> = strings   // 编译错误：数组不协变


    // 需要 Array<Any> 时，只能显式复制元素

    val anys: Array<Any> = Array(strings.size) { strings[it] }

    println(anys.contentToString())     // [Runoob, www.runoob.com]

}
```

## 代码块 28

```kotlin
[Runoob, www.runoob.com]
```

## 代码块 29

```kotlin
val a: Int = 100
println(a === a) // true，值相等，对象地址相等

//经过了装箱，创建了两个不同的对象
val boxedA: Int? = a
val anotherBoxedA: Int? = a

//虽然经过了装箱，但是值是相等的，都是100
println(boxedA === anotherBoxedA) //  true，值相等，128 之前对象地址一样
println(boxedA == anotherBoxedA) // true，值相等
```

## 代码块 30

```kotlin
val a = 10000//不显示声明类型不会封装新对象
val boxedA = a
val anotherBoxedA = a
println(boxedA === anotherBoxedA) //  true
```

## 代码块 31

```kotlin
val num: Int = 10000
val num1: Int = num
val num2: Int = num
println(num1 === num2)  //true
```

## 代码块 32

```kotlin
// Int? Int? Int?
val a1: Int? = 128
var boxedA: Int? = a1
var boxedB: Int? = a1
log(" boxedA === boxedB ? " + (boxedA === boxedB))//true
log(" boxedA == boxedB ? " + (boxedA == boxedB))//true

// Int Int? Int?
val a2: Int = 128
boxedA = a2
boxedB = a2
log(" boxedA === boxedB ? " + (boxedA === boxedB))//false
//值相等
log(" boxedA == boxedB ? " + (boxedA == boxedB))//true

// Int? Int? Int?
val a3: Int? = 127
boxedA = a3
boxedB = a3
log(" boxedA === boxedB ? " + (boxedA === boxedB))//true
//值相等
log(" boxedA == boxedB ? " + (boxedA == boxedB))//true

// Int Int? Int?
val a4: Int = 127
boxedA = a4
boxedB = a4
log(" boxedA === boxedB ? " + (boxedA === boxedB))//true
//值相等
log(" boxedA == boxedB ? " + (boxedA == boxedB))//true


// Int Int Int
val a5: Int = 128
val boxedA2: Int = a5
val boxedB2: Int = a5

log(" boxedA === boxedB ? " + (boxedA2 === boxedB2))//true
//值相等
log(" boxedA == boxedB ? " + (boxedA2 == boxedB2))//true
```
