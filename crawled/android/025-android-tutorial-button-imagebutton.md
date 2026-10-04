# 2.3.3 Button(按钮)与ImageButton(图像按钮)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-button-imagebutton.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true" android:drawable="@drawable/ic_course_bg_fen"/>
    <item android:state_enabled="false" android:drawable="@drawable/ic_course_bg_pressed"/>
    <item android:drawable="@drawable/ic_course_bg_cheng"/>
</selector>
```

## 代码块 2

```xml
<Button
        android:id="@+id/btnOne"
        android:layout_width="match_parent"
        android:layout_height="64dp"
        android:background="@drawable/btn_bg1"
        android:text="按钮"/>


    <Button
        android:id="@+id/btnTwo"
        android:layout_width="match_parent"
        android:layout_height="64dp"
        android:text="按钮不可用"/>
```

## 代码块 3

```java
public class MainActivity extends Activity {

    private Button btnOne,btnTwo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnOne = (Button) findViewById(R.id.btnOne);
        btnTwo = (Button) findViewById(R.id.btnTwo);
        btnTwo.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                if(btnTwo.getText().toString().equals("按钮不可用")){
                    btnOne.setEnabled(false);
                    btnTwo.setText("按钮可用");
                }else{
                    btnOne.setEnabled(true);
                    btnTwo.setText("按钮不可用");
                }
            }
        });
    }

}
```

## 代码块 4

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">

    <item android:state_pressed="true"><shape>
            <solid android:color="@color/bbutton_danger_pressed" />
            <stroke android:width="1dp" android:color="@color/bbutton_danger_edge" />
            <corners android:radius="@dimen/bbuton_rounded_corner_radius"/>
        </shape></item>


    <item android:state_enabled="false"><shape>
        <solid android:color="@color/bbutton_danger_disabled" />
            <stroke android:width="1dp" android:color="@color/bbutton_danger_disabled_edge" />
            <corners android:radius="@dimen/bbuton_rounded_corner_radius"/>
        </shape></item>


    <item><shape>
            <solid android:color="@color/bbutton_danger" />
            <stroke android:width="1dp" android:color="@color/bbutton_danger_edge" />
            <corners android:radius="@dimen/bbuton_rounded_corner_radius"/>
        </shape></item>


</selector>
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="bbutton_danger_pressed">#ffd2322d</color>
    <color name="bbutton_danger_edge">#ffd43f3a</color>
    <color name="bbutton_danger_disabled">#a5d9534f</color>
    <color name="bbutton_danger_disabled_edge">#a5d43f3a</color>
    <color name="bbutton_danger">#ffd9534f</color>
    <color name="text_font_white">#FFFFFF</color>
</resources>
```

## 代码块 6

```xml
<dimen name="bbuton_rounded_corner_radius">5dp</dimen>
```

## 代码块 7

```java
package demo.com.jay.buttondemo;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.os.SystemClock;
import android.util.AttributeSet;
import android.view.MotionEvent;
import android.view.ViewConfiguration;
import android.widget.ImageButton;

/**
 * Created by coder-pig on 2015/7/16 0016.
 */
public class MyButton extends ImageButton {


    private static final int INVALIDATE_DURATION = 15;     //每次刷新的时间间隔
    private static int DIFFUSE_GAP = 10;                  //扩散半径增量
    private static int TAP_TIMEOUT;                         //判断点击和长按的时间

    private int viewWidth, viewHeight;                   //控件宽高
    private int pointX, pointY;                          //控件原点坐标（左上角）
    private int maxRadio;                             //扩散的最大半径
    private int shaderRadio;                        //扩散的半径

    private Paint bottomPaint, colorPaint;          //画笔:背景和水波纹
    private boolean isPushButton;                 //记录是否按钮被按下

    private int eventX, eventY;                  //触摸位置的X,Y坐标
    private long downTime = 0;                 //按下的时间


    public MyButton(Context context, AttributeSet attrs) {
        super(context, attrs);
        initPaint();
        TAP_TIMEOUT = ViewConfiguration.getLongPressTimeout();
    }


    /*
    * 初始化画笔
    * */
    private void initPaint() {
        colorPaint = new Paint();
        bottomPaint = new Paint();
        colorPaint.setColor(getResources().getColor(R.color.reveal_color));
        bottomPaint.setColor(getResources().getColor(R.color.bottom_color));
    }


    @Override
    public boolean onTouchEvent(MotionEvent event) {
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                if (downTime == 0) downTime = SystemClock.elapsedRealtime();
                eventX = (int) event.getX();
                eventY = (int) event.getY();
                //计算最大半径：
                countMaxRadio();
                isPushButton = true;
                postInvalidateDelayed(INVALIDATE_DURATION);
                break;
            case MotionEvent.ACTION_UP:
            case MotionEvent.ACTION_CANCEL:
                if(SystemClock.elapsedRealtime() - downTime < TAP_TIMEOUT){
                    DIFFUSE_GAP = 30;
                    postInvalidate();
                }else{
                    clearData();
                }
                break;
        }
        return super.onTouchEvent(event);
    }


    @Override
    protected void dispatchDraw(Canvas canvas) {
        super.dispatchDraw(canvas);
        if(!isPushButton) return; //如果按钮没有被按下则返回
        //绘制按下后的整个背景
        canvas.drawRect(pointX, pointY, pointX + viewWidth, pointY + viewHeight, bottomPaint);
        canvas.save();
        //绘制扩散圆形背景
        canvas.clipRect(pointX, pointY, pointX + viewWidth, pointY + viewHeight);
        canvas.drawCircle(eventX, eventY, shaderRadio, colorPaint);
        canvas.restore();
        //直到半径等于最大半径
        if(shaderRadio < maxRadio){
            postInvalidateDelayed(INVALIDATE_DURATION,
                    pointX, pointY, pointX + viewWidth, pointY + viewHeight);
            shaderRadio += DIFFUSE_GAP;
        }else{
            clearData();
        }
    }

    /*
        * 计算最大半径的方法
        * */
    private void countMaxRadio() {
        if (viewWidth > viewHeight) {
            if (eventX < viewWidth / 2) {
                maxRadio = viewWidth - eventX;
            } else {
                maxRadio = viewWidth / 2 + eventX;
            }
        } else {
            if (eventY < viewHeight / 2) {
                maxRadio = viewHeight - eventY;
            } else {
                maxRadio = viewHeight / 2 + eventY;
            }
        }
    }


    /*
    * 重置数据的方法
    * */
    private void clearData(){
        downTime = 0;
        DIFFUSE_GAP = 10;
        isPushButton = false;
        shaderRadio = 0;
        postInvalidate();
    }

    @Override
    protected void onSizeChanged(int w, int h, int oldw, int oldh) {
        super.onSizeChanged(w, h, oldw, oldh);
        this.viewWidth = w;
        this.viewHeight = h;
    }
}
```

## 代码块 8

```xml
<code>
<p><b>color.xml：</b></p>
<pre>
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="reveal_color">#FFFFFF</color>
    <color name="bottom_color">#3086E4</color>
    <color name="bottom_bg">#40BAF8</color>
</resources>
```

## 代码块 9

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <demo.com.jay.buttondemo.MyButton
        android:id="@+id/myBtn"
        android:layout_width="match_parent"
        android:layout_height="64dp"
        android:src="@mipmap/ic_tur_icon"
        android:background="@color/bottom_bg"
        android:scaleType="center"/>

</RelativeLayout>
```
