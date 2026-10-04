# Kotlin 测试

> 来源: https://www.runoob.com/kotlin/kotlin-testing.html

## 代码块 1

```kotlin
// 文件路径：build.gradle.kts


plugins {

    kotlin("jvm") version "2.2.0"

}


repositories {

    mavenCentral()

}


dependencies {

    // kotlin.test 统一断言 API，版本随 Kotlin 插件自动确定

    testImplementation(kotlin("test"))

    // JUnit 5 聚合包，包含 API 与运行引擎

    testImplementation("org.junit.jupiter:junit-jupiter:5.11.4")

}


tasks.test {

    // Kotlin 1.5 起，使用 JUnit 5 必须显式声明测试平台

    useJUnitPlatform()

}
```

## 代码块 2

```kotlin
// 文件路径：src/main/kotlin/com/runoob/Calculator.kt

package com.runoob


class Calculator {

    // 两数相加

    fun add(a: Int, b: Int): Int = a + b


    // 两数相除；除数为 0 时抛出异常

    fun divide(a: Int, b: Int): Int {

        require(b != 0) { "除数不能为 0" }

        return a / b

    }

}
```

## 代码块 3

```kotlin
// 文件路径：src/test/kotlin/com/runoob/CalculatorTest.kt

package com.runoob


import kotlin.test.Test

import kotlin.test.assertEquals

import kotlin.test.assertFailsWith

import kotlin.test.assertTrue


class CalculatorTest {


    // 每个测试方法执行前都会重新创建这个实例

    private val calculator = Calculator()


    @Test

    fun addReturnsSumOfTwoNumbers() {

        // assertEquals(期望值, 实际值)

        assertEquals(5, calculator.add(2, 3))

        assertEquals(0, calculator.add(-1, 1))

    }


    @Test

    fun divideByZeroThrowsException() {

        // assertFailsWith 断言代码块抛出指定异常，并返回该异常对象

        val error = assertFailsWith<IllegalArgumentException> {

            calculator.divide(10, 0)

        }

        assertEquals("除数不能为 0", error.message)

    }


    @Test

    fun divideReturnsPositiveResult() {

        assertTrue(calculator.divide(10, 2) > 0)

    }

}
```

## 代码块 4

```kotlin
$ ./gradlew test

> Task :test
BUILD SUCCESSFUL in 2s

3 tests completed
```

## 代码块 5

```kotlin
$ ./gradlew test

> Task :test FAILED

CalculatorTest > addReturnsSumOfTwoNumbers FAILED
    java.lang.AssertionError at CalculatorTest.kt:16
        expected: 6 but was: 5

BUILD FAILED in 2s
```

## 代码块 6

```kotlin
// 第三个参数是失败时显示的消息，便于排查

assertEquals(5, calculator.add(2, 3), "2 + 3 应该等于 5")
```

## 代码块 7

```kotlin
// 文件路径：src/test/kotlin/com/runoob/SiteTest.kt

package com.runoob


import kotlin.test.AfterTest

import kotlin.test.BeforeTest

import kotlin.test.Test

import kotlin.test.assertEquals


class SiteTest {


    // 测试数据容器，每个测试方法执行前都会重建

    private lateinit var sites: MutableList<String>


    @BeforeTest

    fun setUp() {

        // 每个测试方法都从干净的数据开始，避免测试之间互相影响

        sites = mutableListOf("Runoob", "RUNOOB")

    }


    @AfterTest

    fun tearDown() {

        // 清理数据，释放内存

        sites.clear()

    }


    @Test

    fun addSiteIncreasesSize() {

        sites.add("www.runoob.com")

        assertEquals(3, sites.size)

    }


    @Test

    fun sitesStartWithTwoElements() {

        // 因为 setUp 每个方法都执行，这里始终是 2

        assertEquals(2, sites.size)

    }

}
```

## 代码块 8

```kotlin
// 文件路径：src/test/kotlin/com/runoob/CalculatorParameterizedTest.kt

package com.runoob


import org.junit.jupiter.params.ParameterizedTest

import org.junit.jupiter.params.provider.CsvSource

import kotlin.test.assertEquals


class CalculatorParameterizedTest {


    private val calculator = Calculator()


    // 每一行 CSV 数据都会执行一次测试方法

    @ParameterizedTest(name = "{0} + {1} = {2}")

    @CsvSource(

        "1, 2, 3",

        "0, 0, 0",

        "-1, 1, 0",

        "100, 200, 300"

    )

    fun addReturnsExpectedSum(a: Int, b: Int, expected: Int) {

        assertEquals(expected, calculator.add(a, b))

    }

}
```

## 代码块 9

```kotlin
$ ./gradlew test

> Task :test
CalculatorParameterizedTest > 1 + 2 = 3 PASSED
CalculatorParameterizedTest > 0 + 0 = 0 PASSED
CalculatorParameterizedTest > -1 + 1 = 0 PASSED
CalculatorParameterizedTest > 100 + 200 = 300 PASSED

BUILD SUCCESSFUL in 2s
```

## 代码块 10

```kotlin
// 文件路径：build.gradle.kts


dependencies {

    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.10.2")

    testImplementation(kotlin("test"))

    // 协程测试库，提供 runTest 与测试调度器

    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.10.2")

}
```

## 代码块 11

```kotlin
// 文件路径：src/test/kotlin/com/runoob/GreetTest.kt

package com.runoob


import kotlinx.coroutines.delay

import kotlinx.coroutines.test.runTest

import kotlin.test.Test

import kotlin.test.assertEquals


// 被测的挂起函数

suspend fun greet(name: String): String {

    delay(1000)   // 模拟耗时操作，runTest 中会被虚拟时间跳过

    return "Hello, $name"

}


class GreetTest {


    @Test

    fun greetReturnsGreeting() = runTest {

        // 整个测试瞬间完成，不会真的等待 1 秒

        assertEquals("Hello, Runoob", greet("Runoob"))

    }

}
```

## 代码块 12

```kotlin
$ ./gradlew test --tests "com.runoob.CalculatorTest"

> Task :test
BUILD SUCCESSFUL in 1s

3 tests completed, 3 passed
```
