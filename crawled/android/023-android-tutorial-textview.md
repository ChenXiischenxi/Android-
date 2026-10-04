# 2.3.1 TextView(文本框)详解

> 来源: https://www.runoob.com/w3cnote/android-tutorial-textview.html

## 代码块 1

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:gravity="center"
    android:background="#8fffad">

    <TextView
        android:id="@+id/txtOne"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:gravity="center"
        android:text="TextView(显示框)"
        android:textColor="#EA5246"
        android:textStyle="bold|italic"
        android:background="#000000"
        android:textSize="18sp" />

</RelativeLayout>
```

## 代码块 2

```xml
<TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerInParent="true"
        android:shadowColor="#F9F900"
        android:shadowDx="10.0"
        android:shadowDy="10.0"
        android:shadowRadius="3.0"
        android:text="带阴影的TextView"
        android:textColor="#4A4AFF"
        android:textSize="30sp" />
```

## 代码块 3

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" >

    <!-- 设置一个黑色边框 -->
    <stroke android:width="2px" android:color="#000000"/>
    <!-- 渐变 -->
    <gradient
        android:angle="270"
        android:endColor="#C0C0C0"
        android:startColor="#FCD209" />
    <!-- 设置一下边距,让空间大一点 -->
    <padding
        android:left="5dp"
        android:top="5dp"
        android:right="5dp"
        android:bottom="5dp"/>

</shape>
```

## 代码块 4

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- 设置透明背景色 -->
    <solid android:color="#87CEEB" />

    <!-- 设置一个黑色边框 -->
    <stroke
        android:width="2px"
        android:color="#000000" />
    <!-- 设置四个圆角的半径 -->
    <corners
        android:bottomLeftRadius="10px"
        android:bottomRightRadius="10px"
        android:topLeftRadius="10px"
        android:topRightRadius="10px" />
    <!-- 设置一下边距,让空间大一点 -->
    <padding
        android:bottom="5dp"
        android:left="5dp"
        android:right="5dp"
        android:top="5dp" />

</shape>
```

## 代码块 5

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#FFFFFF"
    android:gravity="center"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/txtOne"
        android:layout_width="200dp"
        android:layout_height="64dp"
        android:textSize="18sp"
        android:gravity="center"
        android:background="@drawable/txt_rectborder"
        android:text="矩形边框的TextView" />

    <TextView
        android:id="@+id/txtTwo"
        android:layout_width="200dp"
        android:layout_height="64dp"
        android:layout_marginTop="10dp"
        android:textSize="18sp"
        android:gravity="center"
        android:background="@drawable/txt_radiuborder"
        android:text="圆角边框的TextView" />


</LinearLayout>
```

## 代码块 6

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="com.jay.example.test.MainActivity" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerInParent="true"
        android:drawableTop="@drawable/show1"
        android:drawableLeft="@drawable/show1"
        android:drawableRight="@drawable/show1"
        android:drawableBottom="@drawable/show1"
        android:drawablePadding="10dp"
        android:text="张全蛋" />

</RelativeLayout>
```

## 代码块 7

```java
package com.jay.example.test;

import android.app.Activity;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    private TextView txtZQD;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtZQD = (TextView) findViewById(R.id.txtZQD);
        Drawable[] drawable = txtZQD.getCompoundDrawables();
        // 数组下表0~3,依次是:左上右下
        drawable[1].setBounds(100, 0, 200, 200);
        txtZQD.setCompoundDrawables(drawable[0], drawable[1], drawable[2],
                drawable[3]);
    }
}
```

## 代码块 8

```java
package jay.com.example.textviewdemo;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.text.util.Linkify;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView t1 = (TextView)findViewById(R.id.txtOne);
        String s1 = "<font color='blue'><b>百度一下，你就知道~：</b></font><br>";
        s1 += "<a href = 'http://www.baidu.com'>百度</a>";
        t1.setText(Html.fromHtml(s1));
        t1.setMovementMethod(LinkMovementMethod.getInstance());
    }
}
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView t1 = (TextView) findViewById(R.id.txtOne);
        String s1 = "图片：<img src = 'icon'/><br>";
        t1.setText(Html.fromHtml(s1, new Html.ImageGetter() {
            @Override
            public Drawable getDrawable(String source) {
                Drawable draw = null;
                try {
                    Field field = R.drawable.class.getField(source);
                    int resourceId = Integer.parseInt(field.get(null).toString());
                    draw = getResources().getDrawable(resourceId);
                    draw.setBounds(0, 0, draw.getIntrinsicWidth(), draw.getIntrinsicHeight());
                } catch (Exception e) {
                    e.printStackTrace();
                }
                return draw;
            }
        }, null));
    }
}
```

## 代码块 10

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView t1 = (TextView) findViewById(R.id.txtOne);
        TextView t2 = (TextView) findViewById(R.id.txtTwo);

        SpannableString span = new SpannableString("红色打电话斜体删除线绿色下划线图片:.");
        //1.设置背景色,setSpan时需要指定的flag,Spanned.SPAN_EXCLUSIVE_EXCLUSIVE(前后都不包括)
        span.setSpan(new ForegroundColorSpan(Color.RED), 0, 2, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
        //2.用超链接标记文本
        span.setSpan(new URLSpan("tel:4155551212"), 2, 5, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
        //3.用样式标记文本（斜体）
        span.setSpan(new StyleSpan(Typeface.BOLD_ITALIC), 5, 7, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
        //4.用删除线标记文本
        span.setSpan(new StrikethroughSpan(), 7, 10, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
        //5.用下划线标记文本
        span.setSpan(new UnderlineSpan(), 10, 16, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
        //6.用颜色标记
        span.setSpan(new ForegroundColorSpan(Color.GREEN), 10, 13,Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
        //7.//获取Drawable资源
        Drawable d = getResources().getDrawable(R.drawable.icon);
        d.setBounds(0, 0, d.getIntrinsicWidth(), d.getIntrinsicHeight());
        //8.创建ImageSpan,然后用ImageSpan来替换文本
        ImageSpan imgspan = new ImageSpan(d, ImageSpan.ALIGN_BASELINE);
        span.setSpan(imgspan, 18, 19, Spannable.SPAN_INCLUSIVE_EXCLUSIVE);
        t1.setText(span);
    }
}
```

## 代码块 11

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView t1 = (TextView) findViewById(R.id.txtOne);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 20; i++) {
            sb.append("好友" + i + "，");
        }

        String likeUsers = sb.substring(0, sb.lastIndexOf("，")).toString();
        t1.setMovementMethod(LinkMovementMethod.getInstance());
        t1.setText(addClickPart(likeUsers), TextView.BufferType.SPANNABLE);
    }

    //定义一个点击每个部分文字的处理方法
    private SpannableStringBuilder addClickPart(String str) {
        //赞的图标，这里没有素材，就找个笑脸代替下~
        ImageSpan imgspan = new ImageSpan(MainActivity.this, R.drawable.ic_widget_face);
        SpannableString spanStr = new SpannableString("p.");
        spanStr.setSpan(imgspan, 0, 1, Spannable.SPAN_INCLUSIVE_EXCLUSIVE);

        //创建一个SpannableStringBuilder对象，连接多个字符串
        SpannableStringBuilder ssb = new SpannableStringBuilder(spanStr);
        ssb.append(str);
        String[] likeUsers = str.split("，");
        if (likeUsers.length > 0) {
            for (int i = 0; i < likeUsers.length; i++) {
                final String name = likeUsers[i];
                final int start = str.indexOf(name) + spanStr.length();
                ssb.setSpan(new ClickableSpan() {
                    @Override
                    public void onClick(View widget) {
                        Toast.makeText(MainActivity.this, name,
                                Toast.LENGTH_SHORT).show();
                    }

                    @Override
                    public void updateDrawState(TextPaint ds) {
                        super.updateDrawState(ds);
                        //删除下划线，设置字体颜色为蓝色
                        ds.setColor(Color.BLUE);
                        ds.setUnderlineText(false);
                    }
                },start,start + name.length(),0);
            }
        }
    return ssb.append("等" + likeUsers.length + "个人觉得很赞");
    }
}
```

## 代码块 12

```xml
<TextView
        android:id="@+id/txtOne"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:singleLine="true"
        android:ellipsize="marquee"
        android:marqueeRepeatLimit="marquee_forever"
        android:focusable="true"
        android:focusableInTouchMode="true"
        android:text="你整天说着日了狗日了狗，但是你却没有来，呵呵呵呵呵呵呵呵呵呵~"/>
```

## 代码块 13

```java
android:textScaleX：控制字体水平方向的缩放，默认值1.0f，值是float
Java中setScaleX(2.0f);
```

## 代码块 14

```java
android:singleLine = "false"
```

## 代码块 15

```java
android:singleLine = "true"
```
