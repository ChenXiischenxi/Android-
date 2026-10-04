# 2.3.9 RatingBar(星级评分条)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-ratingbar.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {
    private RatingBar rb_normal;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        rb_normal = (RatingBar) findViewById(R.id.rb_normal);
        rb_normal.setOnRatingBarChangeListener(new RatingBar.OnRatingBarChangeListener() {
            @Override
            public void onRatingChanged(RatingBar ratingBar, float rating, boolean fromUser) {
                Toast.makeText(MainActivity.this, "rating:" + String.valueOf(rating),
                        Toast.LENGTH_LONG).show();
            }
        });
    }
}
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@android:id/background"
        android:drawable="@mipmap/ic_rating_off1" />
    <item android:id="@android:id/secondaryProgress"
        android:drawable="@mipmap/ic_rating_off1" />
    <item android:id="@android:id/progress"
        android:drawable="@mipmap/ic_rating_on1" />
</layer-list>
```

## 代码块 3

```xml
<style name="roomRatingBar" parent="@android:style/Widget.RatingBar">
        <item name="android:progressDrawable">@drawable/ratingbar_full</item>
        <item name="android:minHeight">24dip</item>
        <item name="android:maxHeight">24dip</item>
    </style>
```

## 代码块 4

```xml
<RatingBar
        android:id="@+id/rb_normal"
        style="@style/roomRatingBar"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />
```
