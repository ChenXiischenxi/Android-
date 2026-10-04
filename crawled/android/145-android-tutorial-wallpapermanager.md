# 10.9 WallpaperManager(壁纸管理器)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-wallpapermanager.html

## 代码块 1

```java
WallpaperManager wpManager =WallpaperManager.getInstance(this);
```

## 代码块 2

```xml
<uses-permission android:name="android.permission.SET_WALLPAPER"/>
```

## 代码块 3

```java
Button btn_set = (Button) findViewById(R.id.btn_set);
    btn_set.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            Intent chooseIntent = new Intent(Intent.ACTION_SET_WALLPAPER);
            startActivity(Intent.createChooser(chooseIntent, "选择壁纸"));
        }
    });
```

## 代码块 4

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    setTheme(android.R.style.Theme_Wallpaper_NoTitleBar_Fullscreen);
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
}
```

## 代码块 5

```xml
<activity android:name=".MainActivity"
android:theme="@android:style/Theme.Wallpaper.NoTitleBar"/>
```

## 代码块 6

```java
/**
 * Created by Jay on 2015/11/13 0013.
 */
public class WallPaperService extends Service {

    private int current = 0;  //当前壁纸下标
    private int[] papers = new int[]{R.mipmap.gui_1,R.mipmap.gui_2,R.mipmap.gui_3,R.mipmap.gui_4};
    private WallpaperManager wManager = null;   //定义WallpaperManager服务

    @Override
    public void onCreate() {
        super.onCreate();
        wManager = WallpaperManager.getInstance(this);
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if(current >= 4)current = 0;
        try{
            wManager.setResource(papers[current++]);
        }catch(Exception e){e.printStackTrace();}
        return START_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
```

## 代码块 7

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_on"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="开启自动换壁纸" />

    <Button
        android:id="@+id/btn_off"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="关闭自动换壁纸" />

    <Button
        android:id="@+id/btn_clean"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="清除壁纸" />

</LinearLayout>
```

## 代码块 8

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_on;
    private Button btn_off;
    private Button btn_clean;
    private AlarmManager aManager;
    private PendingIntent pi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //①获得AlarmManager对象:
        aManager = (AlarmManager) getSystemService(ALARM_SERVICE);
        //②指定要启动的Service,并指明动作是Servce:
        Intent intent = new Intent(MainActivity.this, WallPaperService.class);
        pi = PendingIntent.getService(MainActivity.this, 0, intent, 0);
        bindViews();
    }

    private void bindViews() {
        btn_on = (Button) findViewById(R.id.btn_on);
        btn_off = (Button) findViewById(R.id.btn_off);
        btn_clean = (Button) findViewById(R.id.btn_clean);
        btn_on.setOnClickListener(this);
        btn_off.setOnClickListener(this);
        btn_clean.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_on:
                aManager.setRepeating(AlarmManager.RTC_WAKEUP, 0, 3000, pi);
                btn_on.setEnabled(false);
                btn_off.setEnabled(true);
                Toast.makeText(MainActivity.this, "自动更换壁纸设置成功", Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_off:
                btn_on.setEnabled(true);
                btn_off.setEnabled(false);
                aManager.cancel(pi);
                break;
            case R.id.btn_clean:
                try {
                    WallpaperManager.getInstance(getApplicationContext()).clear();
                    Toast.makeText(MainActivity.this, "清除壁纸成功~", Toast.LENGTH_SHORT).show();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                break;
        }
    }
}
```

## 代码块 9

```xml
<uses-permission android:name="android.permission.SET_WALLPAPER" />
<service android:name=".WallPaperService"/>
```
