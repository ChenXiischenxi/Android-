# 8.1.2 Android中的13种Drawable小结 Part 2

> 来源: https://www.runoob.com/w3cnote/android-tutorial-drawable2.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<bitmap xmlns:android="http://schemas.android.com/apk/res/android"
    android:dither="true"
    android:src="@drawable/ic_launcher"
    android:tileMode="mirror" />
```

## 代码块 2

```java
BitmapDrawable bitDrawable = new BitmapDrawable(bitmap);
bitDrawable.setDither(true);
bitDrawable.setTileModeXY(TileMode.MIRROR,TileMode.MIRROR);
```

## 代码块 3

```xml
<?xml version="1.0" encoding="utf-8"?>
<inset xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/test1"
    android:insetBottom="10dp"
    android:insetLeft="10dp"
    android:insetRight="10dp"
    android:insetTop="10dp" />
```

## 代码块 4

```java
InsetDrawable insetDrawable = new InsetDrawable(getResources()
        .getDrawable(R.drawable.test1), 10, 10, 10, 10);
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<clip xmlns:android="http://schemas.android.com/apk/res/android"
    android:clipOrientation="horizontal"
    android:drawable="@mipmap/ic_bg_meizi"
    android:gravity="left" />
```

## 代码块 6

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <ImageView
        android:id="@+id/img_show"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:src="@drawable/clip_bg" />

</LinearLayout>
```

## 代码块 7

```java
public class MainActivity extends AppCompatActivity {

    private ImageView img_show;
    private ClipDrawable cd;
    private Handler handler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            if (msg.what == 0x123) {
                cd.setLevel(cd.getLevel() + 500);
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_show = (ImageView) findViewById(R.id.img_show);
        // 核心实现代码
        cd = (ClipDrawable) img_show.getDrawable();
        final Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                handler.sendEmptyMessage(0x123);
                if (cd.getLevel() >= 10000) {
                    timer.cancel();
                }
            }
        }, 0, 300);
    }
}
```

## 代码块 8

```xml
<?xml version="1.0" encoding="utf-8"?>
<rotate xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@mipmap/ic_launcher"
    android:fromDegrees="-180"
    android:pivotX="50%"
    android:pivotY="50%" />
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity {

    private ImageView img_show;
    private RotateDrawable cd;
    private Handler handler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            if (msg.what == 0x123) {
                if (cd.getLevel() >= 10000)
                    Toast.makeText(MainActivity.this, "转完了~",
                            Toast.LENGTH_LONG).show();
                cd.setLevel(cd.getLevel() + 400);
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_show = (ImageView) findViewById(R.id.img_show);
        // 核心实现代码
        cd = (RotateDrawable) img_show.getDrawable();
        final Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                handler.sendEmptyMessage(0x123);
                if (cd.getLevel() >= 10000) {
                    timer.cancel();
                }
            }
        }, 0, 100);
    }
}
```

## 代码块 10

```xml
<?xml version="1.0" encoding="utf-8"?>
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="false">

    <item
        android:drawable="@mipmap/ic_pull_to_refresh_loading01"
        android:duration="100" />

    <item
        android:drawable="@mipmap/ic_pull_to_refresh_loading02"
        android:duration="100" />
    <item
        android:drawable="@mipmap/ic_pull_to_refresh_loading03"
        android:duration="100" />
    <item
        android:drawable="@mipmap/ic_pull_to_refresh_loading04"
        android:duration="100" />
    <item
        android:drawable="@mipmap/ic_pull_to_refresh_loading05"
        android:duration="100" />
    <item
        android:drawable="@mipmap/ic_pull_to_refresh_loading06"
        android:duration="100" />

</animation-list>
```

## 代码块 11

```java
public class MainActivity extends AppCompatActivity {

    private ImageView img_show;
    private AnimationDrawable ad;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_show = (ImageView) findViewById(R.id.img_show);
        // 核心实现代码
        ad = (AnimationDrawable) img_show.getDrawable();
        Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                ad.start();
            }
        }, 300);
    }
}
```
