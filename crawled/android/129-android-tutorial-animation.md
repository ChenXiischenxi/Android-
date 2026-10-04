# 8.4.1 Android动画合集之帧动画

> 来源: https://www.runoob.com/w3cnote/android-tutorial-animation.html

## 代码块 1

```xml
<?xml version="1.0" encoding="utf-8"?>
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="false">
    <item
        android:drawable="@mipmap/img_miao1"
        android:duration="80" />
    <item
        android:drawable="@mipmap/img_miao2"
        android:duration="80" />
    <item
        android:drawable="@mipmap/img_miao3"
        android:duration="80" />
    <!--限于篇幅，省略其他item，自己补上-->
    ...
</animation-list>
```

## 代码块 2

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_start"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="开始" />

    <Button
        android:id="@+id/btn_stop"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="停止" />

    <ImageView
        android:id="@+id/img_show"
        android:layout_width="120dp"
        android:layout_height="120dp"
        android:layout_gravity="center"
        android:background="@anim/miao_gif" />

</LinearLayout>
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_start;
    private Button btn_stop;
    private ImageView img_show;
    private AnimationDrawable anim;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
        anim = (AnimationDrawable) img_show.getBackground();
    }

    private void bindViews() {
        btn_start = (Button) findViewById(R.id.btn_start);
        btn_stop = (Button) findViewById(R.id.btn_stop);
        img_show = (ImageView) findViewById(R.id.img_show);
        btn_start.setOnClickListener(this);
        btn_stop.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_start:
                anim.start();
                break;
            case R.id.btn_stop:
                anim.stop();
                break;
        }
    }
}
```

## 代码块 4

```xml
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="true">
    <item
        android:drawable="@mipmap/img_zhuan1"
        android:duration="80" />
    <item
        android:drawable="@mipmap/img_zhuan2"
        android:duration="80" />
    <item
        android:drawable="@mipmap/img_zhuan3"
        android:duration="80" />
     <!--限于篇幅，省略其他item，自己补上-->
    ...
</animation-list>
```

## 代码块 5

```java
/**
 * Created by Jay on 2015/11/15 0015.
 */
public class FrameView extends ImageView {

    private AnimationDrawable anim;

    public FrameView(Context context) {
        super(context);
    }

    public FrameView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public FrameView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    public void setAnim(AnimationDrawable anim){
        this.anim = anim;
    }

    public void setLocation(int top,int left){
        this.setFrame(left,top,left + 200,top + 200);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        try{
            //反射调用AnimationDrawable里的mCurFrame值
            Field field = AnimationDrawable.class
                    .getDeclaredField("mCurFrame");
            field.setAccessible(true);
            int curFrame = field.getInt(anim);// 获取anim动画的当前帧
            if (curFrame == anim.getNumberOfFrames() - 1)// 如果已经到了最后一帧
            {
                //让该View隐藏
                setVisibility(View.INVISIBLE);
            }
        }catch (Exception e){e.printStackTrace();}
        super.onDraw(canvas);
    }
}
```

## 代码块 6

```java
public class MainActivity extends AppCompatActivity {

    private FrameView fView;
    private AnimationDrawable anim = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        FrameLayout fly = new FrameLayout(this);
        setContentView(fly);
        fView = new FrameView(this);
        fView.setBackgroundResource(R.anim.anim_zhuan);
        fView.setVisibility(View.INVISIBLE);
        anim = (AnimationDrawable) fView.getBackground();
        fView.setAnim(anim);
        fly.addView(fView);
        fly.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                //设置按下时才产生动画效果
                if(event.getAction() == MotionEvent.ACTION_DOWN){
                    anim.stop();
                    float x = event.getX();
                    float y = event.getY();
                    fView.setLocation((int) y - 40,(int)x-20);  //View显示的位置
                    fView.setVisibility(View.VISIBLE);
                    anim.start();    //开启动画
                }
                return false;
            }
        });
    }
}
```
