# 2.3.8 SeekBar(拖动条)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-seekbar.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {

    private SeekBar sb_normal;
    private TextView txt_cur;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        bindViews();
    }

    private void bindViews() {
        sb_normal = (SeekBar) findViewById(R.id.sb_normal);
        txt_cur = (TextView) findViewById(R.id.txt_cur);
        sb_normal.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                txt_cur.setText("当前进度值:" + progress + "  / 100 ");
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
                Toast.makeText(mContext, "触碰SeekBar", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                Toast.makeText(mContext, "放开SeekBar", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true" android:drawable="@mipmap/seekbar_thumb_pressed"/>
    <item android:state_pressed="false" android:drawable="@mipmap/seekbar_thumb_normal"/>
</selector>
```

## 代码块 3

```xml
<?xml version="1.0" encoding="utf-8"?>
<layer-list
    xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@android:id/background">
        <shape>
            <solid android:color="#FFFFD042" />
        </shape>
    </item>
    <item android:id="@android:id/secondaryProgress">
        <clip>
            <shape>
                <solid android:color="#FFFFFFFF" />
            </shape>
        </clip>
    </item>
    <item android:id="@android:id/progress">
        <clip>
            <shape>
                <solid android:color="#FF96E85D" />
            </shape>
        </clip>
    </item>
</layer-list>
```

## 代码块 4

```xml
<SeekBar
        android:id="@+id/sb_normal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:maxHeight="5.0dp"
        android:minHeight="5.0dp"
        android:progressDrawable="@drawable/sb_bar"
        android:thumb="@drawable/sb_thumb"/>
```
