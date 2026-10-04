# Kotlin 基础语法

> 来源: https://www.runoob.com/kotlin/kotlin-basic-syntax.html

本文从包声明和程序入口开始，逐步介绍 Kotlin 最基础也最常用的语法要素。

这些规则几乎会出现在之后每一篇教程里，值得先花时间弄明白。

---

## 包声明与 import

包声明写在源文件最上方，用来给代码分组并避免命名冲突。

包名不要求与目录结构完全一致，但保持一致是通行做法，工程上几乎都会遵守。

输出结果如下。

如果名字冲突，可以用 `as` 给导入的声明起个别名。

用 `*` 可以一次性导入某个包下的所有声明。

---

## 默认导入的包

为了减少样板代码，Kotlin 默认已经导入了一批常用包，写代码时无需手动 import。

| 默认导入 | 包含内容

| kotlin.* | 标准库核心，如 Int、String、println、arrayOf

| kotlin.annotation.* | 注解相关，如 Target、Retention

| kotlin.collections.* | 集合类型，如 List、Set、Map

| kotlin.comparisons.* | 比较器工具，如 compareBy、naturalOrder

| kotlin.io.* | 输入输出，如 readln、readLine

| kotlin.ranges.* | 区间，如 IntRange、until

| kotlin.sequences.* | 序列，如 sequenceOf、generateSequence

| kotlin.text.* | 字符串与正则，如 Regex、StringBuilder

| java.lang.* | JVM 平台额外默认导入，仅 Kotlin/JVM 有效

| kotlin.jvm.* | JVM 平台相关工具，仅 Kotlin/JVM 有效

最后两行是 JVM 后端特有的，编译到 JS 或 Native 时不存在。

因此 `println`、`listOf`、`Regex` 这些都用不着 import。

---

## 程序入口 main

Kotlin 程序的入口是 `main` 函数，它必须写在顶层，也就是不属于任何类。

最简形式不接收参数，等价于 Java 的 `public static void main(String[] args)`。

需要读取命令行参数时，用带参数的写法，参数类型是字符串数组。

执行 `kotlinc -script` 或直接运行时带上参数，输出如下。

Kotlin 1.3 起还支持挂起函数作为入口，写法是 `suspend fun main()`。

它在协程中运行，可以直接调用其他挂起函数，常用于命令行工具和协程示例。

> **提示：**一个文件里可以同时存在普通 `main` 和 `suspend main` 吗？不行，JVM 入口只能有一个，同时写会编译报错。

---

## 变量与常量

Kotlin 用 `val` 声明不可变变量，用 `var` 声明可变变量。

val 相当于 Java 的 final 变量，一旦赋值就不能再指向别的对象。

官方风格指南建议优先使用 `val`，只有在确实需要修改时才用 `var`。

这样能减少状态变化，让代码更容易推理和测试。

### 类型推断

声明变量时可以省略类型，编译器会根据初始值自动推断。

也可以显式写出类型，声明与赋值分开时就必须写。

> **注意：**只声明不赋值时，编译器无法推断类型，必须显式写出。var 允许先声明后赋值，val 则必须在声明处就完成赋值。

---

## 注释

Kotlin 的注释分为单行注释和块注释，写法和 C 系语言一致。

单行注释以两个斜杠开头，块注释用一对斜杠星号包起来。

运行结果如下，注释部分不会产生任何输出。

和 Java 不同的是，Kotlin 的块注释可以嵌套。

这个特性在注释掉一段已经含有块注释的代码时非常实用。

Java 的块注释不能嵌套，所以同样的写法在 Java 里会导致编译错误。

---

## 字符串模板

字符串模板是 Kotlin 最讨喜的语法之一，可以直接在字符串里引用变量。

用 `$` 加变量名即可，简单表达式用 `${}` 包起来。

如果 `$` 后面跟的不是合法标识符，就不需要转义。

想在字符串里输出美元符号本身，用反斜杠转义即可。

---

## 分号可省略

Kotlin 不要求语句末尾写分号，换行本身就代表语句结束。

写成一行时可以用分号分隔，但官方风格指南不推荐。

要注意换行位置，Kotlin 按换行切分语句，某些跨行表达式会被误解。

把减号写在上一行行尾，才能得到 `y = 7` 的结果。

---

## 空安全初探

Kotlin 把「可能为 null」这件事编码进类型系统，这是它和 Java 最大的差异之一。

类型后面加问号表示可空，不加问号表示一定不为空。

可空类型不能直接调用成员，必须先用 `?.` 或 `?:` 处理。

正是这条规则，让 Kotlin 在编译期就消除了绝大部分空指针异常。

> **提示：**空安全涉及 `?.`、`?:`、`!!`、`lateinit`、平台类型等多个主题，本文只做初步认识，完整内容见第 27 篇《[Kotlin 空安全](kotlin-null-safety.html)》。

---

## 常见问题

下面几个坑在初学阶段出现频率最高。

### Val cannot be reassigned

试图给 val 变量重新赋值，改成 var，或者换一个变量名。

### Unresolved reference

拼写错误，或者忘记 import 对应的包。IDEA 里按 Alt+Enter 可以自动补全导入。

### 顶层 main 函数报错

确认 main 写在文件顶层而不是某个类内部，参数类型必须是 `Array<String>`。

### 字符串模板里 $ 后面跟了非法字符

改成 `${'$'}` 或者用反斜杠转义。
