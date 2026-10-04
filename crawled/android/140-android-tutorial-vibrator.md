# 10.4 Vibrator(振动器)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-vibrator.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_hasVibrator"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="判断是否有振动器" />


    <Button
        android:id="@+id/btn_short"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="短振动" />

    <Button
        android:id="@+id/btn_long"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="长振动" />

    <Button
        android:id="@+id/btn_rhythm"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="节奏振动" />

    <Button
        android:id="@+id/btn_cancle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="取消振动" />
</LinearLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_hasVibrator;
    private Button btn_short;
    private Button btn_long;
    private Button btn_rhythm;
    private Button btn_cancle;
    private Vibrator myVibrator;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //获得系统的Vibrator实例:
        myVibrator = (Vibrator) getSystemService(Service.VIBRATOR_SERVICE);
        mContext = MainActivity.this;
        bindViews();
    }

    private void bindViews() {
        btn_hasVibrator = (Button) findViewById(R.id.btn_hasVibrator);
        btn_short = (Button) findViewById(R.id.btn_short);
        btn_long = (Button) findViewById(R.id.btn_long);
        btn_rhythm = (Button) findViewById(R.id.btn_rhythm);
        btn_cancle = (Button) findViewById(R.id.btn_cancle);

        btn_hasVibrator.setOnClickListener(this);
        btn_short.setOnClickListener(this);
        btn_long.setOnClickListener(this);
        btn_rhythm.setOnClickListener(this);
        btn_cancle.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_hasVibrator:
                Toast.makeText(mContext, myVibrator.hasVibrator() ? "当前设备有振动器" : "当前设备无振动器",
                        Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_short:
                myVibrator.cancel();
                myVibrator.vibrate(new long[]{100, 200, 100, 200}, 0);
                Toast.makeText(mContext, "短振动", Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_long:
                myVibrator.cancel();
                myVibrator.vibrate(new long[]{100, 100, 100, 1000}, 0);
                Toast.makeText(mContext, "长振动", Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_rhythm:
                myVibrator.cancel();
                myVibrator.vibrate(new long[]{500, 100, 500, 100, 500, 100}, 0);
                Toast.makeText(mContext, "节奏振动", Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_cancle:
                myVibrator.cancel();
                Toast.makeText(mContext, "取消振动", Toast.LENGTH_SHORT).show();
        }
    }
}
```

## 代码块 3

```xml
<uses-permission android:name="android.permission.VIBRATE"/>
```
