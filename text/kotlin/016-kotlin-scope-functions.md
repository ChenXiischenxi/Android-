# Kotlin 作用域函数

> 来源: https://www.runoob.com/kotlin/kotlin-scope-functions.html

作用域函数是 Kotlin 标准库提供的一组小工具，它们让对象在一个临时的作用域里被操作，并决定这段代码最终返回什么。

用好它们能让代码更短、更清晰；用错则会让返回值与预期不符，这是初学者最容易踩的坑之一。

---

## 什么是作用域函数

作用域函数本质上都是接收一个 lambda 的普通函数，区别只有两点：lambda 里怎么引用对象，以及整个调用返回什么。

引用对象有两种方式：作为 lambda 的接收者（用 `this` 访问），或作为 lambda 的参数（用 `it` 访问）。

返回值也有两种：返回 lambda 最后一行的结果，或返回对象本身。

这两点组合起来，就得到了五个最常用的作用域函数：`let`、`run`、`with`、`apply`、`also`。

---

## 五个作用域函数总览

下表先建立整体印象，后面再逐个展开。

| 函数 | 引用方式 | 返回值 | 典型用途 | 起始版本

| let | it | lambda 结果 | 可空对象判空后转换、把对象变成另一个值 | Kotlin 1.0

| run | this | lambda 结果 | 在对象上下文里做多步计算并返回结果 | Kotlin 1.0

| with | this | lambda 结果 | 对同一个对象连续调用多个成员 | Kotlin 1.0

| apply | this | 接收者本身 | 配置对象属性后返回对象 | Kotlin 1.0

| also | it | 接收者本身 | 附加日志、校验等操作后返回对象 | Kotlin 1.1 起

| runCatching | 无 / this | Result 包装 | 把可能抛异常的代码包起来统一处理 | Kotlin 1.3 起

![图1](../../images/13-scope-matrix.svg)

表中最后一行 `runCatching` 严格说不是作用域函数，而是异常处理工具，因为它经常和作用域函数一起出现，这里一并列出。

记忆口诀：`let` 和 `also` 用 it，`run`、`with`、`apply` 用 this。

返回 lambda 结果的是 `let`、`run`、`with`；返回接收者本身的是 `apply` 和 `also`。

---

## let

`let` 把对象作为参数传给 lambda，用 `it` 引用，返回 lambda 最后一行的结果。

它最常见的用法是配合安全调用处理可空对象，只有对象非空时 lambda 才会执行。

输出结果：

因为 `let` 返回 lambda 的结果，所以它也常用来把对象转换成另一种类型或格式。

输出结果：

---

## run 与 runCatching

`run` 把对象作为接收者，用 `this` 引用，同样返回 lambda 的结果。

当 lambda 里要反复访问对象的成员时，`run` 比 `let` 更顺手，因为不用每次都写 `it.`。

输出结果：

`run` 还有不带接收者的形式，用来把几行语句收成一个有返回值的代码块。

输出结果：

### runCatching 与 Result

`runCatching` 自 Kotlin 1.3 起可用，它把代码块包起来执行，把成功或失败都装进 `Result` 对象返回，不再向外抛异常。

输出结果：

常用的 `Result` 方法有 `isSuccess`、`isFailure`、`getOrNull()`、`getOrDefault()`、`exceptionOrNull()`、`onSuccess()` 与 `onFailure()`。

> **注意：**runCatching 捕获的是 Throwable，其中包括协程的 CancellationException。在协程里使用它会吞掉取消信号，需要谨慎。

---

## with

`with` 不是扩展函数，它把接收者写在括号里，lambda 内用 `this` 引用，返回 lambda 结果。

它适合对一个已经存在的对象连续做多件事，代码读起来像一段普通的顺序逻辑。

输出结果：

`with` 的接收者不能是 null，如果对象可能为空，要先判空，或者改用 `?.run`。

---

## apply

`apply` 用 `this` 引用接收者，但返回的是接收者本身，而不是 lambda 的结果。

这个特性让 `apply` 成为配置对象的首选：花括号里设置属性，整个表达式的结果就是配置好的对象。

输出结果：

因为返回的是对象本身，`apply` 也常用来在创建对象后立即执行一次初始化逻辑。

---

## also

`also` 自 Kotlin 1.1 起可用，它用 `it` 引用接收者，返回接收者本身。

它与 `apply` 的唯一区别是引用方式，因此更适合做与对象配置无关的附加操作，例如打印日志、参数校验。

输出结果：

把 `also` 串在链式调用中间，可以在不打断链的前提下观察每一步的值。

---

## 选择决策表

遇到具体场景时，按下面这张表选择即可。

| 需求 | 推荐函数 | 原因

| 拿到 lambda 的结果，用 it 指代对象 | let | 返回 lambda 结果，it 不易与外部 this 混淆

| 拿到 lambda 的结果，用 this 指代对象 | run / with | this 便于直接调用对象成员

| 返回对象本身，用 this 配置属性 | apply | 返回接收者，适合链式配置

| 返回对象本身，用 it 做附加操作 | also | 返回接收者，it 语义清晰

| 统一处理可能抛出的异常并拿到结果 | runCatching | 返回 Result 包装，不中断流程

再补一条经验：如果一个函数返回的是接收者，它的价值在于不打断链式调用；如果返回的是 lambda 结果，它的价值在于把对象转成别的值。

---

## 常见误用

下面三个问题在实际代码里出现频率最高，写之前先想清楚返回的是谁。

### 把 apply 的返回值当成 lambda 的结果

`apply` 返回接收者，所以下面这段代码拿到的不是大写字符串。

输出结果：

`apply` 里的 `uppercase()` 确实执行了，只是返回值被丢弃了，因为 `apply` 只关心对象本身。

### 嵌套时 it 被遮蔽

连续嵌套两个用 `it` 的作用域函数时，内层的 `it` 会遮蔽外层，代码虽然能编译，但很容易读错。

输出结果：

另一种做法是把其中一层改成 `this` 形式的 `run`，这样 `it` 就不会冲突。

### 在可空对象上忘记安全调用

作用域函数本身不会处理 null，可空对象必须先判空或用 `?.`。

输出结果：

---

## 常见问题

下面几个问题是选择作用域函数时最常遇到的。

### let 和 run 都能返回结果，怎么选

看 lambda 里是否需要频繁访问对象成员。需要就用 `run`（this），否则用 `let`（it），后者在嵌套时更安全。

### apply 和 also 都返回对象，怎么选

配置属性用 `apply`，因为写属性时 `this` 更自然；做附加操作、打印日志用 `also`，因为 `it` 不会和外部 this 混淆。

### with 和 run 有什么区别

功能几乎一样，区别在调用形式：`with(obj) { }` 是普通函数调用，`obj.run { }` 是扩展调用，后者可以配合 `?.` 处理空值。

### 作用域函数会影响性能吗

五个常用函数都是 inline 函数，lambda 不会产生额外的函数对象，运行时开销可以忽略。

### 图片清单

1. 图1 -> images/13-scope-matrix.svg （原图：https://www.runoob.com/wp-content/uploads/2026/09/13-scope-matrix.svg）
