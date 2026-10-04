# Kotlin 集合操作

> 来源: https://www.runoob.com/kotlin/kotlin-collection-ops.html

Kotlin 标准库为集合提供了一整套链式操作函数，把「筛选、变换、汇总、排序、分组、查找」这些常见任务写成一行表达式即可完成。

这些函数绝大多数返回新集合，不会改动原集合，因此可以放心地串起来使用。

本章节按七个类别讲解最常用的集合操作，每个函数都配有可直接运行的示例和真实输出。

---

## 过滤

过滤操作按条件挑选元素，结果是一个新列表，原集合保持不变。

| 函数 | 作用 | 返回类型

| filter | 保留使 lambda 返回 true 的元素 | `List<T>`

| filterNot | 保留使 lambda 返回 false 的元素，即 filter 的反面 | `List<T>`

| filterNotNull | 去掉所有 null，并把元素类型从 `T?` 收窄为 `T` | `List<T>`

| partition | 按一个条件拆成「满足」和「不满足」两个列表 | `Pair<List<T>, List<T>>`

> **提示：**filterNotNull 的价值不只是去空，它还会把类型从 `List<String?>` 变成 `List<String>`，后续代码就不必再写 `!!` 或 `?.`。

---

## 映射

映射把集合中的每个元素按规则转换成另一个值，元素个数通常不变（mapNotNull 和 flatMap 除外）。

| 函数 | 作用 | 结果长度

| map | 对每个元素应用变换，得到同长度的新列表 | 与原集合相同

| mapNotNull | 变换结果非 null 才保留，相当于 map + filterNotNull | 小于等于原长度

| mapIndexed | 变换时额外拿到元素下标，lambda 参数为 (index, element) | 与原集合相同

| flatMap | 先对每个元素产生一个集合，再把所有结果拍平成一层 | 等于各子集合长度之和

---

## 聚合

聚合把整个集合压缩成一个值，例如求和、求平均值、找最大值，是统计类逻辑最常用的一组函数。

| 函数 | 作用 | 空集合时的行为

| fold | 从初始值开始，逐个元素累积 | 返回初始值

| reduce | 用第一个元素作起点累积，没有初始值 | 抛 `UnsupportedOperationException`

| sum | 对数值集合求和 | 返回 0

| sumOf | 先用选择器取值再求和，支持 Int、Long、Double、BigDecimal | 返回 0

| average | 求平均值，结果永远是 Double | 抛 `NoSuchElementException`

| maxOrNull | 返回最大元素，空集合返回 null | 返回 null

| minOrNull | 返回最小元素，空集合返回 null | 返回 null

> **注意：**`maxOrNull()` 与 `minOrNull()` 从 Kotlin 1.4 起使用，旧版直接叫 `max()` / `min()`，它们在 1.7 已被移除。旧写法遇到空集合会抛异常，新写法返回 null 更安全。

`sumOf` 同样从 Kotlin 1.4 起提供，它能根据选择器的返回类型自动选择 Int、Long、Double 等求和方式。

---

## 排序

排序函数都返回一个新列表，原列表的顺序不变，这一点与 `MutableList.sort()` 原地排序不同。

字符串按字典序比较时区分大小写，大写字母的码点小于小写字母，所以 `RUNOOB` 排在 `kotlin` 前面。

---

## 分组与切分

分组把元素按某个键重新组织成 Map，切分则把列表按固定长度切成若干块或滑动窗口。

| 函数 | 作用 | 返回类型

| groupBy | 按键分组，同一个键的元素收集成列表 | `Map<K, List<V>>`

| associateBy | 按键建索引，键重复时后面的覆盖前面的 | `Map<K, V>`

| chunked | 按固定长度切成块，最后一块可以不足 | `List<List<T>>`

| windowed | 生成固定长度的滑动窗口，默认步长为 1 | `List<List<T>>`

> **区别：**groupBy 的键可以重复，一个键对应多个元素；associateBy 的键必须唯一，重复时只保留最后一个元素。需要「一个键对应一个对象」时用 associateBy，需要「一个键对应一组对象」时用 groupBy。

`chunked` 与 `windowed` 从 Kotlin 1.2 起提供，处理分页和滑动统计时非常方便。

---

## 查找与判断

查找函数用于定位元素，判断函数用于回答「有没有满足条件的元素」这类问题。

| 函数 | 作用 | 找不到时的行为

| find | 返回第一个满足条件的元素 | 返回 null

| first | 返回第一个元素，可带条件 | 抛 `NoSuchElementException`

| firstOrNull | 同 first，但找不到时返回 null | 返回 null

| last | 返回最后一个元素，可带条件 | 抛 `NoSuchElementException`

| any | 是否存在满足条件的元素 | 返回 false

| all | 是否所有元素都满足条件 | 返回 true

| none | 是否没有任何元素满足条件 | 返回 true

| count | 统计元素个数，可带条件 | 返回 0

> **注意：**`first()`、`last()` 在空集合或条件无匹配时会抛异常。除非你能确定一定有值，否则优先用 `firstOrNull()` 和 `find()`，让返回值自己表达「可能没有」。

---

## 拼接

`joinToString` 把集合拼成一个字符串，是打印日志和生成文本时最常用的收尾函数。

| 参数 | 默认值 | 说明

| separator | `", "` | 元素之间的分隔符

| prefix | `""` | 整体前缀

| postfix | `""` | 整体后缀

| limit | `-1` | 最多拼接几个元素，-1 表示不限制

| truncated | `"..."` | 被截断时追加的字符串

| transform | 无 | 拼接前对每个元素做变换的 lambda

---

## 常见问题

下面汇总初学者在使用集合操作时最容易踩的几个坑。

| 问题 | 原因 | 建议

| sorted() 后原列表没变 | sorted 返回新列表，不修改原集合 | 接住返回值，或对 MutableList 用 sort()

| reduce 在空集合上崩溃 | reduce 没有初始值，无法确定起点 | 改用 fold，或者先判断集合非空

| average 返回的是 Double | 平均值天然可能带小数 | 需要整数结果时用 sum() / count() 自行计算

| map 里返回了 null 结果却还在 | map 不会过滤 null | 需要过滤时用 mapNotNull

| filter 条件写反 | 把「保留」当成了「排除」 | 用 filterNot 明确表达排除语义
