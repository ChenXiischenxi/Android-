# 3.1.1 基于监听的事件处理机制

> 来源: https://www.runoob.com/w3cnote/android-tutorial-listen-event-handle.html

## 代码块 1

```java
package com.jay.example.innerlisten;

import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Toast;
import android.app.Activity;


public class MainActivity extends Activity {
    private Button btnshow;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnshow = (Button) findViewById(R.id.btnshow);
        btnshow.setOnClickListener(new OnClickListener() {
            //重写点击事件的处理方法onClick()
            @Override
            public void onClick(View v) {
                //显示Toast信息
                Toast.makeText(getApplicationContext(), "你点击了按钮", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

## 代码块 2

```java
package com.jay.example.innerlisten;

import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Toast;
import android.app.Activity;


public class MainActivity extends Activity {
    private Button btnshow;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnshow = (Button) findViewById(R.id.btnshow);
        //直接new一个内部类对象作为参数
        btnshow.setOnClickListener(new BtnClickListener());
    }
    //定义一个内部类,实现View.OnClickListener接口,并重写onClick()方法
    class BtnClickListener implements View.OnClickListener
    {
        @Override
        public void onClick(View v) {
            Toast.makeText(getApplicationContext(), "按钮被点击了", Toast.LENGTH_SHORT).show();
        }
    }
}
```

## 代码块 3

```java
package com.jay.example.innerlisten;

import android.view.View;
import android.view.View.OnClickListener;
import android.widget.TextView;

public class MyClick implements OnClickListener {
    private TextView textshow;
    //把文本框作为参数传入
    public MyClick(TextView txt)
    {
        textshow = txt;
    }
    @Override
    public void onClick(View v) {
        //点击后设置文本框显示的文字
        textshow.setText("点击了按钮!");
    }
}
```

## 代码块 4

```java
package com.jay.example.innerlisten;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.app.Activity;


public class MainActivity extends Activity {
    private Button btnshow;
    private TextView txtshow;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnshow = (Button) findViewById(R.id.btnshow);
        txtshow = (TextView) findViewById(R.id.textshow);
        //直接new一个外部类，并把TextView作为参数传入
        btnshow.setOnClickListener(new MyClick(txtshow));
    }
}
```

## 代码块 5

```java
package com.jay.example.innerlisten;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Toast;
import android.app.Activity;

//让Activity方法实现OnClickListener接口
public class MainActivity extends Activity implements OnClickListener{
    private Button btnshow;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnshow = (Button) findViewById(R.id.btnshow);
        //直接写个this
        btnshow.setOnClickListener(this);
    }
    //重写接口中的抽象方法
    @Override
    public void onClick(View v) {
        Toast.makeText(getApplicationContext(), "点击了按钮", Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 6

```java
package com.jay.example.caller;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    //自定义一个方法,传入一个view组件作为参数
    public void myclick(View source)
    {
        Toast.makeText(getApplicationContext(), "按钮被点击了", Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 7

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical" >
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="按钮"
        android:onClick="myclick"/>
 </LinearLayout>
```
