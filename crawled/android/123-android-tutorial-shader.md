# 8.3.13 Paint API之—— Shader(图像渲染)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-shader.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/11/4 0030.
 */
public class BitmapShaderView extends View {


    private Bitmap mBitmap = null;
    private ShapeDrawable sDrawable = null;
    private Paint mPaint = null;
    private int bitW = 0, bitH = 0;     //Bitmap宽高

    private Shader mBitmapShader = null;   //Bitmap渲染
    private Shader mLinearGradient = null; //线性渐变渲染
    private Shader mComposeShader = null; //混合渲染
    private Shader mRadialGradient = null; //环形渐变渲染
    private Shader mSweepGradient = null; //梯度渲染


    public BitmapShaderView(Context context) {
        this(context, null);
    }

    public BitmapShaderView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public BitmapShaderView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }


    private void init() {

        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.img_cat);
        bitW = mBitmap.getWidth();
        bitH = mBitmap.getHeight();
        mPaint = new Paint();

        //创建BitmapShader
        mBitmapShader = new BitmapShader(mBitmap, Shader.TileMode.MIRROR, Shader.TileMode.MIRROR);

        //创建LinearGradient并设置渐变的颜色数组
        mLinearGradient = new LinearGradient(0, 0, 100, 100,
                new int[]{Color.RED, Color.GREEN, Color.BLUE, Color.WHITE},
                null, Shader.TileMode.REPEAT);

        //混合渲染，这里使用了BitmapShader和LinearGradient进行混合，可以试试其他~
        mComposeShader = new ComposeShader(mBitmapShader, mLinearGradient, PorterDuff.Mode.DARKEN);

        //环形渐变渲染
        mRadialGradient = new RadialGradient(50, 200, 50,
                new int[]{Color.GREEN, Color.RED, Color.BLUE, Color.WHITE},
                null, Shader.TileMode.REPEAT);

        //梯度渲染
        mSweepGradient = new SweepGradient(30, 30, new int[]{Color.GREEN, Color.RED,
                Color.BLUE, Color.WHITE}, null);

    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);

        //将图片裁剪为椭圆形
        sDrawable = new ShapeDrawable(new OvalShape());
        sDrawable.getPaint().setShader(mBitmapShader);
        sDrawable.setBounds(0, 0, bitW, bitH);
        sDrawable.draw(canvas);

        //绘制线性渐变的矩形
        mPaint.setShader(mLinearGradient);
        canvas.drawRect(bitW, 0, bitW * 2, bitH, mPaint);

        //绘制混合渲染效果
        mPaint.setShader(mComposeShader);
        canvas.drawRect(0, bitH, bitW , bitH * 2, mPaint);

        //绘制环形渐变
        mPaint.setShader(mRadialGradient);
        canvas.drawCircle(bitW * 2.8f, bitH / 2, bitH / 2, mPaint);

        //绘制梯度渐变
        mPaint.setShader(mSweepGradient);
        canvas.drawRect(bitW, bitH, bitW * 2, bitH * 2, mPaint);


    }
}
```
