# 10.11 传感器专题(2)——方向传感器

> 来源: https://www.runoob.com/w3cnote/android-tutorial-sensor2.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="5dp">

    <TextView
        android:id="@+id/tv_value1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:text="方位角"
        android:textSize="18sp"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/tv_value2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:text="倾斜角"
        android:textSize="18sp"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/tv_value3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:text="滚动角"
        android:textSize="18sp"
        android:textStyle="bold" />

</LinearLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private TextView tv_value1;
    private TextView tv_value2;
    private TextView tv_value3;
    private SensorManager sManager;
    private Sensor mSensorOrientation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        mSensorOrientation = sManager.getDefaultSensor(Sensor.TYPE_ORIENTATION);
        sManager.registerListener(this, mSensorOrientation, SensorManager.SENSOR_DELAY_UI);
        bindViews();
    }

    private void bindViews() {
        tv_value1 = (TextView) findViewById(R.id.tv_value1);
        tv_value2 = (TextView) findViewById(R.id.tv_value2);
        tv_value3 = (TextView) findViewById(R.id.tv_value3);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        tv_value1.setText("方位角：" + (float) (Math.round(event.values[0] * 100)) / 100);
        tv_value2.setText("倾斜角：" + (float) (Math.round(event.values[1] * 100)) / 100);
        tv_value3.setText("滚动角：" + (float) (Math.round(event.values[2] * 100)) / 100);
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }
}
```

## 代码块 3

```java
/**
 * Created by Jay on 2015/11/14 0014.
 */
public class CompassView extends View implements Runnable{

    private Paint mTextPaint;
    private int sWidth,sHeight;
    private float dec = 0.0f;
    private String msg  = "正北 0°";

    public CompassView(Context context) {
        this(context, null);
    }

    public CompassView(Context context, AttributeSet attrs) {
        super(context, attrs);
        sWidth = ScreenUtil.getScreenW(context);
        sHeight = ScreenUtil.getScreenH(context);
        init();
        new Thread(this).start();
    }


    public CompassView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void init() {

        mTextPaint = new Paint();
        mTextPaint.setColor(Color.GRAY);
        mTextPaint.setTextSize(64);
        mTextPaint.setStyle(Paint.Style.FILL);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        canvas.drawText(msg, sWidth / 4 , sWidth / 2, mTextPaint);
    }

    // 更新指南针角度
    public void setDegree(float degree)
    {
        // 设置灵敏度
        if(Math.abs(dec - degree) >= 2 )
        {
            dec = degree;
            int range = 22;
            String degreeStr = String.valueOf(dec);

            // 指向正北
            if(dec > 360 - range && dec < 360 + range)
            {
                msg = "正北 " + degreeStr + "°";
            }

            // 指向正东
            if(dec > 90 - range && dec < 90 + range)
            {
                msg = "正东 " + degreeStr + "°";
            }

            // 指向正南
            if(dec > 180 - range && dec < 180 + range)
            {
                msg = "正南 " + degreeStr + "°";
            }

            // 指向正西
            if(dec > 270 - range && dec < 270 + range)
            {
                msg = "正西 " + degreeStr + "°";
            }

            // 指向东北
            if(dec > 45 - range && dec < 45 + range)
            {
                msg = "东北 " + degreeStr + "°";
            }

            // 指向东南
            if(dec > 135 - range && dec < 135 + range)
            {
                msg = "东南 " + degreeStr + "°";
            }

            // 指向西南
            if(dec > 225 - range && dec < 225 + range)
            {
                msg = "西南 " + degreeStr + "°";
            }

            // 指向西北
            if(dec > 315 - range && dec < 315 + range)
            {
                msg = "西北 " + degreeStr + "°";
            }
        }
    }


    @Override
    public void run() {
        while(!Thread.currentThread().isInterrupted())
        {
            try
            {
                Thread.sleep(100);
            }
            catch(InterruptedException e)
            {
                Thread.currentThread().interrupt();
            }
            postInvalidate();
        }
    }
}
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private CompassView cView;
    private SensorManager sManager;
    private Sensor mSensorOrientation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        cView = new CompassView(MainActivity.this);
        sManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        mSensorOrientation = sManager.getDefaultSensor(Sensor.TYPE_ORIENTATION);
        sManager.registerListener(this, mSensorOrientation, SensorManager.SENSOR_DELAY_UI);
        setContentView(cView);
    }


    @Override
    public void onSensorChanged(SensorEvent event) {
        cView.setDegree(event.values[0]);
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        sManager.unregisterListener(this);
    }
}
```
