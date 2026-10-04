# 8.3.15 Paint API之——Typeface(字型)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-typeface.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/11/5 0005.
 */
public class MyView extends View{

    private Paint mPaint1,mPaint2,mPaint3,mPaint4,mPaint5;
    private Context mContext;

    public MyView(Context context) {
        this(context,null);
    }

    public MyView(Context context, AttributeSet attrs) {
        super(context, attrs);
        mContext = context;
        init();
    }

    public MyView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void init(){
        mPaint1 = new Paint();
        mPaint2 = new Paint();
        mPaint3 = new Paint();
        mPaint4 = new Paint();
        mPaint5 = new Paint();

        mPaint1.setColor(Color.RED);
        mPaint2.setColor(Color.BLUE);
        mPaint3.setColor(Color.BLACK);
        mPaint4.setColor(Color.YELLOW);
        mPaint5.setColor(Color.GRAY);


        mPaint1.setTextSize(100);
        mPaint2.setTextSize(100);
        mPaint3.setTextSize(100);
        mPaint4.setTextSize(100);
        mPaint5.setTextSize(100);


        mPaint1.setTypeface(Typeface.DEFAULT_BOLD);
        mPaint2.setTypeface(Typeface.MONOSPACE);
        mPaint3.setTypeface(Typeface.SANS_SERIF);
        mPaint4.setTypeface(Typeface.SERIF);
        mPaint5.setTypeface(Typeface.createFromAsset(mContext.getAssets(), "font/MONACO.ttf"));

    }

    @Override
    protected void onDraw(Canvas canvas) {
        canvas.drawText("Coder-pig", 100, 100, mPaint1);
        canvas.drawText("Coder-pig", 100, 200, mPaint2);
        canvas.drawText("Coder-pig", 100, 300, mPaint3);
        canvas.drawText("Coder-pig", 100, 400, mPaint4);
        canvas.drawText("Coder-pig", 100, 500, mPaint5);
    }
}
```
