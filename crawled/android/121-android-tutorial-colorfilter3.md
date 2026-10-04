# 8.3.11 Paint API之—— ColorFilter(颜色过滤器)(3-3)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-colorfilter3.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <ImageView
        android:id="@+id/img_show"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@mipmap/ic_launcher" />

    <TextView
        android:id="@+id/tv_color"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:textSize="12sp"
        android:text="颜色"
        android:textColor="#FFFFFFFF" />

    <TextView
        android:id="@+id/tv_mode"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textColor="#FFD9ECFF"
        android:text="模式"/>

</LinearLayout>
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/10/29 0029.
 */
public class Data {
    private int color;
    private PorterDuff.Mode mode;

    public Data() {
    }

    public Data(int color, PorterDuff.Mode mode) {
        this.color = color;
        this.mode = mode;
    }

    public int getColor() {
        return color;
    }

    public PorterDuff.Mode getMode() {
        return mode;
    }

    public void setColor(int color) {
        this.color = color;
    }

    public void setMode(PorterDuff.Mode mode) {
        this.mode = mode;
    }
}
```

## 代码块 3

```java
/**
 * 设置ColorFilter
 * */
public ViewHolder setColorFilter(int id,int color,PorterDuff.Mode mode){
    View view = getView(id);
    if (view instanceof ImageView) {
        ((ImageView) view).setColorFilter(color,mode);
    }
    return this;
}
```

## 代码块 4

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <GridView
        android:id="@+id/gd_show"
        android:background="#FF333333"
        android:numColumns="6"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>

</LinearLayout>
```

## 代码块 5

```java
public class MainActivity extends AppCompatActivity {

    private GridView gd_show;
    private ArrayList<Data> items = null;
    private MyAdapter<Data> myAdapter = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        gd_show = (GridView) findViewById(R.id.gd_show);

        //填充数据，遍历Mode模式：
        items = new ArrayList<Data>();
        for (PorterDuff.Mode mode : PorterDuff.Mode.class.getEnumConstants()) {
            items.add(new Data(0x77E50961, mode));
            items.add(new Data(0xFFE50961, mode));
            items.add(new Data(0x77FFFFFF, mode));
            items.add(new Data(0xFFFFFFFF, mode));
            items.add(new Data(0x77000000, mode));
            items.add(new Data(0xFF000000, mode));
        }
        myAdapter = new MyAdapter<Data>(items, R.layout.view_item) {
            @Override
            public void bindView(ViewHolder holder, Data obj) {
                holder.setColorFilter(R.id.img_show, obj.getColor(), obj.getMode());
                holder.setText(R.id.tv_color, String.format("%08X", obj.getColor()));
                holder.setText(R.id.tv_mode, obj.getMode().toString());
            }
        };
        gd_show.setAdapter(myAdapter);
    }
}
```
