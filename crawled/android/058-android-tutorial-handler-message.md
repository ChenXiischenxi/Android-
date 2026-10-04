# 3.3 Handler消息传递机制浅析

> 来源: https://www.runoob.com/w3cnote/android-tutorial-handler-message.html

## 代码块 1

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/RelativeLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    tools:context="com.jay.example.handlerdemo1.MainActivity" >

    <ImageView
        android:id="@+id/imgchange"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true" />

</RelativeLayout>
```

## 代码块 2

```java
public class MainActivity extends Activity {

    //定义切换的图片的数组id
    int imgids[] = new int[]{
        R.drawable.s_1, R.drawable.s_2,R.drawable.s_3,
        R.drawable.s_4,R.drawable.s_5,R.drawable.s_6,
        R.drawable.s_7,R.drawable.s_8
    };
    int imgstart = 0;

    final Handler myHandler = new Handler()
    {
      @Override
      //重写handleMessage方法,根据msg中what的值判断是否执行后续操作
      public void handleMessage(Message msg) {
        if(msg.what == 0x123)
           {
            imgchange.setImageResource(imgids[imgstart++ % 8]);
           }
        }
    };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final ImageView imgchange = (ImageView) findViewById(R.id.imgchange);

        //使用定时器,每隔200毫秒让handler发送一个空信息
        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                myHandler.sendEmptyMessage(0x123);

            }
        }, 0,200);
    }

}
```

## 代码块 3

```xml
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    <EditText
        android:id="@+id/etNum"
        android:inputType="number"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="请输入上限"/>
    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="cal"
        android:text="计算"/>
</LinearLayout>
```

## 代码块 4

```java
public class CalPrime extends Activity
{
    static final String UPPER_NUM = "upper";
    EditText etNum;
    CalThread calThread;
    // 定义一个线程类
    class CalThread extends Thread
    {
        public Handler mHandler;

        public void run()
        {
            Looper.prepare();
            mHandler = new Handler()
            {
                // 定义处理消息的方法
                @Override
                public void handleMessage(Message msg)
                {
                    if(msg.what == 0x123)
                    {
                        int upper = msg.getData().getInt(UPPER_NUM);
                        List<Integer> nums = new ArrayList<Integer>();
                        // 计算从2开始、到upper的所有质数
                        outer:
                        for (int i = 2 ; i <= upper ; i++)
                        {
                            // 用i处于从2开始、到i的平方根的所有数
                            for (int j = 2 ; j <= Math.sqrt(i) ; j++)
                            {
                                // 如果可以整除，表明这个数不是质数
                                if(i != 2 && i % j == 0)
                                {
                                    continue outer;
                                }
                            }
                            nums.add(i);
                        }
                        // 使用Toast显示统计出来的所有质数
                        Toast.makeText(CalPrime.this , nums.toString()
                            , Toast.LENGTH_LONG).show();
                    }
                }
            };
            Looper.loop();
        }
    }
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        etNum = (EditText)findViewById(R.id.etNum);
        calThread = new CalThread();
        // 启动新线程
        calThread.start();
    }
    // 为按钮的点击事件提供事件处理函数
    public void cal(View source)
    {
        // 创建消息
        Message msg = new Message();
        msg.what = 0x123;
        Bundle bundle = new Bundle();
        bundle.putInt(UPPER_NUM ,
            Integer.parseInt(etNum.getText().toString()));
        msg.setData(bundle);
        // 向新线程中的Handler发送消息
        calThread.mHandler.sendMessage(msg);
    }
}
```
