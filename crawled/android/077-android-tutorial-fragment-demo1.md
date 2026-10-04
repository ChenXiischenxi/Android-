# 5.2.1 Fragment实例精讲——底部导航栏的实现(方法1)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-fragment-demo1.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@mipmap/tab_channel_pressed" android:state_selected="true" />
    <item android:drawable="@mipmap/tab_channel_normal" />
</selector>
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/text_yellow" android:state_selected="true" />
    <item android:color="@color/text_gray" />
</selector>
```

## 代码块 3

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

## 代码块 4

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

## 代码块 5

```java
android:theme="@style/Theme.AppCompat.NoActionBar"
```

## 代码块 6

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

## 代码块 7

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

## 代码块 8

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
