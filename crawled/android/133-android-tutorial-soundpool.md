# 9.1 使用SoundPool播放音效(Duang~)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-soundpool.html

## 代码块 1

```java
SoundPool.Builder spb = new SoundPool.Builder();
spb.setMaxStreams(10);
spb.setAudioAttributes(null);    //转换音频格式
SoundPool sp = spb.build();      //创建SoundPool对象
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Button btn_play1;
    private Button btn_play2;
    private Button btn_play3;
    private Button btn_play4;
    private Button btn_play5;
    private Button btn_release;
    private AssetManager aManager;
    private SoundPool mSoundPool = null;
    private HashMap<Integer, Integer> soundID = new HashMap<Integer, Integer>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        aManager = getAssets();
        try {
            initSP();
        } catch (Exception e) {
            e.printStackTrace();
        }
        bindViews();
    }

    private void bindViews() {
        btn_play1 = (Button) findViewById(R.id.btn_play1);
        btn_play2 = (Button) findViewById(R.id.btn_play2);
        btn_play3 = (Button) findViewById(R.id.btn_play3);
        btn_play4 = (Button) findViewById(R.id.btn_play4);
        btn_play5 = (Button) findViewById(R.id.btn_play5);
        btn_release = (Button) findViewById(R.id.btn_release);

        btn_play1.setOnClickListener(this);
        btn_play2.setOnClickListener(this);
        btn_play3.setOnClickListener(this);
        btn_play4.setOnClickListener(this);
        btn_play5.setOnClickListener(this);
        btn_release.setOnClickListener(this);

    }

    private void initSP() throws Exception{
        //设置最多可容纳5个音频流，音频的品质为5
        mSoundPool = new SoundPool(5, AudioManager.STREAM_SYSTEM, 5);
        soundID.put(1, mSoundPool.load(this, R.raw.duang, 1));
        soundID.put(2 , mSoundPool.load(getAssets().openFd("biaobiao.mp3") , 1));  //需要捕获IO异常
        soundID.put(3, mSoundPool.load(this, R.raw.duang, 1));
        soundID.put(4, mSoundPool.load(this, R.raw.duang, 1));
        soundID.put(5, mSoundPool.load(this, R.raw.duang, 1));
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_play1:
                mSoundPool.play(soundID.get(1), 1, 1, 0, 0, 1);
                break;
            case R.id.btn_play2:
                mSoundPool.play(soundID.get(2), 1, 1, 0, 0, 1);
                break;
            case R.id.btn_play3:
                mSoundPool.play(soundID.get(3), 1, 1, 0, 0, 1);
                break;
            case R.id.btn_play4:
                mSoundPool.play(soundID.get(4), 1, 1, 0, 0, 1);
                break;
            case R.id.btn_play5:
                mSoundPool.play(soundID.get(5), 1, 1, 0, 0, 1);
                break;
            case R.id.btn_release:
                mSoundPool.release();   //回收SoundPool资源
                break;
        }
    }
}
```

## 代码块 3

```java
mSoundPool.setOnLoadCompleteListener(new SoundPool.OnLoadCompleteListener() {
    @Override
    public void onLoadComplete(SoundPool soundPool, int sampleId, int status) {
        Toast.makeText(MainActivity.this,"加特技准备完毕~",Toast.LENGTH_SHORT).show();
    }
});
```
