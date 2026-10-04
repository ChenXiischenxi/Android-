# 2.3.4 ImageView(图像视图)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-imageview.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="com.jay.example.imageviewdemo.MainActivity" >

    <ImageView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:background="@drawable/pen" />

    <ImageView
        android:layout_width="200dp"
        android:layout_height="wrap_content"
        android:background="@drawable/pen" />

    <ImageView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/pen" />

    <ImageView
        android:layout_width="200dp"
        android:layout_height="wrap_content"
        android:src="@drawable/pen" />

</LinearLayout>
```

## 代码块 2

```xml
<ImageView
        android:layout_width="100dp"
        android:layout_height="50dp"
        android:src="@drawable/pen" />
```

## 代码块 3

```java
LinearLayout.LayoutParams layoutParam = new LinearLayout.LayoutParams(48, 48);
        layout.addView(ibtnPen, layoutParam);
```

## 代码块 4

```xml
<bitmap
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@id/pen_bg"
    android:gravity="top"
    android:src="@drawable/pen"
    android:tileMode="disabled" >
</bitmap>
```

## 代码块 5

```xml
<ImageView
    android:layout_width="150dp"
    android:layout_height="wrap_content"
    android:src="@drawable/pig"
    android:background="#6699FF" />
```

## 代码块 6

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <!-- 正常的图片 -->
    <ImageView
        android:id="@+id/imageView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_margin="5px"
        android:src="@mipmap/meinv" />
    <!-- 限制了最大宽度与高度,并且设置了调整边界来保持所显示图像的长宽比-->
    <ImageView
        android:id="@+id/imageView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_margin="5px"
        android:adjustViewBounds="true"
        android:maxHeight="200px"
        android:maxWidth="200px"
        android:src="@mipmap/meinv" />

</LinearLayout>
```

## 代码块 7

```xml
<!-- 保持图片的横纵比缩放,知道该图片能够显示在ImageView组件上,并将缩放好的图片显示在imageView的右下角 -->
    <ImageView
        android:id="@+id/imageView3"
        android:layout_width="300px"
        android:layout_height="300px"
        android:layout_margin="5px"
        android:scaleType="fitEnd"
        android:src="@mipmap/meinv" />
```

## 代码块 8

```xml
<ImageView
        android:layout_width="300px"
        android:layout_height="300px"
        android:layout_margin="5px"
        android:scaleType="centerCrop"
        android:src="@mipmap/meinv" />

    <ImageView
        android:layout_width="300px"
        android:layout_height="300px"
        android:layout_margin="5px"
        android:scaleType="centerInside"
        android:src="@mipmap/meinv" />
```

## 代码块 9

```xml
<ImageView
        android:layout_width="300px"
        android:layout_height="300px"
        android:layout_margin="5px"
        android:scaleType="fixXY"
        android:src="@mipmap/meinv" />
```

## 代码块 10

```xml
<ImageView
        android:layout_width="300px"
        android:layout_height="300px"
        android:layout_margin="5px"
        android:scaleType="matrix"
        android:src="@mipmap/meinv" />
```

## 代码块 11

```xml
<ImageView
        android:layout_width="300px"
        android:layout_height="300px"
        android:layout_margin="5px"
        android:scaleType="center"
        android:src="@mipmap/meinv" />
```

## 代码块 12

```java
package com.jay.demo.imageviewdemo;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.PaintFlagsDrawFilter;
import android.graphics.Path;
import android.graphics.Rect;
import android.graphics.Region;
import android.util.AttributeSet;
import android.widget.ImageView;

/**
 * Created by coder-pig on 2015/7/18 0018.
 */
public class RoundImageView extends ImageView {

    private Bitmap mBitmap;
    private Rect mRect = new Rect();
    private PaintFlagsDrawFilter pdf = new PaintFlagsDrawFilter(0, Paint.ANTI_ALIAS_FLAG);
    private Paint mPaint = new Paint();
    private Path mPath=new Path();
    public RoundImageView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }


    //传入一个Bitmap对象
    public void setBitmap(Bitmap bitmap) {
        this.mBitmap = bitmap;
    }


    private void init() {
        mPaint.setStyle(Paint.Style.STROKE);
        mPaint.setFlags(Paint.ANTI_ALIAS_FLAG);
        mPaint.setAntiAlias(true);// 抗锯尺
    }


    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        if(mBitmap == null)
        {
            return;
        }
        mRect.set(0,0,getWidth(),getHeight());
        canvas.save();
        canvas.setDrawFilter(pdf);
        mPath.addCircle(getWidth() / 2, getWidth() / 2, getHeight() / 2, Path.Direction.CCW);
        canvas.clipPath(mPath, Region.Op.REPLACE);
        canvas.drawBitmap(mBitmap, null, mRect, mPaint);
        canvas.restore();
    }
}
```

## 代码块 13

```xml
<com.jay.demo.imageviewdemo.RoundImageView
        android:id="@+id/img_round"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:layout_margin="5px"/>
```

## 代码块 14

```java
package com.jay.demo.imageviewdemo;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private RoundImageView img_round;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_round = (RoundImageView) findViewById(R.id.img_round);
        Bitmap bitmap = BitmapFactory.decodeResource(getResources(),R.mipmap.meinv);
        img_round.setBitmap(bitmap);
    }
}
```
