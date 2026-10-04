# 3.2 基于回调的事件处理机制

> 来源: https://www.runoob.com/w3cnote/android-tutorial-callback-event-handle.html

## 代码块 1

```java
public class MyButton extends Button{
    private static String TAG = "呵呵";
    public MyButton(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    //重写键盘按下触发的事件
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        super.onKeyDown(keyCode,event);
        Log.i(TAG, "onKeyDown方法被调用");
        return true;
    }

    //重写弹起键盘触发的事件
    @Override
    public boolean onKeyUp(int keyCode, KeyEvent event) {
        super.onKeyUp(keyCode,event);
        Log.i(TAG,"onKeyUp方法被调用");
        return true;
    }

    //组件被触摸了
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        super.onTouchEvent(event);
        Log.i(TAG,"onTouchEvent方法被调用");
        return true;
    }
}
```

## 代码块 2

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MyActivity">

    <example.jay.com.mybutton.MyButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="按钮"/>
```

## 代码块 3

```java
public class MyButton extends Button{
    private static String TAG = "呵呵";
    public MyButton(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    //重写键盘按下触发的事件
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        super.onKeyDown(keyCode,event);
        Log.i(TAG, "自定义按钮的onKeyDown方法被调用");
        return false;
    }
}
```

## 代码块 4

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MyActivity">

    <example.jay.com.mybutton.MyButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="自定义按钮"
        android:id="@+id/btn_my"/>
</LinearLayout>
```

## 代码块 5

```java
public class MyActivity extends ActionBarActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);

        Button btn = (Button)findViewById(R.id.btn_my);
        btn.setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if(event.getAction() == KeyEvent.ACTION_DOWN)
                {
                    Log.i("呵呵","监听器的onKeyDown方法被调用");
                }
                return false;
            }
        });
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        super.onKeyDown(keyCode, event);
        Log.i("呵呵","Activity的onKeyDown方法被调用");
        return false;
    }
}
```
