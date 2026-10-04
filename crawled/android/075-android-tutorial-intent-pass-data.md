# 4.5.2 Intent之复杂数据的传递

> 来源: https://www.runoob.com/w3cnote/android-tutorial-intent-pass-data.html

## 代码块 1

```java
bd.putStringArray("StringArray", new String[]{"呵呵","哈哈"});
//可把StringArray换成其他数据类型,比如int,float等等...
```

## 代码块 2

```java
String[] str = bd.getStringArray("StringArray")
```

## 代码块 3

```java
intent.putStringArrayListExtra(name, value)
intent.putIntegerArrayListExtra(name, value)
```

## 代码块 4

```java
intent.getStringArrayListExtra(name)
intent.getIntegerArrayListExtra(name)
```

## 代码块 5

```java
putExtras(key, (Serializable)list)
```

## 代码块 6

```java
(List<Object>) getIntent().getSerializable(key)
```

## 代码块 7

```java
//传递复杂些的参数
Map<String, Object> map1 = new HashMap<String, Object>();
map1.put("key1", "value1");
map1.put("key2", "value2");
List<Map<String, Object>> list = new ArrayList<Map<String, Object>>();
list.add(map1);

Intent intent = new Intent();
intent.setClass(MainActivity.this,ComplexActivity.class);
Bundle bundle = new Bundle();

//须定义一个list用于在budnle中传递需要传递的ArrayList<Object>,这个是必须要的
ArrayList bundlelist = new ArrayList();
bundlelist.add(list);
bundle.putParcelableArrayList("list",bundlelist);
intent.putExtras(bundle);
startActivity(intent);
```

## 代码块 8

```java
public class Book{
    private int id;
    private String title;
    //...
}

public class Author{
    private int id;
    private String name;
    //...
}
```

## 代码块 9

```java
Book book=new Book();
book.setTitle("Java编程思想");
Author author=new Author();
author.setId(1);
author.setName("Bruce Eckel");
book.setAuthor(author);
Intent intent=new Intent(this,SecondActivity.class);
intent.putExtra("book",new Gson().toJson(book));
startActivity(intent);
```

## 代码块 10

```java
String bookJson=getIntent().getStringExtra("book");
Book book=new Gson().fromJson(bookJson,Book.class);
Log.d(TAG,"book title->"+book.getTitle());
Log.d(TAG,"book author name->"+book.getAuthor().getName());
```

## 代码块 11

```java
//Internal Description Interface,You do not need to manage
@Override
public int describeContents() {
     return 0;
}


@Override
public void writeToParcel(Parcel parcel, int flags){
    parcel.writeString(bookName);
    parcel.writeString(author);
    parcel.writeInt(publishTime);
}


public static final Parcelable.Creator<Book> CREATOR = new Creator<Book>() {
    @Override
    public Book[] newArray(int size) {
        return new Book[size];
    }

    @Override
    public Book createFromParcel(Parcel source) {
        Book mBook = new Book();
        mBook.bookName = source.readString();
        mBook.author = source.readString();
        mBook.publishTime = source.readInt();
        return mBook;
    }
};
```

## 代码块 12

```java
Bitmap bitmap = null;
Intent intent = new Intent();
Bundle bundle = new Bundle();
bundle.putParcelable("bitmap", bitmap);
intent.putExtra("bundle", bundle);
```

## 代码块 13

```java
class MyApp extends Application {
    private String myState;
    public String getState(){
        return myState;
    }
    public void setState(String s){
        myState = s;
    }
}
```

## 代码块 14

```xml
<application android:name=".MyApp" android:icon="@drawable/icon"
  android:label="@string/app_name">
```

## 代码块 15

```java
class Blah extends Activity {
    @Override
    public void onCreate(Bundle b){
        ...
    MyApp appState = ((MyApp)getApplicationContext());
    String state = appState.getState();
        ...
    }
}
```

## 代码块 16

```java
class MyApp extends Application {
    private String myState;
    private static MyApp instance;

    public static MyApp getInstance(){
        return instance;
    }


    public String getState(){
        return myState;
    }
    public void setState(String s){
        myState = s;
    }

    @Override
    public void onCreate(){
        onCreate();
        instance = this;
    }

}
```

## 代码块 17

```java
public class XclSingleton
{
    //单例模式实例
    private static XclSingleton instance = null;

    //synchronized 用于线程安全，防止多线程同时创建实例
    public synchronized static XclSingleton getInstance(){
        if(instance == null){
            instance = new XclSingleton();
        }
        return instance;
    }

    final HashMap<String, Object> mMap;
    private XclSingleton()
    {
        mMap = new HashMap<String,Object>();
    }

    public void put(String key,Object value){
        mMap.put(key,value);
    }

    public Object get(String key)
    {
        return mMap.get(key);
    }

}
```

## 代码块 18

```java
XclSingleton.getInstance().put("key1", "value1");
XclSingleton.getInstance().put("key2", "value2");
```
