# 9.3 使用Camera拍照

> 来源: https://www.runoob.com/w3cnote/android-tutorial-camera.html

## 代码块 1

```java
Intent it = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
startActivityForResult(it,Activity.DEFAULT_KEYS_DIALER);

//重写onActivityResult方法
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if(requestCode == Activity.RESULT_OK){
            Bundle bundle = data.getExtras();
            Bitmap bitmap = (Bitmap) bundle.get("data");
            img_show.setImageBitmap(bitmap);
        }
}
```

## 代码块 2

```java
//定义一个保存图片的File变量
private File currentImageFile = null;

//在按钮点击事件处写上这些东西，这些是在SD卡创建图片文件的:
            @Override
            public void onClick(View v) {
                File dir = new File(Environment.getExternalStorageDirectory(),"pictures");
                if(dir.exists()){
                    dir.mkdirs();
                }
                currentImageFile = new File(dir,System.currentTimeMillis() + ".jpg");
                if(!currentImageFile.exists()){
                    try {
                        currentImageFile.createNewFile();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }

                Intent it = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                it.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(currentImageFile));
                startActivityForResult(it, Activity.DEFAULT_KEYS_DIALER);
            }

//onActivityResult：
 @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == Activity.DEFAULT_KEYS_DIALER) {
        img_show.setImageURI(Uri.fromFile(currentImageFile));
        }
}
```

## 代码块 3

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <SurfaceView
        android:id="@+id/sfv_preview"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1" />

    <Button
        android:id="@+id/btn_take"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="调用系统照相机" />

</LinearLayout>
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity {

    private SurfaceView sfv_preview;
    private Button btn_take;
    private Camera camera = null;
    private SurfaceHolder.Callback cpHolderCallback = new SurfaceHolder.Callback() {
        @Override
        public void surfaceCreated(SurfaceHolder holder) {
            startPreview();
        }

        @Override
        public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {

        }

        @Override
        public void surfaceDestroyed(SurfaceHolder holder) {
            stopPreview();
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        sfv_preview = (SurfaceView) findViewById(R.id.sfv_preview);
        btn_take = (Button) findViewById(R.id.btn_take);
        sfv_preview.getHolder().addCallback(cpHolderCallback);

        btn_take.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                camera.takePicture(null, null, new Camera.PictureCallback() {
                    @Override
                    public void onPictureTaken(byte[] data, Camera camera) {
                        String path = "";
                        if ((path = saveFile(data)) != null) {
                            Intent it = new Intent(MainActivity.this, PreviewActivity.class);
                            it.putExtra("path", path);
                            startActivity(it);
                        } else {
                            Toast.makeText(MainActivity.this, "保存照片失败", Toast.LENGTH_SHORT).show();
                        }
                    }
                });
            }
        });
    }

    //保存临时文件的方法
    private String saveFile(byte[] bytes){
        try {
            File file = File.createTempFile("img","");
            FileOutputStream fos = new FileOutputStream(file);
            fos.write(bytes);
            fos.flush();
            fos.close();
            return file.getAbsolutePath();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "";
    }


    //开始预览
    private void startPreview(){
        camera = Camera.open();
        try {
            camera.setPreviewDisplay(sfv_preview.getHolder());
            camera.setDisplayOrientation(90);   //让相机旋转90度
            camera.startPreview();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //停止预览
    private void stopPreview() {
        camera.stopPreview();
        camera.release();
        camera = null;
    }

}
```

## 代码块 5

```java
/**
 * Created by Jay on 2015/11/22 0022.
 */
public class PreviewActivity extends AppCompatActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ImageView img = new ImageView(this);
        String path = getIntent().getStringExtra("path");
        if(path != null){
            img.setImageURI(Uri.fromFile(new File(path)));
        }
        setContentView(img);
    }
}
```

## 代码块 6

```xml
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```
