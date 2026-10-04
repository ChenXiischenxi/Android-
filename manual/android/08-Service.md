# Service

> 本章归并自 3 页教程代码块，来源见各节。

## 4.2.1 Service初涉

> 来源: https://www.runoob.com/w3cnote/android-tutorial-service-1.html

```java
new Thread(myThread).start();
```

```java
new Thread(new Runnable(){
     public void run();
         }).start();
```

```java
public class TestService1 extends Service {
    private final String TAG = "TestService1";
    //必须要实现的方法
    @Override
    public IBinder onBind(Intent intent) {
        Log.i(TAG, "onBind方法被调用!");
        return null;
    }

    //Service被创建时调用
    @Override
    public void onCreate() {
        Log.i(TAG, "onCreate方法被调用!");
        super.onCreate();
    }

    //Service被启动时调用
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i(TAG, "onStartCommand方法被调用!");
        return super.onStartCommand(intent, flags, startId);
    }

    //Service被关闭之前回调
    @Override
    public void onDestroy() {
        Log.i(TAG, "onDestory方法被调用!");
        super.onDestroy();
    }
}
```

```xml
<!-- 配置Service组件,同时配置一个action -->
<service android:name=".TestService1">
            <intent-filter>
                <action android:name="com.jay.example.service.TEST_SERVICE1"/>
            </intent-filter>
</service>
```

```java
public class MainActivity extends Activity {

    private Button start;
    private Button stop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        start = (Button) findViewById(R.id.btnstart);
        stop = (Button) findViewById(R.id.btnstop);
        //创建启动Service的Intent,以及Intent属性
        final Intent intent = new Intent();
        intent.setAction("com.jay.example.service.TEST_SERVICE1");
        //为两个按钮设置点击事件,分别是启动与停止service
        start.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                startService(intent);
            }
        });

        stop.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                stopService(intent);

            }
        });
    }
}
```

```java
public class TestService2 extends Service {
    private final String TAG = "TestService2";
    private int count;
    private boolean quit;

    //定义onBinder方法所返回的对象
    private MyBinder binder = new MyBinder();
    public class MyBinder extends Binder
    {
        public int getCount()
        {
            return count;
        }
    }

    //必须实现的方法,绑定改Service时回调该方法
    @Override
    public IBinder onBind(Intent intent) {
        Log.i(TAG, "onBind方法被调用!");
        return binder;
    }

    //Service被创建时回调
    @Override
    public void onCreate() {
        super.onCreate();
        Log.i(TAG, "onCreate方法被调用!");
        //创建一个线程动态地修改count的值
        new Thread()
        {
            public void run()
            {
                while(!quit)
                {
                    try
                    {
                        Thread.sleep(1000);
                    }catch(InterruptedException e){e.printStackTrace();}
                    count++;
                }
            };
        }.start();

    }

    //Service断开连接时回调
    @Override
    public boolean onUnbind(Intent intent) {
        Log.i(TAG, "onUnbind方法被调用!");
        return true;
    }

    //Service被关闭前回调
    @Override
    public void onDestroy() {
        super.onDestroy();
        this.quit = true;
        Log.i(TAG, "onDestroyed方法被调用!");
    }

    @Override
    public void onRebind(Intent intent) {
        Log.i(TAG, "onRebind方法被调用!");
        super.onRebind(intent);
    }
}
```

```xml
<service android:name=".TestService2" android:exported="false">
        <intent-filter>
            <action android:name="com.jay.example.service.TEST_SERVICE2"/>
        </intent-filter>
</service>
```

```java
public class MainActivity extends Activity {

    private Button btnbind;
    private Button btncancel;
    private Button btnstatus;

    //保持所启动的Service的IBinder对象,同时定义一个ServiceConnection对象
    TestService2.MyBinder binder;
    private ServiceConnection conn = new ServiceConnection() {

        //Activity与Service断开连接时回调该方法
        @Override
        public void onServiceDisconnected(ComponentName name) {
            System.out.println("------Service DisConnected-------");
        }

        //Activity与Service连接成功时回调该方法
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            System.out.println("------Service Connected-------");
            binder = (TestService2.MyBinder) service;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnbind = (Button) findViewById(R.id.btnbind);
        btncancel = (Button) findViewById(R.id.btncancel);
        btnstatus  = (Button) findViewById(R.id.btnstatus);
        final Intent intent = new Intent();
        intent.setAction("com.jay.example.service.TEST_SERVICE2");
        btnbind.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                //绑定service
                bindService(intent, conn, Service.BIND_AUTO_CREATE);
            }
        });

        btncancel.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                //解除service绑定
                unbindService(conn);
            }
        });

        btnstatus.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "Service的count的值为:"
                        + binder.getCount(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

## 4.2.2 Service进阶

> 来源: https://www.runoob.com/w3cnote/android-tutorial-service-2.html

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

```xml
<service android:name=".TestService3" android:exported="false">
    <intent-filter >
        <action android:name="com.test.intentservice"/>
    </intent-filter>
</service>
```

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

```java
public class AlarmReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        Intent i = new Intent(context,LongRunningService.class);
        context.startService(i);
    }
}
```

## 4.2.3 Service精通

> 来源: https://www.runoob.com/w3cnote/android-tutorial-service-3.html

```java
package com.jay.aidl;

interface IPerson {
    String queryPerson(int num);
}
```

```java
/*
 * This file is auto-generated.  DO NOT MODIFY.
 * Original file: C:\\Code\\ASCode\\AIDLServer\\app\\src\\main\\aidl\\com\\jay\\aidl\\IPerson.aidl
 */
package com.jay.aidl;
public interface IPerson extends android.os.IInterface
{
/** Local-side IPC implementation stub class. */
public static abstract class Stub extends android.os.Binder implements com.jay.aidl.IPerson
{
private static final java.lang.String DESCRIPTOR = "com.jay.aidl.IPerson";
/** Construct the stub at attach it to the interface. */
public Stub()
{
this.attachInterface(this, DESCRIPTOR);
}
/**
 * Cast an IBinder object into an com.jay.aidl.IPerson interface,
 * generating a proxy if needed.
 */
public static com.jay.aidl.IPerson asInterface(android.os.IBinder obj)
{
if ((obj==null)) {
return null;
}
android.os.IInterface iin = obj.queryLocalInterface(DESCRIPTOR);
if (((iin!=null)&&(iin instanceof com.jay.aidl.IPerson))) {
return ((com.jay.aidl.IPerson)iin);
}
return new com.jay.aidl.IPerson.Stub.Proxy(obj);
}
@Override public android.os.IBinder asBinder()
{
return this;
}
@Override public boolean onTransact(int code, android.os.Parcel data, android.os.Parcel reply, int flags) throws android.os.RemoteException
{
switch (code)
{
case INTERFACE_TRANSACTION:
{
reply.writeString(DESCRIPTOR);
return true;
}
case TRANSACTION_queryPerson:
{
data.enforceInterface(DESCRIPTOR);
int _arg0;
_arg0 = data.readInt();
java.lang.String _result = this.queryPerson(_arg0);
reply.writeNoException();
reply.writeString(_result);
return true;
}
}
return super.onTransact(code, data, reply, flags);
}
private static class Proxy implements com.jay.aidl.IPerson
{
private android.os.IBinder mRemote;
Proxy(android.os.IBinder remote)
{
mRemote = remote;
}
@Override public android.os.IBinder asBinder()
{
return mRemote;
}
public java.lang.String getInterfaceDescriptor()
{
return DESCRIPTOR;
}
@Override public java.lang.String queryPerson(int num) throws android.os.RemoteException
{
android.os.Parcel _data = android.os.Parcel.obtain();
android.os.Parcel _reply = android.os.Parcel.obtain();
java.lang.String _result;
try {
_data.writeInterfaceToken(DESCRIPTOR);
_data.writeInt(num);
mRemote.transact(Stub.TRANSACTION_queryPerson, _data, _reply, 0);
_reply.readException();
_result = _reply.readString();
}
finally {
_reply.recycle();
_data.recycle();
}
return _result;
}
}
static final int TRANSACTION_queryPerson = (android.os.IBinder.FIRST_CALL_TRANSACTION + 0);
}
public java.lang.String queryPerson(int num) throws android.os.RemoteException;
}
```

```java
package com.jay.aidlserver;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;
import com.jay.aidl.IPerson.Stub;

/**
 * Created by Jay on 2015/8/18 0018.
 */
public class AIDLService extends Service {

    private IBinder binder = new PersonQueryBinder();
    private String[] names = {"B神","艹神","基神","J神","翔神"};

    private String query(int num)
    {
        if(num > 0 && num < 6){
            return names[num - 1];
        }
        return null;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    private final class PersonQueryBinder extends Stub{
        @Override
        public String queryPerson(int num) throws RemoteException {
            return query(num);
        }
    }
}
```

```xml
<service android:name=".AIDLService">
            <intent-filter>
                <action android:name="android.intent.action.AIDLService" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
        </service>
```

```java
package com.jay.aidlclient;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.jay.aidl.IPerson;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private EditText edit_num;
    private Button btn_query;
    private TextView txt_name;
    private IPerson iPerson;
    private PersonConnection conn = new PersonConnection();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
        //绑定远程Service
        Intent service = new Intent("android.intent.action.AIDLService");
        service.setPackage("com.jay.aidlserver");

        bindService(service, conn, BIND_AUTO_CREATE);
        btn_query.setOnClickListener(this);
    }

    private void bindViews() {
        edit_num = (EditText) findViewById(R.id.edit_num);
        btn_query = (Button) findViewById(R.id.btn_query);
        txt_name = (TextView) findViewById(R.id.txt_name);
    }

    @Override
    public void onClick(View v) {
        String number = edit_num.getText().toString();
        int num = Integer.valueOf(number);
        try {
            txt_name.setText(iPerson.queryPerson(num));
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        edit_num.setText("");
    }

    private final class PersonConnection implements ServiceConnection {
        public void onServiceConnected(ComponentName name, IBinder service) {
            iPerson = IPerson.Stub.asInterface(service);
        }
        public void onServiceDisconnected(ComponentName name) {
            iPerson = null;
        }
    }
}
```

```java
Person.aidl:     parcelable Person;
Salary.aidl:     parcelable Salary;
```

```java
package com.jay.example.aidl;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by Jay on 2015/8/18 0018.
 */
public class Person implements Parcelable{

    private Integer id;
    private String name;

    public Person() {}

    public Person(Integer id, String name) {
        this.id = id;
        this.name = name;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }


    //实现Parcelable必须实现的方法,不知道拿来干嘛的,直接返回0就行了
    @Override
    public int describeContents() {
        return 0;
    }


    //写入数据到Parcel中的方法
    @Override
    public void writeToParcel(Parcel dest, int flags) {
        //把对象所包含的数据写入到parcel中
        dest.writeInt(id);
        dest.writeString(name);
    }

    //必须提供一个名为CREATOR的static final属性 该属性需要实现
    //android.os.Parcelable.Creator<T>接口
    public static final Parcelable.Creator<Person> CREATOR = new Parcelable.Creator<Person>() {
        //从Parcel中读取数据,返回Person对象
        @Override
        public Person createFromParcel(Parcel source) {
            return new Person(source.readInt(),source.readString());
        }
        @Override
        public Person[] newArray(int size) {
            return new Person[size];
        }
    };

    //因为我们集合取出元素的时候是根据Person对象来取得,所以比较麻烦,
    //需要我们重写hashCode()和equals()方法
    @Override
    public int hashCode()
    {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((name == null) ? 0 : name.hashCode());
        return result;
    }
    @Override
    public boolean equals(Object obj)
    {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Person other = (Person) obj;
        if (name == null)
        {
            if (other.name != null)
                return false;
        }
        else if (!name.equals(other.name))
            return false;
        return true;
    }
}
<pre><p><strong>Salary.java</strong>~照葫芦画瓢</p>

<pre>
package com.jay.example.aidl;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by Jay on 2015/8/18 0018.
 */
public class Salary implements Parcelable {

    private String type;
    private Integer salary;

    public Salary() {
    }

    public Salary(String type, Integer salary) {
        this.type = type;
        this.salary = salary;
    }

    public String getType() {
        return type;
    }

    public Integer getSalary() {
        return salary;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setSalary(Integer salary) {
        this.salary = salary;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(type);
        dest.writeInt(salary);
    }

    public static final Parcelable.Creator<Salary> CREATOR = new Parcelable.Creator<Salary>() {
        //从Parcel中读取数据,返回Person对象
        @Override
        public Salary createFromParcel(Parcel source) {
            return new Salary(source.readString(), source.readInt());
        }

        @Override
        public Salary[] newArray(int size) {
            return new Salary[size];
        }
    };

    public String toString() {
        return "工作:" + type + "    薪水: " + salary;
    }
}
```

```java
package com.jay.example.aidl;

import com.jay.example.aidl.Salary;
import com.jay.example.aidl.Person;
interface ISalary
{
    //定义一个Person对象作为传入参数
    //接口中定义方法时,需要制定新参的传递模式,这里是传入,所以前面有一个in
    Salary getMsg(in Person owner);
}
```

```java
package com.jay.example.aidl_complexservice;

import java.util.HashMap;
import java.util.Map;
import com.jay.example.aidl.ISalary.Stub;
import com.jay.example.aidl.Person;
import com.jay.example.aidl.Salary;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;

public class AidlService extends Service {

    private SalaryBinder salaryBinder;
    private static Map<Person,Salary> ss = new HashMap<Person, Salary>();
    //初始化Map集合,这里在静态代码块中进行初始化,当然你可也以在构造方法中完成初始化
    static
    {
        ss.put(new Person(1, "Jay"), new Salary("码农", 2000));
        ss.put(new Person(2, "GEM"), new Salary("歌手", 20000));
        ss.put(new Person(3, "XM"), new Salary("学生", 20));
        ss.put(new Person(4, "MrWang"), new Salary("老师", 2000));
    }


    @Override
    public void onCreate() {
        super.onCreate();
        salaryBinder = new SalaryBinder();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return salaryBinder;
    }


    //同样是继承Stub,即同时实现ISalary接口和IBinder接口
    public class SalaryBinder extends Stub
    {
        @Override
        public Salary getMsg(Person owner) throws RemoteException {
            return ss.get(owner);
        }
    }

    @Override
    public void onDestroy() {
        System.out.println("服务结束！");
        super.onDestroy();
    }
}
```

```xml
<service android:name=".AidlService">
    <intent-filter>
        <action android:name="android.intent.action.AIDLService" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</service>
```

```java
package com.jay.example.aidl_complexclient;

import com.jay.example.aidl.ISalary;
import com.jay.example.aidl.Person;
import com.jay.example.aidl.Salary;

import android.app.Activity;
import android.app.Service;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;


public class MainActivity extends Activity {

    private ISalary salaryService;
    private Button btnquery;
    private EditText editname;
    private TextView textshow;
    private ServiceConnection conn = new ServiceConnection() {

        @Override
        public void onServiceDisconnected(ComponentName name) {
            salaryService = null;
        }

        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            //返回的是代理对象,要调用这个方法哦!
            salaryService = ISalary.Stub.asInterface(service);
        }
    };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnquery = (Button) findViewById(R.id.btnquery);
        editname = (EditText) findViewById(R.id.editname);
        textshow = (TextView) findViewById(R.id.textshow);

        Intent it = new Intent();
        it.setAction("com.jay.aidl.AIDL_SERVICE");
        bindService(it, conn, Service.BIND_AUTO_CREATE);

        btnquery.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                try
                {
                    String name = editname.getText().toString();
                    Salary salary = salaryService.getMsg(new Person(1,name));
                    textshow.setText(name + salary.toString());
                }catch(RemoteException e){e.printStackTrace();}
            }
        });

    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        this.unbindService(conn);
    }

}
```

```java
/**
 * Created by Jay on 2015/8/18 0018.
 */
public class IPCService extends Service{

    private static final String DESCRIPTOR = "IPCService";
    private final String[] names = {"B神","艹神","基神","J神","翔神"};
    private MyBinder mBinder = new MyBinder();


    private class MyBinder extends Binder {
        @Override
        protected boolean onTransact(int code, Parcel data, Parcel reply, int flags) throws RemoteException {
            switch (code){
                case 0x001: {
                    data.enforceInterface(DESCRIPTOR);
                    int num = data.readInt();
                    reply.writeNoException();
                    reply.writeString(names[num]);
                    return true;
                }
            }
            return super.onTransact(code, data, reply, flags);
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }
}
```

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private EditText edit_num;
    private Button btn_query;
    private TextView txt_result;
    private IBinder mIBinder;
    private ServiceConnection PersonConnection  = new ServiceConnection()
    {
        @Override
        public void onServiceDisconnected(ComponentName name)
        {
            mIBinder = null;
        }

        @Override
        public void onServiceConnected(ComponentName name, IBinder service)
        {
            mIBinder = service;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();

        //绑定远程Service
        Intent service = new Intent("android.intent.action.IPCService");
        service.setPackage("com.jay.ipcserver");
        bindService(service, PersonConnection, BIND_AUTO_CREATE);
        btn_query.setOnClickListener(this);
    }

    private void bindViews() {
        edit_num = (EditText) findViewById(R.id.edit_num);
        btn_query = (Button) findViewById(R.id.btn_query);
        txt_result = (TextView) findViewById(R.id.txt_result);
    }

    @Override
    public void onClick(View v) {
        int num = Integer.parseInt(edit_num.getText().toString());
        if (mIBinder == null)
        {
            Toast.makeText(this, "未连接服务端或服务端被异常杀死", Toast.LENGTH_SHORT).show();
        } else {
            android.os.Parcel _data = android.os.Parcel.obtain();
            android.os.Parcel _reply = android.os.Parcel.obtain();
            String _result = null;
            try{
                _data.writeInterfaceToken("IPCService");
                _data.writeInt(num);
                mIBinder.transact(0x001, _data, _reply, 0);
                _reply.readException();
                _result = _reply.readString();
                txt_result.setText(_result);
                edit_num.setText("");
            }catch (RemoteException e)
            {
                e.printStackTrace();
            } finally
            {
                _reply.recycle();
                _data.recycle();
            }
        }
    }
}
```
