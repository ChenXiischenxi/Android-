# 2.3.6 开关按钮ToggleButton和开关Switch

> 来源: https://www.runoob.com/w3cnote/android-tutorial-togglebutton-switch.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true" android:drawable="@drawable/switch_btn_pressed"/>
    <item android:state_pressed="false" android:drawable="@drawable/switch_btn_normal"/>
</selector>
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_checked="true" android:drawable="@drawable/switch_btn_bg_green"/>
    <item android:state_checked="false" android:drawable="@drawable/switch_btn_bg_white"/>
</selector>
```

## 代码块 3

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <ToggleButton
        android:id="@+id/tbtn_open"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:checked="true"
        android:textOff="关闭声音"
        android:textOn="打开声音" />

    <Switch
        android:id="@+id/swh_status"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textOff=""
        android:textOn=""
        android:thumb="@drawable/thumb_selctor"
        android:track="@drawable/track_selctor" />

</LinearLayout>
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements CompoundButton.OnCheckedChangeListener{

    private ToggleButton tbtn_open;
    private Switch swh_status;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tbtn_open = (ToggleButton) findViewById(R.id.tbtn_open);
        swh_status = (Switch) findViewById(R.id.swh_status);
        tbtn_open.setOnCheckedChangeListener(this);
        swh_status.setOnCheckedChangeListener(this);
    }

    @Override
    public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
        switch (compoundButton.getId()){
            case R.id.tbtn_open:
                if(compoundButton.isChecked()) Toast.makeText(this,"打开声音",Toast.LENGTH_SHORT).show();
                else Toast.makeText(this,"打开声音",Toast.LENGTH_SHORT).show();
                break;
            case R.id.swh_status:
                if(compoundButton.isChecked()) Toast.makeText(this,"开关:ON",Toast.LENGTH_SHORT).show();
                else Toast.makeText(this,"开关:OFF",Toast.LENGTH_SHORT).show();
                break;

        }
    }
}
```
