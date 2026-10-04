# 7.5.5 WebView缓存问题

> 来源: https://www.runoob.com/w3cnote/android-tutorial-webview-cache.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {

    private WebView wView;
    private Button btn_clear_cache;
    private Button btn_refresh;
    private static final String APP_CACHE_DIRNAME = "/webcache"; // web缓存目录
    private static final String URL = "http://blog.csdn.net/coder_pig";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        wView = (WebView) findViewById(R.id.wView);
        btn_clear_cache = (Button) findViewById(R.id.btn_clear_cache);
        btn_refresh = (Button) findViewById(R.id.btn_refresh);
        wView.loadUrl(URL);
        wView.setWebViewClient(new WebViewClient() {
            //设置在webView点击打开的新网页在当前界面显示,而不跳转到新的浏览器中
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }
        });
        WebSettings settings = wView.getSettings();
        settings.setJavaScriptEnabled(true);
        //设置缓存模式
        settings.setCacheMode(WebSettings.LOAD_CACHE_ELSE_NETWORK);
        // 开启DOM storage API 功能
        settings.setDomStorageEnabled(true);
        // 开启database storage API功能
        settings.setDatabaseEnabled(true);
        String cacheDirPath = getFilesDir().getAbsolutePath() + APP_CACHE_DIRNAME;
        Log.i("cachePath", cacheDirPath);
        // 设置数据库缓存路径
        settings.setAppCachePath(cacheDirPath);
        settings.setAppCacheEnabled(true);
        Log.i("databasepath", settings.getDatabasePath());

        btn_clear_cache.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                wView.clearCache(true);
            }
        });

        btn_refresh.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                wView.reload();
            }
        });
    }

    //重写回退按钮的点击事件
    @Override
    public void onBackPressed() {
        if(wView.canGoBack()){
            wView.goBack();
        }else{
            super.onBackPressed();
        }
    }
}
```
