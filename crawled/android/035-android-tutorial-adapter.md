# 2.4.4 Adapter基础讲解

> 来源: https://www.runoob.com/w3cnote/android-tutorial-adapter.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //要显示的数据
        String[] strs = {"基神","B神","翔神","曹神","J神"};
        //创建ArrayAdapter
        ArrayAdapter<String> adapter = new ArrayAdapter<String>
                (this,android.R.layout.simple_expandable_list_item_1,strs);
        //获取ListView对象，通过调用setAdapter方法为ListView设置Adapter设置适配器
        ListView list_test = (ListView) findViewById(R.id.list_test);
        list_test.setAdapter(adapter);
    }
}
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="myarray">
    <item>语文</item>
    <item>数学</item>
    <item>英语</item>
    </string-array>
</resources>
```

## 代码块 3

```xml
<ListView
        android:id="@id/list_test"
        android:layout_height="match_parent"
        android:layout_width="match_parent"
        android:entries="@array/myarray"/>
```

## 代码块 4

```java
ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
        R.array.myarray,android.R.layout.simple_list_item_multiple_choice );
```

## 代码块 5

```java
List<String> data = new ArrayList<String>();
data.add("基神");
data.add("B神")；
ArrayAdapter<String> adapter = new ArrayAdapter<String>
                (this,android.R.layout.simple_expandable_list_item_1,data);
```

## 代码块 6

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal">

    <!-- 定义一个用于显示头像的ImageView -->
    <ImageView
        android:id="@+id/imgtou"
        android:layout_width="64dp"
        android:layout_height="64dp"
        android:baselineAlignBottom="true"
        android:paddingLeft="8dp" />

    <!-- 定义一个竖直方向的LinearLayout,把QQ呢称与说说的文本框设置出来 -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/name"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:paddingLeft="8dp"
            android:textColor="#1D1D1C"
            android:textSize="20sp" />

        <TextView
            android:id="@+id/says"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:paddingLeft="8px"
            android:textColor="#B4B4B9"
            android:textSize="14sp" />

    </LinearLayout>

</LinearLayout>
```

## 代码块 7

```java
public class MainActivity extends AppCompatActivity {

    private String[] names = new String[]{"B神", "基神", "曹神"};
    private String[] says = new String[]{"无形被黑，最为致命", "大神好厉害~", "我将带头日狗~"};
    private int[] imgIds = new int[]{R.mipmap.head_icon1, R.mipmap.head_icon2, R.mipmap.head_icon3};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        List<Map<String, Object>> listitem = new ArrayList<Map<String, Object>>();
        for (int i = 0; i < names.length; i++) {
            Map<String, Object> showitem = new HashMap<String, Object>();
            showitem.put("touxiang", imgIds[i]);
            showitem.put("name", names[i]);
            showitem.put("says", says[i]);
            listitem.add(showitem);
        }

        //创建一个simpleAdapter
        SimpleAdapter myAdapter = new SimpleAdapter(getApplicationContext(), listitem, R.layout.list_item, new String[]{"touxiang", "name", "says"}, new int[]{R.id.imgtou, R.id.name, R.id.says});
        ListView listView = (ListView) findViewById(R.id.list_test);
        listView.setAdapter(myAdapter);
    }
}
```

## 代码块 8

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal">


    <TextView
        android:id="@+id/list_name"
        android:layout_width="0dp"
        android:layout_height="64dp"
        android:layout_weight="1"
        android:gravity="center"
        android:text="小猪"
        android:textColor="#0000FF"
        android:textSize="18sp" />

    <TextView
        android:id="@+id/list_phone"
        android:layout_width="0dp"
        android:layout_height="64dp"
        android:layout_weight="1"
        android:gravity="center"
        android:text="13798989898"
        android:textColor="#EA5C4D"
        android:textSize="18sp" />


</LinearLayout>
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ListView list_test = (ListView) findViewById(R.id.list_test);
        //读取联系人
        Cursor cursor = getContentResolver()
                .query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null, null, null, null);
        SimpleCursorAdapter spcAdapter = new SimpleCursorAdapter(this,R.layout.list_item,cursor,
                new String[]{ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME,ContactsContract.CommonDataKinds.Phone.NUMBER},
                new int[]{R.id.list_name,R.id.list_phone});
        list_test.setAdapter(spcAdapter);
    }
}
```

## 代码块 10

```xml
<uses-permission android:name="android.permission.READ_CONTACTS"/>
```
