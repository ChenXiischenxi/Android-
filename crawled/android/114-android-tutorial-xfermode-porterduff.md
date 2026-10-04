# 8.3.4 Paint API之—— Xfermode与PorterDuff详解(一)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-xfermode-porterduff.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/10/22 0022.
 */
public class AvoidXfermodeView1 extends View {

    private Paint mPaint;
    private Bitmap mBitmap;
    private AvoidXfermode avoidXfermode;

    public AvoidXfermodeView1(Context context) {
        super(context);
        init();
    }

    public AvoidXfermodeView1(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public AvoidXfermodeView1(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }

    private void init() {
        mPaint = new Paint(Paint.ANTI_ALIAS_FLAG);  //抗锯齿
        avoidXfermode = new AvoidXfermode(0XFFCCD1D4, 0, AvoidXfermode.Mode.TARGET);
        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.iv_meizi);

    }

    @Override
    protected void onDraw(Canvas canvas) {
        canvas.drawBitmap(mBitmap, 50, 50, mPaint);
        mPaint.setARGB(255, 222, 83, 71);
        mPaint.setXfermode(avoidXfermode);
        canvas.drawRect(50, 50, 690, 1010, mPaint);
    }
}
```

## 代码块 2

```java
avoidXfermode = new AvoidXfermode(0XFFD9E5F3, 25, AvoidXfermode.Mode.TARGET);
```

## 代码块 3

```java
avoidXfermode = new AvoidXfermode(0XFFD9E5F3,230, AvoidXfermode.Mode.AVOID);
```

## 代码块 4

```java
/**
 * Created by Jay on 2015/10/22 0022.
 */
public class PixelXorXfermodeView1 extends View{

    private Paint mPaint;
    private Bitmap mBitmap;
    private PixelXorXfermode pixelxorXfermode;

    public PixelXorXfermodeView1(Context context) {
        super(context);
        init();

    }

    public PixelXorXfermodeView1(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public PixelXorXfermodeView1(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }

    private void init() {
        mPaint = new Paint(Paint.ANTI_ALIAS_FLAG);  //抗锯齿
        pixelxorXfermode = new PixelXorXfermode(0XFFD9E5F3);
        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.iv_meizi);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        canvas.drawBitmap(mBitmap, 50, 50, mPaint);
        mPaint.setARGB(255, 222, 83, 71);
        mPaint.setXfermode(pixelxorXfermode);
        canvas.drawRect(50, 50, 690, 1010, mPaint);
    }

}
```
