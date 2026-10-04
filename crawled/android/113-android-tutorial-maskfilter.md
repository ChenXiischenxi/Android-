# 8.3.3 Paint API之—— MaskFilter(面具)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-maskfilter.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/10/21 0021.
 */
public class BlurMaskFilterView extends View{

    public BlurMaskFilterView(Context context) {
        super(context);
    }

    public BlurMaskFilterView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public BlurMaskFilterView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    @Override
    protected void onDraw(Canvas canvas) {

        BlurMaskFilter bmf = null;
        Paint paint=new Paint();
        paint.setAntiAlias(true);          //抗锯齿
        paint.setColor(Color.RED);//画笔颜色
        paint.setStyle(Paint.Style.FILL);  //画笔风格
        paint.setTextSize(68);             //绘制文字大小，单位px
        paint.setStrokeWidth(5);           //画笔粗细

        bmf = new BlurMaskFilter(10f,BlurMaskFilter.Blur.NORMAL);
        paint.setMaskFilter(bmf);
        canvas.drawText("最喜欢看曹神日狗了~", 100, 100, paint);
        bmf = new BlurMaskFilter(10f,BlurMaskFilter.Blur.OUTER);
        paint.setMaskFilter(bmf);
        canvas.drawText("最喜欢看曹神日狗了~", 100, 200, paint);
        bmf = new BlurMaskFilter(10f,BlurMaskFilter.Blur.INNER);
        paint.setMaskFilter(bmf);
        canvas.drawText("最喜欢看曹神日狗了~", 100, 300, paint);
        bmf = new BlurMaskFilter(10f,BlurMaskFilter.Blur.SOLID);
        paint.setMaskFilter(bmf);
        canvas.drawText("最喜欢看曹神日狗了~", 100, 400, paint);

        setLayerType(View.LAYER_TYPE_SOFTWARE, null);     //关闭硬件加速
    }
}
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/10/22 0022.
 */
public class EmbossMaskFilterView extends View{

    public EmbossMaskFilterView(Context context) {
        super(context);
    }

    public EmbossMaskFilterView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public EmbossMaskFilterView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        float[] direction = new float[]{ 1, 1, 3 };   // 设置光源的方向
        float light = 0.4f;     //设置环境光亮度
        float specular = 8;     // 定义镜面反射系数
        float blur = 3.0f;      //模糊半径
        EmbossMaskFilter emboss=new EmbossMaskFilter(direction,light,specular,blur);

        Paint paint = new Paint();
        paint.setAntiAlias(true);          //抗锯齿
        paint.setColor(Color.BLUE);//画笔颜色
        paint.setStyle(Paint.Style.FILL);  //画笔风格
        paint.setTextSize(70);             //绘制文字大小，单位px
        paint.setStrokeWidth(8);           //画笔粗细
        paint.setMaskFilter(emboss);

        paint.setMaskFilter(emboss);
        canvas.drawText("最喜欢看曹神日狗了~", 50, 100, paint);


        Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.ic_bg_meizi1);
        canvas.drawBitmap(bitmap, 150, 200, paint);

        setLayerType(View.LAYER_TYPE_SOFTWARE, null);     //关闭硬件加速
    }
}
```
