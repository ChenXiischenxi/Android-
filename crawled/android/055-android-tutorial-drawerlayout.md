# 2.6.4 DrawerLayout(官方侧滑菜单)的简单使用

> 来源: https://www.runoob.com/w3cnote/android-tutorial-drawerlayout.html

## 代码块 1

```xml
<android.support.v4.widget.DrawerLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/drawer_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <FrameLayout
        android:id="@+id/ly_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

    <ListView
        android:id="@+id/list_left_drawer"
        android:layout_width="180dp"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        android:background="#080808"
        android:choiceMode="singleChoice"
        android:divider="#FFFFFF"
        android:dividerHeight="1dp" />

</android.support.v4.widget.DrawerLayout>
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/tv_content"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerInParent="true"
        android:textSize="25sp" />

</RelativeLayout>
```

## 代码块 3

```java
/**
 * Created by Jay on 2015/10/8 0008.
 */
public class ContentFragment extends Fragment {

    private TextView tv_content;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_content, container, false);
        tv_content = (TextView) view.findViewById(R.id.tv_content);
        String text = getArguments().getString("text");
        tv_content.setText(text);
        return view;
    }
}
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener{

    private DrawerLayout drawer_layout;
    private ListView list_left_drawer;
    private ArrayList<Item> menuLists;
    private MyAdapter<Item> myAdapter = null;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        drawer_layout = (DrawerLayout) findViewById(R.id.drawer_layout);
        list_left_drawer = (ListView) findViewById(R.id.list_left_drawer);

        menuLists = new ArrayList<Item>();
        menuLists.add(new Item(R.mipmap.iv_menu_realtime,"实时信息"));
        menuLists.add(new Item(R.mipmap.iv_menu_alert,"提醒通知"));
        menuLists.add(new Item(R.mipmap.iv_menu_trace,"活动路线"));
        menuLists.add(new Item(R.mipmap.iv_menu_settings,"相关设置"));
        myAdapter = new MyAdapter<Item>(menuLists,R.layout.item_list) {
            @Override
            public void bindView(ViewHolder holder, Item obj) {
                holder.setImageResource(R.id.img_icon,obj.getIconId());
                holder.setText(R.id.txt_content, obj.getIconName());
            }
        };
        list_left_drawer.setAdapter(myAdapter);
        list_left_drawer.setOnItemClickListener(this);
    }


    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        ContentFragment contentFragment = new ContentFragment();
        Bundle args = new Bundle();
        args.putString("text", menuLists.get(position).getIconName());
        contentFragment.setArguments(args);
        FragmentManager fm = getSupportFragmentManager();
        fm.beginTransaction().replace(R.id.ly_content,contentFragment).commit();
        drawer_layout.closeDrawer(list_left_drawer);
    }
}
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ImageView
        android:id="@+id/img_bg"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="@mipmap/bg_menu_left"/>

</LinearLayout>
```

## 代码块 6

```java
/**
 * Created by Jay on 2015/10/9 0009.
 */
public class LeftFragment extends Fragment{

    private DrawerLayout drawer_layout;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_left, container, false);
        ImageView img_bg = (ImageView) view.findViewById(R.id.img_bg);
        img_bg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                getActivity().startActivity(new Intent(getActivity(),OtherActivity.class));
                drawer_layout.closeDrawer(Gravity.START);
            }
        });
        return view;
    }

    //暴露给Activity，用于传入DrawerLayout，因为点击后想关掉DrawerLayout
    public void setDrawerLayout(DrawerLayout drawer_layout){
        this.drawer_layout = drawer_layout;
    }
}
```

## 代码块 7

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#2F9AF2"
    android:gravity="center"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_one"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="菜单项一" />

    <Button
        android:id="@+id/btn_two"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="菜单项二" />

    <Button
        android:id="@+id/btn_three"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="菜单项三" />

</LinearLayout>
```

## 代码块 8

```java
/**
 * Created by Jay on 2015/10/9 0009.
 */
public class RightFragment extends Fragment implements View.OnClickListener{

    private DrawerLayout drawer_layout;
    private FragmentManager fManager;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_right, container, false);
        view.findViewById(R.id.btn_one).setOnClickListener(this);
        view.findViewById(R.id.btn_two).setOnClickListener(this);
        view.findViewById(R.id.btn_three).setOnClickListener(this);
        fManager = getActivity().getSupportFragmentManager();
        return view;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_one:
                ContentFragment cFragment1 = new ContentFragment("1.点击了右侧菜单项一",R.color.blue);
                fManager.beginTransaction().replace(R.id.fly_content,cFragment1).commit();
                drawer_layout.closeDrawer(Gravity.END);
                break;
            case R.id.btn_two:
                ContentFragment cFragment2 = new ContentFragment("2.点击了右侧菜单项二",R.color.red);
                fManager.beginTransaction().replace(R.id.fly_content,cFragment2).commit();
                drawer_layout.closeDrawer(Gravity.END);
                break;
            case R.id.btn_three:
                ContentFragment cFragment3 = new ContentFragment("3.点击了右侧菜单项三",R.color.yellow);
                fManager.beginTransaction().replace(R.id.fly_content,cFragment3).commit();
                drawer_layout.closeDrawer(Gravity.END);
                break;
        }
    }

    public void setDrawerLayout(DrawerLayout drawer_layout){
        this.drawer_layout = drawer_layout;
    }

}
```

## 代码块 9

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/tv_content"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerInParent="true"
        android:textSize="25sp" />

</RelativeLayout>
```

## 代码块 10

```java
public class ContentFragment extends Fragment {

    private TextView tv_content;
    private String strContent;
    private int bgColor;

    public ContentFragment(String strContent,int bgColor) {
        this.strContent = strContent;
        this.bgColor = bgColor;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fg_content, container, false);
        view.setBackgroundColor(getResources().getColor(bgColor));
        tv_content = (TextView) view.findViewById(R.id.tv_content);
        tv_content.setText(strContent);
        return view;
    }
}
```

## 代码块 11

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:background="#DCDEDB">

    <Button
        android:id="@+id/btn_right"
        android:layout_width="40dp"
        android:layout_height="40dp"
        android:layout_centerVertical="true"
        android:layout_alignParentRight="true"
        android:background="@drawable/btn_selctor"/>

</RelativeLayout>
```

## 代码块 12

```xml
<android.support.v4.widget.DrawerLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/drawer_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <include
            android:id="@+id/topbar"
            layout="@layout/view_topbar"
            android:layout_width="wrap_content"
            android:layout_height="48dp" />

        <FrameLayout
            android:id="@+id/fly_content"
            android:layout_width="match_parent"
            android:layout_height="match_parent" />

    </LinearLayout>

    <fragment
        android:id="@+id/fg_left_menu"
        android:name="jay.com.drawerlayoutdemo2.LeftFragment"
        android:layout_width="300dp"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        android:tag="LEFT"
        tools:layout="@layout/fg_left" />

    <fragment
        android:id="@+id/fg_right_menu"
        android:name="jay.com.drawerlayoutdemo2.RightFragment"
        android:layout_width="100dp"
        android:layout_height="match_parent"
        android:layout_gravity="end"
        android:tag="RIGHT"
        tools:layout="@layout/fg_right" />

</android.support.v4.widget.DrawerLayout>
```

## 代码块 13

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private DrawerLayout drawer_layout;
    private FrameLayout fly_content;
    private View topbar;
    private Button btn_right;
    private RightFragment fg_right_menu;
    private LeftFragment fg_left_menu;
    private FragmentManager fManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        fManager = getSupportFragmentManager();
        fg_right_menu = (RightFragment) fManager.findFragmentById(R.id.fg_right_menu);
        fg_left_menu = (LeftFragment) fManager.findFragmentById(R.id.fg_left_menu);
        initViews();
    }

    private void initViews() {
        drawer_layout = (DrawerLayout) findViewById(R.id.drawer_layout);
        fly_content = (FrameLayout) findViewById(R.id.fly_content);
        topbar = findViewById(R.id.topbar);
        btn_right = (Button) topbar.findViewById(R.id.btn_right);
        btn_right.setOnClickListener(this);

        //设置右面的侧滑菜单只能通过编程来打开
        drawer_layout.setDrawerLockMode(DrawerLayout.LOCK_MODE_LOCKED_CLOSED,
                Gravity.END);

        drawer_layout.setDrawerListener(new DrawerLayout.DrawerListener() {
            @Override
            public void onDrawerSlide(View view, float v) {

            }

            @Override
            public void onDrawerOpened(View view) {

            }

            @Override
            public void onDrawerClosed(View view) {
                drawer_layout.setDrawerLockMode(
                        DrawerLayout.LOCK_MODE_LOCKED_CLOSED, Gravity.END);
            }

            @Override
            public void onDrawerStateChanged(int i) {

            }
        });

        fg_right_menu.setDrawerLayout(drawer_layout);
        fg_left_menu.setDrawerLayout(drawer_layout);
    }

    @Override
    public void onClick(View v) {
        drawer_layout.openDrawer(Gravity.RIGHT);
        drawer_layout.setDrawerLockMode(DrawerLayout.LOCK_MODE_UNLOCKED,
                Gravity.END);    //解除锁定
    }
}
```
