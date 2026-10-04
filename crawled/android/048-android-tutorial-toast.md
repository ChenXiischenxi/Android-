# 2.5.7 Toast(吐司)的基本使用

> 来源: https://www.runoob.com/w3cnote/android-tutorial-toast.html

## 代码块 1

```java
void midToast(String str, int showTime)
{
    Toast toast = Toast.makeText(global_context, str, showTime);
    toast.setGravity(Gravity.CENTER_VERTICAL|Gravity.CENTER_HORIZONTAL , 0, 0);  //设置显示位置
    TextView v = (TextView) toast.getView().findViewById(android.R.id.message);
    v.setTextColor(Color.YELLOW);     //设置字体颜色
    toast.show();
}
```

## 代码块 2

```java
private void midToast(String str, int showTime)
{
    Toast toast = Toast.makeText(mContext, str, showTime);
    toast.setGravity(Gravity.CENTER_HORIZONTAL|Gravity.BOTTOM , 0, 0);  //设置显示位置
    LinearLayout layout = (LinearLayout) toast.getView();
    layout.setBackgroundColor(Color.BLUE);
    ImageView image = new ImageView(this);
    image.setImageResource(R.mipmap.ic_icon_qitao);
    layout.addView(image, 0);
    TextView v = (TextView) toast.getView().findViewById(android.R.id.message);
    v.setTextColor(Color.YELLOW);     //设置字体颜色
    toast.show();
}
```

## 代码块 3

```java
private void midToast(String str, int showTime)
{
    LayoutInflater inflater = getLayoutInflater();
    View view = inflater.inflate(R.layout.view_toast_custom,
            (ViewGroup) findViewById(R.id.lly_toast));
    ImageView img_logo = (ImageView) view.findViewById(R.id.img_logo);
    TextView tv_msg = (TextView) view.findViewById(R.id.tv_msg);
    tv_msg.setText(str);
    Toast toast = new Toast(mContext);
    toast.setGravity(Gravity.CENTER, 0, 0);
    toast.setDuration(Toast.LENGTH_LONG);
    toast.setView(view);
    toast.show();
}
```

## 代码块 4

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- 设置透明背景色 -->
    <solid android:color="#BADB66" />
    <!-- 设置一个黑色边框 -->
    <stroke
        android:width="1px"
        android:color="#FFFFFF" />
    <!-- 设置四个圆角的半径 -->
    <corners
        android:bottomLeftRadius="50px"
        android:bottomRightRadius="50px"
        android:topLeftRadius="50px"
        android:topRightRadius="50px" />
    <!-- 设置一下边距,让空间大一点 -->
    <padding
        android:bottom="5dp"
        android:left="5dp"
        android:right="5dp"
        android:top="5dp" />
</shape>
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/lly_toast"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/bg_toast"
    android:orientation="horizontal">

    <ImageView
        android:id="@+id/img_logo"
        android:layout_width="24dp"
        android:layout_height="24dp"
        android:layout_marginLeft="10dp"
        android:src="@mipmap/iv_lol_icon1" />

    <TextView
        android:id="@+id/tv_msg"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="10dp"
        android:textSize="20sp" />

</LinearLayout>
```
