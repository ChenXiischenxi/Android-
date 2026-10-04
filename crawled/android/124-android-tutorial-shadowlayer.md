# 8.3.14 Paint几个枚举/常量值以及ShadowLayer阴影效果

> 来源: https://www.runoob.com/w3cnote/android-tutorial-shadowlayer.html

## 代码块 1

```java
public enum Style {
    //定义枚举,通过括号赋值
    FILL            (0),
    STROKE          (1),
    FILL_AND_STROKE (2);
    //有参构造方法
    Style(int nativeInt) {
        this.nativeInt = nativeInt;
    }
    final int nativeInt;
}
//设置画笔Style的方法
public void setStyle(Style style) {
    native_setStyle(mNativePaint, style.nativeInt);
}
//JNI设置画笔风格的方法，这里我们无需关注
private static native void native_setStyle(long native_object, int style);
```

## 代码块 2

```java
mPaint1.setShadowLayer(5,0,0,Color.BLACK);
canvas.drawText("毕竟基神~", 400, 400, mPaint1);    //绘制文字
```
