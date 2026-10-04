# 8.3.18 Canvas API详解(Part 3)Matrix和drawBitmapMesh

> 来源: https://www.runoob.com/w3cnote/android-tutorial-canvas-api3.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/11/11 0011.
 */
public class MyView extends View {

    private Bitmap mBitmap;
    private Matrix matrix = new Matrix();
    private float sx = 0.0f;          //设置倾斜度
    private int width,height;         //位图宽高
    private float scale = 1.0f;       //缩放比例
    private int method = 0;

    public MyView(Context context) {
        this(context, null);
    }

    public MyView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public MyView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void init() {
        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.img_meizi);
        width = mBitmap.getWidth();
        height = mBitmap.getHeight();
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        switch (method){
            case 0:
                matrix.reset();
                break;
            case 1:
                sx += 0.1;
                matrix.setSkew(sx,0);
                break;
            case 2:
                sx -= 0.1;
                matrix.setSkew(sx,0);
                break;
            case 3:
                if(scale < 2.0){
                    scale += 0.1;
                }
                matrix.setScale(scale,scale);
                break;
            case 4:
                if(scale > 0.5){
                    scale -= 0.1;
                }
                matrix.setScale(scale,scale);
                break;
        }
        //根据原始位图与Matrix创建新图片
        Bitmap bitmap = Bitmap.createBitmap(mBitmap,0,0,width,height,matrix,true);
        canvas.drawBitmap(bitmap,matrix,null);    //绘制新位图
    }

    public void setMethod(int i){
        method = i;
        postInvalidate();
    }
}
```

## 代码块 2

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:id="@+id/ly_bar"
        android:layout_width="match_parent"
        android:layout_height="64dp"
        android:layout_alignParentBottom="true">

        <Button
            android:id="@+id/btn_reset"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:text="重置" />

        <Button
            android:id="@+id/btn_left"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:text="左倾" />

        <Button
            android:id="@+id/btn_right"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:text="右倾" />

        <Button
            android:id="@+id/btn_zoomin"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:text="放大" />

        <Button
            android:id="@+id/btn_zoomout"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:text="缩小" />
    </LinearLayout>


    <com.jay.canvasdemo3.MyView
        android:id="@+id/myView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_above="@id/ly_bar" />

</RelativeLayout>
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Button btn_reset;
    private Button btn_left;
    private Button btn_right;
    private Button btn_zoomin;
    private Button btn_zoomout;
    private MyView myView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        btn_reset = (Button) findViewById(R.id.btn_reset);
        btn_left = (Button) findViewById(R.id.btn_left);
        btn_right = (Button) findViewById(R.id.btn_right);
        btn_zoomin = (Button) findViewById(R.id.btn_zoomin);
        btn_zoomout = (Button) findViewById(R.id.btn_zoomout);
        myView = (MyView) findViewById(R.id.myView);


        btn_reset.setOnClickListener(this);
        btn_left.setOnClickListener(this);
        btn_right.setOnClickListener(this);
        btn_zoomin.setOnClickListener(this);
        btn_zoomout.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_reset:
                myView.setMethod(0);
                break;
            case R.id.btn_left:
                myView.setMethod(1);
                break;
            case R.id.btn_right:
                myView.setMethod(2);
                break;
            case R.id.btn_zoomin:
                myView.setMethod(3);
                break;
            case R.id.btn_zoomout:
                myView.setMethod(4);
                break;
        }
    }
}
```

## 代码块 4

```java
/**
 * Created by Jay on 2015/11/11 0011.
 */
public class MyView extends View {

    //将水平和竖直方向上都划分为20格
    private final int WIDTH = 20;
    private final int HEIGHT = 20;
    private final int COUNT = (WIDTH + 1) * (HEIGHT + 1);  //记录该图片包含21*21个点
    private final float[] verts = new float[COUNT * 2];    //扭曲前21*21个点的坐标
    private final float[] orig = new float[COUNT * 2];    //扭曲后21*21个点的坐标
    private Bitmap mBitmap;
    private float bH,bW;


    public MyView(Context context) {
        this(context, null);
    }

    public MyView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public MyView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void init() {
        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.img_wuliao);
        bH = mBitmap.getWidth();
        bW = mBitmap.getHeight();
        int index = 0;
        //初始化orig和verts数组。
        for (int y = 0; y <= HEIGHT; y++)
        {
            float fy = bH * y / HEIGHT;
            for (int x = 0; x <= WIDTH; x++)
            {
                float fx = bW * x / WIDTH;
                orig[index * 2 + 0] = verts[index * 2 + 0] = fx;
                orig[index * 2 + 1] = verts[index * 2 + 1] = fy;
                index += 1;
            }
        }
        //设置背景色
        setBackgroundColor(Color.WHITE);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        canvas.drawBitmapMesh(mBitmap, WIDTH, HEIGHT, verts
                , 0, null, 0, null);
    }

    //工具方法，用于根据触摸事件的位置计算verts数组里各元素的值
    private void warp(float cx, float cy)
    {
        for (int i = 0; i < COUNT * 2; i += 2)
        {
            float dx = cx - orig[i + 0];
            float dy = cy - orig[i + 1];
            float dd = dx * dx + dy * dy;
            //计算每个座标点与当前点（cx、cy）之间的距离
            float d = (float)Math.sqrt(dd);
            //计算扭曲度，距离当前点（cx、cy）越远，扭曲度越小
            float pull = 80000 / ((float) (dd * d));
            //对verts数组（保存bitmap上21 * 21个点经过扭曲后的座标）重新赋值
            if (pull >= 1)
            {
                verts[i + 0] = cx;
                verts[i + 1] = cy;
            }
            else
            {
                //控制各顶点向触摸事件发生点偏移
                verts[i + 0] = orig[i + 0] + dx * pull;
                verts[i + 1] = orig[i + 1] + dy * pull;
            }
        }
        //通知View组件重绘
        invalidate();
    }

    @Override
    public boolean onTouchEvent(MotionEvent event)
    {
        //调用warp方法根据触摸屏事件的座标点来扭曲verts数组
        warp(event.getX(), event.getY());
        return true;
    }

}
```
