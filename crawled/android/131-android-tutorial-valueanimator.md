# 8.4.3 Android动画合集之属性动画-初见

> 来源: https://www.runoob.com/w3cnote/android-tutorial-valueanimator.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/ly_root"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_one"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="动画1" />

    <Button
        android:id="@+id/btn_two"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="动画2" />

    <Button
        android:id="@+id/btn_three"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="动画3" />

    <Button
        android:id="@+id/btn_four"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="动画4" />

    <ImageView
        android:id="@+id/img_babi"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:background="@mipmap/img_babi" />

</LinearLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_one;
    private Button btn_two;
    private Button btn_three;
    private Button btn_four;
    private LinearLayout ly_root;
    private ImageView img_babi;
    private int width;
    private int height;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        ly_root = (LinearLayout) findViewById(R.id.ly_root);
        btn_one = (Button) findViewById(R.id.btn_one);
        btn_two = (Button) findViewById(R.id.btn_two);
        btn_three = (Button) findViewById(R.id.btn_three);
        btn_four = (Button) findViewById(R.id.btn_four);
        img_babi = (ImageView) findViewById(R.id.img_babi);

        btn_one.setOnClickListener(this);
        btn_two.setOnClickListener(this);
        btn_three.setOnClickListener(this);
        btn_four.setOnClickListener(this);
        img_babi.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_one:
                lineAnimator();
                break;
            case R.id.btn_two:
                scaleAnimator();
                break;
            case R.id.btn_three:
                raAnimator();
                break;
            case R.id.btn_four:
                circleAnimator();
                break;
            case R.id.img_babi:
                Toast.makeText(MainActivity.this, "不愧是coder-pig~", Toast.LENGTH_SHORT).show();
                break;
        }
    }


    //定义一个修改ImageView位置的方法
    private void moveView(View view, int rawX, int rawY) {
        int left = rawX - img_babi.getWidth() / 2;
        int top = rawY - img_babi.getHeight();
        int width = left + view.getWidth();
        int height = top + view.getHeight();
        view.layout(left, top, width, height);
    }


    //定义属性动画的方法：

    //按轨迹方程来运动
    private void lineAnimator() {
        width = ly_root.getWidth();
        height = ly_root.getHeight();
        ValueAnimator xValue = ValueAnimator.ofInt(height,0,height / 4,height / 2,height / 4 * 3 ,height);
        xValue.setDuration(3000L);
        xValue.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                // 轨迹方程 x = width / 2
                int y = (Integer) animation.getAnimatedValue();
                int x = width / 2;
                moveView(img_babi, x, y);
            }
        });
        xValue.setInterpolator(new LinearInterpolator());
        xValue.start();
    }

    //缩放效果
    private void scaleAnimator(){

        //这里故意用两个是想让大家体会下组合动画怎么用而已~
        final float scale = 0.5f;
        AnimatorSet scaleSet = new AnimatorSet();
        ValueAnimator valueAnimatorSmall = ValueAnimator.ofFloat(1.0f, scale);
        valueAnimatorSmall.setDuration(500);

        ValueAnimator valueAnimatorLarge = ValueAnimator.ofFloat(scale, 1.0f);
        valueAnimatorLarge.setDuration(500);

        valueAnimatorSmall.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                float scale = (Float) animation.getAnimatedValue();
                img_babi.setScaleX(scale);
                img_babi.setScaleY(scale);
            }
        });
        valueAnimatorLarge.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                float scale = (Float) animation.getAnimatedValue();
                img_babi.setScaleX(scale);
                img_babi.setScaleY(scale);
            }
        });

        scaleSet.play(valueAnimatorLarge).after(valueAnimatorSmall);
        scaleSet.start();

        //其实可以一个就搞定的
//        ValueAnimator vValue = ValueAnimator.ofFloat(1.0f, 0.6f, 1.2f, 1.0f, 0.6f, 1.2f, 1.0f);
//        vValue.setDuration(1000L);
//        vValue.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
//            @Override
//            public void onAnimationUpdate(ValueAnimator animation) {
//                float scale = (Float) animation.getAnimatedValue();
//                img_babi.setScaleX(scale);
//                img_babi.setScaleY(scale);
//            }
//        });
//        vValue.setInterpolator(new LinearInterpolator());
//        vValue.start();
    }


    //旋转的同时透明度变化
    private void raAnimator(){
        ValueAnimator rValue = ValueAnimator.ofInt(0, 360);
        rValue.setDuration(1000L);
        rValue.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                int rotateValue = (Integer) animation.getAnimatedValue();
                img_babi.setRotation(rotateValue);
                float fractionValue = animation.getAnimatedFraction();
                img_babi.setAlpha(fractionValue);
            }
        });
        rValue.setInterpolator(new DecelerateInterpolator());
        rValue.start();
    }

    //圆形旋转
    protected void circleAnimator() {
        width = ly_root.getWidth();
        height = ly_root.getHeight();
        final int R = width / 4;
        ValueAnimator tValue = ValueAnimator.ofFloat(0,
                (float) (2.0f * Math.PI));
        tValue.setDuration(1000);
        tValue.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                // 圆的参数方程 x = R * sin(t) y = R * cos(t)
                float t = (Float) animation.getAnimatedValue();
                int x = (int) (R * Math.sin(t) + width / 2);
                int y = (int) (R * Math.cos(t) + height / 2);
                moveView(img_babi, x, y);
            }
        });
        tValue.setInterpolator(new DecelerateInterpolator());
        tValue.start();
    }
}
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private Button btn_one;
    private Button btn_two;
    private Button btn_three;
    private Button btn_four;
    private Button btn_five;
    private LinearLayout ly_root;
    private TextView tv_pig;
    private int height;
    private ObjectAnimator animator1;
    private ObjectAnimator animator2;
    private ObjectAnimator animator3;
    private ObjectAnimator animator4;
    private AnimatorSet animSet;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
        initAnimator();
    }

    private void bindViews() {
        ly_root = (LinearLayout) findViewById(R.id.ly_root);
        btn_one = (Button) findViewById(R.id.btn_one);
        btn_two = (Button) findViewById(R.id.btn_two);
        btn_three = (Button) findViewById(R.id.btn_three);
        btn_four = (Button) findViewById(R.id.btn_four);
        btn_five = (Button) findViewById(R.id.btn_five);
        tv_pig = (TextView) findViewById(R.id.tv_pig);

        height = ly_root.getHeight();
        btn_one.setOnClickListener(this);
        btn_two.setOnClickListener(this);
        btn_three.setOnClickListener(this);
        btn_four.setOnClickListener(this);
        btn_five.setOnClickListener(this);
        tv_pig.setOnClickListener(this);
    }

    //初始化动画
    private void initAnimator() {
        animator1 = ObjectAnimator.ofFloat(tv_pig, "alpha", 1f, 0f, 1f, 0f, 1f);
        animator2 = ObjectAnimator.ofFloat(tv_pig, "rotation", 0f, 360f, 0f);
        animator3 = ObjectAnimator.ofFloat(tv_pig, "scaleX", 2f, 4f, 1f, 0.5f, 1f);
        animator4 = ObjectAnimator.ofFloat(tv_pig, "translationY", height / 8, -100, height / 2);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_one:
                animator1.setDuration(3000l);
                animator1.start();
                break;
            case R.id.btn_two:
                animator2.setDuration(3000l);
                animator2.start();
                break;
            case R.id.btn_three:
                animator3.setDuration(3000l);
                animator3.start();
                break;
            case R.id.btn_four:
                animator4.setDuration(3000l);
                animator4.start();
                break;
            case R.id.btn_five:
                //将前面的动画集合到一起~
                animSet = new AnimatorSet();
                animSet.play(animator4).with(animator3).with(animator2).after(animator1);
                animSet.setDuration(5000l);
                animSet.start();
                break;
            case R.id.tv_pig:
                Toast.makeText(MainActivity.this, "不愧是coder-pig~", Toast.LENGTH_SHORT).show();
                break;
        }
    }
}
```

## 代码块 4

```xml
<animator xmlns:android="http://schemas.android.com/apk/res/android"
    android:valueFrom="0"
    android:valueTo="100"
    android:valueType="intType"/>
```

## 代码块 5

```xml
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:valueFrom="1"
    android:valueTo="0"
    android:valueType="floatType"
    android:propertyName="alpha"/>
```

## 代码块 6

```xml
<set android:ordering="sequentially" >
    <set>
        <objectAnimator
            android:duration="500"
            android:propertyName="x"
            android:valueTo="400"
            android:valueType="intType" />
        <objectAnimator
            android:duration="500"
            android:propertyName="y"
            android:valueTo="300"
            android:valueType="intType" />
    </set>
    <objectAnimator
        android:duration="500"
        android:propertyName="alpha"
        android:valueTo="1f" />
</set>
```

## 代码块 7

```java
AnimatorSet set = (AnimatorSet)AnimatorInflater.loadAnimator(mContext,
             R.animator.property_animator);
animator.setTarget(view);
animator.start();
```
