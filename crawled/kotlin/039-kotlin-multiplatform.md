# Kotlin 多平台与 Kotlin/JS、Native

> 来源: https://www.runoob.com/kotlin/kotlin-multiplatform.html

## 代码块 1

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("jvm") version "2.2.0"

}


kotlin {

    compilerOptions {

        // 生成的字节码版本，按项目实际运行环境调整

        jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17)

    }

}
```

## 代码块 2

```kotlin
// 文件路径：src/jsMain/kotlin/Main.kt


// external 声明：告诉 Kotlin 这个 API 由 JavaScript 提供

// 编译器只做类型检查，不生成实现

external fun alert(message: String)


external class Console {

    fun log(message: String)

}


external val console: Console


// @JsExport：把函数导出给 JavaScript 调用

@JsExport

fun greetFromKotlin(name: String): String = "你好，$name"


@JsExport

fun showMessage(text: String) {

    console.log("RUNOOB 提示：$text")

    alert(text)

}
```

## 代码块 3

```kotlin
// 文件路径：index.js

// Kotlin/JS 打包后会生成一个 ES 模块

import { greetFromKotlin } from './kotlin-app.mjs';


console.log(greetFromKotlin('RUNOOB'));   // 输出：你好，RUNOOB
```

## 代码块 4

```kotlin
你好，RUNOOB
```

## 代码块 5

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("multiplatform") version "2.2.0"

}


kotlin {

    js {                              // Kotlin/JS 目标（IR 是唯一后端）

        browser {                     // 浏览器环境

            binaries.executable()     // 生成可直接运行的产物

        }

    }

}
```

## 代码块 6

```kotlin
// 文件路径：src/nativeInterop/cinterop/runoob.h

#ifndef RUNOOB_H

#define RUNOOB_H


// 返回库的版本号

int runoob_version(void);


// 把两个整数相加

int runoob_add(int a, int b);


#endif
```

## 代码块 7

```kotlin
# 文件路径：src/nativeInterop/cinterop/runoob.def
headers = runoob.h
package = runoob
```

## 代码块 8

```kotlin
// 文件路径：src/nativeMain/kotlin/main.kt

import runoob.runoob_add

import runoob.runoob_version


fun main() {

    println("C 库版本：${runoob_version()}")

    println("runoob_add(3, 4) = ${runoob_add(3, 4)}")

}
```

## 代码块 9

```kotlin
C 库版本：1
runoob_add(3, 4) = 7
```

## 代码块 10

```kotlin
// 文件路径：src/iosMain/kotlin/Greeter.kt

class Greeter {

    fun greet(name: String): String = "你好，$name"


    // @Throws 让 Swift 侧看到受检异常

    @Throws(IllegalArgumentException::class)

    fun check(age: Int): Int {

        require(age > 0) { "年龄必须大于 0" }

        return age

    }

}
```

## 代码块 11

```kotlin
// 文件路径：iosApp/GreeterView.swift

import shared                       // Kotlin/Native 生成的 framework


let greeter = Greeter()

print(greeter.greet(name: "RUNOOB"))
```

## 代码块 12

```kotlin
你好，RUNOOB
```

## 代码块 13

```kotlin
// 文件路径：build.gradle.kts

kotlin {

    wasmJs {                      // 浏览器方向的 Wasm 目标

        browser {

            binaries.executable()

        }

    }

}
```

## 代码块 14

```kotlin
// 文件路径：src/commonMain/kotlin/Platform.kt

// expect：只声明不实现，各平台必须提供对应的 actual

expect fun platformName(): String


expect val isDesktop: Boolean


fun greeting(): String = "欢迎使用 Kotlin 多平台，当前平台：$platformName"
```

## 代码块 15

```kotlin
// 文件路径：src/jvmMain/kotlin/Platform.kt

actual fun platformName(): String = "Kotlin/JVM"


actual val isDesktop: Boolean = true
```

## 代码块 16

```kotlin
// 文件路径：src/jsMain/kotlin/Platform.kt

actual fun platformName(): String = "Kotlin/JS"


actual val isDesktop: Boolean = false
```

## 代码块 17

```kotlin
// 文件路径：src/jvmMain/kotlin/Main.kt

fun main() {

    println(greeting())

    println("isDesktop = $isDesktop")

}
```

## 代码块 18

```kotlin
欢迎使用 Kotlin 多平台，当前平台：Kotlin/JVM
isDesktop = true
```

## 代码块 19

```kotlin
runoob-multiplatform/
├── build.gradle.kts              # 根构建脚本，声明目标平台
├── settings.gradle.kts
├── gradle/
│   └── libs.versions.toml        # 版本目录，集中管理依赖版本
└── src/
    ├── commonMain/kotlin/        # 所有平台共享的代码
    │   └── Platform.kt
    ├── commonTest/kotlin/        # 共享测试
    ├── jvmMain/kotlin/           # 仅 JVM 平台
    ├── jsMain/kotlin/            # 仅 Kotlin/JS
    ├── nativeMain/kotlin/        # 所有 Kotlin/Native 目标共享
    └── iosMain/kotlin/           # 仅 iOS 目标
```

## 代码块 20

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("multiplatform") version "2.2.0"

}


kotlin {

    // 声明需要编译的目标平台

    jvm()                                        // 桌面 / 服务端

    js { browser(); binaries.executable() }       // 浏览器

    wasmJs { browser() }                         // WebAssembly（Beta）

    iosArm64()                                   // iPhone 真机

    iosSimulatorArm64()                          // Apple 芯片模拟器

    macosArm64()                                 // Apple 芯片 macOS


    sourceSets {

        // 所有平台共享的依赖

        commonMain.dependencies {

            implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.10.2")

        }

        // 仅 JVM 平台的依赖

        jvmMain.dependencies {

            implementation("com.google.code.gson:gson:2.11.0")

        }

        // 共享测试

        commonTest.dependencies {

            implementation(kotlin("test"))

        }

    }

}
```
