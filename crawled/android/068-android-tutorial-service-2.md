# 4.2.2 Service进阶

> 来源: https://www.runoob.com/w3cnote/android-tutorial-service-2.html

## 代码块 1

```java
public class TestService3 extends IntentService {
    private final String TAG = "hehe";
    //必须实现父类的构造方法
    public TestService3()
    {
        super("TestService3");
    }

    //必须重写的核心方法
    @Override
    protected void onHandleIntent(Intent intent) {
        //Intent是从Activity发过来的，携带识别参数，根据参数不同执行不同的任务
        String action = intent.getExtras().getString("param");
        if(action.equals("s1"))Log.i(TAG,"启动service1");
        else if(action.equals("s2"))Log.i(TAG,"启动service2");
        else if(action.equals("s3"))Log.i(TAG,"启动service3");

        //让服务休眠2秒
        try{
            Thread.sleep(2000);
        }catch(InterruptedException e){e.printStackTrace();}
    }

    //重写其他方法,用于查看方法的调用顺序
    @Override
    public IBinder onBind(Intent intent) {
        Log.i(TAG,"onBind");
        return super.onBind(intent);
    }

    @Override
    public void onCreate() {
        Log.i(TAG,"onCreate");
        super.onCreate();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i(TAG,"onStartCommand");
        return super.onStartCommand(intent, flags, startId);
    }


    @Override
    public void setIntentRedelivery(boolean enabled) {
        super.setIntentRedelivery(enabled);
        Log.i(TAG,"setIntentRedelivery");
    }

    @Override
    public void onDestroy() {
        Log.i(TAG,"onDestroy");
        super.onDestroy();
    }

}
```

## 代码块 2

```xml
<service android:name=".TestService3" android:exported="false">
    <intent-filter >
        <action android:name="com.test.intentservice"/>
    </intent-filter>
</service>
```

## 代码块 3

```java
public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Intent it1 = new Intent("com.test.intentservice");
        Bundle b1 = new Bundle();
        b1.putString("param", "s1");
        it1.putExtras(b1);

        Intent it2 = new Intent("com.test.intentservice");
        Bundle b2 = new Bundle();
        b2.putString("param", "s2");
        it2.putExtras(b2);

        Intent it3 = new Intent("com.test.intentservice");
        Bundle b3 = new Bundle();
        b3.putString("param", "s3");
        it3.putExtras(b3);

        //接着启动多次IntentService,每次启动,都会新建一个工作线程
        //但始终只有一个IntentService实例
        startService(it1);
        startService(it2);
        startService(it3);
    }
}
```

## 代码块 4

```java
public void onCreate()
{
    super.onCreate();
    Notification.Builder localBuilder = new Notification.Builder(this);
    localBuilder.setContentIntent(PendingIntent.getActivity(this, 0, new Intent(this, MainActivity.class), 0));
    localBuilder.setAutoCancel(false);
    localBuilder.setSmallIcon(R.mipmap.ic_cow_icon);
    localBuilder.setTicker("Foreground Service Start");
    localBuilder.setContentTitle("Socket服务端");
    localBuilder.setContentText("正在运行...");
    startForeground(1, localBuilder.getNotification());
}
```

## 代码块 5

```java
public class LongRunningService extends Service {
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        //这里开辟一条线程,用来执行具体的逻辑操作:
        new Thread(new Runnable() {
            @Override
            public void run() {
                Log.d("BackService", new Date().toString());
            }
        }).start();
        AlarmManager manager = (AlarmManager) getSystemService(ALARM_SERVICE);
        //这里是定时的,这里设置的是每隔两秒打印一次时间=-=,自己改
        int anHour = 2 * 1000;
        long triggerAtTime = SystemClock.elapsedRealtime() + anHour;
        Intent i = new Intent(this,AlarmReceiver.class);
        PendingIntent pi = PendingIntent.getBroadcast(this, 0, i, 0);
        manager.set(AlarmManager.ELAPSED_REALTIME_WAKEUP, triggerAtTime, pi);
        return super.onStartCommand(intent, flags, startId);
    }
}
```

## 代码块 6

```java
public class AlarmReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        Intent i = new Intent(context,LongRunningService.class);
        context.startService(i);
    }
}
```
