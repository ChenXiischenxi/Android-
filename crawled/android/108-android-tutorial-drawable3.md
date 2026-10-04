# 8.1.3 Android中的13种Drawable小结 Part 3

> 来源: https://www.runoob.com/w3cnote/android-tutorial-drawable3.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@android:id/background">
        <shape android:shape="rectangle">
            <solid android:color="#C2C2C1" />
            <corners android:radius="50dp" />
        </shape>
    </item>
    <item android:id="@android:id/progress">
        <clip>
            <shape android:shape="rectangle">
                <solid android:color="#BCDA73" />
                <corners android:radius="50dp" />
            </shape>
        </clip>
    </item>
</layer-list>
```

## 代码块 2

```xml
<SeekBar
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:indeterminateDrawable="@android:drawable/progress_indeterminate_horizontal"
        android:indeterminateOnly="false"
        android:maxHeight="10dp"
        android:minHeight="5dp"
        android:progressDrawable="@drawable/layerlist_one"
        android:thumb="@drawable/shape_slider" />
```

## 代码块 3

```xml
<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item>
        <bitmap
            android:gravity="center"
            android:src="@mipmap/ic_bg_ciwei" />
    </item>
    <item
        android:left="25dp"
        android:top="25dp">
        <bitmap
            android:gravity="center"
            android:src="@mipmap/ic_bg_ciwei" />
    </item>
    <item
        android:left="50dp"
        android:top="50dp">
        <bitmap
            android:gravity="center"
            android:src="@mipmap/ic_bg_ciwei" />
    </item>
</layer-list>
```

## 代码块 4

```xml
<ImageView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/layerlist_two"/>
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<transition xmlns:android="http://schemas.android.com/apk/res/android" >
    <item android:drawable="@mipmap/ic_bg_meizi1"/>
    <item android:drawable="@mipmap/ic_bg_meizi2"/>
</transition>
```

## 代码块 6

```java
public class MainActivity extends AppCompatActivity {
    private ImageView img_show;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_show = (ImageView) findViewById(R.id.img_show);
        TransitionDrawable td = (TransitionDrawable) img_show.getDrawable();
        td.startTransition(3000);
        //你可以可以反过来播放，使用reverseTransition即可~
        //td.reverseTransition(3000);
    }
}
```

## 代码块 7

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval">
    <solid android:color="#2C96ED"/>
    <size android:height="20dp" android:width="20dp"/>
</shape>
```

## 代码块 8

```xml
<?xml version="1.0" encoding="utf-8"?>
<level-list xmlns:android="http://schemas.android.com/apk/res/android" >
    <item android:drawable="@drawable/shape_cir1" android:maxLevel="2000"/>
    <item android:drawable="@drawable/shape_cir2" android:maxLevel="4000"/>
    <item android:drawable="@drawable/shape_cir3" android:maxLevel="6000"/>
    <item android:drawable="@drawable/shape_cir4" android:maxLevel="8000"/>
    <item android:drawable="@drawable/shape_cir5" android:maxLevel="10000"/>
</level-list>
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity {

    private ImageView img_show;

    private LevelListDrawable ld;
    private Handler handler = new Handler() {
        public void handleMessage(Message msg) {
            if (msg.what == 0x123) {
                if (ld.getLevel() > 10000) ld.setLevel(0);
                img_show.setImageLevel(ld.getLevel() + 2000);
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_show = (ImageView) findViewById(R.id.img_show);
        ld = (LevelListDrawable) img_show.getDrawable();
        img_show.setImageLevel(0);
        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                handler.sendEmptyMessage(0x123);
            }
        }, 0, 100);
    }
}
```

## 代码块 10

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <solid android:color="#DD788A"/>
    <corners android:radius="5dp"/>
    <padding android:top="2dp" android:bottom="2dp"/>
</shape>
```

## 代码块 11

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true" android:drawable="@drawable/shape_btn_pressed"/>
    <item android:drawable="@drawable/shape_btn_normal"/>
</selector>
```
