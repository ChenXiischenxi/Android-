# 8.3.10 Paint API之—— ColorFilter(颜色过滤器)(2-3)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-colorfilterl2.html

## 代码块 1

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="5dp"
    tools:context=".MainActivity">

    <ImageView
        android:id="@+id/img_meizi"
        android:layout_width="300dp"
        android:layout_height="300dp"
        android:src="@mipmap/img_meizi" />

    <EditText
        android:id="@+id/edit_mul"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/img_meizi"
        android:text="0" />

    <EditText
        android:id="@+id/edit_add"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/edit_mul"
        android:text="0" />


    <Button
        android:id="@+id/btn_change"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@id/img_meizi"
        android:layout_below="@id/img_meizi"
        android:text="变化" />

</RelativeLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private ImageView img_meizi;
    private EditText edit_mul;
    private EditText edit_add;
    private Button btn_change;
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
        edit_mul = (EditText) findViewById(R.id.edit_mul);
        edit_add = (EditText) findViewById(R.id.edit_add);
        btn_change = (Button) findViewById(R.id.btn_change);

        btn_change.setOnClickListener(this);

    }


    private Bitmap ProcessImage(Bitmap bp,int mul,int add){
        Bitmap bitmap = Bitmap.createBitmap(bp.getWidth(),bp.getHeight(), Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        paint.setColorFilter(new LightingColorFilter(mul,add));
        canvas.drawBitmap(bp,0,0,paint);
        return bitmap;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_change:
                int mul = Integer.parseInt(edit_mul.getText().toString());
                int add = Integer.parseInt(edit_add.getText().toString());
                img_meizi.setImageBitmap(ProcessImage(mBitmap,mul,add));
                break;
        }
    }
}
```
