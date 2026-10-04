# 2.2.1 LinearLayout(线性布局)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-linearlayout.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="fill_parent"
        android:background="#ADFF2F"
        android:layout_weight="1"/>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="fill_parent"
        android:background="#DA70D6"
        android:layout_weight="2"/>

</LinearLayout>
```

## 代码块 2

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal" >

    <TextView
        android:layout_weight="1"
        android:layout_width="wrap_content"
        android:layout_height="fill_parent"
        android:text="one"
        android:background="#98FB98"
     />
     <TextView
        android:layout_weight="2"
        android:layout_width="wrap_content"
        android:layout_height="fill_parent"
        android:text="two"
        android:background="#FFFF00"
     />
     <TextView
        android:layout_weight="3"
        android:layout_width="wrap_content"
        android:layout_height="fill_parent"
        android:text="three"
        android:background="#FF00FF"
     />

</LinearLayout>
```

## 代码块 3

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent" >

    <TextView
        android:layout_weight="1"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:text="one"
        android:background="#98FB98"
     />
     <TextView
        android:layout_weight="2"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:text="two"
        android:background="#FFFF00"
     />
     <TextView
        android:layout_weight="3"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:text="three"
        android:background="#FF00FF"
     />

</LinearLayout>
```

## 代码块 4

```java
setLayoutParams(new LayoutParams(LayoutParams.FILL_PARENT,
        LayoutParams.WRAP_CONTENT, 1));
```

## 代码块 5

```xml
<View
    android:layout_width="match_parent"
    android:layout_height="1px"
    android:background="#000000" />
```

## 代码块 6

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:divider="@drawable/ktv_line_div"
    android:orientation="vertical"
    android:showDividers="middle"
    android:dividerPadding="10dp"
    tools:context="com.jay.example.linearlayoutdemo.MainActivity" >

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="按钮1" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="按钮2" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="按钮3" />

</LinearLayout>
```

## 代码块 7

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical"
    tools:context=".MainActivity" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="请输入要保存的电话号码"/>
    <EditText
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"/>
    <LinearLayout
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="right">
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="保存"/>
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="清空"/>
    </LinearLayout>
</LinearLayout>
```

## 代码块 8

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal"
    tools:context="com.jay.example.getscreendemo.MainActivity" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="200dp"
        android:layout_gravity="left"
        android:background="#FF7878"
        android:gravity="center"
        android:text="O(∩_∩)O哈哈~" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="200dp"
        android:layout_gravity="right"
        android:background="#FF7428"
        android:gravity="center"
        android:text="(*^__^*) 嘻嘻……" />

</LinearLayout>
```

## 代码块 9

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal"
    android:gravity="left"
    tools:context="com.jay.example.getscreendemo.MainActivity" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="200dp"
        android:background="#FF7878"
        android:gravity="center"
        android:text="O(∩_∩)O哈哈~" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="200dp"
        android:layout_gravity="right"
        android:background="#FF7428"
        android:gravity="center"
        android:text="(*^__^*) 嘻嘻……" />

</LinearLayout>
```
