# 4.3.1 BroadcastReceiver牛刀小试

> 来源: https://www.runoob.com/w3cnote/android-tutorial-broadcastreceiver.html

## 代码块 1

```java
public class MyBRReceiver extends BroadcastReceiver{
    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context,"网络状态发生改变~",Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity {

    MyBRReceiver myReceiver;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //核心部分代码：
        myReceiver = new MyBRReceiver();
        IntentFilter itFilter = new IntentFilter();
        itFilter.addAction("android.net.conn.CONNECTIVITY_CHANGE");
        registerReceiver(myReceiver, itFilter);
    }

    //别忘了将广播取消掉哦~
    @Override
    protected void onDestroy() {
        super.onDestroy();
        unregisterReceiver(myReceiver);
    }
}
```

## 代码块 3

```java
public class BootCompleteReceiver extends BroadcastReceiver {
    private final String ACTION_BOOT = "android.intent.action.BOOT_COMPLETED";
    @Override
    public void onReceive(Context context, Intent intent) {
    if (ACTION_BOOT.equals(intent.getAction()))
        Toast.makeText(context, "开机完毕~", Toast.LENGTH_LONG).show();
    }
}
```

## 代码块 4

```xml
<receiver android:name=".BootCompleteReceiver">
    <intent-filter>
        <action android:name = "android.intent.cation.BOOT_COMPLETED">
    </intent-filter>
</receiver>

<!-- 权限 -->
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
```

## 代码块 5

```java
public class MyBroadcastReceiver extends BroadcastReceiver {
    private final String ACTION_BOOT = "com.example.broadcasttest.MY_BROADCAST";
    @Override
    public void onReceive(Context context, Intent intent) {
        if(ACTION_BOOT.equals(intent.getAction()))
        Toast.makeText(context, "收到告白啦~",Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 6

```xml
<receiver android:name=".MyBroadcastReceiver">
    <intent-filter>
        <action android:name="com.example.broadcasttest.MY_BROADCAST"/>
    </intent-filter>
</receiver>
```

## 代码块 7

```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn_send = (Button) findViewById(R.id.btn_send);
        btn_send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sendBroadcast(new Intent("com.example.broadcasttest.MY_BROADCAST"));
            }
        });
    }
}
```
