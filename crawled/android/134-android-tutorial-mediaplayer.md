# 9.2 MediaPlayer播放音频与视频

> 来源: https://www.runoob.com/w3cnote/android-tutorial-mediaplayer.html

## 代码块 1

```java
MediaPlayer mp = new MediaPlayer();
MediaPlayer mp = MediaPlayer.create(this, R.raw.test);  //无需再调用setDataSource
```

## 代码块 2

```java
//①raw下的资源：
MediaPlayer.create(this, R.raw.test);

//②本地文件路径：
mp.setDataSource("/sdcard/test.mp3");

//③网络URL文件：
mp.setDataSource("http://www.xxx.com/music/test.mp3");
```

## 代码块 3

```java
AssetFileDescriptor fileDescriptor = getAssets().openFd("rain.mp3");
m_mediaPlayer.setDataSource(fileDescriptor.getFileDescriptor(),fileDescriptor.getStartOffset(), fileDescriptor.getLength());
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Button btn_play;
    private Button btn_pause;
    private Button btn_stop;
    private MediaPlayer mPlayer = null;
    private boolean isRelease = true;   //判断是否MediaPlayer是否释放的标志

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        btn_play = (Button) findViewById(R.id.btn_play);
        btn_pause = (Button) findViewById(R.id.btn_pause);
        btn_stop = (Button) findViewById(R.id.btn_stop);

        btn_play.setOnClickListener(this);
        btn_pause.setOnClickListener(this);
        btn_stop.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_play:
                if(isRelease){
                    mPlayer = MediaPlayer.create(this,R.raw.fly);
                    isRelease = false;
                }
                mPlayer.start();   //开始播放
                btn_play.setEnabled(false);
                btn_pause.setEnabled(true);
                btn_stop.setEnabled(true);
                break;
            case R.id.btn_pause:
                mPlayer.pause();     //停止播放
                btn_play.setEnabled(true);
                btn_pause.setEnabled(false);
                btn_stop.setEnabled(false);
                break;
            case R.id.btn_stop:
                mPlayer.reset();     //重置MediaPlayer
                mPlayer.release();   //释放MediaPlayer
                isRelease = true;
                btn_play.setEnabled(true);
                btn_pause.setEnabled(false);
                btn_stop.setEnabled(false);
                break;
        }
    }
}
```

## 代码块 5

```java
Uri myUri = ....; // initialize Uri here
MediaPlayer mediaPlayer = new MediaPlayer();
mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
mediaPlayer.setDataSource(getApplicationContext(), myUri);
mediaPlayer.prepare();
mediaPlayer.start();
```

## 代码块 6

```java
String url = "http://........"; // your URL here
MediaPlayer mediaPlayer = new MediaPlayer();
mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
mediaPlayer.setDataSource(url);
mediaPlayer.prepare(); // might take long! (for buffering, etc)
mediaPlayer.start();
```

## 代码块 7

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="5dp">

    <SurfaceView
        android:id="@+id/sfv_show"
        android:layout_width="match_parent"
        android:layout_height="300dp" />

    <Button
        android:id="@+id/btn_start"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="开始" />

    <Button
        android:id="@+id/btn_pause"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="暂停 " />

    <Button
        android:id="@+id/btn_stop"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="终止" />

</LinearLayout>
```

## 代码块 8

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener, SurfaceHolder.Callback {

    private MediaPlayer mPlayer = null;
    private SurfaceView sfv_show;
    private SurfaceHolder surfaceHolder;
    private Button btn_start;
    private Button btn_pause;
    private Button btn_stop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        sfv_show = (SurfaceView) findViewById(R.id.sfv_show);
        btn_start = (Button) findViewById(R.id.btn_start);
        btn_pause = (Button) findViewById(R.id.btn_pause);
        btn_stop = (Button) findViewById(R.id.btn_stop);

        btn_start.setOnClickListener(this);
        btn_pause.setOnClickListener(this);
        btn_stop.setOnClickListener(this);

        //初始化SurfaceHolder类，SurfaceView的控制器
        surfaceHolder = sfv_show.getHolder();
        surfaceHolder.addCallback(this);
        surfaceHolder.setFixedSize(320, 220);   //显示的分辨率,不设置为视频默认

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_start:
                mPlayer.start();
                break;
            case R.id.btn_pause:
                mPlayer.pause();
                break;
            case R.id.btn_stop:
                mPlayer.stop();
                break;
        }
    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {
        mPlayer = MediaPlayer.create(MainActivity.this, R.raw.lesson);
        mPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
        mPlayer.setDisplay(surfaceHolder);    //设置显示视频显示在SurfaceView上
    }

    @Override
    public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {}

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {}

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mPlayer.isPlaying()) {
            mPlayer.stop();
        }
        mPlayer.release();
    }
}
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private VideoView videoView;
    private Button btn_start;
    private Button btn_pause;
    private Button btn_stop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        videoView = (VideoView) findViewById(R.id.videoView);
        btn_start = (Button) findViewById(R.id.btn_start);
        btn_pause = (Button) findViewById(R.id.btn_pause);
        btn_stop = (Button) findViewById(R.id.btn_stop);

        btn_start.setOnClickListener(this);
        btn_pause.setOnClickListener(this);
        btn_stop.setOnClickListener(this);

        //根据文件路径播放
        if (Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
            videoView.setVideoPath(Environment.getExternalStorageDirectory() + "/lesson.mp4");
        }

        //读取放在raw目录下的文件
        //videoView.setVideoURI(Uri.parse("android.resource://com.jay.videoviewdemo/" + R.raw.lesson));
        videoView.setMediaController(new MediaController(this));
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_start:
                videoView.start();
                break;
            case R.id.btn_pause:
                videoView.pause();
                break;
            case R.id.btn_stop:
                videoView.stopPlayback();
                break;
        }
    }
}
```
