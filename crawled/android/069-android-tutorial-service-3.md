# 4.2.3 Service精通

> 来源: https://www.runoob.com/w3cnote/android-tutorial-service-3.html

## 代码块 1

```java
package com.jay.aidl;

interface IPerson {
    String queryPerson(int num);
}
```

## 代码块 2

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

## 代码块 3

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

## 代码块 4

```xml
<service android:name=".AIDLService">
            <intent-filter>
                <action android:name="android.intent.action.AIDLService" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
        </service>
```

## 代码块 5

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

## 代码块 6

```java
Person.aidl:     parcelable Person;
Salary.aidl:     parcelable Salary;
```

## 代码块 7

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

## 代码块 8

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

## 代码块 9

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

## 代码块 10

```xml
<service android:name=".AidlService">
    <intent-filter>
        <action android:name="android.intent.action.AIDLService" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</service>
```

## 代码块 11

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

## 代码块 12

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

## 代码块 13

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
