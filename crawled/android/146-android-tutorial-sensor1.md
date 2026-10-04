# 10.10 传感器专题(1)——相关介绍

> 来源: https://www.runoob.com/w3cnote/android-tutorial-sensor1.html

## 代码块 1

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        <TextView
            android:id="@+id/txt_show"
            android:layout_width="match_parent"
            android:layout_height="match_parent" />
    </ScrollView>
</RelativeLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity {

    private TextView txt_show;
    private SensorManager sm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sm = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        txt_show = (TextView) findViewById(R.id.txt_show);

        List<Sensor> allSensors = sm.getSensorList(Sensor.TYPE_ALL);
        StringBuilder sb = new StringBuilder();

        sb.append("此手机有" + allSensors.size() + "个传感器，分别有：\n\n");
        for(Sensor s:allSensors){
            switch (s.getType()){
                case Sensor.TYPE_ACCELEROMETER:
                    sb.append(s.getType() + " 加速度传感器(Accelerometer sensor)" + "\n");
                    break;
                case Sensor.TYPE_GYROSCOPE:
                    sb.append(s.getType() + " 陀螺仪传感器(Gyroscope sensor)" + "\n");
                    break;
                case Sensor.TYPE_LIGHT:
                    sb.append(s.getType() + " 光线传感器(Light sensor)" + "\n");
                    break;
                case Sensor.TYPE_MAGNETIC_FIELD:
                    sb.append(s.getType() + " 磁场传感器(Magnetic field sensor)" + "\n");
                    break;
                case Sensor.TYPE_ORIENTATION:
                    sb.append(s.getType() + " 方向传感器(Orientation sensor)" + "\n");
                    break;
                case Sensor.TYPE_PRESSURE:
                    sb.append(s.getType() + " 气压传感器(Pressure sensor)" + "\n");
                    break;
                case Sensor.TYPE_PROXIMITY:
                    sb.append(s.getType() + " 距离传感器(Proximity sensor)" + "\n");
                    break;
                case Sensor.TYPE_TEMPERATURE:
                    sb.append(s.getType() + " 温度传感器(Temperature sensor)" + "\n");
                    break;
                default:
                    sb.append(s.getType() + " 其他传感器" + "\n");
                    break;
            }
            sb.append("设备名称：" + s.getName() + "\n 设备版本：" + s.getVersion() + "\n 供应商："
                    + s.getVendor() + "\n\n");
        }
        txt_show.setText(sb.toString());
    }
}
```

## 代码块 3

```java
SensorManager sm = (SensorManager)getSystemService(SENSOR_SERVICE);
```

## 代码块 4

```java
List<Sensor> allSensors = sm.getSensorList(Sensor.TYPE_ALL);
```

## 代码块 5

```java
for(Sensor s:allSensors){
    sensor.getName();   //获得传感器名称
    sensor.getType();     //获得传感器种类
    sensor.getVendor();    //获得传感器供应商
    sensor.getVersion();    //获得传感器版本
    sensor.getResolution();  //获得精度值
    sensor.getMaximumRange(); //获得最大范围
    sensor.getPower();        //传感器使用时的耗电量
}
```

## 代码块 6

```java
SensorManager sm = (SensorManager)getSystemService(SENSOR_SERVICE);
```

## 代码块 7

```java
Sensor mSensorOrientation = sm.getDefaultSensor(Sensor.TYPE_ORIENTATION);
```

## 代码块 8

```java
@Override
public void onSensorChanged(SensorEvent event) {
    final float[] _Data = event.values;
   this.mService.onSensorChanged(_Data[0],_Data[1],_Data[2]);
}
@Override
public void onAccuracyChanged(Sensor sensor, int accuracy) {
}
```

## 代码块 9

```xml
<code>ms.registerListener(mContext, mSensorOrientation, android.hardware.SensorManager.SENSOR_DELAY_UI);
</code>
```

## 代码块 10

```java
ms.registerListener(mContext, mSensorOrientation, android.hardware.SensorManager.SENSOR_DELAY_UI);
```
