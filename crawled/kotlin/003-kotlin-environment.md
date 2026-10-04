# Kotlin 环境搭建

> 来源: https://www.runoob.com/kotlin/kotlin-environment.html

## 代码块 1

```kotlin
// 在线运行的最小示例

fun main() {

    val siteName = "菜鸟教程"                  // 声明不可变变量

    println("Hello, $siteName!")               // 字符串模板

    println("网址：www.runoob.com")

}
```

## 代码块 2

```kotlin
Hello, 菜鸟教程!
网址：www.runoob.com
```

## 代码块 3

```kotlin
// 文件路径：src/main/kotlin/Main.kt

fun main() {

    val url = "www.runoob.com"

    println("项目创建成功，目标站点：$url")

}
```

## 代码块 4

```kotlin
项目创建成功，目标站点：www.runoob.com
```

## 代码块 5

```kotlin
// 文件路径：build.gradle.kts

plugins {

    kotlin("jvm") version "2.2.0"      // Kotlin/JVM 插件，版本号需与编译器一致

    application                        // 提供 run 任务，方便直接运行程序

}


group = "com.runoob"                   // 项目组名，通常用反写的域名

version = "1.0.0"                      // 项目版本号


repositories {

    mavenCentral()                     // 从 Maven 中央仓库下载依赖

}


dependencies {

    testImplementation(kotlin("test")) // 引入 Kotlin 官方测试库

}


application {

    // 主类名由「文件名 + Kt」构成，Main.kt 对应 MainKt

    mainClass.set("com.runoob.MainKt")

}


kotlin {

    // 指定编译使用的 JDK 版本，本机没装时 Gradle 会尝试自动下载

    jvmToolchain(17)

}
```

## 代码块 6

```kotlin
// 文件路径：settings.gradle.kts

rootProject.name = "kotlin-demo"       // 根项目名称
```

## 代码块 7

```kotlin
kotlin-demo/
├── build.gradle.kts
├── settings.gradle.kts
└── src
    └── main
        └── kotlin
            └── com
                └── runoob
                    └── Main.kt
```

## 代码块 8

```kotlin
// 文件路径：src/main/kotlin/com/runoob/Main.kt

package com.runoob                    // 包声明，需与目录结构对应


fun main() {

    println("Hello, Runoob!")

    println("教程站点：www.runoob.com")

}
```

## 代码块 9

```kotlin
$ ./gradlew run

> Task :run
Hello, Runoob!
教程站点：www.runoob.com

BUILD SUCCESSFUL in 3s
```

## 代码块 10

```xml
<!-- 文件路径：pom.xml -->

<project xmlns="http://maven.apache.org/POM/4.0.0"

         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0

                             http://maven.apache.org/xsd/maven-4.0.0.xsd">


    <modelVersion>4.0.0</modelVersion>

    <groupId>com.runoob</groupId>              <!-- 组织标识 -->

    <artifactId>kotlin-demo</artifactId>       <!-- 项目名 -->

    <version>1.0.0</version>                   <!-- 版本号 -->


    <properties>

        <kotlin.version>2.2.0</kotlin.version>

        <maven.compiler.release>8</maven.compiler.release>   <!-- 目标字节码版本 -->

        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>

    </properties>


    <dependencies>

        <!-- Kotlin 标准库，编译和运行都需要 -->

        <dependency>

            <groupId>org.jetbrains.kotlin</groupId>

            <artifactId>kotlin-stdlib</artifactId>

            <version>${kotlin.version}</version>

        </dependency>

    </dependencies>


    <build>

        <!-- Kotlin 源码目录，Maven 默认的 java 目录不适用 -->

        <sourceDirectory>src/main/kotlin</sourceDirectory>

        <plugins>

            <plugin>

                <groupId>org.jetbrains.kotlin</groupId>

                <artifactId>kotlin-maven-plugin</artifactId>

                <version>${kotlin.version}</version>

                <executions>

                    <execution>

                        <id>compile</id>

                        <phase>compile</phase>            <!-- 绑定到 compile 阶段 -->

                        <goals>

                            <goal>compile</goal>

                        </goals>

                    </execution>

                </executions>

            </plugin>

        </plugins>

    </build>

</project>
```

## 代码块 11

```kotlin
$ mvn compile
$ mvn exec:java -Dexec.mainClass=com.runoob.MainKt

Hello, Runoob!
教程站点：www.runoob.com
```

## 代码块 12

```kotlin
// 文件路径：app/build.gradle.kts（Android 应用模块）

plugins {

    id("com.android.application")            // Android 应用插件

    id("org.jetbrains.kotlin.android")       // Kotlin 对 Android 的支持

}


android {

    namespace = "com.runoob.demo"            // 包命名空间

    compileSdk = 35                          // 编译时使用的 Android SDK 版本


    defaultConfig {

        applicationId = "com.runoob.demo"    // 应用唯一标识

        minSdk = 21                          // 最低支持的 Android 版本

        targetSdk = 35                       // 目标 Android 版本

        versionCode = 1                      // 内部版本号，只能是整数

        versionName = "1.0"                  // 对外展示的版本名

    }

}
```

## 代码块 13

```kotlin
// 文件路径：build.gradle.kts（项目根目录）

plugins {

    id("com.android.application") version "8.7.0" apply false          // 仅声明版本，不在根项目应用

    id("org.jetbrains.kotlin.android") version "2.2.0" apply false     // Kotlin 插件版本

}
```
