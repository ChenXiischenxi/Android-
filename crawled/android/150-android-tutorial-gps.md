# 10.14 Android GPS初涉

> 来源: https://www.runoob.com/w3cnote/android-tutorial-gps.html

## 代码块 1

```java
LocationManager lm = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
```

## 代码块 2

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
```

## 代码块 3

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_one"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="获得系统所有的LocationProvider" />

    <Button
        android:id="@+id/btn_two"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="根据条件获取LocationProvider" />

    <Button
        android:id="@+id/btn_three"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="获取指定的LocationProvider" />

    <TextView
        android:id="@+id/tv_result"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_margin="10dp"
        android:background="#81BB4D"
        android:padding="5dp"
        android:textColor="#FFFFFF"
        android:textSize="20sp"
        android:textStyle="bold" />

</LinearLayout>
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_one;
    private Button btn_two;
    private Button btn_three;
    private TextView tv_result;
    private LocationManager lm;
    private List<String> pNames = new ArrayList<String>(); // 存放LocationProvider名称的集合

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        bindViews();
    }

    private void bindViews() {
        btn_one = (Button) findViewById(R.id.btn_one);
        btn_two = (Button) findViewById(R.id.btn_two);
        btn_three = (Button) findViewById(R.id.btn_three);
        tv_result = (TextView) findViewById(R.id.tv_result);

        btn_one.setOnClickListener(this);
        btn_two.setOnClickListener(this);
        btn_three.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_one:
                pNames.clear();
                pNames = lm.getAllProviders();
                tv_result.setText(getProvider());
                break;
            case R.id.btn_two:
                pNames.clear();
                Criteria criteria = new Criteria();
                criteria.setCostAllowed(false);   //免费
                criteria.setAltitudeRequired(true);  //能够提供高度信息
                criteria.setBearingRequired(true);   //能够提供方向信息
                pNames = lm.getProviders(criteria, true);
                tv_result.setText(getProvider());
                break;
            case R.id.btn_three:
                pNames.clear();
                pNames.add(lm.getProvider(LocationManager.GPS_PROVIDER).getName()); //指定名称
                tv_result.setText(getProvider());
                break;
        }
    }

    //遍历数组返回字符串的方法
    private String getProvider(){
        StringBuilder sb = new StringBuilder();
        for (String s : pNames) {
            sb.append(s + "\n");
        }
        return sb.toString();
    }
}
```

## 代码块 5

```java
private boolean isGpsAble(LocationManager lm){
    return lm.isProviderEnabled(android.location.LocationManager.GPS_PROVIDER)?true:false;
}
```

## 代码块 6

```java
//强制帮用户打开GPS 5.0以前可用
private void openGPS(Context context){
    Intent gpsIntent = new Intent();
    gpsIntent.setClassName("com.android.settings", "com.android.settings.widget.SettingsAppWidgetProvider");
    gpsIntent.addCategory("android.intent.category.ALTERNATIVE");
    gpsIntent.setData(Uri.parse("custom:3"));
    try {
        PendingIntent.getBroadcast(LocationActivity.this, 0, gpsIntent, 0).send();
    } catch (PendingIntent.CanceledException e) {
        e.printStackTrace();
    }
}
```

## 代码块 7

```java
//打开位置信息设置页面让用户自己设置
private void openGPS2(){
    Intent intent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
    startActivityForResult(intent,0);
}
```

## 代码块 8

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/tv_show"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="5dp"
        android:textSize="20sp"
        android:textStyle="bold" />

</LinearLayout>
```

## 代码块 9

```java
/**
 * Created by Jay on 2015/11/20 0020.
 */
public class LocationActivity extends AppCompatActivity {

    private LocationManager lm;
    private TextView tv_show;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_location);
        tv_show = (TextView) findViewById(R.id.tv_show);
        lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        if (!isGpsAble(lm)) {
            Toast.makeText(LocationActivity.this, "请打开GPS~", Toast.LENGTH_SHORT).show();
            openGPS2();
        }
        //从GPS获取最近的定位信息
        Location lc = lm.getLastKnownLocation(LocationManager.GPS_PROVIDER);
        updateShow(lc);
        //设置间隔两秒获得一次GPS定位信息
        lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 2000, 8, new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                // 当GPS定位信息发生改变时，更新定位
                updateShow(location);
            }

            @Override
            public void onStatusChanged(String provider, int status, Bundle extras) {

            }

            @Override
            public void onProviderEnabled(String provider) {
                // 当GPS LocationProvider可用时，更新定位
                updateShow(lm.getLastKnownLocation(provider));
            }

            @Override
            public void onProviderDisabled(String provider) {
                updateShow(null);
            }
        });
    }


    //定义一个更新显示的方法
    private void updateShow(Location location) {
        if (location != null) {
            StringBuilder sb = new StringBuilder();
            sb.append("当前的位置信息：\n");
            sb.append("精度：" + location.getLongitude() + "\n");
            sb.append("纬度：" + location.getLatitude() + "\n");
            sb.append("高度：" + location.getAltitude() + "\n");
            sb.append("速度：" + location.getSpeed() + "\n");
            sb.append("方向：" + location.getBearing() + "\n");
            sb.append("定位精度：" + location.getAccuracy() + "\n");
            tv_show.setText(sb.toString());
        } else tv_show.setText("");
    }


    private boolean isGpsAble(LocationManager lm) {
        return lm.isProviderEnabled(android.location.LocationManager.GPS_PROVIDER) ? true : false;
    }


    //打开设置页面让用户自己设置
    private void openGPS2() {
        Intent intent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
        startActivityForResult(intent, 0);
    }

}
```

## 代码块 10

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

## 代码块 11

```java
/**
 * Created by Jay on 2015/11/21 0021.
 */
public class ProximityActivity extends AppCompatActivity {
    private LocationManager lm;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_proximity);
        lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        //定义固定点的经纬度
        double longitude = 113.56843;
        double latitude = 22.374937;
        float radius = 10;     //定义半径，米
        Intent intent = new Intent(this, ProximityReceiver.class);
        PendingIntent pi = PendingIntent.getBroadcast(this, -1, intent, 0);
        lm.addProximityAlert(latitude, longitude, radius, -1, pi);
    }
}
```

## 代码块 12

```java
/**
 * Created by Jay on 2015/11/21 0021.
 */
public class ProximityReceiver extends BroadcastReceiver{
    @Override
    public void onReceive(Context context, Intent intent) {
        boolean isEnter = intent.getBooleanExtra( LocationManager.KEY_PROXIMITY_ENTERING, false);
        if(isEnter) Toast.makeText(context, "你已到达南软B1栋附近", Toast.LENGTH_LONG).show();
        else Toast.makeText(context, "你已离开南软B1栋附近", Toast.LENGTH_LONG).show();
    }
}
```

## 代码块 13

```xml
<receiver android:name=".ProximityReceiver"/>
```
