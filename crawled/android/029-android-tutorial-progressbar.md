# 2.3.7 ProgressBar(进度条)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-progressbar.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <!-- 系统提供的圆形进度条,依次是大中小 -->

    <ProgressBar
        style="@android:style/Widget.ProgressBar.Small"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <ProgressBar
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <ProgressBar
        style="@android:style/Widget.ProgressBar.Large"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <!--系统提供的水平进度条-->
    <ProgressBar
        style="@android:style/Widget.ProgressBar.Horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:max="100"
        android:progress="18" />

    <ProgressBar
        style="@android:style/Widget.ProgressBar.Horizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:indeterminate="true" />

</LinearLayout>
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="false" >

    <item
        android:drawable="@drawable/loading_01"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_02"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_03"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_04"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_05"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_06"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_07"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_08"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_09"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_10"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_11"
        android:duration="200"/>
    <item
        android:drawable="@drawable/loading_12"
        android:duration="200"/>

</animation-list>
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity {

    private ImageView img_pgbar;
    private AnimationDrawable ad;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_pgbar = (ImageView) findViewById(R.id.img_pgbar);
        ad = (AnimationDrawable) img_pgbar.getDrawable();
        img_pgbar.postDelayed(new Runnable() {
            @Override
            public void run() {
                ad.start();
            }
        }, 100);
    }

}
```

## 代码块 4

```java
/**
 * Created by Jay on 2015/8/5 0005.
 */
public class CirclePgBar extends View {


    private Paint mBackPaint;
    private Paint mFrontPaint;
    private Paint mTextPaint;
    private float mStrokeWidth = 50;
    private float mHalfStrokeWidth = mStrokeWidth / 2;
    private float mRadius = 200;
    private RectF mRect;
    private int mProgress = 0;
    //目标值，想改多少就改多少
    private int mTargetProgress = 90;
    private int mMax = 100;
    private int mWidth;
    private int mHeight;


    public CirclePgBar(Context context) {
        super(context);
        init();
    }

    public CirclePgBar(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public CirclePgBar(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }


    //完成相关参数初始化
    private void init() {
        mBackPaint = new Paint();
        mBackPaint.setColor(Color.WHITE);
        mBackPaint.setAntiAlias(true);
        mBackPaint.setStyle(Paint.Style.STROKE);
        mBackPaint.setStrokeWidth(mStrokeWidth);

        mFrontPaint = new Paint();
        mFrontPaint.setColor(Color.GREEN);
        mFrontPaint.setAntiAlias(true);
        mFrontPaint.setStyle(Paint.Style.STROKE);
        mFrontPaint.setStrokeWidth(mStrokeWidth);


        mTextPaint = new Paint();
        mTextPaint.setColor(Color.GREEN);
        mTextPaint.setAntiAlias(true);
        mTextPaint.setTextSize(80);
        mTextPaint.setTextAlign(Paint.Align.CENTER);
    }


    //重写测量大小的onMeasure方法和绘制View的核心方法onDraw()
    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);
        mWidth = getRealSize(widthMeasureSpec);
        mHeight = getRealSize(heightMeasureSpec);
        setMeasuredDimension(mWidth, mHeight);

    }


    @Override
    protected void onDraw(Canvas canvas) {
        initRect();
        float angle = mProgress / (float) mMax * 360;
        canvas.drawCircle(mWidth / 2, mHeight / 2, mRadius, mBackPaint);
        canvas.drawArc(mRect, -90, angle, false, mFrontPaint);
        canvas.drawText(mProgress + "%", mWidth / 2 + mHalfStrokeWidth, mHeight / 2 + mHalfStrokeWidth, mTextPaint);
        if (mProgress < mTargetProgress) {
            mProgress += 1;
            invalidate();
        }

    }

    public int getRealSize(int measureSpec) {
        int result = 1;
        int mode = MeasureSpec.getMode(measureSpec);
        int size = MeasureSpec.getSize(measureSpec);

        if (mode == MeasureSpec.AT_MOST || mode == MeasureSpec.UNSPECIFIED) {
            //自己计算
            result = (int) (mRadius * 2 + mStrokeWidth);
        } else {
            result = size;
        }

        return result;
    }

    private void initRect() {
        if (mRect == null) {
            mRect = new RectF();
            int viewSize = (int) (mRadius * 2);
            int left = (mWidth - viewSize) / 2;
            int top = (mHeight - viewSize) / 2;
            int right = left + viewSize;
            int bottom = top + viewSize;
            mRect.set(left, top, right, bottom);
        }
    }


}
```

## 代码块 5

```xml
 <com.jay.progressbardemo.CirclePgBar
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
```
