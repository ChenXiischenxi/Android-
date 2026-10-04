# 3.8 Gestures(手势)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-gestures.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {

    private MyGestureListener mgListener;
    private GestureDetector mDetector;
    private final static String TAG = "MyGesture";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //实例化GestureListener与GestureDetector对象
        mgListener = new MyGestureListener();
        mDetector = new GestureDetector(this, mgListener);

    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        return mDetector.onTouchEvent(event);
    }

    //自定义一个GestureListener,这个是View类下的，别写错哦！！！
    private class MyGestureListener implements GestureDetector.OnGestureListener {

        @Override
        public boolean onDown(MotionEvent motionEvent) {
            Log.d(TAG, "onDown:按下");
            return false;
        }

        @Override
        public void onShowPress(MotionEvent motionEvent) {
            Log.d(TAG, "onShowPress:手指按下一段时间,不过还没到长按");
        }

        @Override
        public boolean onSingleTapUp(MotionEvent motionEvent) {
            Log.d(TAG, "onSingleTapUp:手指离开屏幕的一瞬间");
            return false;
        }

        @Override
        public boolean onScroll(MotionEvent motionEvent, MotionEvent motionEvent1, float v, float v1) {
            Log.d(TAG, "onScroll:在触摸屏上滑动");
            return false;
        }

        @Override
        public void onLongPress(MotionEvent motionEvent) {
            Log.d(TAG, "onLongPress:长按并且没有松开");
        }

        @Override
        public boolean onFling(MotionEvent motionEvent, MotionEvent motionEvent1, float v, float v1) {
            Log.d(TAG, "onFling:迅速滑动，并松开");
            return false;
        }
    }

}
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity {

    private GestureDetector mDetector;
    private final static int MIN_MOVE = 200;   //最小距离
    private MyGestureListener mgListener;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //实例化SimpleOnGestureListener与GestureDetector对象
        mgListener = new MyGestureListener();
        mDetector = new GestureDetector(this, mgListener);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        return mDetector.onTouchEvent(event);
    }

    //自定义一个GestureListener,这个是View类下的，别写错哦！！！
    private class MyGestureListener extends GestureDetector.SimpleOnGestureListener {

        @Override
        public boolean onFling(MotionEvent e1, MotionEvent e2, float v, float v1) {
            if(e1.getY() - e2.getY() > MIN_MOVE){
                startActivity(new Intent(MainActivity.this, MainActivity.class));
                Toast.makeText(MainActivity.this, "通过手势启动Activity", Toast.LENGTH_SHORT).show();
            }else if(e1.getY() - e2.getY()  < MIN_MOVE){
                finish();
                Toast.makeText(MainActivity.this,"通过手势关闭Activity",Toast.LENGTH_SHORT).show();
            }
            return true;
        }
    }

}
```

## 代码块 3

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="请在下方屏幕中绘制手势~"
        android:textSize="20sp"/>


    <!-- gestureStrokeType控制手势是否需要一笔完成,multiple表示允许多笔-->
    <android.gesture.GestureOverlayView
        android:id="@+id/gesture"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gestureStrokeType="multiple" />

</LinearLayout>
```

## 代码块 4

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginRight="8dp"
            android:text="请填写手势名称："/>
        <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/edit_name"/>
    </LinearLayout>

    <ImageView
        android:id="@+id/img_show"
        android:layout_width="128dp"
        android:layout_height="128dp"
        android:layout_marginTop="10dp"/>

</LinearLayout>
```

## 代码块 5

```java
public class MainActivity extends AppCompatActivity {

    private EditText editText;
    private GestureOverlayView gesture;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //获取手势编辑组件后，设置相关参数
        gesture = (GestureOverlayView) findViewById(R.id.gesture);
        gesture.setGestureColor(Color.GREEN);
        gesture.setGestureStrokeWidth(5);
        gesture.addOnGesturePerformedListener(new GestureOverlayView.OnGesturePerformedListener() {
            @Override
            public void onGesturePerformed(GestureOverlayView gestureOverlayView, final Gesture gesture) {
                View saveDialog = getLayoutInflater().inflate(R.layout.dialog_save,null,false);
                ImageView img_show = (ImageView) saveDialog.findViewById(R.id.img_show);
                final EditText edit_name = (EditText) saveDialog.findViewById(R.id.edit_name);
                Bitmap bitmap = gesture.toBitmap(128,128,10,0xffff0000);
                img_show.setImageBitmap(bitmap);
                new AlertDialog.Builder(MainActivity.this).setView(saveDialog)
                        .setPositiveButton("保存",new DialogInterface.OnClickListener()
                        {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                //获取文件对应的手势库
                                GestureLibrary gestureLib = GestureLibraries.fromFile("/mnt/sdcard/mygestures");
                                gestureLib.addGesture(edit_name.getText().toString(),gesture);
                                gestureLib.save();
                            }
                        }).setNegativeButton("取消", null).show();
            }
        });
    }
}
```

## 代码块 6

```xml
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

## 代码块 7

```java
public class MainActivity extends AppCompatActivity {

    private GestureOverlayView gesture;
    private GestureLibrary gestureLibrary;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        gestureLibrary = GestureLibraries.fromFile("mmt/sdcard/mygestures");
        if (gestureLibrary.load()) {
            Toast.makeText(mContext, "手势库加载成功", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(mContext, "手势库加载失败", Toast.LENGTH_SHORT).show();
        }

        //获取手势编辑组件后，设置相关参数
        gesture = (GestureOverlayView) findViewById(R.id.gesture);
        gesture.setGestureColor(Color.GREEN);
        gesture.setGestureStrokeWidth(5);
        gesture.addOnGesturePerformedListener(new GestureOverlayView.OnGesturePerformedListener() {
            @Override
            public void onGesturePerformed(GestureOverlayView gestureOverlayView, final Gesture gesture) {
                //识别用户刚绘制的手势
                ArrayList<Prediction> predictions = gestureLibrary.recognize(gesture);
                ArrayList<String> result = new ArrayList<String>();
                //遍历所有找到的Prediction对象
                for (Prediction pred : predictions) {
                    if (pred.score > 2.0) {
                        result.add("与手势【" + pred.name + "】相似度为" + pred.score);
                    }
                }
                if (result.size() > 0) {
                    ArrayAdapter<Object> adapter = new ArrayAdapter<Object>(mContext,
                            android.R.layout.simple_dropdown_item_1line, result.toArray());
                    new AlertDialog.Builder(mContext).setAdapter(adapter,null).setPositiveButton("确定",null).show();
                }else{
                    Toast.makeText(mContext,"无法找到匹配的手势！",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
```

## 代码块 8

```xml
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```
