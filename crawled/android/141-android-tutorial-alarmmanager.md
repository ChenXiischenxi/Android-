# 10.5 AlarmManager(闹钟服务)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-alarmmanager.html

## 代码块 1

```java
AlarmManager alarmManager = (AlarmManager) getSystemService(ALARM_SERVICE);
```

## 代码块 2

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/btn_set"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="设置闹钟" />

    <Button
        android:id="@+id/btn_cancel"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="关闭闹钟"
        android:visibility="gone" />

</LinearLayout>
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Button btn_set;
    private Button btn_cancel;
    private AlarmManager alarmManager;
    private PendingIntent pi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        btn_set = (Button) findViewById(R.id.btn_set);
        btn_cancel = (Button) findViewById(R.id.btn_cancel);
        alarmManager = (AlarmManager) getSystemService(ALARM_SERVICE);

        Intent intent = new Intent(MainActivity.this, ClockActivity.class);
        pi = PendingIntent.getActivity(MainActivity.this, 0, intent, 0);

        btn_set.setOnClickListener(this);
        btn_cancel.setOnClickListener(this);

    }


    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btn_set:
                Calendar currentTime = Calendar.getInstance();
                new TimePickerDialog(MainActivity.this, 0,
                        new TimePickerDialog.OnTimeSetListener() {
                            @Override
                            public void onTimeSet(TimePicker view,
                                                  int hourOfDay, int minute) {
                                //设置当前时间
                                Calendar c = Calendar.getInstance();
                                c.setTimeInMillis(System.currentTimeMillis());
                                // 根据用户选择的时间来设置Calendar对象
                                c.set(Calendar.HOUR, hourOfDay);
                                c.set(Calendar.MINUTE, minute);
                                // ②设置AlarmManager在Calendar对应的时间启动Activity
                                alarmManager.set(AlarmManager.RTC_WAKEUP, c.getTimeInMillis(), pi);
                                Log.e("HEHE",c.getTimeInMillis()+"");   //这里的时间是一个unix时间戳
                                // 提示闹钟设置完毕:
                                Toast.makeText(MainActivity.this, "闹钟设置完毕~"+ c.getTimeInMillis(),
                                        Toast.LENGTH_SHORT).show();
                            }
                        }, currentTime.get(Calendar.HOUR_OF_DAY), currentTime
                        .get(Calendar.MINUTE), false).show();
                btn_cancel.setVisibility(View.VISIBLE);
                break;
            case R.id.btn_cancel:
                alarmManager.cancel(pi);
                btn_cancel.setVisibility(View.GONE);
                Toast.makeText(MainActivity.this, "闹钟已取消", Toast.LENGTH_SHORT)
                        .show();
                break;
        }
    }
}
```

## 代码块 4

```java
/**
 * Created by Jay on 2015/10/25 0025.
 */
public class ClockActivity extends AppCompatActivity {

    private MediaPlayer mediaPlayer;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_clock);
        mediaPlayer = mediaPlayer.create(this,R.raw.pig);
        mediaPlayer.start();
        //创建一个闹钟提醒的对话框,点击确定关闭铃声与页面
        new AlertDialog.Builder(ClockActivity.this).setTitle("闹钟").setMessage("小猪小猪快起床~")
                .setPositiveButton("关闭闹铃", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        mediaPlayer.stop();
                        ClockActivity.this.finish();
                    }
                }).show();
    }
}
```
