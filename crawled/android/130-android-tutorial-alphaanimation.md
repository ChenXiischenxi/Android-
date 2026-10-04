# 8.4.2 Android动画合集之补间动画

> 来源: https://www.runoob.com/w3cnote/android-tutorial-alphaanimation.html

## 代码块 1

```xml
<alpha xmlns:android="http://schemas.android.com/apk/res/android"
    android:interpolator="@android:anim/accelerate_decelerate_interpolator"
    android:fromAlpha="1.0"
    android:toAlpha="0.1"
    android:duration="2000"/>
```

## 代码块 2

```xml
<scale xmlns:android="http://schemas.android.com/apk/res/android"
    android:interpolator="@android:anim/accelerate_interpolator"
    android:fromXScale="0.2"
    android:toXScale="1.5"
    android:fromYScale="0.2"
    android:toYScale="1.5"
    android:pivotX="50%"
    android:pivotY="50%"
    android:duration="2000"/>
```

## 代码块 3

```xml
<translate xmlns:android="http://schemas.android.com/apk/res/android"
    android:interpolator="@android:anim/accelerate_decelerate_interpolator"
    android:fromXDelta="0"
    android:toXDelta="320"
    android:fromYDelta="0"
    android:toYDelta="0"
    android:duration="2000"/>
```

## 代码块 4

```xml
<rotate xmlns:android="http://schemas.android.com/apk/res/android"
    android:interpolator="@android:anim/accelerate_decelerate_interpolator"
    android:fromDegrees="0"
    android:toDegrees="360"
    android:duration="1000"
    android:repeatCount="1"
    android:repeatMode="reverse"/>
```

## 代码块 5

```xml
<set xmlns:android="http://schemas.android.com/apk/res/android"
    android:interpolator="@android:anim/decelerate_interpolator"
    android:shareInterpolator="true" >

    <scale
        android:duration="2000"
        android:fromXScale="0.2"
        android:fromYScale="0.2"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toXScale="1.5"
        android:toYScale="1.5" />

    <rotate
        android:duration="1000"
        android:fromDegrees="0"
        android:repeatCount="1"
        android:repeatMode="reverse"
        android:toDegrees="360" />

    <translate
        android:duration="2000"
        android:fromXDelta="0"
        android:fromYDelta="0"
        android:toXDelta="320"
        android:toYDelta="0" />

    <alpha
        android:duration="2000"
        android:fromAlpha="1.0"
        android:toAlpha="0.1" />

</set>
```

## 代码块 6

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_alpha"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="透明度渐变" />

    <Button
        android:id="@+id/btn_scale"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="缩放渐变" />

    <Button
        android:id="@+id/btn_tran"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="位移渐变" />

    <Button
        android:id="@+id/btn_rotate"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="旋转渐变" />

    <Button
        android:id="@+id/btn_set"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="组合渐变" />

    <ImageView
        android:id="@+id/img_show"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:layout_marginTop="48dp"
        android:src="@mipmap/img_face" />

</LinearLayout>
```

## 代码块 7

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Button btn_alpha;
    private Button btn_scale;
    private Button btn_tran;
    private Button btn_rotate;
    private Button btn_set;
    private ImageView img_show;
    private Animation animation = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        btn_alpha = (Button) findViewById(R.id.btn_alpha);
        btn_scale = (Button) findViewById(R.id.btn_scale);
        btn_tran = (Button) findViewById(R.id.btn_tran);
        btn_rotate = (Button) findViewById(R.id.btn_rotate);
        btn_set = (Button) findViewById(R.id.btn_set);
        img_show = (ImageView) findViewById(R.id.img_show);

        btn_alpha.setOnClickListener(this);
        btn_scale.setOnClickListener(this);
        btn_tran.setOnClickListener(this);
        btn_rotate.setOnClickListener(this);
        btn_set.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_alpha:
                animation = AnimationUtils.loadAnimation(this,
                        R.anim.anim_alpha);
                img_show.startAnimation(animation);
                break;
            case R.id.btn_scale:
                animation = AnimationUtils.loadAnimation(this,
                        R.anim.anim_scale);
                img_show.startAnimation(animation);
                break;
            case R.id.btn_tran:
                animation = AnimationUtils.loadAnimation(this,
                        R.anim.anim_translate);
                img_show.startAnimation(animation);
                break;
            case R.id.btn_rotate:
                animation = AnimationUtils.loadAnimation(this,
                        R.anim.anim_rotate);
                img_show.startAnimation(animation);
                break;
            case R.id.btn_set:
                animation = AnimationUtils.loadAnimation(this,
                        R.anim.anim_set);
                img_show.startAnimation(animation);
                break;
        }
    }
}
```

## 代码块 8

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#DDE2E3"
    tools:context=".MainActivity">

    <LinearLayout
        android:id="@+id/start_ctrl"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:orientation="vertical"
        android:visibility="gone">

        <Button
            android:id="@+id/start_login"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:background="#F26968"
            android:gravity="center"
            android:paddingBottom="15dp"
            android:paddingTop="15dp"
            android:text="登陆"
            android:textColor="#FFFFFF"
            android:textSize="18sp" />

        <Button
            android:id="@+id/start_register"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:background="#323339"
            android:gravity="center"
            android:paddingBottom="15dp"
            android:paddingTop="15dp"
            android:text="注册"
            android:textColor="#FFFFFF"
            android:textSize="18sp" />
    </LinearLayout>

</RelativeLayout>
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity {
    private LinearLayout start_ctrl;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        start_ctrl = (LinearLayout) findViewById(R.id.start_ctrl);
        //设置动画，从自身位置的最下端向上滑动了自身的高度，持续时间为500ms
        final TranslateAnimation ctrlAnimation = new TranslateAnimation(
                TranslateAnimation.RELATIVE_TO_SELF, 0, TranslateAnimation.RELATIVE_TO_SELF, 0,
                TranslateAnimation.RELATIVE_TO_SELF, 1, TranslateAnimation.RELATIVE_TO_SELF, 0);
        ctrlAnimation.setDuration(500l);     //设置动画的过渡时间
        start_ctrl.postDelayed(new Runnable() {
            @Override
            public void run() {
                start_ctrl.setVisibility(View.VISIBLE);
                start_ctrl.startAnimation(ctrlAnimation);
            }
        }, 2000);
    }
}
```
