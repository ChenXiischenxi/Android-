# 10.3 AudioManager(音频管理器)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-audiomanager.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_start"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="播放" />

    <Button
        android:id="@+id/btn_stop"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:enabled="false"
        android:text="停止" />

    <Button
        android:id="@+id/btn_higher"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="调高音量" />

    <Button
        android:id="@+id/btn_lower"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="调低音量" />

    <Button
        android:id="@+id/btn_quite"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="静音" />

</LinearLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_start;
    private Button btn_stop;
    private Button btn_higher;
    private Button btn_lower;
    private Button btn_quite;
    private MediaPlayer mePlayer;
    private AudioManager aManager;
    //定义一个标志用来标示是否点击了静音按钮
    private int flag = 1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //获得系统的音频对象
        aManager = (AudioManager) getSystemService(Service.AUDIO_SERVICE);
        //初始化mediaplayer对象,这里播放的是raw文件中的mp3资源
        mePlayer = MediaPlayer.create(MainActivity.this, R.raw.countingstars);
        //设置循环播放:
        mePlayer.setLooping(true);
        bindViews();
    }

    private void bindViews() {
        btn_start = (Button) findViewById(R.id.btn_start);
        btn_stop = (Button) findViewById(R.id.btn_stop);
        btn_higher = (Button) findViewById(R.id.btn_higher);
        btn_lower = (Button) findViewById(R.id.btn_lower);
        btn_quite = (Button) findViewById(R.id.btn_quite);

        btn_start.setOnClickListener(this);
        btn_stop.setOnClickListener(this);
        btn_higher.setOnClickListener(this);
        btn_lower.setOnClickListener(this);
        btn_quite.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_start:
                btn_stop.setEnabled(true);
                mePlayer.start();
                btn_start.setEnabled(false);
                break;
            case R.id.btn_stop:
                btn_start.setEnabled(true);
                mePlayer.pause();
                btn_stop.setEnabled(false);
                break;
            case R.id.btn_higher:
                // 指定调节音乐的音频，增大音量，而且显示音量图形示意
                aManager.adjustStreamVolume(AudioManager.STREAM_MUSIC,
                        AudioManager.ADJUST_RAISE, AudioManager.FLAG_SHOW_UI);
                break;
            case R.id.btn_lower:
                // 指定调节音乐的音频，降低音量，只有声音,不显示图形条
                aManager.adjustStreamVolume(AudioManager.STREAM_MUSIC,
                        AudioManager.ADJUST_LOWER, AudioManager.FLAG_PLAY_SOUND);
                break;
            case R.id.btn_quite:
                // 指定调节音乐的音频，根据isChecked确定是否需要静音
                flag *= -1;
                if (flag == -1) {
                    aManager.setStreamMute(AudioManager.STREAM_MUSIC, true);   //API 23过期- -
//                    aManager.adjustStreamVolume(AudioManager.STREAM_MUSIC, AudioManager.ADJUST_MUTE,
//                            AudioManager.FLAG_SHOW_UI);   //23以后的版本用这个
                    btn_quite.setText("取消静音");
                } else {
                    aManager.setStreamMute(AudioManager.STREAM_MUSIC, false);//API 23过期- -
//                    aManager.adjustStreamVolume(AudioManager.STREAM_MUSIC, AudioManager.ADJUST_UNMUTE,
//                            AudioManager.FLAG_SHOW_UI);  //23以后的版本用这个
                    aManager.setMicrophoneMute(false);
                    btn_quite.setText("静音");
                }
                break;
        }
    }
}
```

## 代码块 3

```xml
<**uses-permission android:name="android.permission.VIBRATE"**/>
```
