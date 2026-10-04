# 7.5.3 Android 4.4后WebView的一些注意事项

> 来源: https://www.runoob.com/w3cnote/android-tutorial-webview-attention.html

## 代码块 1

```java
runOnUiThread(newRunnable(){
@Override
publicvoid run(){
   // Code for WebView goes here
   }
});
```

## 代码块 2

```java
// This code is BAD and will block the UI thread
webView.loadUrl("javascript:fn()");
while(result ==null) {
    Thread.sleep(100);
}
```

## 代码块 3

```java
mWebView.evaluateJavascript(script, new ValueCallback<String>() {
 @Override
 public void onReceiveValue(String value) {
      //TODO
 }
});
```

## 代码块 4

```xml
<a href="showProfile">Show Profile</a>
```

## 代码块 5

```xml
<a href="example-app:showProfile">Show Profile</a>
```

## 代码块 6

```java
// The URL scheme should be non-hierarchical (no trailing slashes)
 privatestaticfinalString APP_SCHEME ="example-app:";
 @Override
 publicboolean shouldOverrideUrlLoading(WebView view,String url){
     if(url.startsWith(APP_SCHEME)){
         urlData =URLDecoder.decode(url.substring(APP_SCHEME.length()),"UTF-8");
         respondToData(urlData);
         returntrue;
     }
     returnfalse;
}
```

## 代码块 7

```java
webView.loadDataWithBaseURL("example-app://example.co.uk/", HTML_DATA,null,"UTF-8",null);
```

## 代码块 8

```java
Mozilla/5.0 (Linux; Android 4.4; Nexus 4 Build/KRT16H)
AppleWebKit/537.36(KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0
Mobile Safari/537.36
```

## 代码块 9

```java
mWebView.getSettings().setUserAgentString(ua);
mWebView.getSettings().getUserAgentString();
```

## 代码块 10

```java
class JsObject {
    @JavascriptInterface
    public String toString() { return "injectedObject"; }
}

webView.addJavascriptInterface(new JsObject(), "injectedObject");
webView.loadData("", "text/html", null);
webView.loadUrl("javascript:alert(injectedObject.toString())");
```
