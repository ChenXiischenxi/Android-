# 8.3.17 Canvas API详解(Part 2)剪切方法合集

> 来源: https://www.runoob.com/w3cnote/android-tutorial-canvas-api2.html

## 代码块 1

```java
private void init() {
    mPaint = new Paint();
    mPaint.setAntiAlias(true);
    mPaint.setStrokeWidth(6);
    mPaint.setColor(getResources().getColor(R.color.blush));
}

private void drawScene(Canvas canvas){
    canvas.drawRect(0, 0, 200, 200, mPaint);
}
```

## 代码块 2

```java
canvas.clipRect(10, 10, 110, 110);        //第一个
canvas.clipRect(50, 50, 150, 150, Region.Op.DIFFERENCE); //第二个
drawScene(canvas);
```

## 代码块 3

```java
canvas.clipRect(10, 10, 110, 110);        //第一个
canvas.clipRect(50, 50, 150, 150, Region.Op.INTERSECT); //第二个
drawScene(canvas);
```

## 代码块 4

```java
canvas.clipRect(10, 10, 110, 110);        //第一个
canvas.clipRect(40, 40, 140, 140, Region.Op.UNION); //第二个
drawScene(canvas);
```

## 代码块 5

```java
canvas.clipRect(10, 10, 110, 110);        //第一个
canvas.clipRect(50, 50, 150, 150, Region.Op.XOR); //第二个
drawScene(canvas);
```

## 代码块 6

```java
canvas.clipRect(10, 10, 110, 110);        //第一个
canvas.clipRect(50, 50, 150, 150, Region.Op.REVERSE_DIFFERENCE); //第二个
drawScene(canvas);
```

## 代码块 7

```java
canvas.clipRect(10, 10, 110, 110);        //第一个
canvas.clipRect(50, 50, 150, 150, Region.Op.REPLACE); //第二个
drawScene(canvas);
```

## 代码块 8

```java
/**
 * Created by Jay on 2015/11/10 0010.
 */
public class MyView extends View{

    private Bitmap mBitmap = null;
    private int limitLength = 0;     //
    private int width;
    private int heigth;
    private static final int CLIP_HEIGHT = 50;

    private boolean status = HIDE;//显示还是隐藏的状态，最开始为HIDE
    private static final boolean SHOW = true;//显示图片
    private static final boolean HIDE = false;//隐藏图片

    public MyView(Context context) {
        this(context, null);
    }

    public MyView(Context context, AttributeSet attrs) {
        super(context, attrs);
        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.img_meizi);
        limitLength = width = mBitmap.getWidth();
        heigth = mBitmap.getHeight();
    }

    public MyView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        Region region = new Region();
        int i = 0;
        while (i * CLIP_HEIGHT <= heigth) {//计算clip的区域
            if (i % 2 == 0) {
                region.union(new Rect(0, i * CLIP_HEIGHT, limitLength, (i + 1) * CLIP_HEIGHT));
            } else {
                region.union(new Rect(width - limitLength, i * CLIP_HEIGHT, width, (i + 1)
                        * CLIP_HEIGHT));
            }
            i++;
        }
        canvas.clipRegion(region);
        canvas.drawBitmap(mBitmap, 0, 0, new Paint());
        if (status == HIDE) {//如果此时是隐藏
            limitLength -= 10;
            if(limitLength <= 0)
                status=SHOW;
        } else {//如果此时是显示
            limitLength += 5;
            if(limitLength >= width)
                status=HIDE;
        }
        invalidate();
    }
}
```

## 代码块 9

```java
mPaint = new Paint();
mPaint.setAntiAlias(true);
mPaint.setColor(Color.BLACK);
mPaint.setTextSize(60);

canvas.translate(300,300);
canvas.clipRect(100, 100, 300, 300);                //设置显示范围
canvas.drawColor(Color.WHITE);                      //白色背景
canvas.drawText("双11，继续吃我的狗粮...", 150, 300, mPaint); //绘制字符串
```

## 代码块 10

```java
/**
 * Created by coder-pig on 2015/7/18 0018.
 */
public class RoundImageView extends ImageView {

    private Bitmap mBitmap;
    private Rect mRect = new Rect();
    private PaintFlagsDrawFilter pdf = new PaintFlagsDrawFilter(0, Paint.ANTI_ALIAS_FLAG);
    private Paint mPaint = new Paint();
    private Path mPath=new Path();
    public RoundImageView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }


    //传入一个Bitmap对象
    public void setBitmap(Bitmap bitmap) {
        this.mBitmap = bitmap;
    }


    private void init() {
        mPaint.setStyle(Paint.Style.STROKE);
        mPaint.setFlags(Paint.ANTI_ALIAS_FLAG);
        mPaint.setAntiAlias(true);// 抗锯尺
    }


    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        if(mBitmap == null)
        {
            return;
        }
        mRect.set(0,0,getWidth(),getHeight());
        canvas.save();
        canvas.setDrawFilter(pdf);
        mPath.addCircle(getWidth() / 2, getWidth() / 2, getHeight() / 2, Path.Direction.CCW);
        canvas.clipPath(mPath, Region.Op.REPLACE);
        canvas.drawBitmap(mBitmap, null, mRect, mPaint);
        canvas.restore();
    }
}
```

## 代码块 11

```xml
<com.jay.demo.imageviewdemo.RoundImageView
        android:id="@+id/img_round"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:layout_margin="5px"/>
```

## 代码块 12

```java
public class MainActivity extends AppCompatActivity {

    private RoundImageView img_round;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img_round = (RoundImageView) findViewById(R.id.img_round);
        Bitmap bitmap = BitmapFactory.decodeResource(getResources(),R.mipmap.meinv);
        img_round.setBitmap(bitmap);
    }
}
```
