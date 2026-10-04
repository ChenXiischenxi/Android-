# 6.2 数据存储与访问之——SharedPreferences保存用户偏好参数

> 来源: https://www.runoob.com/w3cnote/android-tutorial-sharedpreferences.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MyActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="用户登陆" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:text="请输入用户名" />

    <EditText
        android:id="@+id/editname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="用户名" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="请输入密码" />

    <EditText
        android:id="@+id/editpasswd"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="密码"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/btnlogin"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="登录" />
</LinearLayout>
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/9/2 0002.
 */
public class SharedHelper {

    private Context mContext;

    public SharedHelper() {
    }

    public SharedHelper(Context mContext) {
        this.mContext = mContext;
    }


    //定义一个保存数据的方法
    public void save(String username, String passwd) {
        SharedPreferences sp = mContext.getSharedPreferences("mysp", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sp.edit();
        editor.putString("username", username);
        editor.putString("passwd", passwd);
        editor.commit();
        Toast.makeText(mContext, "信息已写入SharedPreference中", Toast.LENGTH_SHORT).show();
    }

    //定义一个读取SP文件的方法
    public Map<String, String> read() {
        Map<String, String> data = new HashMap<String, String>();
        SharedPreferences sp = mContext.getSharedPreferences("mysp", Context.MODE_PRIVATE);
        data.put("username", sp.getString("username", ""));
        data.put("passwd", sp.getString("passwd", ""));
        return data;
    }
}
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity {

    private EditText editname;
    private EditText editpasswd;
    private Button btnlogin;
    private String strname;
    private String strpasswd;
    private SharedHelper sh;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = getApplicationContext();
        sh = new SharedHelper(mContext);
        bindViews();
    }

    private void bindViews() {
        editname = (EditText)findViewById(R.id.editname);
        editpasswd = (EditText)findViewById(R.id.editpasswd);
        btnlogin = (Button)findViewById(R.id.btnlogin);
        btnlogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                strname = editname.getText().toString();
                strpasswd = editpasswd.getText().toString();
                sh.save(strname,strpasswd);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Map<String,String> data = sh.read();
        editname.setText(data.get("username"));
        editpasswd.setText(data.get("passwd"));
    }
}
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity {

    private Context othercontext;
    private SharedPreferences sp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btnshow = (Button) findViewById(R.id.btnshow);
        btnshow.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //获得第一个应用的包名,从而获得对应的Context,需要对异常进行捕获
                try {
                    othercontext = createPackageContext("com.jay.sharedpreferencedemo", Context.CONTEXT_IGNORE_SECURITY);
                } catch (PackageManager.NameNotFoundException e) {
                    e.printStackTrace();
                }
                //根据Context取得对应的SharedPreferences
                sp = othercontext.getSharedPreferences("mysp", Context.MODE_WORLD_READABLE);
                String name = sp.getString("username", "");
                String passwd = sp.getString("passwd", "");
                Toast.makeText(getApplicationContext(), "Demo1的SharedPreference存的\n用户名为：" + name + "\n密码为：" + passwd, Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

## 代码块 5

```java
/**
 * Created by Jay on 2015/9/2 0002.
 */
public class MD5 {
    public static String getMD5(String content) {
        try {
            MessageDigest digest = MessageDigest.getInstance("MD5");
            digest.update(content.getBytes());
            return getHashString(digest);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return null;
    }

    private static String getHashString(MessageDigest digest) {
        StringBuilder builder = new StringBuilder();
        for (byte b : digest.digest()) {
            builder.append(Integer.toHexString((b >> 4) & 0xf));
            builder.append(Integer.toHexString(b & 0xf));
        }
        return builder.toString();
    }
}
```

## 代码块 6

```java
Log.e("HeHe", MD5.getMD5("呵呵"));
```

## 代码块 7

```java
public static String getMD5x100(String content){
    String s1 = content;
    for(int i = 0;i < 100;i++){
        s1 = getMD5(s1);
    }
    return s1;
}
```

## 代码块 8

```java
package com.jay.sharedpreferencedemo3;

import android.content.Context;
import android.content.SharedPreferences;

import java.util.Map;

/**
 * Created by Jay on 2015/9/2 0002.
 */
public class SPUtils {
    /**
     * 保存在手机里的SP文件名
     */
    public static final String FILE_NAME = "my_sp";

    /**
     * 保存数据
     */
    public static void put(Context context, String key, Object obj) {
        SharedPreferences sp = context.getSharedPreferences(FILE_NAME, context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sp.edit();
        if (obj instanceof Boolean) {
            editor.putBoolean(key, (Boolean) obj);
        } else if (obj instanceof Float) {
            editor.putFloat(key, (Float) obj);
        } else if (obj instanceof Integer) {
            editor.putInt(key, (Integer) obj);
        } else if (obj instanceof Long) {
            editor.putLong(key, (Long) obj);
        } else {
            editor.putString(key, (String) obj);
        }
        editor.commit();
    }


    /**
     * 获取指定数据
     */
    public static Object get(Context context, String key, Object defaultObj) {
        SharedPreferences sp = context.getSharedPreferences(FILE_NAME, context.MODE_PRIVATE);
        if (defaultObj instanceof Boolean) {
            return sp.getBoolean(key, (Boolean) defaultObj);
        } else if (defaultObj instanceof Float) {
            return sp.getFloat(key, (Float) defaultObj);
        } else if (defaultObj instanceof Integer) {
            return sp.getInt(key, (Integer) defaultObj);
        } else if (defaultObj instanceof Long) {
            return sp.getLong(key, (Long) defaultObj);
        } else if (defaultObj instanceof String) {
            return sp.getString(key, (String) defaultObj);
        }
        return null;
    }

    /**
     * 删除指定数据
     */
    public static void remove(Context context, String key) {
        SharedPreferences sp = context.getSharedPreferences(FILE_NAME, context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sp.edit();
        editor.remove(key);
        editor.commit();
    }


    /**
     * 返回所有键值对
     */
    public static Map<String, ?> getAll(Context context) {
        SharedPreferences sp = context.getSharedPreferences(FILE_NAME, context.MODE_PRIVATE);
        Map<String, ?> map = sp.getAll();
        return map;
    }

    /**
     * 删除所有数据
     */
    public static void clear(Context context) {
        SharedPreferences sp = context.getSharedPreferences(FILE_NAME, context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sp.edit();
        editor.clear();
        editor.commit();
    }

    /**
     * 检查key对应的数据是否存在
     */
    public static boolean contains(Context context, String key) {
        SharedPreferences sp = context.getSharedPreferences(FILE_NAME, context.MODE_PRIVATE);
        return sp.contains(key);
    }

}
```
