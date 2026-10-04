# Kotlin 注解

> 来源: https://www.runoob.com/kotlin/kotlin-annotation.html

注解（Annotation）是一种给代码附加元数据的机制，它本身不影响程序逻辑，但能被编译器、框架和注解处理器读取。

Kotlin 的注解既能作用于 Kotlin 自身的声明，也能精确指定落到 JVM 的哪个位置，比如字段、getter 或 setter。

本章节讲注解的定义与元注解、参数类型、使用处目标，以及日常开发最常用的内置注解。

---

## 注解的定义与使用

用 `annotation class` 定义一个注解，它也可以有构造参数。

使用注解时把 `@注解名` 放在目标声明之前，带参数的注解用括号传入实参。

> **提示：**方法注解只写了 author，version 就取默认值 "1.0"。如果 `@Retention` 不是 RUNTIME，反射就读取不到这个注解。

---

## 元注解

元注解是「用来修饰注解的注解」，它们决定一个注解能用在哪里、保留到什么时候。

| 元注解 | 作用 | 可选值

| @Target | 限定注解可以标注哪些目标 | CLASS、FUNCTION、PROPERTY、FIELD、VALUE_PARAMETER、CONSTRUCTOR、EXPRESSION、FILE 等

| @Retention | 决定注解保留到哪个阶段 | SOURCE、BINARY（默认）、RUNTIME

| @Repeatable | 允许同一注解在同一位置重复出现 | 无参数，Kotlin 1.6 起支持

| @MustBeDocumented | 把注解包含进生成的 API 文档 | 无参数

三种保留级别对应不同的可见范围，选错级别会导致框架读不到注解。

| 保留级别 | 保存在何处 | 典型用途

| SOURCE | 只存在于源码，编译后丢弃 | 编译期检查，如 @Suppress

| BINARY | 写入 class 文件，但反射读不到 | Kotlin 的默认值，供注解处理器使用

| RUNTIME | 写入 class 文件且反射可读 | 运行时框架，如序列化、依赖注入

> **注意：**Kotlin 中不写 `@Retention` 时默认是 BINARY，而 Java 的默认是 CLASS，两者行为一致。想让反射读到，必须显式写成 RUNTIME。

---

## 注解参数

注解参数不是任意值都能写，它们必须是编译期就能确定的常量。

允许的类型包括基本类型、String、KClass、枚举、其他注解，以及这些类型的数组。

> **限制：**注解参数不能是可空类型，也不能是任意对象；传入的值必须是字面量或 `const val` 常量，不能在运行时计算。

---

## 使用处目标

一个 Kotlin 属性在 JVM 上会同时产生字段、getter 和 setter，注解到底标在哪一个上，需要用使用处目标来指定。

| 目标 | 作用位置 | 示例

| @file: | 整个文件，必须写在包声明之前 | `@file:JvmName("RunoobUtils")`

| @field: | 属性背后的 JVM 字段 | `@field:Transient`

| @property: | Kotlin 属性本身，Java 侧看不到 | `@property:Marker("...")`

| @get: | 属性的 getter 方法 | `@get:JvmName("getName")`

| @set: | 属性的 setter 方法 | `@set:JvmName("setName")`

| @param: | 构造器参数 | `@param:Marker("...")`

| @setparam: | setter 的参数 | `@setparam:Nullable`

| @receiver: | 扩展函数或扩展属性的接收者 | `@receiver:Marker("...")`

| @delegate: | 委托属性保存委托对象的字段 | `@delegate:Transient`

不写使用处目标时，Kotlin 按 param、property、field 的优先级自动选择。

文件级注解必须放在文件最顶部，包声明之前，下面是它的真实写法。

> **注意：**`@property:` 标注的注解在 Java 侧完全不可见，因为 JVM 上根本没有「属性」这个概念；如果 Java 框架需要读取，请改用 `@field:` 或 `@get:`。

---

## 常用内置注解

Kotlin 标准库和 JVM 扩展提供了大量开箱即用的注解，下面按用途分类介绍。

| 注解 | 作用 | 适用范围

| @Deprecated | 标记过时 API，可指定提示语、替代写法和级别 | 类、函数、属性等

| @JvmStatic | 为伴生对象或单例的方法生成真正的静态方法 | object、companion object 的成员

| @JvmField | 把属性暴露为字段，不再生成 getter/setter | 有 backing field 的非私有属性

| @JvmOverloads | 为带默认参数的函数生成多个重载版本 | 函数、构造器

| @JvmName | 修改编译后在 JVM 上看到的名字 | 函数、属性访问器、文件

| @Synchronized | 给方法加锁，等价于 JVM 的 synchronized | 函数、属性访问器

| @Throws | 向 Java 调用方声明可能抛出的受检异常 | 函数、构造器

| @OptIn | 显式选择使用被标记为实验性的 API | 类、函数、表达式

`@Synchronized` 和 `@Volatile` 用于并发场景，它们只在 JVM 平台有效。

`@Repeatable` 让同一个注解可以重复标注，Kotlin 1.6 起会自动生成容器注解。

使用实验性 API 时，需要先用 `@RequiresOptIn` 标记它，调用方再用 `@OptIn` 表态。

> **提示：**不想在每个调用处都写 `@OptIn`，可以在编译参数里加上 `-opt-in=ExperimentalSiteApi`，让整个模块默认选择使用该 API。

---

## 注解处理：KSP 与 kapt

注解本身只是元数据，真正干活的是注解处理器，它在编译期扫描注解并生成代码。

Kotlin 生态里有两套方案，KSP 是官方主推的新方案，kapt 则用于兼容已有的 Java 注解处理器。

| 对比项 | KSP | kapt

| 全称 | Kotlin Symbol Processing | Kotlin Annotation Processing Tool

| 工作方式 | 直接读取 Kotlin 符号与语法树 | 先生成 Java 桩代码，再交给 Java 处理器

| 编译速度 | 快 | 慢，桩生成开销明显

| 多平台支持 | 支持 | 不支持，仅限 JVM

| 典型使用者 | Room、Moshi、Hilt | 依赖 Java 处理器的旧项目

| 当前状态 | 官方主推，KSP2 随 Kotlin 2.0 推出 | Kotlin 1.9 起进入维护模式

在 Gradle 中启用 KSP 只需要加一个插件，然后把注解处理器的依赖从 kapt 换成 ksp。

> **注意：**KSP 与 kapt 不能对同一个注解处理器同时启用，迁移时要把 `kapt(...)` 整行替换为 `ksp(...)`，并删除 kapt 插件。

---

## 常见问题

下面汇总注解使用中最容易遇到的几个问题。

| 问题 | 原因 | 解决办法

| 反射读不到注解 | 保留级别是默认的 BINARY | 加上 `@Retention(AnnotationRetention.RUNTIME)`

| 注解写不到字段上 | 默认位置落在了 property 而不是 field | 显式写成 `@field:注解名`

| Java 框架读不到 Kotlin 属性注解 | JVM 上没有属性概念 | 改用 `@get:` 或 `@field:`

| @JvmField 报错 | 属性是 private、override 或委托属性 | 去掉 private，或改用普通属性

| 重复标注同一注解编译失败 | 注解没有加 @Repeatable | 给注解类加上 `@Repeatable`

| 调用实验性 API 出现警告 | 该 API 被 @RequiresOptIn 标记 | 在调用处加 `@OptIn`，或配置编译参数
