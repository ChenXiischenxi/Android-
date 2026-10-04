# 5.1 Fragment基本概述

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-base.html

## 代码块 1

```java
public class Fragmentone extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment1, container,false);
        return view;
    }
}
```

## 代码块 2

```xml
<fragment
    android:id="@+id/fragment1"
    android:name="com.jay.example.fragmentdemo.Fragmentone"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    android:layout_weight="1" />
```

## 代码块 3

```java
public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Display dis = getWindowManager().getDefaultDisplay();
        if(dis.getWidth() > dis.getHeight())
        {
            Fragment1 f1 = new Fragment1();
            getFragmentManager().beginTransaction().replace(R.id.LinearLayout1, f1).commit();
        }

        else
        {
            Fragment2 f2 = new Fragment2();
            getFragmentManager().beginTransaction().replace(R.id.LinearLayout1, f2).commit();
        }
    }
}
```

## 代码块 4

```java
/*接口*/
public interface CallBack{
    /*定义一个获取信息的方法*/
    public void getResult(String result);
}
```

## 代码块 5

```java
/*接口回调*/
public void getData(CallBack callBack){
    /*获取文本框的信息,当然你也可以传其他类型的参数,看需求咯*/
    String msg = editText.getText().toString();
    callBack.getResult(msg);
}
```

## 代码块 6

```java
/* 使用接口回调的方法获取数据 */
leftFragment.getData(new CallBack() {
 @Override
       public void getResult(String result) {              /*打印信息*/
            Toast.makeText(MainActivity.this, "-->>" + result, 1).show();
            }
        });
```

## 代码块 7

```java
FragmentManager fManager = getSupportFragmentManager( );
FragmentTransaction fTransaction = fManager.beginTransaction();
Fragmentthree t1 = new Fragmentthree();
Fragmenttwo t2 = new Fragmenttwo();
Bundle bundle = new Bundle();
bundle.putString("key",id);
t2.setArguments(bundle);
fTransaction.add(R.id.fragmentRoot, t2, "~~~");
fTransaction.addToBackStack(t1);
fTransaction.commit();
```
