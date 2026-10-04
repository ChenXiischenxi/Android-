# 7.5.6 WebView处理网页返回的错误码信息

> 来源: https://www.runoob.com/w3cnote/android-tutorial-webview-error-code.html

## 代码块 1

```java
wView.setWebViewClient(new WebViewClient() {
//设置在webView点击打开的新网页在当前界面显示,而不跳转到新的浏览器中
@Override
public boolean shouldOverrideUrlLoading(WebView view, String url) {
    view.loadUrl(url);
    return true;
}

@Override
public void onReceivedError(WebView view, int errorCode, String description,
    String failingUrl) {
        super.onReceivedError(view, errorCode, description, failingUrl);
        wView.loadUrl("file:///android_asset/error.html");
    }
});
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private WebView wView;
    private ImageView img_error_back;
    private Button btn_refresh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        wView = (WebView) findViewById(R.id.wView);
        img_error_back = (ImageView) findViewById(R.id.img_error_back);
        btn_refresh = (Button) findViewById(R.id.btn_refresh);
        wView.loadUrl("http://www.baidu.com");
        wView.setWebViewClient(new WebViewClient() {
            //设置在webView点击打开的新网页在当前界面显示,而不跳转到新的浏览器中
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }

            @Override
            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                super.onReceivedError(view, errorCode, description, failingUrl);
                wView.setVisibility(View.GONE);
                img_error_back.setVisibility(View.VISIBLE);
            }
        });
        btn_refresh.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        wView.loadUrl("http://www.baidu.com");
        img_error_back.setVisibility(View.GONE);
        wView.setVisibility(View.VISIBLE);
    }
}
```
