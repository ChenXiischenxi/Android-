# 1.8 工程相关解析(各种文件，资源访问)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-project-src-analysis.html

## 代码块 1

```java
txtName.setText(getResources().getText(R.string.name));
```

## 代码块 2

```java
imgIcon.setBackgroundDrawableResource(R.drawable.icon);
```

## 代码块 3

```java
txtName.setTextColor(getResouces().getColor(R.color.red));
```

## 代码块 4

```java
setContentView(R.layout.main);
```

## 代码块 5

```java
txtName = (TextView)findViewById(R.id.txt_name);
```

## 代码块 6

```xml
<TextView android:text="@string/hello_world" android:layout_width="wrap_content" android:layout_height="wrap_content" android:background = "@drawable/img_back"/>
```

## 代码块 7

```java
package jay.com.example.firstapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```

## 代码块 8

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/hello_world" />

</RelativeLayout>
```

## 代码块 9

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="jay.com.example.firstapp" >

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme" >
        <activity
            android:name=".MainActivity"
            android:label="@string/app_name" >
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```
