# 12.1Android 实战 ：DrySister看妹子应用(第一版) &#8212; 项目搭建与简单实现

> 来源: https://www.runoob.com/w3cnote/android-tutorial-exercise-1.html

## 代码块 1

```java
public class PictureLoader {
    private ImageView loadImg;
    private String imgUrl;
    private byte[] picByte;

    Handler handler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            if (msg.what == 0x123) {
                if (picByte != null) {
                    Bitmap bitmap = BitmapFactory.decodeByteArray(picByte, 0, picByte.length);
                    loadImg.setImageBitmap(bitmap);
                }
            }
        }
    };

    public void load(ImageView loadImg, String imgUrl) {
        this.loadImg = loadImg;
        this.imgUrl = imgUrl;
        Drawable drawable = loadImg.getDrawable();
        if(drawable != null && drawable instanceof BitmapDrawable) {
            Bitmap bitmap = ((BitmapDrawable)drawable).getBitmap();
            if(bitmap != null && !bitmap.isRecycled()) {
                bitmap.recycle();
            }
        }
        new Thread(runnable).start();
    }

    Runnable runnable = new Runnable() {
        @Override
        public void run() {
            try {
                URL url = new URL(imgUrl);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setReadTimeout(10000);
                if (conn.getResponseCode() == 200) {
                    InputStream in = conn.getInputStream();
                    ByteArrayOutputStream out = new ByteArrayOutputStream();
                    byte[] bytes = new byte[1024];
                    int length = -1;
                    while ((length = in.read(bytes)) != -1) {
                        out.write(bytes, 0, length);
                    }
                    picByte = out.toByteArray();
                    in.close();
                    out.close();
                    handler.sendEmptyMessage(0x123);
                }

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    };
}
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private Button showBtn;
    private ImageView showImg;
    private ArrayList<String> urls;
    private int curPos = 0;
    private PictureLoader loader;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        loader = new PictureLoader();
        initData();
        initUI();
    }

    private void initData() {
        urls = new ArrayList<>();
        urls.add("http://ww4.sinaimg.cn/large/610dc034jw1f6ipaai7wgj20dw0kugp4.jpg");
        urls.add("http://ww3.sinaimg.cn/large/610dc034jw1f6gcxc1t7vj20hs0hsgo1.jpg");
        urls.add("http://ww4.sinaimg.cn/large/610dc034jw1f6f5ktcyk0j20u011hacg.jpg");
        urls.add("http://ww1.sinaimg.cn/large/610dc034jw1f6e1f1qmg3j20u00u0djp.jpg");
        urls.add("http://ww3.sinaimg.cn/large/610dc034jw1f6aipo68yvj20qo0qoaee.jpg");
        urls.add("http://ww3.sinaimg.cn/large/610dc034jw1f69c9e22xjj20u011hjuu.jpg");
        urls.add("http://ww3.sinaimg.cn/large/610dc034jw1f689lmaf7qj20u00u00v7.jpg");
        urls.add("http://ww3.sinaimg.cn/large/c85e4a5cjw1f671i8gt1rj20vy0vydsz.jpg");
        urls.add("http://ww2.sinaimg.cn/large/610dc034jw1f65f0oqodoj20qo0hntc9.jpg");
        urls.add("http://ww2.sinaimg.cn/large/c85e4a5cgw1f62hzfvzwwj20hs0qogpo.jpg");
    }

    private void initUI() {
        showBtn = (Button) findViewById(R.id.btn_show);
        showImg = (ImageView) findViewById(R.id.img_show);
        showBtn.setOnClickListener(this);
    }

    @Override public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_show:
                if (curPos > 9) {
                    curPos = 0;
                }
                loader.load(showImg, urls.get(curPos));
                curPos++;
                break;
        }
    }
}
```
