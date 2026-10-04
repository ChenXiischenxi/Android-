# 2.6.3 ViewPager的简单使用

> 来源: https://www.runoob.com/w3cnote/android-tutorial-viewpager.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#FFBA55"
    android:gravity="center"
    android:orientation="vertical">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="第一个Page"
        android:textColor="#000000"
        android:textSize="18sp"
        android:textStyle="bold" />
</LinearLayout>
```

## 代码块 2

```java
public class MyPagerAdapter extends PagerAdapter {
    private ArrayList<View> viewLists;

    public MyPagerAdapter() {
    }

    public MyPagerAdapter(ArrayList<View> viewLists) {
        super();
        this.viewLists = viewLists;
    }

    @Override
    public int getCount() {
        return viewLists.size();
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == object;
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        container.addView(viewLists.get(position));
        return viewLists.get(position);
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView(viewLists.get(position));
    }
}
```

## 代码块 3

```java
public class OneActivity extends AppCompatActivity{

    private ViewPager vpager_one;
    private ArrayList<View> aList;
    private MyPagerAdapter mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_one);
        vpager_one = (ViewPager) findViewById(R.id.vpager_one);

        aList = new ArrayList<View>();
        LayoutInflater li = getLayoutInflater();
        aList.add(li.inflate(R.layout.view_one,null,false));
        aList.add(li.inflate(R.layout.view_two,null,false));
        aList.add(li.inflate(R.layout.view_three,null,false));
        mAdapter = new MyPagerAdapter(aList);
        vpager_one.setAdapter(mAdapter);
    }
}
```

## 代码块 4

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:background="#CCFF99"
        android:gravity="center"
        android:text="PagerTitleStrip效果演示"
        android:textColor="#000000"
        android:textSize="18sp" />

    <android.support.v4.view.ViewPager
        android:id="@+id/vpager_two"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center">

        <android.support.v4.view.PagerTitleStrip
            android:id="@+id/pagertitle"
            android:layout_width="wrap_content"
            android:layout_height="40dp"
            android:layout_gravity="top"
            android:textColor="#FFFFFF" />
   </android.support.v4.view.ViewPager>

</LinearLayout>
```

## 代码块 5

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="35dp"
        android:background="#C0C080"
        android:gravity="center"
        android:text="PagerTabStrip效果演示"
        android:textSize="18sp" />

    <android.support.v4.view.ViewPager
        android:id="@+id/vpager_three"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center">

        <android.support.v4.view.PagerTabStrip
            android:id="@+id/pagertitle"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="top" />
     </android.support.v4.view.ViewPager>
</LinearLayout>
```

## 代码块 6

```java
/**
 * Created by Jay on 2015/10/8 0008.
 */
public class MyPagerAdapter2 extends PagerAdapter {
    private ArrayList<View> viewLists;
    private ArrayList<String> titleLists;

    public MyPagerAdapter2() {}
    public MyPagerAdapter2(ArrayList<View> viewLists,ArrayList<String> titleLists)
    {
        this.viewLists = viewLists;
        this.titleLists = titleLists;
    }

    @Override
    public int getCount() {
        return viewLists.size();
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == object;
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        container.addView(viewLists.get(position));
        return viewLists.get(position);
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView(viewLists.get(position));
    }

    @Override
    public CharSequence getPageTitle(int position) {
        return titleLists.get(position);
    }
}
```

## 代码块 7

```java
/**
 * Created by Jay on 2015/10/8 0008.
 */
public class TwoActivity extends AppCompatActivity {

    private ViewPager vpager_two;
    private ArrayList<View> aList;
    private ArrayList<String> sList;
    private MyPagerAdapter2 mAdapter;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_two);
        vpager_two = (ViewPager) findViewById(R.id.vpager_two);
        aList = new ArrayList<View>();
        LayoutInflater li = getLayoutInflater();
        aList.add(li.inflate(R.layout.view_one,null,false));
        aList.add(li.inflate(R.layout.view_two,null,false));
        aList.add(li.inflate(R.layout.view_three, null, false));
        sList = new ArrayList<String>();
        sList.add("橘黄");
        sList.add("淡黄");
        sList.add("浅棕");
        mAdapter = new MyPagerAdapter2(aList,sList);
        vpager_two.setAdapter(mAdapter);
    }
}
```

## 代码块 8

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <LinearLayout
        android:layout_width="fill_parent"
        android:layout_height="48dp"
        android:background="#FFFFFF">

        <TextView
            android:id="@+id/tv_one"
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:layout_weight="1.0"
            android:gravity="center"
            android:text="橘黄"
            android:textColor="#000000" />

        <TextView
            android:id="@+id/tv_two"
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:layout_weight="1.0"
            android:gravity="center"
            android:text="淡黄"
            android:textColor="#000000" />

        <TextView
            android:id="@+id/tv_three"
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:layout_weight="1.0"
            android:gravity="center"
            android:text="浅棕"
            android:textColor="#000000" />
    </LinearLayout>

    <ImageView
        android:id="@+id/img_cursor"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:scaleType="matrix"
        android:src="@mipmap/line" />

    <android.support.v4.view.ViewPager
        android:id="@+id/vpager_four"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_gravity="center"
        android:layout_weight="1.0"
        android:flipInterval="30"
        android:persistentDrawingCache="animation" />

</LinearLayout>
```

## 代码块 9

```java
/**
 * Created by Jay on 2015/10/8 0008.
 */
public class FourActivity extends AppCompatActivity implements View.OnClickListener,
        ViewPager.OnPageChangeListener {

    private ViewPager vpager_four;
    private ImageView img_cursor;
    private TextView tv_one;
    private TextView tv_two;
    private TextView tv_three;

    private ArrayList<View> listViews;
    private int offset = 0;//移动条图片的偏移量
    private int currIndex = 0;//当前页面的编号
    private int bmpWidth;// 移动条图片的长度
    private int one = 0; //移动条滑动一页的距离
    private int two = 0; //滑动条移动两页的距离

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_four);
        initViews();
    }


    private void initViews() {
        vpager_four = (ViewPager) findViewById(R.id.vpager_four);
        tv_one = (TextView) findViewById(R.id.tv_one);
        tv_two = (TextView) findViewById(R.id.tv_two);
        tv_three = (TextView) findViewById(R.id.tv_three);
        img_cursor = (ImageView) findViewById(R.id.img_cursor);

        //下划线动画的相关设置：
        bmpWidth = BitmapFactory.decodeResource(getResources(), R.mipmap.line).getWidth();// 获取图片宽度
        DisplayMetrics dm = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);
        int screenW = dm.widthPixels;// 获取分辨率宽度
        offset = (screenW / 3 - bmpWidth) / 2;// 计算偏移量
        Matrix matrix = new Matrix();
        matrix.postTranslate(offset, 0);
        img_cursor.setImageMatrix(matrix);// 设置动画初始位置
        //移动的距离
        one = offset * 2 + bmpWidth;// 移动一页的偏移量,比如1->2,或者2->3
        two = one * 2;// 移动两页的偏移量,比如1直接跳3


        //往ViewPager填充View，同时设置点击事件与页面切换事件
        listViews = new ArrayList<View>();
        LayoutInflater mInflater = getLayoutInflater();
        listViews.add(mInflater.inflate(R.layout.view_one, null, false));
        listViews.add(mInflater.inflate(R.layout.view_two, null, false));
        listViews.add(mInflater.inflate(R.layout.view_three, null, false));
        vpager_four.setAdapter(new MyPagerAdapter(listViews));
        vpager_four.setCurrentItem(0);          //设置ViewPager当前页，从0开始算

        tv_one.setOnClickListener(this);
        tv_two.setOnClickListener(this);
        tv_three.setOnClickListener(this);

        vpager_four.addOnPageChangeListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.tv_one:
                vpager_four.setCurrentItem(0);
                break;
            case R.id.tv_two:
                vpager_four.setCurrentItem(1);
                break;
            case R.id.tv_three:
                vpager_four.setCurrentItem(2);
                break;
        }
    }

    @Override
    public void onPageSelected(int index) {
        Animation animation = null;
        switch (index) {
            case 0:
                if (currIndex == 1) {
                    animation = new TranslateAnimation(one, 0, 0, 0);
                } else if (currIndex == 2) {
                    animation = new TranslateAnimation(two, 0, 0, 0);
                }
                break;
            case 1:
                if (currIndex == 0) {
                    animation = new TranslateAnimation(offset, one, 0, 0);
                } else if (currIndex == 2) {
                    animation = new TranslateAnimation(two, one, 0, 0);
                }
                break;
            case 2:
                if (currIndex == 0) {
                    animation = new TranslateAnimation(offset, two, 0, 0);
                } else if (currIndex == 1) {
                    animation = new TranslateAnimation(one, two, 0, 0);
                }
                break;
        }
        currIndex = index;
        animation.setFillAfter(true);// true表示图片停在动画结束位置
        animation.setDuration(300); //设置动画时间为300毫秒
        img_cursor.startAnimation(animation);//开始动画
    }

    @Override
    public void onPageScrollStateChanged(int i) {

    }

    @Override
    public void onPageScrolled(int i, float v, int i1) {

    }
}
```
