# 4.1.2 Activity初窥门径

> 来源: https://www.runoob.com/w3cnote/android-tutorial-activity-start.html

## 代码块 1

```java
public class ActivityCollector {
    public static LinkedList<Activity> activities = new LinkedList<Activity>();
    public static void addActivity(Activity activity)
    {
        activities.add(activity);
    }
    public static void removeActivity(Activity activity)
    {
        activities.remove(activity);
    }
    public static void finishAll()
    {
        for(Activity activity:activities)
        {
            if(!activity.isFinishing())
            {
                activity.finish();
            }
        }
    }
}
```

## 代码块 2

```java
/**
 * 退出应用程序
 */
public void AppExit(Context context) {
    try {
        ActivityCollector.finishAll();
        ActivityManager activityMgr = (ActivityManager) context
                .getSystemService(Context.ACTIVITY_SERVICE);
        activityMgr.killBackgroundProcesses(context.getPackageName());
        System.exit(0);
    } catch (Exception ignored) {}
}
```

## 代码块 3

```java
// 定义一个变量，来标识是否退出
private static boolean isExit = false;
Handler mHandler = new Handler() {
    @Override
    public void handleMessage(Message msg) {
        super.handleMessage(msg);
        isExit = false;
    }
};

public boolean onKeyDown(int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_BACK) {
        if (!isExit) {
            isExit = true;
            Toast.makeText(getApplicationContext(), "再按一次退出程序",
                    Toast.LENGTH_SHORT).show();
            // 利用handler延迟发送更改状态信息
            mHandler.sendEmptyMessageDelayed(0, 2000);
        } else {
            exit(this);
        }
        return false;
    }
return super.onKeyDown(keyCode, event);}
```

## 代码块 4

```java
//保存点击的时间
private long exitTime = 0;
public boolean onKeyDown(int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_BACK) {
        if ((System.currentTimeMillis() - exitTime) > 2000) {
            Toast.makeText(getApplicationContext(), "再按一次退出程序",
                    Toast.LENGTH_SHORT).show();
            exitTime = System.currentTimeMillis();
        } else {
                        exit();
                      }
        return false;
    }
        return super.onKeyDown(keyCode, event);
}
```

## 代码块 5

```xml
<!-- 默认Activity跳转动画 -->
<style name="default_animation" mce_bogus="1" parent="@android:style/Animation.Activity">
    <item name="android:activityOpenEnterAnimation">@anim/default_anim_in</item>
    <item name="android:activityOpenExitAnimation">@anim/anim_stay</item>
    <item name="android:activityCloseEnterAnimation">@anim/anim_stay</item>
    <item name="android:activityCloseExitAnimation">@anim/default_anim_out</item>
</style>
```

## 代码块 6

```xml
<style name="AppTheme" mce_bogus="1" parent="@android:style/Theme.Light">
        <item name="android:windowAnimationStyle">@style/default_animation</item>
        <item name="android:windowNoTitle">true</item>
</style>
```

## 代码块 7

```xml
<application
   android:icon="@drawable/logo"
   android:label="@string/app_name"
   android:theme="@style/AppTheme" >
```

## 代码块 8

```java
android:theme="@android:style/Theme.Dialog"
```

## 代码块 9

```java
//设置左上角小图标
requestWindowFeature(Window.FEATURE_LEFT_ICON);
setContentView(R.layout.main);
getWindow().setFeatureDrawableResource(Window.FEATURE_LEFT_ICON, android.R.drawable.ic_lion_icon);
//设置文字:
setTitle(R.string.actdialog_title);  //XML代码中设置:android:label="@string/activity_dialog"
```
