# 7.5.1 WebView(网页视图)基本用法

> 来源: https://www.runoob.com/w3cnote/android-tutorial-webview.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {

    private WebView webView;
    private long exitTime = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        webView = new WebView(this);
        webView.setWebViewClient(new WebViewClient() {
            //设置在webView点击打开的新网页在当前界面显示,而不跳转到新的浏览器中
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }
        });
        webView.getSettings().setJavaScriptEnabled(true);  //设置WebView属性,运行执行js脚本
        webView.loadUrl("http://www.baidu.com/");          //调用loadUrl方法为WebView加入链接
        setContentView(webView);                           //调用Activity提供的setContentView将webView显示出来
    }


    //我们需要重写回退按钮的时间,当用户点击回退按钮：
    //1.webView.canGoBack()判断网页是否能后退,可以则goback()
    //2.如果不可以连续点击两次退出App,否则弹出提示Toast
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            if ((System.currentTimeMillis() - exitTime) > 2000) {
                Toast.makeText(getApplicationContext(), "再按一次退出程序",
                        Toast.LENGTH_SHORT).show();
                exitTime = System.currentTimeMillis();
            } else {
                super.onBackPressed();
            }

        }
    }
}
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {


    private Button btn_back;
    private TextView txt_title;
    private Button btn_top;
    private Button btn_refresh;
    private WebView wView;
    private long exitTime = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }


    private void bindViews() {
        btn_back = (Button) findViewById(R.id.btn_back);
        txt_title = (TextView) findViewById(R.id.txt_title);
        btn_top = (Button) findViewById(R.id.btn_top);
        btn_refresh = (Button) findViewById(R.id.btn_refresh);
        wView = (WebView) findViewById(R.id.wView);

        btn_back.setOnClickListener(this);
        btn_refresh.setOnClickListener(this);
        btn_top.setOnClickListener(this);

        wView.loadUrl("http://www.baidu.com");
        wView.setWebChromeClient(new WebChromeClient() {
            //这里设置获取到的网站title
            @Override
            public void onReceivedTitle(WebView view, String title) {
                super.onReceivedTitle(view, title);
                txt_title.setText(title);
            }
        });


        wView.setWebViewClient(new WebViewClient() {
            //在webview里打开新链接
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }
        });
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_back:
                finish();          //关闭当前Activity
                break;
            case R.id.btn_refresh:
                wView.reload();    //刷新当前页面
                break;
            case R.id.btn_top:
                wView.setScrollY(0);   //滚动到顶部
                break;
        }
    }

    @Override
    public void onBackPressed() {
        if (wView.canGoBack()) {
            wView.goBack();
        } else {
            if ((System.currentTimeMillis() - exitTime) > 2000) {
                Toast.makeText(getApplicationContext(), "再按一次退出程序",
                        Toast.LENGTH_SHORT).show();
                exitTime = System.currentTimeMillis();
            } else {
                finish();
            }

        }
    }
}
```

## 代码块 3

```java
/**
 * Created by Jay on 2015/9/11 0011.
 */
public class MyWebView extends WebView {

    private OnScrollChangedCallback mOnScrollChangedCallback;

    public MyWebView(Context context) {
        super(context);
    }

    public MyWebView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public MyWebView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    @Override
    protected void onScrollChanged(int l, int t, int oldl, int oldt) {
        super.onScrollChanged(l, t, oldl, oldt);
        if (mOnScrollChangedCallback != null) {
            mOnScrollChangedCallback.onScroll(l - oldl, t - oldt);
        }
    }

    public OnScrollChangedCallback getOnScrollChangedCallback() {
        return mOnScrollChangedCallback;
    }

    public void setOnScrollChangedCallback(
            final OnScrollChangedCallback onScrollChangedCallback) {
        mOnScrollChangedCallback = onScrollChangedCallback;
    }

    public static interface OnScrollChangedCallback {
        //这里的dx和dy代表的是x轴和y轴上的偏移量，你也可以自己把l, t, oldl, oldt四个参数暴露出来
        public void onScroll(int dx, int dy);
    }

}
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity {

    private MyWebView wView;
    private Button btn_icon;
    private long exitTime = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn_icon = (Button) findViewById(R.id.btn_icon);
        wView = (MyWebView) findViewById(R.id.wView);
        wView.loadUrl("http://www.hao123.com");
        wView.setWebViewClient(new WebViewClient() {
            //在webview里打开新链接
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }
        });

        //比如这里做一个简单的判断，当页面发生滚动，显示那个Button
        wView.setOnScrollChangedCallback(new MyWebView.OnScrollChangedCallback() {
            @Override
            public void onScroll(int dx, int dy) {
                if (dy > 0) {
                    btn_icon.setVisibility(View.VISIBLE);
                } else {
                    btn_icon.setVisibility(View.GONE);
                }
            }
        });

        btn_icon.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                wView.setScrollY(0);
                btn_icon.setVisibility(View.GONE);
            }
        });

    }

    @Override
    public void onBackPressed() {
        if (wView.canGoBack()) {
            wView.goBack();
        } else {
            if ((System.currentTimeMillis() - exitTime) > 2000) {
                Toast.makeText(getApplicationContext(), "再按一次退出程序",
                        Toast.LENGTH_SHORT).show();
                exitTime = System.currentTimeMillis();
            } else {
                finish();
            }

        }
    }
}
```

## 代码块 5

```java
WebSettings settings = wView.getSettings();
settings.setUseWideViewPort(true);//设定支持viewport
settings.setLoadWithOverviewMode(true);   //自适应屏幕
settings.setBuiltInZoomControls(true);
settings.setDisplayZoomControls(false);
settings.setSupportZoom(true);//设定支持缩放
```

## 代码块 6

```java
settings.setDisplayZoomControls(false);
```

## 代码块 7

```java
wView.setInitialScale(25);//为25%，最小缩放等级
```

## 代码块 8

```java
settings.setTextZoom(int)；
```

## 代码块 9

```java
settings.setTextSize(TextSize.LARGER)；
```

## 代码块 10

```java
@Override
public void onPageFinished(WebView view, String url) {
    CookieManager cookieManager = CookieManager.getInstance();
    String CookieStr = cookieManager.getCookie(url);
    Log.e("HEHE", "Cookies = " + CookieStr);
    super.onPageFinished(view, url);
}
```

## 代码块 11

```java
CookieSyncManager.createInstance(MainActivity.this);
CookieManager cookieManager = CookieManager.getInstance();
cookieManager.setAcceptCookie(true);
cookieManager.setCookie(url, cookies);  //cookies是要设置的cookie字符串
CookieSyncManager.getInstance().sync();
```
