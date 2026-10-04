# 10.8 LayoutInflater(布局服务)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-layoutinflater.html

## 代码块 1

```java
LayoutInflater inflater1 = LayoutInflater.from(this);
LayoutInflater inflater2 = getLayoutInflater();
LayoutInflater inflater3 = (LayoutInflater) getSystemService(LAYOUT_INFLATER_SERVICE);
```

## 代码块 2

```java
LinearLayout.LayoutParams lp1 = new LinearLayout.LayoutParams(
        LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
```

## 代码块 3

```java
RelativeLayout rly = new RelativeLayout(this);
RelativeLayout.LayoutParams lp2 = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
lp2.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
Button btnOne = new Button(this);
rly.addView(btnOne, lp2);
```

## 代码块 4

```java
public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        RelativeLayout rly = new RelativeLayout(this);
        Button btnOne = new Button(this);
        btnOne.setText("按钮1");
        Button btnTwo = new Button(this);
        btnTwo.setText("按钮2");
        // 为按钮1设置一个id值
        btnOne.setId(123);
        // 设置按钮1的位置,在父容器中居中
        RelativeLayout.LayoutParams rlp1 = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
        rlp1.addRule(RelativeLayout.CENTER_IN_PARENT);
        // 设置按钮2的位置,在按钮1的下方,并且对齐父容器右面
        RelativeLayout.LayoutParams rlp2 = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
        rlp2.addRule(RelativeLayout.BELOW, 123);
        rlp2.addRule(RelativeLayout.ALIGN_PARENT_RIGHT);
        // 将组件添加到外部容器中
        rly.addView(btnTwo, rlp2);
        rly.addView(btnOne, rlp1);
        // 设置当前视图加载的View即rly
        setContentView(rly);
    }
}
```

## 代码块 5

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/RelativeLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent" >

    <TextView
        android:id="@+id/txtTitle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="我是xml文件加载的布局"/>

</RelativeLayout>
```

## 代码块 6

```java
public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Button btnOne = new Button(this);
        btnOne.setText("我是动态添加的按钮");
        RelativeLayout.LayoutParams lp2 = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
        lp2.addRule(RelativeLayout.CENTER_IN_PARENT);
        LayoutInflater inflater = LayoutInflater.from(this);
        RelativeLayout rly = (RelativeLayout) inflater.inflate(
                R.layout.activity_main, null)
                .findViewById(R.id.RelativeLayout1);
        rly.addView(btnOne,lp2);
        setContentView(rly);
    }
}
```

## 代码块 7

```java
public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btnOne = new Button(this);
        btnOne.setText("我是动态添加的按钮");
        RelativeLayout.LayoutParams lp2 = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
        lp2.addRule(RelativeLayout.CENTER_IN_PARENT);
        RelativeLayout rly = (RelativeLayout) findViewById(R.id.RelativeLayout1);
        rly.addView(btnOne,lp2);
    }
}
```

## 代码块 8

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/RelativeLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent" >
    <Button
        android:id="@+id/btnLoad"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="动态加载布局"/>
</RelativeLayout>
```

## 代码块 9

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:id="@+id/ly_inflate" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="我是Java代码加载的布局" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="我是布局里的一个小按钮" />

</LinearLayout>
```

## 代码块 10

```java
public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //获得LayoutInflater对象;
        final LayoutInflater inflater = LayoutInflater.from(this);
        //获得外部容器对象
        final RelativeLayout rly = (RelativeLayout) findViewById(R.id.RelativeLayout1);
        Button btnLoad = (Button) findViewById(R.id.btnLoad);
        btnLoad.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                //加载要添加的布局对象
                LinearLayout ly = (LinearLayout) inflater.inflate(
                        R.layout.inflate, null, false).findViewById(
                        R.id.ly_inflate);
                //设置加载布局的大小与位置
                RelativeLayout.LayoutParams lp = new RelativeLayout.LayoutParams(
                        LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
                lp.addRule(RelativeLayout.CENTER_IN_PARENT);
                rly.addView(ly,lp);
            }
        });
    }
}
```

## 代码块 11

```java
final RelativeLayout rly = (RelativeLayout) findViewById(R.id.RelativeLayout1);
```

## 代码块 12

```java
final LayoutInflater inflater = LayoutInflater.from(this);
LinearLayout ly = (LinearLayout) inflater.inflate(R.layout.inflate, null, false)
   .findViewById(R.id.ly_inflate);
```

## 代码块 13

```java
RelativeLayout.LayoutParams lp = new RelativeLayout.LayoutParams(
               LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
       lp.addRule(RelativeLayout.CENTER_IN_PARENT);
```

## 代码块 14

```java
rly.addView(ly,lp);
```

## 代码块 15

```java
public View inflate(XmlPullParser parser, ViewGroup root, boolean attachToRoot) {
    synchronized (mConstructorArgs) {
        final AttributeSet attrs = Xml.asAttributeSet(parser);
        mConstructorArgs[0] = mContext;
        View result = root;
        try {
            int type;
            while ((type = parser.next()) != XmlPullParser.START_TAG &&
                    type != XmlPullParser.END_DOCUMENT) {
            }
            if (type != XmlPullParser.START_TAG) {
                throw new InflateException(parser.getPositionDescription()
                        + ": No start tag found!");
            }
            final String name = parser.getName();
            if (TAG_MERGE.equals(name)) {
                if (root == null || !attachToRoot) {
                    throw new InflateException("merge can be used only with a valid "
                            + "ViewGroup root and attachToRoot=true");
                }
                rInflate(parser, root, attrs);
            } else {
                View temp = createViewFromTag(name, attrs);
                ViewGroup.LayoutParams params = null;
                if (root != null) {
                    params = root.generateLayoutParams(attrs);
                    if (!attachToRoot) {
                        temp.setLayoutParams(params);
                    }
                }
                rInflate(parser, temp, attrs);
                if (root != null && attachToRoot) {
                    root.addView(temp, params);
                }
                if (root == null || !attachToRoot) {
                    result = temp;
                }
            }
        } catch (XmlPullParserException e) {
            InflateException ex = new InflateException(e.getMessage());
            ex.initCause(e);
            throw ex;
        } catch (IOException e) {
            InflateException ex = new InflateException(
                    parser.getPositionDescription()
                    + ": " + e.getMessage());
            ex.initCause(e);
            throw ex;
        }
        return result;
    }
}
```
