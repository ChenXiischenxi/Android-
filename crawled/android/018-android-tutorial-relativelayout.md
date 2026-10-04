# 2.2.2 RelativeLayout(相对布局)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-relativelayout.html

## 代码块 1

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/RelativeLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent" >

    <!-- 这个是在容器中央的 -->

    <ImageView
        android:id="@+id/img1"
        android:layout_width="80dp"
        android:layout_height="80dp"
        android:layout_centerInParent="true"
        android:src="@drawable/pic1"/>

    <!-- 在中间图片的左边 -->
    <ImageView
        android:id="@+id/img2"
        android:layout_width="80dp"
        android:layout_height="80dp"
        android:layout_toLeftOf="@id/img1"
        android:layout_centerVertical="true"
        android:src="@drawable/pic2"/>

    <!-- 在中间图片的右边 -->
    <ImageView
        android:id="@+id/img3"
        android:layout_width="80dp"
        android:layout_height="80dp"
        android:layout_toRightOf="@id/img1"
        android:layout_centerVertical="true"
        android:src="@drawable/pic3"/>

    <!-- 在中间图片的上面-->
    <ImageView
        android:id="@+id/img4"
        android:layout_width="80dp"
        android:layout_height="80dp"
        android:layout_above="@id/img1"
        android:layout_centerHorizontal="true"
        android:src="@drawable/pic4"/>

    <!-- 在中间图片的下面 -->
    <ImageView
        android:id="@+id/img5"
        android:layout_width="80dp"
        android:layout_height="80dp"
        android:layout_below="@id/img1"
        android:layout_centerHorizontal="true"
        android:src="@drawable/pic5"/>

</RelativeLayout>
```

## 代码块 2

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    tools:context=".MainActivity" >

    <Button
        android:id="@+id/btn1"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text="Button"/>
    <Button
        android:paddingLeft="100dp"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text="Button"
        android:layout_toRightOf="@id/btn1"/>

    <Button
        android:id="@+id/btn2"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text="Button"
        android:layout_alignParentBottom="true"/>
    <Button
        android:layout_marginLeft="100dp"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text="Button"
        android:layout_toRightOf="@id/btn2"
        android:layout_alignParentBottom="true"/>

</RelativeLayout>
```

## 代码块 3

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="com.jay.example.relativelayoutdemo.MainActivity"
    android:background="#00CCCCFF">

    <ImageView
        android:id="@+id/imgBack"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:layout_centerInParent="true"
        android:background="@drawable/myicon" />

    <ImageView
        android:id="@+id/imgCancle"
        android:layout_width="28dp"
        android:layout_height="28dp"
        android:layout_alignRight="@id/imgBack"
        android:layout_alignTop="@id/imgBack"
        android:background="@drawable/cancel"
        android:layout_marginTop="-15dp"
        android:layout_marginRight="-10dp" />

</RelativeLayout>
```
