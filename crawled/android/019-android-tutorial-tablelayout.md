# 2.2.3 TableLayout(表格布局)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-tablelayout.html

## 代码块 1

```xml
<TableLayout
    android:id="@+id/TableLayout2"
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:collapseColumns="0,2" >

    <TableRow>

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="one" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="two" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="three" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="four" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="five" />
    </TableRow>
</TableLayout>
```

## 代码块 2

```xml
<TableLayout
    android:id="@+id/TableLayout2"
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:stretchColumns="1" >

    <TableRow>

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="one" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="two" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="three" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="four" />
    </TableRow>
</TableLayout>
```

## 代码块 3

```xml
<TableLayout
    android:id="@+id/TableLayout2"
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:shrinkColumns="1" >

    <TableRow>

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="one" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="two" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="three" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="four" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="five" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="文本XX" />
    </TableRow>
</TableLayout>
```

## 代码块 4

```xml
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/TableLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:stretchColumns="0,3"
    android:gravity="center_vertical"
    android:background="#66FF66"
    >

    <TableRow>
        <TextView />
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="用户名:"/>
        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:minWidth="150dp"/>
        <TextView />
    </TableRow>

    <TableRow>
        <TextView />
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="密  码:"
        />
        <EditText
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:minWidth="150dp"
        />
        <TextView />
    </TableRow>

    <TableRow>
        <TextView />
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="登陆"/>
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="退出"/>
        <TextView />
    </TableRow>

</TableLayout>
```
