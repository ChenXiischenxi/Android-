# Fragment

> 本章归并自 6 页教程代码块，来源见各节。

## 5.1 Fragment基本概述

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-base.html

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

```xml
<fragment
    android:id="@+id/fragment1"
    android:name="com.jay.example.fragmentdemo.Fragmentone"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    android:layout_weight="1" />
```

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

```java
/*接口*/
public interface CallBack{
    /*定义一个获取信息的方法*/
    public void getResult(String result);
}
```

```java
/*接口回调*/
public void getData(CallBack callBack){
    /*获取文本框的信息,当然你也可以传其他类型的参数,看需求咯*/
    String msg = editText.getText().toString();
    callBack.getResult(msg);
}
```

```java
/* 使用接口回调的方法获取数据 */
leftFragment.getData(new CallBack() {
 @Override
       public void getResult(String result) {              /*打印信息*/
            Toast.makeText(MainActivity.this, "-->>" + result, 1).show();
            }
        });
```

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

## 5.2.1 Fragment实例精讲——底部导航栏的实现(方法1)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-demo1.html

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@mipmap/tab_channel_pressed" android:state_selected="true" />
    <item android:drawable="@mipmap/tab_channel_normal" />
</selector>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/text_yellow" android:state_selected="true" />
    <item android:color="@color/text_gray" />
</selector>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_selected="true">
        <shape>
            <solid android:color="#FFC4C4C4" />
        </shape>
    </item>
    <item>
        <shape>
            <solid android:color="@color/transparent" />
        </shape>
    </item>
</selector>
```

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <RelativeLayout
        android:id="@+id/ly_top_bar"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:background="@color/bg_topbar">

        <TextView
            android:id="@+id/txt_topbar"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:gravity="center"
            android:textSize="18sp"
            android:textColor="@color/text_topbar"
            android:text="信息"/>


        <View
            android:layout_width="match_parent"
            android:layout_height="2px"
            android:background="@color/div_white"
            android:layout_alignParentBottom="true"/>

    </RelativeLayout>


    <LinearLayout
        android:id="@+id/ly_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:layout_alignParentBottom="true"
        android:background="@color/bg_white"
        android:orientation="horizontal">

        <TextView
            android:id="@+id/txt_channel"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:background="@drawable/tab_menu_bg"
            android:drawablePadding="3dp"
            android:drawableTop="@drawable/tab_menu_channel"
            android:gravity="center"
            android:padding="5dp"
            android:text="@string/tab_menu_alert"
            android:textColor="@drawable/tab_menu_text"
            android:textSize="16sp" />

        <TextView
            android:id="@+id/txt_message"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:background="@drawable/tab_menu_bg"
            android:drawablePadding="3dp"
            android:drawableTop="@drawable/tab_menu_message"
            android:gravity="center"
            android:padding="5dp"
            android:text="@string/tab_menu_profile"
            android:textColor="@drawable/tab_menu_text"
            android:textSize="16sp" />

        <TextView
            android:id="@+id/txt_better"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:background="@drawable/tab_menu_bg"
            android:drawablePadding="3dp"
            android:drawableTop="@drawable/tab_menu_better"
            android:gravity="center"
            android:padding="5dp"
            android:text="@string/tab_menu_pay"
            android:textColor="@drawable/tab_menu_text"
            android:textSize="16sp" />

        <TextView
            android:id="@+id/txt_setting"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:background="@drawable/tab_menu_bg"
            android:drawablePadding="3dp"
            android:drawableTop="@drawable/tab_menu_setting"
            android:gravity="center"
            android:padding="5dp"
            android:text="@string/tab_menu_setting"
            android:textColor="@drawable/tab_menu_text"
            android:textSize="16sp"/>

    </LinearLayout>

    <View
        android:id="@+id/div_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="2px"
        android:background="@color/div_white"
        android:layout_above="@id/ly_tab_bar"/>


    <FrameLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@id/ly_top_bar"
        android:layout_above="@id/div_tab_bar"
        android:id="@+id/ly_content">

    </FrameLayout>

</RelativeLayout>
```

```java
android:theme="@style/Theme.AppCompat.NoActionBar"
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_white">

    <TextView
        android:id="@+id/txt_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:text="呵呵"
        android:textColor="@color/text_yellow"
        android:textSize="20sp"/>

</LinearLayout>
```

```java
/**
 * Created by Coder-pig on 2015/8/28 0028.
 */
public class MyFragment extends Fragment {

    private String content;
    public MyFragment(String content) {
        this.content = content;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_content,container,false);
        TextView txt_content = (TextView) view.findViewById(R.id.txt_content);
        txt_content.setText(content);
        return view;
    }
}
```

```java
/**
 * Created by Coder-pig on 2015/8/28 0028.
 */
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    //UI Object
    private TextView txt_topbar;
    private TextView txt_channel;
    private TextView txt_message;
    private TextView txt_better;
    private TextView txt_setting;
    private FrameLayout ly_content;

    //Fragment Object
    private MyFragment fg1,fg2,fg3,fg4;
    private FragmentManager fManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_main);
        fManager = getFragmentManager();
        bindViews();
        txt_channel.performClick();   //模拟一次点击，既进去后选择第一项
    }

    //UI组件初始化与事件绑定
    private void bindViews() {
        txt_topbar = (TextView) findViewById(R.id.txt_topbar);
        txt_channel = (TextView) findViewById(R.id.txt_channel);
        txt_message = (TextView) findViewById(R.id.txt_message);
        txt_better = (TextView) findViewById(R.id.txt_better);
        txt_setting = (TextView) findViewById(R.id.txt_setting);
        ly_content = (FrameLayout) findViewById(R.id.ly_content);

        txt_channel.setOnClickListener(this);
        txt_message.setOnClickListener(this);
        txt_better.setOnClickListener(this);
        txt_setting.setOnClickListener(this);
    }

    //重置所有文本的选中状态
    private void setSelected(){
        txt_channel.setSelected(false);
        txt_message.setSelected(false);
        txt_better.setSelected(false);
        txt_setting.setSelected(false);
    }

    //隐藏所有Fragment
    private void hideAllFragment(FragmentTransaction fragmentTransaction){
        if(fg1 != null)fragmentTransaction.hide(fg1);
        if(fg2 != null)fragmentTransaction.hide(fg2);
        if(fg3 != null)fragmentTransaction.hide(fg3);
        if(fg4 != null)fragmentTransaction.hide(fg4);
    }


    @Override
    public void onClick(View v) {
        FragmentTransaction fTransaction = fManager.beginTransaction();
        hideAllFragment(fTransaction);
        switch (v.getId()){
            case R.id.txt_channel:
                setSelected();
                txt_channel.setSelected(true);
                if(fg1 == null){
                    fg1 = new MyFragment("第一个Fragment");
                    fTransaction.add(R.id.ly_content,fg1);
                }else{
                    fTransaction.show(fg1);
                }
                break;
            case R.id.txt_message:
                setSelected();
                txt_message.setSelected(true);
                if(fg2 == null){
                    fg2 = new MyFragment("第二个Fragment");
                    fTransaction.add(R.id.ly_content,fg2);
                }else{
                    fTransaction.show(fg2);
                }
                break;
            case R.id.txt_better:
                setSelected();
                txt_better.setSelected(true);
                if(fg3 == null){
                    fg3 = new MyFragment("第三个Fragment");
                    fTransaction.add(R.id.ly_content,fg3);
                }else{
                    fTransaction.show(fg3);
                }
                break;
            case R.id.txt_setting:
                setSelected();
                txt_setting.setSelected(true);
                if(fg4 == null){
                    fg4 = new MyFragment("第四个Fragment");
                    fTransaction.add(R.id.ly_content,fg4);
                }else{
                    fTransaction.show(fg4);
                }
                break;
        }
        fTransaction.commit();
    }
}
```

## 5.2.2 Fragment实例精讲——底部导航栏的实现(方法2)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-demo2.html

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@mipmap/tab_channel_pressed" android:state_checked="true" />
    <item android:drawable="@mipmap/tab_channel_normal" />
</selector>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/text_yellow" android:state_checked="true" />
    <item android:color="@color/text_gray" />
</selector>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_selected="true">
        <shape>
            <solid android:color="#FFC4C4C4" />
        </shape>
    </item>
    <item>
        <shape>
            <solid android:color="@color/transparent" />
        </shape>
    </item>
</selector>
```

```xml
<RadioButton
            android:id="@+id/rb_channel"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:background="@drawable/tab_menu_bg"
            android:button="@null"
            android:drawableTop="@drawable/tab_menu_channel"
            android:gravity="center"
            android:paddingTop="3dp"
            android:text="@string/tab_menu_alert"
            android:textColor="@drawable/tab_menu_text"
            android:textSize="18sp" />
```

```xml
<style name="tab_menu_item">
    <item name="android:layout_width">0dp</item>
    <item name="android:layout_weight">1</item>
    <item name="android:layout_height">match_parent</item>
    <item name="android:background">@drawable/tab_menu_bg</item>
    <item name="android:button">@null</item>
    <item name="android:gravity">center</item>
    <item name="android:paddingTop">3dp</item>
    <item name="android:textColor">@drawable/tab_menu_text</item>
    <item name="android:textSize">18sp</item>
</style>
```

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_gray"
    tools:context=".MainActivity">


    <RelativeLayout
        android:id="@+id/ly_top_bar"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:background="@color/bg_topbar">

        <TextView
            android:id="@+id/txt_topbar"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:gravity="center"
            android:text="信息"
            android:textColor="@color/text_topbar"
            android:textSize="18sp" />

        <View
            android:layout_width="match_parent"
            android:layout_height="2px"
            android:layout_alignParentBottom="true"
            android:background="@color/div_white" />

    </RelativeLayout>

    <RadioGroup
        android:id="@+id/rg_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:layout_alignParentBottom="true"
        android:background="@color/bg_white"
        android:orientation="horizontal">

        <RadioButton
            android:id="@+id/rb_channel"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_channel"
            android:text="@string/tab_menu_alert" />

        <RadioButton
            android:id="@+id/rb_message"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_message"
            android:text="@string/tab_menu_profile" />

        <RadioButton
            android:id="@+id/rb_better"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_better"
            android:text="@string/tab_menu_pay" />

        <RadioButton
            android:id="@+id/rb_setting"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_setting"
            android:text="@string/tab_menu_setting"/>

    </RadioGroup>

    <View
        android:id="@+id/div_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="2px"
        android:layout_above="@id/rg_tab_bar"
        android:background="@color/div_white" />

    <FrameLayout
        android:id="@+id/ly_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_above="@id/div_tab_bar"
        android:layout_below="@id/ly_top_bar"></FrameLayout>

</RelativeLayout>
```

```java
android:theme="@style/Theme.AppCompat.NoActionBar"
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_white">

    <TextView
        android:id="@+id/txt_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:text="呵呵"
        android:textColor="@color/text_yellow"
        android:textSize="20sp"/>

</LinearLayout>
```

```java
/**
 * Created by Coder-pig on 2015/8/29 0028.
 */
public class MyFragment extends Fragment {

    private String content;
    public MyFragment(String content) {
        this.content = content;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_content,container,false);
        TextView txt_content = (TextView) view.findViewById(R.id.txt_content);
        txt_content.setText(content);
        return view;
    }
}
```

```java
/**
 * Created by Coder-pig on 2015/8/29 0028.
 */
public class MainActivity extends AppCompatActivity implements RadioGroup.OnCheckedChangeListener{

    private RadioGroup rg_tab_bar;
    private RadioButton rb_channel;

    //Fragment Object
    private MyFragment fg1,fg2,fg3,fg4;
    private FragmentManager fManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        fManager = getFragmentManager();
        rg_tab_bar = (RadioGroup) findViewById(R.id.rg_tab_bar);
        rg_tab_bar.setOnCheckedChangeListener(this);
        //获取第一个单选按钮，并设置其为选中状态
        rb_channel = (RadioButton) findViewById(R.id.rb_channel);
        rb_channel.setChecked(true);
    }


    @Override
    public void onCheckedChanged(RadioGroup group, int checkedId) {
        FragmentTransaction fTransaction = fManager.beginTransaction();
        hideAllFragment(fTransaction);
        switch (checkedId){
            case R.id.rb_channel:
                if(fg1 == null){
                    fg1 = new MyFragment("第一个Fragment");
                    fTransaction.add(R.id.ly_content,fg1);
                }else{
                    fTransaction.show(fg1);
                }
                break;
            case R.id.rb_message:
                if(fg2 == null){
                    fg2 = new MyFragment("第二个Fragment");
                    fTransaction.add(R.id.ly_content,fg2);
                }else{
                    fTransaction.show(fg2);
                }
                break;
            case R.id.rb_better:
                if(fg3 == null){
                    fg3 = new MyFragment("第三个Fragment");
                    fTransaction.add(R.id.ly_content,fg3);
                }else{
                    fTransaction.show(fg3);
                }
                break;
            case R.id.rb_setting:
                if(fg4 == null){
                    fg4 = new MyFragment("第四个Fragment");
                    fTransaction.add(R.id.ly_content,fg4);
                }else{
                    fTransaction.show(fg4);
                }
                break;
        }
        fTransaction.commit();
    }

    //隐藏所有Fragment
    private void hideAllFragment(FragmentTransaction fragmentTransaction){
        if(fg1 != null)fragmentTransaction.hide(fg1);
        if(fg2 != null)fragmentTransaction.hide(fg2);
        if(fg3 != null)fragmentTransaction.hide(fg3);
        if(fg4 != null)fragmentTransaction.hide(fg4);
    }

}
```

## 5.2.3 Fragment实例精讲——底部导航栏的实现(方法3)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-demo3.html

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/text_yellow" android:state_selected="true" />
    <item android:color="@color/text_gray" />
</selector>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@mipmap/tab_better_pressed" android:state_selected="true" />
    <item android:drawable="@mipmap/tab_better_normal" />
</selector>
```

```xml
 <TextView
                    android:id="@+id/tab_menu_channel"
                    android:layout_marginTop="5dp"
                    android:layout_width="wrap_content"
                    android:layout_height="48dp"
                    android:layout_centerInParent="true"
                    android:textColor="@drawable/tab_menu_text"
                    android:drawableTop="@drawable/tab_menu_channel"
                    android:text="@string/tab_menu_alert"/>
                <TextView
                    android:layout_width="20dp"
                    android:layout_height="20dp"
                    android:background="@mipmap/bg_num"
                    android:layout_toRightOf="@+id/tab_menu_channel"
                    android:layout_marginLeft="-10dp"
                    android:text="99+"
                    android:textSize="12sp"
                    android:gravity="center"
                    android:textColor="@color/text_white"/>
```

```xml
<style name="tab_menu_text">
    <item name="android:layout_marginTop">5dp</item>
    <item name="android:layout_width">wrap_content</item>
    <item name="android:layout_height">48dp</item>
    <item name="android:layout_centerInParent">true</item>
    <item name="android:textColor">@drawable/tab_menu_text</item>
</style>


<style name="tab_menu_bgnum">
    <item name="android:layout_width">20dp</item>
    <item name="android:layout_height">20dp</item>
    <item name="android:background">@mipmap/bg_num</item>
    <item name="android:layout_marginLeft">-10dp</item>
    <item name="android:textSize">12sp</item>
    <item name="android:gravity">center</item>
    <item name="android:textColor">@color/text_white</item>
</style>
```

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">


    <RelativeLayout
        android:id="@+id/ly_top_bar"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:background="@color/bg_topbar">

        <TextView
            android:id="@+id/txt_topbar"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:gravity="center"
            android:text="信息"
            android:textColor="@color/text_topbar"
            android:textSize="18sp" />

        <View
            android:layout_width="match_parent"
            android:layout_height="2px"
            android:layout_alignParentBottom="true"
            android:background="@color/div_white" />

    </RelativeLayout>


    <LinearLayout
        android:id="@+id/ly_tab_menu"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:layout_alignParentBottom="true"
        android:background="@color/bg_white"
        android:orientation="horizontal">

        <LinearLayout
            android:id="@+id/ly_tab_menu_channel"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center">

            <RelativeLayout
                android:layout_width="wrap_content"
                android:layout_height="match_parent"
                android:padding="5dp">

                <TextView
                    android:id="@+id/tab_menu_channel"
                    style="@style/tab_menu_text"
                    android:drawableTop="@drawable/tab_menu_channel"
                    android:text="@string/tab_menu_alert" />

                <TextView
                    android:id="@+id/tab_menu_channel_num"
                    style="@style/tab_menu_bgnum"
                    android:layout_toRightOf="@+id/tab_menu_channel"
                    android:text="99+"
                    android:visibility="gone" />
            </RelativeLayout>
        </LinearLayout>

        <LinearLayout
            android:id="@+id/ly_tab_menu_message"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center">

            <RelativeLayout
                android:layout_width="wrap_content"
                android:layout_height="match_parent"
                android:padding="5dp">

                <TextView
                    android:id="@+id/tab_menu_message"
                    style="@style/tab_menu_text"
                    android:drawableTop="@drawable/tab_menu_message"
                    android:text="@string/tab_menu_profile" />

                <TextView
                    android:id="@+id/tab_menu_message_num"
                    style="@style/tab_menu_bgnum"
                    android:layout_toRightOf="@+id/tab_menu_message"
                    android:text="99+"
                    android:visibility="gone" />
            </RelativeLayout>
        </LinearLayout>


        <LinearLayout
            android:id="@+id/ly_tab_menu_better"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center">

            <RelativeLayout
                android:layout_width="wrap_content"
                android:layout_height="match_parent"
                android:padding="5dp">

                <TextView
                    android:id="@+id/tab_menu_better"
                    style="@style/tab_menu_text"
                    android:drawableTop="@drawable/tab_menu_better"
                    android:text="@string/tab_menu_pay" />

                <TextView
                    android:id="@+id/tab_menu_better_num"
                    style="@style/tab_menu_bgnum"
                    android:layout_toRightOf="@+id/tab_menu_better"
                    android:text="99+"
                    android:visibility="gone" />
            </RelativeLayout>
        </LinearLayout>


        <LinearLayout
            android:id="@+id/ly_tab_menu_setting"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center">

            <RelativeLayout
                android:layout_width="wrap_content"
                android:layout_height="match_parent"
                android:padding="5dp">

                <TextView
                    android:id="@+id/tab_menu_setting"
                    style="@style/tab_menu_text"
                    android:drawableTop="@drawable/tab_menu_setting"
                    android:text="@string/tab_menu_alert" />

                <ImageView
                    android:id="@+id/tab_menu_setting_partner"
                    android:layout_width="12dp"
                    android:layout_height="12dp"
                    android:layout_marginLeft="-5dp"
                    android:layout_toRightOf="@id/tab_menu_setting"
                    android:visibility="gone"
                    android:src="@mipmap/partner_red" />

            </RelativeLayout>
        </LinearLayout>

    </LinearLayout>

    <View
        android:id="@+id/div_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="2px"
        android:layout_above="@id/ly_tab_menu"
        android:background="@color/div_white" />


    <FrameLayout
        android:id="@+id/ly_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_above="@id/div_tab_bar"
        android:layout_below="@id/ly_top_bar"/>


</RelativeLayout>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="5dp">

    <Button
        android:id="@+id/btn_one"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="第一个显示信息"/>

    <Button
        android:id="@+id/btn_two"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="第二个显示信息"/>

    <Button
        android:id="@+id/btn_three"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="第三个显示信息"/>

    <Button
        android:id="@+id/btn_four"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="第四个显示信息"/>

</LinearLayout>
```

```java
public class MyFragment extends Fragment implements View.OnClickListener{

    private Context mContext;
    private Button btn_one;
    private Button btn_two;
    private Button btn_three;
    private Button btn_four;

    public MyFragment() {

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_my,container,false);
        //UI Object
        btn_one = (Button) view.findViewById(R.id.btn_one);
        btn_two = (Button) view.findViewById(R.id.btn_two);
        btn_three = (Button) view.findViewById(R.id.btn_three);
        btn_four = (Button) view.findViewById(R.id.btn_four);
        //Bind Event
        btn_one.setOnClickListener(this);
        btn_two.setOnClickListener(this);
        btn_three.setOnClickListener(this);
        btn_four.setOnClickListener(this);
        return view;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_one:
                TextView tab_menu_channel_num = (TextView) getActivity ().findViewById(R.id.tab_menu_channel_num);
                tab_menu_channel_num.setText("11");
                tab_menu_channel_num.setVisibility(View.VISIBLE);
                break;
            case R.id.btn_two:
                TextView tab_menu_message_num = (TextView) getActivity ().findViewById(R.id.tab_menu_message_num);
                tab_menu_message_num.setText("20");
                tab_menu_message_num.setVisibility(View.VISIBLE);
                break;
            case R.id.btn_three:
                TextView tab_menu_better_num = (TextView) getActivity ().findViewById(R.id.tab_menu_better_num);
                tab_menu_better_num.setText("99+");
                tab_menu_better_num.setVisibility(View.VISIBLE);
                break;
            case R.id.btn_four:
                ImageView tab_menu_setting_partner = (ImageView) getActivity ().findViewById(R.id.tab_menu_setting_partner);
                tab_menu_setting_partner.setVisibility(View.VISIBLE);
                break;
        }
    }
}
```

```java
/**
 * Created by Coder-pig on 2015/8/30 0030.
 */
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    //Activity UI Object
    private LinearLayout ly_tab_menu_channel;
    private TextView tab_menu_channel;
    private TextView tab_menu_channel_num;
    private LinearLayout ly_tab_menu_message;
    private TextView tab_menu_message;
    private TextView tab_menu_message_num;
    private LinearLayout ly_tab_menu_better;
    private TextView tab_menu_better;
    private TextView tab_menu_better_num;
    private LinearLayout ly_tab_menu_setting;
    private TextView tab_menu_setting;
    private ImageView tab_menu_setting_partner;
    private FragmentManager fManager;
    private FragmentTransaction fTransaction;
    private MyFragment fg1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
        ly_tab_menu_channel.performClick();
        fg1 = new MyFragment();
        fManager = getFragmentManager();
        fTransaction = fManager.beginTransaction();
        fTransaction.add(R.id.ly_content, fg1).commit();

    }

    private void bindViews() {
        ly_tab_menu_channel = (LinearLayout) findViewById(R.id.ly_tab_menu_channel);
        tab_menu_channel = (TextView) findViewById(R.id.tab_menu_channel);
        tab_menu_channel_num = (TextView) findViewById(R.id.tab_menu_channel_num);
        ly_tab_menu_message = (LinearLayout) findViewById(R.id.ly_tab_menu_message);
        tab_menu_message = (TextView) findViewById(R.id.tab_menu_message);
        tab_menu_message_num = (TextView) findViewById(R.id.tab_menu_message_num);
        ly_tab_menu_better = (LinearLayout) findViewById(R.id.ly_tab_menu_better);
        tab_menu_better = (TextView) findViewById(R.id.tab_menu_better);
        tab_menu_better_num = (TextView) findViewById(R.id.tab_menu_better_num);
        ly_tab_menu_setting = (LinearLayout) findViewById(R.id.ly_tab_menu_setting);
        tab_menu_setting = (TextView) findViewById(R.id.tab_menu_setting);
        tab_menu_setting_partner = (ImageView) findViewById(R.id.tab_menu_setting_partner);

        ly_tab_menu_channel.setOnClickListener(this);
        ly_tab_menu_message.setOnClickListener(this);
        ly_tab_menu_better.setOnClickListener(this);
        ly_tab_menu_setting.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.ly_tab_menu_channel:
                setSelected();
                tab_menu_channel.setSelected(true);
                tab_menu_channel_num.setVisibility(View.INVISIBLE);
                break;
            case R.id.ly_tab_menu_message:
                setSelected();
                tab_menu_message.setSelected(true);
                tab_menu_message_num.setVisibility(View.INVISIBLE);
                break;
            case R.id.ly_tab_menu_better:
                setSelected();
                tab_menu_better.setSelected(true);
                tab_menu_better_num.setVisibility(View.INVISIBLE);
                break;
            case R.id.ly_tab_menu_setting:
                setSelected();
                tab_menu_setting.setSelected(true);
                tab_menu_setting_partner.setVisibility(View.INVISIBLE);
                break;
        }
    }

    //重置所有文本的选中状态
    private void setSelected() {
        tab_menu_channel.setSelected(false);
        tab_menu_message.setSelected(false);
        tab_menu_better.setSelected(false);
        tab_menu_setting.setSelected(false);
    }


}
```

## 5.2.4 Fragment实例精讲——底部导航栏+ViewPager滑动切换页面

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-demo4.html

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <RelativeLayout
        android:id="@+id/ly_top_bar"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:background="@color/bg_topbar">

        <TextView
            android:id="@+id/txt_topbar"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:gravity="center"
            android:text="提醒"
            android:textColor="@color/text_topbar"
            android:textSize="18sp" />

        <View
            android:layout_width="match_parent"
            android:layout_height="2px"
            android:layout_alignParentBottom="true"
            android:background="@color/div_white" />

    </RelativeLayout>


    <RadioGroup
        android:id="@+id/rg_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:layout_alignParentBottom="true"
        android:background="@color/bg_white"
        android:orientation="horizontal">

        <RadioButton
            android:id="@+id/rb_channel"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_channel"
            android:text="@string/tab_menu_alert" />

        <RadioButton
            android:id="@+id/rb_message"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_message"
            android:text="@string/tab_menu_profile" />

        <RadioButton
            android:id="@+id/rb_better"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_better"
            android:text="@string/tab_menu_pay" />

        <RadioButton
            android:id="@+id/rb_setting"
            style="@style/tab_menu_item"
            android:drawableTop="@drawable/tab_menu_setting"
            android:text="@string/tab_menu_setting" />

    </RadioGroup>

    <View
        android:id="@+id/div_tab_bar"
        android:layout_width="match_parent"
        android:layout_height="2px"
        android:layout_above="@id/rg_tab_bar"
        android:background="@color/div_white" />

    <android.support.v4.view.ViewPager
        android:id="@+id/vpager"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_above="@id/div_tab_bar"
        android:layout_below="@id/ly_top_bar" />


</RelativeLayout>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_white"
    android:orientation="vertical">

    <TextView
        android:id="@+id/txt_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:text="呵呵"
        android:textColor="@color/text_yellow"
        android:textSize="20sp" />

</LinearLayout>
```

```java
/**
 * Created by Jay on 2015/8/28 0028.
 */
public class MyFragment1 extends Fragment {

    public MyFragment1() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_content, container, false);
        TextView txt_content = (TextView) view.findViewById(R.id.txt_content);
        txt_content.setText("第一个Fragment");
        Log.e("HEHE", "1日狗");
        return view;
    }
}
```

```java
/**
 * Created by Jay on 2015/8/31 0031.
 */
public class MyFragmentPagerAdapter extends FragmentPagerAdapter {

    private final int PAGER_COUNT = 4;
    private MyFragment1 myFragment1 = null;
    private MyFragment2 myFragment2 = null;
    private MyFragment3 myFragment3 = null;
    private MyFragment4 myFragment4 = null;


    public MyFragmentPagerAdapter(FragmentManager fm) {
        super(fm);
        myFragment1 = new MyFragment1();
        myFragment2 = new MyFragment2();
        myFragment3 = new MyFragment3();
        myFragment4 = new MyFragment4();
    }


    @Override
    public int getCount() {
        return PAGER_COUNT;
    }

    @Override
    public Object instantiateItem(ViewGroup vg, int position) {
        return super.instantiateItem(vg, position);
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        System.out.println("position Destory" + position);
        super.destroyItem(container, position, object);
    }

    @Override
    public Fragment getItem(int position) {
        Fragment fragment = null;
        switch (position) {
            case MainActivity.PAGE_ONE:
                fragment = myFragment1;
                break;
            case MainActivity.PAGE_TWO:
                fragment = myFragment2;
                break;
            case MainActivity.PAGE_THREE:
                fragment = myFragment3;
                break;
            case MainActivity.PAGE_FOUR:
                fragment = myFragment4;
                break;
        }
        return fragment;
    }

}
```

```java
package com.jay.fragmentdemo4;

import android.os.Bundle;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;


/**
 * Created by Coder-pig on 2015/8/28 0028.
 */
public class MainActivity extends AppCompatActivity implements RadioGroup.OnCheckedChangeListener,
        ViewPager.OnPageChangeListener {

    //UI Objects
    private TextView txt_topbar;
    private RadioGroup rg_tab_bar;
    private RadioButton rb_channel;
    private RadioButton rb_message;
    private RadioButton rb_better;
    private RadioButton rb_setting;
    private ViewPager vpager;

    private MyFragmentPagerAdapter mAdapter;

    //几个代表页面的常量
    public static final int PAGE_ONE = 0;
    public static final int PAGE_TWO = 1;
    public static final int PAGE_THREE = 2;
    public static final int PAGE_FOUR = 3;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mAdapter = new MyFragmentPagerAdapter(getSupportFragmentManager());
        bindViews();
        rb_channel.setChecked(true);
    }

    private void bindViews() {
        txt_topbar = (TextView) findViewById(R.id.txt_topbar);
        rg_tab_bar = (RadioGroup) findViewById(R.id.rg_tab_bar);
        rb_channel = (RadioButton) findViewById(R.id.rb_channel);
        rb_message = (RadioButton) findViewById(R.id.rb_message);
        rb_better = (RadioButton) findViewById(R.id.rb_better);
        rb_setting = (RadioButton) findViewById(R.id.rb_setting);
        rg_tab_bar.setOnCheckedChangeListener(this);

        vpager = (ViewPager) findViewById(R.id.vpager);
        vpager.setAdapter(mAdapter);
        vpager.setCurrentItem(0);
        vpager.addOnPageChangeListener(this);
    }

    @Override
    public void onCheckedChanged(RadioGroup group, int checkedId) {
        switch (checkedId) {
            case R.id.rb_channel:
                vpager.setCurrentItem(PAGE_ONE);
                break;
            case R.id.rb_message:
                vpager.setCurrentItem(PAGE_TWO);
                break;
            case R.id.rb_better:
                vpager.setCurrentItem(PAGE_THREE);
                break;
            case R.id.rb_setting:
                vpager.setCurrentItem(PAGE_FOUR);
                break;
        }
    }


    //重写ViewPager页面切换的处理方法
    @Override
    public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {
    }

    @Override
    public void onPageSelected(int position) {
    }

    @Override
    public void onPageScrollStateChanged(int state) {
        //state的状态有三个，0表示什么都没做，1正在滑动，2滑动完毕
        if (state == 2) {
            switch (vpager.getCurrentItem()) {
                case PAGE_ONE:
                    rb_channel.setChecked(true);
                    break;
                case PAGE_TWO:
                    rb_message.setChecked(true);
                    break;
                case PAGE_THREE:
                    rb_better.setChecked(true);
                    break;
                case PAGE_FOUR:
                    rb_setting.setChecked(true);
                    break;
            }
        }
    }
}
```

## 5.2.5 Fragment实例精讲——新闻(购物)类App列表Fragment的简单实现

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-demo5.html

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/white"
    android:orientation="horizontal">

    <ListView
        android:id="@+id/list_news"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/txt_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:textColor="@color/blue"
        android:textSize="20sp" />

</LinearLayout>
```

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/txt_title"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:background="@color/blue"
        android:textColor="@color/white"
        android:text="新闻列表"
        android:textSize="20sp"
        android:textStyle="bold"
        android:gravity="center"/>

    <FrameLayout
        android:id="@+id/fl_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@id/txt_title"/>

</RelativeLayout>
```

```java
/**
 * Created by Jay on 2015/9/6 0006.
 */
public class Data {

    private String new_title;
    private String new_content;

    public Data(){}

    public Data(String new_title, String new_content) {
        this.new_title = new_title;
        this.new_content = new_content;
    }

    public String getNew_title() {
        return new_title;
    }

    public String getNew_content() {
        return new_content;
    }

    public void setNew_title(String new_title) {
        this.new_title = new_title;
    }

    public void setNew_content(String new_content) {
        this.new_content = new_content;
    }
}
```

```java
/**
 * Created by Jay on 2015/9/6 0006.
 */
public class MyAdapter extends BaseAdapter{

    private List<Data> mData;
    private Context mContext;

    public MyAdapter(List<Data> mData, Context mContext) {
        this.mData = mData;
        this.mContext = mContext;
    }

    @Override
    public int getCount() {
        return mData.size();
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder viewHolder;
        if(convertView == null){
            convertView = LayoutInflater.from(mContext).inflate(R.layout.list_item,parent,false);
            viewHolder = new ViewHolder();
            viewHolder.txt_item_title = (TextView) convertView.findViewById(R.id.txt_item_title);
            convertView.setTag(viewHolder);
        }else{
            viewHolder = (ViewHolder) convertView.getTag();
        }
        viewHolder.txt_item_title.setText(mData.get(position).getNew_title());
        return convertView;
    }

    private class ViewHolder{
        TextView txt_item_title;
    }

}
```

```java
public class MainActivity extends AppCompatActivity {

    private TextView txt_title;
    private FrameLayout fl_content;
    private Context mContext;
    private ArrayList<Data> datas = null;
    private FragmentManager fManager = null;
    private long exitTime = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        fManager = getFragmentManager();
        bindViews();

        datas = new ArrayList<Data>();
        for (int i = 1; i <= 20; i++) {
            Data data = new Data("新闻标题" + i, i + "~新闻内容~~~~~~~~");
            datas.add(data);
        }
        NewListFragment nlFragment = new NewListFragment(fManager, datas);
        FragmentTransaction ft = fManager.beginTransaction();
        ft.replace(R.id.fl_content, nlFragment);
        ft.commit();
    }


    private void bindViews() {
        txt_title = (TextView) findViewById(R.id.txt_title);
        fl_content = (FrameLayout) findViewById(R.id.fl_content);
    }


    //点击回退键的处理：判断Fragment栈中是否有Fragment
    //没，双击退出程序，否则像是Toast提示
    //有，popbackstack弹出栈
    @Override
    public void onBackPressed() {
        if (fManager.getBackStackEntryCount() == 0) {
            if ((System.currentTimeMillis() - exitTime) > 2000) {
                Toast.makeText(getApplicationContext(), "再按一次退出程序",
                        Toast.LENGTH_SHORT).show();
                exitTime = System.currentTimeMillis();
            } else {
                super.onBackPressed();
            }
        } else {
            fManager.popBackStack();
            txt_title.setText("新闻列表");
        }
    }
}
```

```java
package com.jay.fragmentdemo4;

import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by Jay on 2015/9/6 0006.
 */
public class NewListFragment extends Fragment implements AdapterView.OnItemClickListener {
    private FragmentManager fManager;
    private ArrayList<Data> datas;
    private ListView list_news;

    public NewListFragment(FragmentManager fManager, ArrayList<Data> datas) {
        this.fManager = fManager;
        this.datas = datas;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_newlist, container, false);
        list_news = (ListView) view.findViewById(R.id.list_news);
        MyAdapter myAdapter = new MyAdapter(datas, getActivity());
        list_news.setAdapter(myAdapter);
        list_news.setOnItemClickListener(this);
        return view;
    }


    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        FragmentTransaction fTransaction = fManager.beginTransaction();
        NewContentFragment ncFragment = new NewContentFragment();
        Bundle bd = new Bundle();
        bd.putString("content", datas.get(position).getNew_content());
        ncFragment.setArguments(bd);
        //获取Activity的控件
        TextView txt_title = (TextView) getActivity().findViewById(R.id.txt_title);
        txt_title.setText(datas.get(position).getNew_content());
        //加上Fragment替换动画
        fTransaction.setCustomAnimations(R.anim.fragment_slide_left_enter, R.anim.fragment_slide_left_exit);
        fTransaction.replace(R.id.fl_content, ncFragment);
        //调用addToBackStack将Fragment添加到栈中
        fTransaction.addToBackStack(null);
        fTransaction.commit();
    }
}
```

```java
/**
 * Created by Jay on 2015/9/6 0006.
 */
public class NewContentFragment extends Fragment {

    NewContentFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_content, container, false);
        TextView txt_content = (TextView) view.findViewById(R.id.txt_content);
        //getArgument获取传递过来的Bundle对象
        txt_content.setText(getArguments().getString("content"));
        return view;
    }

}
```
