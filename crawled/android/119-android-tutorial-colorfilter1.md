# 8.3.9 Paint API之—— ColorFilter(颜色过滤器)(1/3)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-colorfilter1.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="5dp">

    <ImageView
        android:id="@+id/img_show"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="2" />

    <GridLayout
        android:id="@+id/gp_matrix"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="3"
        android:columnCount="5"
        android:rowCount="4"></GridLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
        <Button
            android:id="@+id/btn_reset"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="重置" />
        <Button
            android:id="@+id/btn_Change"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="变换" />
    </LinearLayout>
</LinearLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private ImageView img_show;
    private GridLayout gp_matrix;
    private Button btn_reset;
    private Button btn_Change;
    private Bitmap mBitmap;
    private int mEtWidth, mEtHeight;
    private EditText[] mEts = new EditText[20];
    private float[] mColorMatrix = new float[20];
    private Context mContext;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        bindViews();


        gp_matrix.post(new Runnable() {
            @Override
            public void run() {
                mEtWidth = gp_matrix.getWidth() / 5;
                mEtHeight = gp_matrix.getHeight() / 4;
                //添加5 * 4个EditText
                for (int i = 0; i < 20; i++) {
                    EditText editText = new EditText(mContext);
                    mEts[i] = editText;
                    gp_matrix.addView(editText, mEtWidth, mEtHeight);
                }
                initMatrix();
            }
        });
    }

    private void bindViews() {
        img_show = (ImageView) findViewById(R.id.img_show);
        gp_matrix = (GridLayout) findViewById(R.id.gp_matrix);
        btn_reset = (Button) findViewById(R.id.btn_reset);
        btn_Change = (Button) findViewById(R.id.btn_Change);

        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.img_meizi);
        img_show.setImageBitmap(mBitmap);

        btn_reset.setOnClickListener(this);
        btn_Change.setOnClickListener(this);
    }


    //定义一个初始化颜色矩阵的方法
    private void initMatrix() {
        for (int i = 0; i < 20; i++) {
            if (i % 6 == 0) {
                mEts[i].setText(String.valueOf(1));
            } else {
                mEts[i].setText(String.valueOf(0));
            }
        }
    }

    //定义一个获取矩阵值得方法
    private void getMatrix() {
        for (int i = 0; i < 20; i++) {
            mColorMatrix[i] = Float.valueOf(mEts[i].getText().toString());
        }
    }

    //根据颜色矩阵的值来处理图片
    private void setImageMatrix() {
        Bitmap bmp = Bitmap.createBitmap(mBitmap.getWidth(), mBitmap.getHeight(),
                Bitmap.Config.ARGB_8888);
        android.graphics.ColorMatrix colorMatrix = new android.graphics.ColorMatrix();
        colorMatrix.set(mColorMatrix);

        Canvas canvas = new Canvas(bmp);
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        paint.setColorFilter(new ColorMatrixColorFilter(colorMatrix));
        canvas.drawBitmap(mBitmap, 0, 0, paint);
        img_show.setImageBitmap(bmp);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_Change:
                getMatrix();
                setImageMatrix();
                break;
            case R.id.btn_reset:
                initMatrix();
                getMatrix();
                setImageMatrix();
                break;
        }
    }
}
```

## 代码块 3

```java
/**
 * Created by Jay on 2015/10/28 0028.
 */
public class ImageHelper {
    /**
     * 该方法用来处理图像，根据色调，饱和度，亮度来调节
     *
     * @param bm:要处理的图像
     * @param hue:色调
     * @param saturation:饱和度
     * @param lum:亮度
     *
     */
    public static Bitmap handleImageEffect(Bitmap bm, float hue, float saturation, float lum) {
        Bitmap bmp = Bitmap.createBitmap(bm.getWidth(), bm.getHeight(), Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bmp);
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);

        ColorMatrix hueMatrix = new ColorMatrix();
        hueMatrix.setRotate(0, hue);    //0代表R，红色
        hueMatrix.setRotate(1, hue);    //1代表G，绿色
        hueMatrix.setRotate(2, hue);    //2代表B，蓝色

        ColorMatrix saturationMatrix = new ColorMatrix();
        saturationMatrix.setSaturation(saturation);

        ColorMatrix lumMatrix = new ColorMatrix();
        lumMatrix.setScale(lum, lum, lum, 1);


        ColorMatrix imageMatrix = new ColorMatrix();
        imageMatrix.postConcat(hueMatrix);
        imageMatrix.postConcat(saturationMatrix);
        imageMatrix.postConcat(lumMatrix);

        paint.setColorFilter(new ColorMatrixColorFilter(imageMatrix));
        canvas.drawBitmap(bm, 0, 0, paint);

        return bmp;
    }
}
```

## 代码块 4

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="5dp">

    <ImageView
        android:id="@+id/img_meizi"
        android:layout_width="300dp"
        android:layout_height="300dp"
        android:layout_centerHorizontal="true"
        android:layout_marginBottom="24dp"
        android:layout_marginTop="24dp" />


    <TextView
        android:id="@+id/txt_hue"
        android:layout_width="wrap_content"
        android:layout_height="32dp"
        android:layout_below="@id/img_meizi"
        android:gravity="center"
        android:text="色调    :"
        android:textSize="18sp" />

    <SeekBar
        android:id="@+id/sb_hue"
        android:layout_width="match_parent"
        android:layout_height="32dp"
        android:layout_below="@id/img_meizi"
        android:layout_toRightOf="@id/txt_hue" />


    <TextView
        android:id="@+id/txt_saturation"
        android:layout_width="wrap_content"
        android:layout_height="32dp"
        android:layout_below="@id/txt_hue"
        android:gravity="center"
        android:text="饱和度:"
        android:textSize="18sp" />

    <SeekBar
        android:id="@+id/sb_saturation"
        android:layout_width="match_parent"
        android:layout_height="32dp"
        android:layout_below="@id/sb_hue"
        android:layout_toRightOf="@id/txt_saturation" />


    <TextView
        android:id="@+id/txt_lun"
        android:layout_width="wrap_content"
        android:layout_height="32dp"
        android:layout_below="@id/txt_saturation"
        android:gravity="center"
        android:text="亮度    :"
        android:textSize="18sp" />

    <SeekBar
        android:id="@+id/sb_lum"
        android:layout_width="match_parent"
        android:layout_height="32dp"
        android:layout_below="@id/sb_saturation"
        android:layout_toRightOf="@id/txt_lun" />

</RelativeLayout>
```

## 代码块 5

```java
public class MainActivity extends AppCompatActivity implements SeekBar.OnSeekBarChangeListener{

    private ImageView img_meizi;
    private SeekBar sb_hue;
    private SeekBar sb_saturation;
    private SeekBar sb_lum;
    private final static int MAX_VALUE = 255;
    private final static int MID_VALUE = 127;
    private float mHue = 0.0f;
    private float mStauration = 1.0f;
    private float mLum = 1.0f;
    private Bitmap mBitmap;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.img_meizi);
        bindViews();
    }

    private void bindViews() {
        img_meizi = (ImageView) findViewById(R.id.img_meizi);
        sb_hue = (SeekBar) findViewById(R.id.sb_hue);
        sb_saturation = (SeekBar) findViewById(R.id.sb_saturation);
        sb_lum = (SeekBar) findViewById(R.id.sb_lum);

        img_meizi.setImageBitmap(mBitmap);
        sb_hue.setMax(MAX_VALUE);
        sb_hue.setProgress(MID_VALUE);
        sb_saturation.setMax(MAX_VALUE);
        sb_saturation.setProgress(MID_VALUE);
        sb_lum.setMax(MAX_VALUE);
        sb_lum.setProgress(MID_VALUE);

        sb_hue.setOnSeekBarChangeListener(this);
        sb_saturation.setOnSeekBarChangeListener(this);
        sb_lum.setOnSeekBarChangeListener(this);

    }

    @Override
    public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
        switch (seekBar.getId()) {
            case R.id.sb_hue:
                mHue = (progress - MID_VALUE) * 1.0F / MID_VALUE * 180;
                break;
            case R.id.sb_saturation:
                mStauration = progress * 1.0F / MID_VALUE;
                break;
            case R.id.sb_lum:
                mLum = progress * 1.0F / MID_VALUE;
                break;
        }
        img_meizi.setImageBitmap(ImageHelper.handleImageEffect(mBitmap, mHue, mStauration, mLum));
    }

    @Override
    public void onStartTrackingTouch(SeekBar seekBar) {}

    @Override
    public void onStopTrackingTouch(SeekBar seekBar) {}
}
```
