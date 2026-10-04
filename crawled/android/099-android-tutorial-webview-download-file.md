# 7.5.4 WebView文件下载

> 来源: https://www.runoob.com/w3cnote/android-tutorial-webview-download-file.html

## 代码块 1

```java
wView.setDownloadListener(new DownloadListener(){
@Override
public void onDownloadStart(String url, String userAgent, String contentDisposition,
    String mimetype, long contentLength) {
        Log.e("HEHE","开始下载");
        Uri uri = Uri.parse(url);
        Intent intent = new Intent(Intent.ACTION_VIEW,uri);
        startActivity(intent);
    }
});
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/9/14 0014.
 */
public class DownLoadThread implements Runnable {

    private String dlUrl;

    public DownLoadThread(String dlUrl) {
        this.dlUrl = dlUrl;
    }

    @Override
    public void run() {
        Log.e("HEHE", "开始下载~~~~~");
        InputStream in = null;
        FileOutputStream fout = null;
        try {
            URL httpUrl = new URL(dlUrl);
            HttpURLConnection conn = (HttpURLConnection) httpUrl.openConnection();
            conn.setDoInput(true);
            conn.setDoOutput(true);
            in = conn.getInputStream();
            File downloadFile, sdFile;
            if (Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
                Log.e("HEHE","SD卡可写");
                downloadFile = Environment.getExternalStorageDirectory();
                sdFile = new File(downloadFile, "csdn_client.apk");
                fout = new FileOutputStream(sdFile);
            }else{
                Log.e("HEHE","SD卡不存在或者不可读写");
            }
            byte[] buffer = new byte[1024];
            int len;
            while ((len = in.read(buffer)) != -1) {
                fout.write(buffer, 0, len);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (fout != null) {
                try {
                    fout.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        Log.e("HEHE", "下载完毕~~~~");
    }
}
```

## 代码块 3

```java
wView.setDownloadListener(new DownloadListener(){
    @Override
    public void onDownloadStart(String url, String userAgent, String contentDisposition,
    String mimetype, long contentLength) {
            Log.e("HEHE","onDownloadStart被调用：下载链接：" + url);
            new Thread(new DownLoadThread(url)).start();
    }
});
```

## 代码块 4

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<!-- 在SDCard中创建与删除文件权限 -->
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
<!-- 往SDCard写入数据权限 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```
