# 8.3.12 Paint API之—— PathEffect(路径效果)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-patheffect.html

## 本节引言：

> 本节继续来学习Paint的API——PathEffect(路径效果)，我们把画笔的sytle设置为Stroke，可以
> 绘制一个个由线构成的图形，而这些线偶尔会显得单调是吧，比如你想把这些先改成虚线，又
> 或者想让路径的转角变得圆滑等，那你就可以考虑使用这个PathEffect来实现了！

> 官方API文档：[PathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/PathEffect.html)
> 进去看文档，可以发现这个PathEffect和我们前面学的MaskFilter(面具)与ColorFilter(颜色
> 过滤器)一样，几乎没有可用的方法：

> ![图1](../../images/8910442.jpg)

> 我们一般使用的是他的六个子类：

> - 
> [ComposePathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/ComposePathEffect.html)

> - [CornerPathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/CornerPathEffect.html)

> - [DashPathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/DashPathEffect.html)

> - 
> [DiscretePathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/DiscretePathEffect.html)

> - [PathDashPathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/PathDashPathEffect.html)

> - [SumPathEffect](http://androiddoc.qiniudn.com/reference/android/graphics/SumPathEffect.html)

> 下面我们依次对他们的作用，以及构造方法进行分析！

## 1.子类作用与构造方法参数分析：

### 1)CornerPathEffect

**CornerPathEffect(float radius)**

> 将Path的各个连接线段之间的夹角用一种更平滑的方式连接，类似于圆弧与切线的效果。
> radius则是指定圆弧的半径！

### 2)DashPathEffect

**DashPathEffect(float[] intervals, float phase)**

> 将Path的线段虚线化，intervals为虚线的ON和OFF的数组，数组中元素数目需要 >= 2；
> 而phase则为绘制时的偏移量！

### 3)DiscretePathEffect

**DiscretePathEffect(float segmentLength, float deviation)**

> 打散Path的线段，使得在原来路径的基础上发生打散效果。
> segmentLength指定最大的段长，deviation则为绘制时的偏离量。

### 4)PathDashPathEffect

**PathDashPathEffect(Path shape, float advance, float phase, PathDashPathEffect.Style style)**

> 作用是使用Path图形来填充当前的路径，shape指的填充图形，advance是每个图形间的间隔，
> style则是该类自由的枚举值，有三种情况：**ROTATE**、**MORPH**和**TRANSLATE**。

> - 
> ROTATE情况下：线段连接处的图形转换以旋转到与下一段移动方向相一致的角度进行连接

> - 
> MORPH情况下：图形会以发生拉伸或压缩等变形的情况与下一段相连接

> - 
> TRANSLATE情况下：图形会以位置平移的方式与下一段相连接

### 5)ComposePathEffect

**ComposePathEffect(PathEffect outerpe, PathEffect innerpe)**

> 作用是：**组合效果**，会首先将innerpe变现出来，接着在innerpe的基础上来增加outerpe效果！

### 6)SumPathEffect

**SumPathEffect(PathEffect first, PathEffect second)**

> 作用是：叠加效果，和ComposePathEffect不同，在表现时会将两个参数的效果都独立的表现出来，
> 接着将两个效果简单的重叠在一起显示出来！

## 2.写代码来验证各自的效果

多说无益，写代码最实际，我们写下代码来试试这几个子类各自所起的效果！

**运行效果图**：

![图2](../../images/1690080.jpg)

**实现代码**：

我们自己来写一个View，里面的线移动的效果是phase增加造成的，每次 + 2，
然后invalidate重绘而已，所以别惊讶！**PathEffectView.java**:

好的，代码的注释已经非常清楚了，这里也不唠叨了~

## 3.本节示例代码下载：

[PathEffectDemo.zip](http://static.runoob.com/download/PathEffectDemo.zip)

## 本节小结

> 本节没什么难的东西，就介绍了PathEffect的六个子类所起的作用，只需调用setPathEffect
> 方法应用到Paint对象中，非常简单~嗯，就说这么多，谢谢~

### 图片清单

1. 图1 -> images/8910442.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/11/8910442.jpg）
2. 图2 -> images/1690080.jpg （原图：https://www.runoob.com/wp-content/uploads/2015/11/1690080.jpg）
