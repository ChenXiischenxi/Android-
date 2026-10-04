# 8.3.5 Paint API之—— Xfermode与PorterDuff详解(二)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-xfermode-porterduff2.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/10/23 0023.
 */
public class ScreenUtil {
    /**
     * 获取屏幕宽高，sdk17后不建议采用
     *
     * @param context
     */
    public static int[] getScreenHW(Context context) {
        WindowManager manager = (WindowManager) context.getSystemService(Context.WINDOW_SERVICE);
        Display display = manager.getDefaultDisplay();
        int width = display.getWidth();
        int height = display.getHeight();
        int[] HW = new int[] { width, height };
        return HW;
    }

    /**
     * 获取屏幕宽高，建议采用
     *
     * @param context
     */
    public static int[] getScreenHW2(Context context) {
        WindowManager manager = (WindowManager) context.getSystemService(Context.WINDOW_SERVICE);
        DisplayMetrics dm = new DisplayMetrics();
        manager.getDefaultDisplay().getMetrics(dm);
        int width = dm.widthPixels;
        int height = dm.heightPixels;
        int[] HW = new int[] { width, height };
        return HW;
    }

    /**
     * 获取屏幕的宽度
     *
     * @param context
     * @return
     */
    public static int getScreenW(Context context) {
        return getScreenHW2(context)[0];
    }

    /**
     * 获取屏幕的高度
     *
     * @param context
     * @return
     */
    public static int getScreenH(Context context) {
        return getScreenHW2(context)[1];
    }
}
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/10/23 0023.
 */
public class XfermodeView extends View {

    private PorterDuffXfermode pdXfermode;   //定义PorterDuffXfermode变量
    //定义MODE常量，等下直接改这里即可进行测试
    private static PorterDuff.Mode PD_MODE = PorterDuff.Mode.ADD;
    private int screenW, screenH; //屏幕宽高
    private int width = 200;      //绘制的图片宽高
    private int height = 200;
    private Bitmap srcBitmap, dstBitmap;     //上层SRC的Bitmap和下层Dst的Bitmap

    public XfermodeView(Context context) {
        this(context, null);
    }

    public XfermodeView(Context context, AttributeSet attrs) {
        super(context, attrs);
        screenW = ScreenUtil.getScreenW(context);
        screenH = ScreenUtil.getScreenH(context);
        //创建一个PorterDuffXfermode对象
        pdXfermode = new PorterDuffXfermode(PD_MODE);
        //实例化两个Bitmap
        srcBitmap = makeSrc(width, height);
        dstBitmap = makeDst(width, height);
    }

    public XfermodeView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }


    //定义一个绘制圆形Bitmap的方法
    private Bitmap makeDst(int w, int h) {
        Bitmap bm = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888);
        Canvas c = new Canvas(bm);
        Paint p = new Paint(Paint.ANTI_ALIAS_FLAG);
        p.setColor(0xFF26AAD1);
        c.drawOval(new RectF(0, 0, w * 3 / 4, h * 3 / 4), p);
        return bm;
    }

    //定义一个绘制矩形的Bitmap的方法
    private Bitmap makeSrc(int w, int h) {
        Bitmap bm = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888);
        Canvas c = new Canvas(bm);
        Paint p = new Paint(Paint.ANTI_ALIAS_FLAG);
        p.setColor(0xFFFFCE43);
        c.drawRect(w / 3, h / 3, w * 19 / 20, h * 19 / 20, p);
        return bm;
    }

    @Override
    protected void onDraw(Canvas canvas) {
        Paint paint = new Paint();
        paint.setFilterBitmap(false);
        paint.setStyle(Paint.Style.FILL);
        canvas.drawBitmap(srcBitmap, (screenW / 3 - width) / 2, (screenH / 2 - height) / 2, paint);
        canvas.drawBitmap(dstBitmap, (screenW / 3 - width) / 2 + screenW / 3, (screenH / 2 - height) / 2, paint);

        //创建一个图层，在图层上演示图形混合后的效果
        int sc = canvas.saveLayer(0, 0, screenW, screenH, null, Canvas.MATRIX_SAVE_FLAG |
                Canvas.CLIP_SAVE_FLAG |
                Canvas.HAS_ALPHA_LAYER_SAVE_FLAG |
                Canvas.FULL_COLOR_LAYER_SAVE_FLAG |
                Canvas.CLIP_TO_LAYER_SAVE_FLAG);

        canvas.drawBitmap(dstBitmap, (screenW / 3 - width) / 2 + screenW / 3 * 2,
                (screenH / 2 - height) / 2, paint);     //绘制i
        //设置Paint的Xfermode
        paint.setXfermode(pdXfermode);
        canvas.drawBitmap(srcBitmap, (screenW / 3 - width) / 2 + screenW / 3 * 2,
                (screenH / 2 - height) / 2, paint);
        paint.setXfermode(null);
        // 还原画布
        canvas.restoreToCount(sc);
    }
}
```
