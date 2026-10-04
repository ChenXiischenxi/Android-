# 2.2.4 FrameLayout(帧布局)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-framelayout.html

## 代码块 1

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/FrameLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:foreground="@drawable/logo"
    android:foregroundGravity="right|bottom">

    <TextView
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:background="#FF6143" />
    <TextView
        android:layout_width="150dp"
        android:layout_height="150dp"
        android:background="#7BFE00" />
     <TextView
        android:layout_width="100dp"
        android:layout_height="100dp"
        android:background="#FFFF00" />

</FrameLayout>
```

## 代码块 2

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/mylayout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:background="@drawable/back" >
</FrameLayout>
```

## 代码块 3

```java
package com.jay.example.framelayoutdemo2;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.view.View;

public class MeziView extends View {
    //定义相关变量,依次是妹子显示位置的X,Y坐标
    public float bitmapX;
    public float bitmapY;
    public MeziView(Context context) {
        super(context);
        //设置妹子的起始坐标
        bitmapX = 0;
        bitmapY = 200;
    }

    //重写View类的onDraw()方法
    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        //创建,并且实例化Paint的对象
        Paint paint = new Paint();
        //根据图片生成位图对象
        Bitmap bitmap = BitmapFactory.decodeResource(this.getResources(), R.drawable.s_jump);
        //绘制萌妹子
        canvas.drawBitmap(bitmap, bitmapX, bitmapY,paint);
        //判断图片是否回收,木有回收的话强制收回图片
        if(bitmap.isRecycled())
        {
            bitmap.recycle();
        }
    }
}
```

## 代码块 4

```java
package com.jay.example.framelayoutdemo2;

import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;
import android.widget.FrameLayout;
import android.app.Activity;


public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        FrameLayout frame = (FrameLayout) findViewById(R.id.mylayout);
        final MeziView mezi = new MeziView(MainActivity.this);
        //为我们的萌妹子添加触摸事件监听器
        mezi.setOnTouchListener(new OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent event) {
                //设置妹子显示的位置
                mezi.bitmapX = event.getX() - 150;
                mezi.bitmapY = event.getY() - 150;
                //调用重绘方法
                mezi.invalidate();
                return true;
            }
        });
        frame.addView(mezi);
    }
}
```

## 代码块 5

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/myframe"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:foregroundGravity="center">
</FrameLayout>
```

## 代码块 6

```java
package com.jay.example.framelayoutdemo3;

import java.util.Timer;
import java.util.TimerTask;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.FrameLayout;
import android.app.Activity;
import android.graphics.drawable.Drawable;

public class MainActivity extends Activity {
    //初始化变量,帧布局
    FrameLayout frame = null;
    //自定义一个用于定时更新UI界面的handler类对象
        Handler handler = new Handler()
        {
            int i = 0;
            @Override
            public void handleMessage(Message msg) {
            //判断信息是否为本应用发出的
                if(msg.what == 0x123)
                {
                    i++;
                    move(i % 8 );
                }
                super.handleMessage(msg);
             }
        };

    //定义走路时切换图片的方法
    void move(int i)
    {
        Drawable a = getResources().getDrawable(R.drawable.s_1);
        Drawable b = getResources().getDrawable(R.drawable.s_2);
        Drawable c = getResources().getDrawable(R.drawable.s_3);
        Drawable d = getResources().getDrawable(R.drawable.s_4);
        Drawable e = getResources().getDrawable(R.drawable.s_5);
        Drawable f = getResources().getDrawable(R.drawable.s_6);
        Drawable g = getResources().getDrawable(R.drawable.s_7);
        Drawable h = getResources().getDrawable(R.drawable.s_8);
        //通过setForeground来设置前景图像
        switch(i)
        {
            case 0:
                frame.setForeground(a);
                break;
            case 1:
                frame.setForeground(b);
                break;
            case 2:
                frame.setForeground(c);
                break;
            case 3:
                frame.setForeground(d);
                break;
            case 4:
                frame.setForeground(e);
                break;
            case 5:
                frame.setForeground(f);
                break;
            case 6:
                frame.setForeground(g);
                break;
            case 7:
                frame.setForeground(h);
                break;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        frame = (FrameLayout) findViewById(R.id.myframe);
        //定义一个定时器对象,定时发送信息给handler
        new Timer().schedule(new TimerTask() {

            @Override
            public void run() {
                //发送一条空信息来通知系统改变前景图片
                handler.sendEmptyMessage(0x123);
            }
        }, 0,170);
    }
}
```
