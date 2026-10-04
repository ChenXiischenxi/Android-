# 2.4.2 Date &#038; Time组件(上)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-date-time-1.html

## 代码块 1

```xml
<TextClock
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:format12Hour="MM/dd/yy h:mmaa"/>
    <TextClock
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:format12Hour="MMM dd, yyyy h:mmaa"/>
    <TextClock
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:format12Hour="MMMM dd, yyyy h:mmaa"/>
    <TextClock
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:format12Hour="E, MMMM dd, yyyy h:mmaa"/>
    <TextClock
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:format12Hour="EEEE, MMMM dd, yyyy h:mmaa"/>
    <TextClock
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:format12Hour="Noteworthy day: 'M/d/yy"/>
```

## 代码块 2

```xml
<AnalogClock
        android:layout_width="100dp"
        android:layout_height="100dp"
        android:dial="@mipmap/ic_c_bg"
        android:hand_hour="@mipmap/zhen_shi"
        android:hand_minute="@mipmap/zhen_fen" />
```

## 代码块 3

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">


    <Chronometer
        android:id="@+id/chronometer"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:gravity="center"
        android:textColor="#ff0000"
        android:textSize="60dip" />

    <LinearLayout
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dip"
        android:orientation="horizontal">

        <Button
            android:id="@+id/btnStart"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="开始记时" />

        <Button
            android:id="@+id/btnStop"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="停止记时" />

        <Button
            android:id="@+id/btnReset"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="重置" />

        <Button
            android:id="@+id/btn_format"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="格式化" />
    </LinearLayout>

</LinearLayout>
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener,Chronometer.OnChronometerTickListener{

    private Chronometer chronometer;
    private Button btn_start,btn_stop,btn_base,btn_format;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
    }

    private void initView() {
        chronometer = (Chronometer) findViewById(R.id.chronometer);
        btn_start = (Button) findViewById(R.id.btnStart);
        btn_stop = (Button) findViewById(R.id.btnStop);
        btn_base = (Button) findViewById(R.id.btnReset);
        btn_format = (Button) findViewById(R.id.btn_format);

        chronometer.setOnChronometerTickListener(this);
        btn_start.setOnClickListener(this);
        btn_stop.setOnClickListener(this);
        btn_base.setOnClickListener(this);
        btn_format.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btnStart:
                chronometer.start();// 开始计时
                break;
            case R.id.btnStop:
                chronometer.stop();// 停止计时
                break;
            case R.id.btnReset:
                chronometer.setBase(SystemClock.elapsedRealtime());// 复位
                break;
            case R.id.btn_format:
                chronometer.setFormat("Time：%s");// 更改时间显示格式
                break;
        }
    }

    @Override
    public void onChronometerTick(Chronometer chronometer) {
        String time = chronometer.getText().toString();
        if(time.equals("00:00")){
            Toast.makeText(MainActivity.this,"时间到了~",Toast.LENGTH_SHORT).show();
        }
    }
}
```
