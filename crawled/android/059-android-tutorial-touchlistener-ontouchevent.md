# 3.4 TouchListener PK OnTouchEvent + 多点触碰

> 来源: https://www.runoob.com/w3cnote/android-tutorial-touchlistener-ontouchevent.html

## 代码块 1

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    android:paddingBottom="@dimen/activity_vertical_margin"
    tools:context=".MyActivity">

    <ImageView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/imgtouch"
        android:background="@drawable/touch"/>
</RelativeLayout>
```

## 代码块 2

```java
public class MyActivity extends ActionBarActivity {

    private ImageView imgtouch;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);

        imgtouch = (ImageView)findViewById(R.id.imgtouch);
        imgtouch.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                Toast.makeText(getApplicationContext(),"你通过监听器模式:OnTouchListener摸了伦家~",Toast.LENGTH_LONG).show();
                return true;
            }
        });
    }
}
```

## 代码块 3

```java
public class MyView extends View{
    public float X = 50;
    public float Y = 50;

    //创建画笔
    Paint paint = new Paint();

    public MyView(Context context,AttributeSet set)
    {
        super(context,set);
    }

    @Override
    public void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        paint.setColor(Color.BLUE);
        canvas.drawCircle(X,Y,30,paint);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        this.X = event.getX();
        this.Y = event.getY();
        //通知组件进行重绘
        this.invalidate();
        return true;
    }
}
```

## 代码块 4

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MyActivity">
    <example.jay.com.touch2.MyView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />
</RelativeLayout>
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent" >

    <ImageView
        android:id="@+id/img_test"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scaleType="matrix"
        android:src="@drawable/pic1" />

</RelativeLayout>
```

## 代码块 6

```java
package com.jay.example.edittextdemo;

import android.app.Activity;
import android.graphics.Matrix;
import android.graphics.PointF;
import android.os.Bundle;
import android.util.FloatMath;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;
import android.widget.ImageView;

public class MainActivity extends Activity implements OnTouchListener {

    private ImageView img_test;

    // 縮放控制
    private Matrix matrix = new Matrix();
    private Matrix savedMatrix = new Matrix();

    // 不同状态的表示：
    private static final int NONE = 0;
    private static final int DRAG = 1;
    private static final int ZOOM = 2;
    private int mode = NONE;

    // 定义第一个按下的点，两只接触点的重点，以及出事的两指按下的距离：
    private PointF startPoint = new PointF();
    private PointF midPoint = new PointF();
    private float oriDis = 1f;

    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onCreate(android.os.Bundle)
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_test = (ImageView) this.findViewById(R.id.img_test);
        img_test.setOnTouchListener(this);
    }

    @Override
    public boolean onTouch(View v, MotionEvent event) {
        ImageView view = (ImageView) v;
        switch (event.getAction() & MotionEvent.ACTION_MASK) {
        // 单指
        case MotionEvent.ACTION_DOWN:
            matrix.set(view.getImageMatrix());
            savedMatrix.set(matrix);
            startPoint.set(event.getX(), event.getY());
            mode = DRAG;
            break;
        // 双指
        case MotionEvent.ACTION_POINTER_DOWN:
            oriDis = distance(event);
            if (oriDis > 10f) {
                savedMatrix.set(matrix);
                midPoint = middle(event);
                mode = ZOOM;
            }
            break;
        // 手指放开
        case MotionEvent.ACTION_UP:
        case MotionEvent.ACTION_POINTER_UP:
            mode = NONE;
            break;
        // 单指滑动事件
        case MotionEvent.ACTION_MOVE:
            if (mode == DRAG) {
                // 是一个手指拖动
                matrix.set(savedMatrix);
                matrix.postTranslate(event.getX() - startPoint.x, event.getY() - startPoint.y);
            } else if (mode == ZOOM) {
                // 两个手指滑动
                float newDist = distance(event);
                if (newDist > 10f) {
                    matrix.set(savedMatrix);
                    float scale = newDist / oriDis;
                    matrix.postScale(scale, scale, midPoint.x, midPoint.y);
                }
            }
            break;
        }
        // 设置ImageView的Matrix
        view.setImageMatrix(matrix);
        return true;
    }

    // 计算两个触摸点之间的距离
    private float distance(MotionEvent event) {
        float x = event.getX(0) - event.getX(1);
        float y = event.getY(0) - event.getY(1);
        return FloatMath.sqrt(x * x + y * y);
    }

    // 计算两个触摸点的中点
    private PointF middle(MotionEvent event) {
        float x = event.getX(0) + event.getX(1);
        float y = event.getY(0) + event.getY(1);
        return new PointF(x / 2, y / 2);
    }

}
```
