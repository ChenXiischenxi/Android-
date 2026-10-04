# Kotlin Gradle 构建

> 来源: https://www.runoob.com/kotlin/kotlin-gradle.html

## 代码块 1

```kotlin
runoob-demo/
├── build.gradle.kts          # 构建脚本，声明插件、依赖、任务
├── settings.gradle.kts       # 项目名与子模块声明
├── gradle.properties         # 可选，构建参数与 JVM 参数
├── gradlew                   # Linux/macOS 下的 Gradle Wrapper 脚本
├── gradlew.bat               # Windows 下的 Gradle Wrapper 脚本
├── gradle/wrapper/           # Wrapper 的 jar 与版本配置
└── src
    ├── main/kotlin/          # 主源码集，参与最终产物
    │   └── com/runoob/Main.kt
    └── test/kotlin/          # 测试源码集，不进入最终产物
        └── com/runoob/MainTest.kt
```

## 代码块 2

```kotlin
// 文件路径：build.gradle.kts


plugins {

    // Kotlin/JVM 插件，2.2.0 是本章节的版本基准

    kotlin("jvm") version "2.2.0"

    // application 插件会生成 run 任务，让项目可以直接启动

    application

}


group = "com.runoob"    // 组织标识，影响发布时的坐标

version = "1.0.0"       // 项目版本号


repositories {

    // 依赖仓库，mavenCentral 是绝大多数开源库的所在地

    mavenCentral()

}


dependencies {

    // 测试依赖，只在 test 源码集可见

    testImplementation(kotlin("test"))

}


kotlin {

    // 锁定编译使用的 JDK 版本，避免不同机器结果不一致

    jvmToolchain(17)

}


application {

    // 主类全名，Kotlin 顶层 main 函数编译后类名带 Kt 后缀

    mainClass.set("com.runoob.MainKt")

}
```

## 代码块 3

```kotlin
// 文件路径：settings.gradle.kts


// 项目名，影响构建产物的默认名称

rootProject.name = "runoob-demo"
```

## 代码块 4

```kotlin
// 文件路径：src/main/kotlin/com/runoob/Main.kt

package com.runoob


fun main() {

    println("Hello, Runoob!")

    println("网站：www.runoob.com")

}
```

## 代码块 5

```kotlin
$ ./gradlew run

> Task :run
Hello, Runoob!
网站：www.runoob.com

BUILD SUCCESSFUL in 1s
```

## 代码块 6

```kotlin
// 文件路径：build.gradle.kts


dependencies {

    // 主代码使用：协程库

    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.10.2")


    // 公共 API 中直接暴露序列化类型，所以用 api

    api("org.jetbrains.kotlinx:kotlinx-serialization-json:1.8.0")


    // 仅测试使用：JUnit 5

    testImplementation("org.junit.jupiter:junit-jupiter:5.11.4")


    // 运行时才需要：MySQL 驱动，编译期代码里不出现它的类

    runtimeOnly("com.mysql:mysql-connector-j:9.1.0")

}
```

## 代码块 7

```kotlin
# 文件路径：gradle/libs.versions.toml


[versions]

# 集中管理版本号，升级时只改这里

kotlin = "2.2.0"

coroutines = "1.10.2"

junit = "5.11.4"


[libraries]

# 依赖别名，供 build.gradle.kts 通过 libs.xxx 引用

coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "coroutines" }

junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }


[plugins]

# 插件别名，供 plugins 块引用

kotlin-jvm = { id = "org.jetbrains.kotlin.jvm", version.ref = "kotlin" }
```

## 代码块 8

```kotlin
// 文件路径：build.gradle.kts


plugins {

    // 引用版本目录中定义的插件别名

    alias(libs.plugins.kotlin.jvm)

    application

}


repositories {

    mavenCentral()

}


dependencies {

    implementation(libs.coroutines.core)

    testImplementation(libs.junit.jupiter)

}


application {

    mainClass.set("com.runoob.MainKt")

}
```

## 代码块 9

```kotlin
$ ./gradlew build

> Task :compileKotlin
> Task :compileJava NO-SOURCE
> Task :processResources
> Task :classes
> Task :jar
> Task :compileTestKotlin
> Task :test
> Task :check
> Task :build

BUILD SUCCESSFUL in 3s
```

## 代码块 10

```kotlin
// 文件路径：settings.gradle.kts


rootProject.name = "runoob-multi"


// 声明子模块，冒号表示目录层级

include(":app")     // 可执行程序模块

include(":core")    // 公共逻辑模块

include(":data")    // 数据访问模块
```

## 代码块 11

```kotlin
// 文件路径：app/build.gradle.kts


plugins {

    kotlin("jvm") version "2.2.0"

    application

}


dependencies {

    // 依赖同项目的 core 模块

    implementation(project(":core"))

    implementation(project(":data"))

}


application {

    mainClass.set("com.runoob.app.MainKt")

}
```

## 代码块 12

```kotlin
// 文件路径：build.gradle.kts（根项目）


// 对所有子项目统一配置

subprojects {

    repositories {

        mavenCentral()

    }

}
```

## 代码块 13

```kotlin
runoob-multi/
├── settings.gradle.kts
├── build.gradle.kts
├── app/
│   ├── build.gradle.kts
│   └── src/main/kotlin/...
├── core/
│   ├── build.gradle.kts
│   └── src/main/kotlin/...
└── data/
    ├── build.gradle.kts
    └── src/main/kotlin/...
```

## 代码块 14

```kotlin
// 文件路径：build.gradle.kts


repositories {

    // 镜像仓库放在前面，优先从镜像下载

    maven { url = uri("https://maven.aliyun.com/repository/public") }

    mavenCentral()

}
```
