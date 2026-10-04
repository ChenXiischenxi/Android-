# 10.7 WindowManager(窗口管理服务)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-windowmanager.html

## 代码块 1

```java
WindowManager wManager = getApplicationContext().getSystemService(Context. WINDOW_ SERVICE);
```

## 代码块 2

```java
WindowManager.LayoutParams wmParams=new WindowManager.LayoutParams();
```

## 代码块 3

```java
public static int[] getScreenHW(Context context) {
    WindowManager manager = (WindowManager)context
    .getSystemService(Context.WINDOW_SERVICE);
    Display display = manager.getDefaultDisplay();
    int width = display.getWidth();
    int height = display.getHeight();
    int[] HW = new int[] { width, height };
    return HW;
}
```

## 代码块 4

```java
public static int[] getScreenHW2(Context context) {
    WindowManager manager = (WindowManager) context.
    getSystemService(Context.WINDOW_SERVICE);
    DisplayMetrics dm = new DisplayMetrics();
    manager.getDefaultDisplay().getMetrics(dm);
    int width = dm.widthPixels;
    int height = dm.heightPixels;
    int[] HW = new int[] { width, height };
    return HW;
}
```

## 代码块 5

```java
public static int getScreenW(Context context) {
    return getScreenHW2(context)[0];
}

public static int getScreenH(Context context) {
    return getScreenHW2(context)[1];
}
```

## 代码块 6

```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        WindowManager wManager = (WindowManager) getSystemService(Context.WINDOW_SERVICE);
        DisplayMetrics dm = new DisplayMetrics();
        wManager.getDefaultDisplay().getMetrics(dm);
        Toast.makeText(MainActivity.this, "当前手机的屏幕宽高：" + dm.widthPixels + "*" +
                dm.heightPixels, Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 7

```java
getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getSupportActionBar().hide();
```

## 代码块 8

```java
public void setKeepScreenOn(Activity activity,boolean keepScreenOn)
{
    if(keepScreenOn)
    {
        activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
    }else{
        activity.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
    }
}
```

## 代码块 9

```java
private void createWindowView() {
    btnView = new Button(getApplicationContext());
    btnView.setBackgroundResource(R.mipmap.ic_launcher);
    windowManager = (WindowManager) getApplicationContext()
            .getSystemService(Context.WINDOW_SERVICE);
    params = new WindowManager.LayoutParams();

    // 设置Window Type
    params.type = WindowManager.LayoutParams.TYPE_SYSTEM_ALERT;
    // 设置悬浮框不可触摸
    params.flags = WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
            | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE;
    // 悬浮窗不可触摸，不接受任何事件,同时不影响后面的事件响应
    params.format = PixelFormat.RGBA_8888;
    // 设置悬浮框的宽高
    params.width = 200;
    params.height = 200;
    params.gravity = Gravity.LEFT;
    params.x = 200;
    params.y = 000;
    // 设置悬浮框的Touch监听
    btnView.setOnTouchListener(new View.OnTouchListener() {
        //保存悬浮框最后位置的变量
        int lastX, lastY;
        int paramX, paramY;

        @Override
        public boolean onTouch(View v, MotionEvent event) {
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    lastX = (int) event.getRawX();
                    lastY = (int) event.getRawY();
                    paramX = params.x;
                    paramY = params.y;
                    break;
                case MotionEvent.ACTION_MOVE:
                    int dx = (int) event.getRawX() - lastX;
                    int dy = (int) event.getRawY() - lastY;
                    params.x = paramX + dx;
                    params.y = paramY + dy;
                    // 更新悬浮窗位置
                    windowManager.updateViewLayout(btnView, params);
                    break;
            }
            return true;
        }
    });
    windowManager.addView(btnView, params);
    isAdded = true;
}
```

## 代码块 10

```java
/**
 * 判断当前界面是否是桌面
 */
public boolean isHome(){
    if(mActivityManager == null) {
        mActivityManager = (ActivityManager)getSystemService(Context.ACTIVITY_SERVICE);
    }
    List<RunningTaskInfo> rti = mActivityManager.getRunningTasks(1);
    return homeList.contains(rti.get(0).topActivity.getPackageName());
}

/**
 * 获得属于桌面的应用的应用包名称
 * @return 返回包含所有包名的字符串列表
 */
private List<String> getHomes() {
    List<String> names = new ArrayList<String>();
    PackageManager packageManager = this.getPackageManager();
    // 属性
    Intent intent = new Intent(Intent.ACTION_MAIN);
    intent.addCategory(Intent.CATEGORY_HOME);
    List<ResolveInfo> resolveInfo = packageManager.queryIntentActivities(intent,
            PackageManager.MATCH_DEFAULT_ONLY);
    for(ResolveInfo ri : resolveInfo) {
        names.add(ri.activityInfo.packageName);
    }
    return names;
}
```

## 代码块 11

```java
//定义一个更新界面的Handler
private Handler mHandler = new Handler() {
    @Override
    public void handleMessage(Message msg) {
        switch(msg.what) {
        case HANDLE_CHECK_ACTIVITY:
            if(isHome()) {
                if(!isAdded) {
                    windowManager.addView(btnView, params);
                    isAdded = true;
                new Thread(new Runnable() {
                    public void run() {
                        for(int i=0;i<10;i++){
                            try {
                                Thread.sleep(1000);
                            } catch (InterruptedException e) {e.printStackTrace();}
                            Message m = new Message();
                            m.what=2;
                            mHandler.sendMessage(m);
                        }
                    }
                }).start();}
            } else {
                if(isAdded) {
                    windowManager.removeView(btnView);
                    isAdded = false;
                }
            }
            mHandler.sendEmptyMessageDelayed(HANDLE_CHECK_ACTIVITY, 0);
            break;
        }
    }
};
```

## 代码块 12

```java
@Override
public int onStartCommand(Intent intent, int flags, int startId) {
    int operation = intent.getIntExtra(OPERATION, OPERATION_SHOW);
    switch(operation) {
    case OPERATION_SHOW:
        mHandler.removeMessages(HANDLE_CHECK_ACTIVITY);
        mHandler.sendEmptyMessage(HANDLE_CHECK_ACTIVITY);
        break;
    case OPERATION_HIDE:
        mHandler.removeMessages(HANDLE_CHECK_ACTIVITY);
        break;
    }
    return super.onStartCommand(intent, flags, startId);
}
```

## 代码块 13

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_on;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }

    private void bindViews() {
        btn_on = (Button) findViewById(R.id.btn_on);
        btn_on.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_on:
                Intent mIntent = new Intent(MainActivity.this, MainService.class);
                mIntent.putExtra(MainService.OPERATION, MainService.OPERATION_SHOW);
                startService(mIntent);
                Toast.makeText(MainActivity.this, "悬浮框已开启~", Toast.LENGTH_SHORT).show();
                break;
        }
    }
}
```

## 代码块 14

```xml
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
<uses-permission android:name="android.permission.GET_TASKS" />

<service android:name=".MainService"/>
```
