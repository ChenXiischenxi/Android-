# 8.2.1 Bitmap(位图)全解析 Part 1

> 来源: https://www.runoob.com/w3cnote/android-tutorial-bitmap1.html

## 代码块 1

```java
BitmapDrawable bmpMeizi = new BitmapDrawable(getAssets().open("pic_meizi.jpg"));
Bitmap mBitmap = bmpMeizi.getBitmap();
img_bg.setImageBitmap(mBitmap);
```

## 代码块 2

```java
//通过资源ID
private Bitmap getBitmapFromResource(Resources res, int resId) {
      return BitmapFactory.decodeResource(res, resId);
}

//文件
private Bitmap getBitmapFromFile(String pathName) {
      return BitmapFactory.decodeFile(pathName);
}

//字节数组
public Bitmap Bytes2Bimap(byte[] b) {
    if (b.length != 0) {
        return BitmapFactory.decodeByteArray(b, 0, b.length);
    } else {
        return null;
    }
}

//输入流
private Bitmap getBitmapFromStream(InputStream inputStream) {
      return BitmapFactory.decodeStream(inputStream);
}
```

## 代码块 3

```java
Bitmap bitmap1 = BitmapFactory.decodeResource(getResources(), R.mipmap.pic_meizi);
Bitmap bitmap2 = Bitmap.createBitmap(bitmap1,100,100,200,200);
img_bg = (ImageView) findViewById(R.id.img_bg);
img_bg.setImageBitmap(bitmap2);
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity {
    static ByteArrayOutputStream byteOut = null;
    private Bitmap bitmap = null;
    private Button btn_cut;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn_cut = (Button) findViewById(R.id.btn_cut);
        btn_cut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                captureScreen();
            }
        });
    }

    public void captureScreen() {
        Runnable action = new Runnable() {
            @Override
            public void run() {
                final View contentView = getWindow().getDecorView();
                try{
                    Log.e("HEHE",contentView.getHeight()+":"+contentView.getWidth());
                    bitmap = Bitmap.createBitmap(contentView.getWidth(),
                            contentView.getHeight(), Bitmap.Config.ARGB_4444);
                    contentView.draw(new Canvas(bitmap));
                    ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                    bitmap.compress(Bitmap.CompressFormat.JPEG, 100, byteOut);
                    savePic(bitmap, "sdcard/short.png");
                }catch (Exception e){e.printStackTrace();}
                finally {
                    try{
                        if (null != byteOut)
                            byteOut.close();
                        if (null != bitmap && !bitmap.isRecycled()) {
//                            bitmap.recycle();
                            bitmap = null;
                        }
                    }catch (IOException e){e.printStackTrace();}

                }
            }
        };
        try {
            action.run();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void savePic(Bitmap b, String strFileName) {
        FileOutputStream fos = null;
        try {
            fos = new FileOutputStream(strFileName);
            if (null != fos) {
                boolean success= b.compress(Bitmap.CompressFormat.PNG, 100, fos);
                fos.flush();
                fos.close();
                if(success)
                    Toast.makeText(MainActivity.this, "截屏成功", Toast.LENGTH_SHORT).show();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
