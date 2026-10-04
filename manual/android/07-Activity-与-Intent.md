# Activity 与 Intent

> 本章归并自 5 页教程代码块，来源见各节。

## 4.1.1 Activity初学乍练

> 来源: https://www.runoob.com/w3cnote/android-tutorial-activity.html

```java
android:persistableMode="persistAcrossReboots"
```

```java
public void onSaveInstanceState(Bundle outState, PersistableBundle outPersistentState)
public void onRestoreInstanceState(Bundle savedInstanceState, PersistableBundle persistentState)
```

```java
startActivity(new Intent(当前Act.this,要启动的Act.class));
```

```java
ComponentName cn = new ComponentName("当前Act的全限定类名","启动Act的全限定类名") ;
Intent intent = new Intent() ;
intent.setComponent(cn) ;
startActivity(intent) ;
```

```java
Intent intent = new Intent("android.intent.action.MAIN");
intent.setClassName("当前Act的全限定类名","启动Act的全限定类名");
startActivity(intent);
```

```java
Intent intent = getPackageManager().getLaunchIntentForPackage
("apk第一个启动的Activity的全限定类名") ;
if(intent != null) startActivity(intent) ;
```

```java
if (this.getResources().getConfiguration().orientation == Configuration.ORIENTATION_LANDSCAPE){
     setContentView(R.layout.横屏);
}

else if (this.getResources().getConfiguration().orientation ==Configuration.ORIENTATION_PORTRAIT) {
    setContentView(R.layout.竖屏);
}
```

```java
onCreate(Bundle savedInstanceState);
onSaveInstanceState(Bundle outState);
onRestoreInstanceState(Bundle savedInstanceState);
```

```java
//1.拨打电话
// 给移动客服10086拨打电话
Uri uri = Uri.parse("tel:10086");
Intent intent = new Intent(Intent.ACTION_DIAL, uri);
startActivity(intent);

//2.发送短信
// 给10086发送内容为“Hello”的短信
Uri uri = Uri.parse("smsto:10086");
Intent intent = new Intent(Intent.ACTION_SENDTO, uri);
intent.putExtra("sms_body", "Hello");
startActivity(intent);

//3.发送彩信（相当于发送带附件的短信）
Intent intent = new Intent(Intent.ACTION_SEND);
intent.putExtra("sms_body", "Hello");
Uri uri = Uri.parse("content://media/external/images/media/23");
intent.putExtra(Intent.EXTRA_STREAM, uri);
intent.setType("image/png");
startActivity(intent);

//4.打开浏览器:
// 打开Google主页
Uri uri = Uri.parse("http://www.baidu.com");
Intent intent  = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//5.发送电子邮件:(阉割了Google服务的没戏!!!!)
// 给[email protected]发邮件
Uri uri = Uri.parse("mailto:[email protected]");
Intent intent = new Intent(Intent.ACTION_SENDTO, uri);
startActivity(intent);
// 给[email protected]发邮件发送内容为“Hello”的邮件
Intent intent = new Intent(Intent.ACTION_SEND);
intent.putExtra(Intent.EXTRA_EMAIL, "[email protected]");
intent.putExtra(Intent.EXTRA_SUBJECT, "Subject");
intent.putExtra(Intent.EXTRA_TEXT, "Hello");
intent.setType("text/plain");
startActivity(intent);
// 给多人发邮件
Intent intent=new Intent(Intent.ACTION_SEND);
String[] tos = {"[email protected]", "[email protected]"}; // 收件人
String[] ccs = {"[email protected]", "[email protected]"}; // 抄送
String[] bccs = {"[email protected]", "[email protected]"}; // 密送
intent.putExtra(Intent.EXTRA_EMAIL, tos);
intent.putExtra(Intent.EXTRA_CC, ccs);
intent.putExtra(Intent.EXTRA_BCC, bccs);
intent.putExtra(Intent.EXTRA_SUBJECT, "Subject");
intent.putExtra(Intent.EXTRA_TEXT, "Hello");
intent.setType("message/rfc822");
startActivity(intent);

//6.显示地图:
// 打开Google地图中国北京位置（北纬39.9，东经116.3）
Uri uri = Uri.parse("geo:39.9,116.3");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//7.路径规划
// 路径规划：从北京某地（北纬39.9，东经116.3）到上海某地（北纬31.2，东经121.4）
Uri uri = Uri.parse("http://maps.google.com/maps?f=d&saddr=39.9 116.3&daddr=31.2 121.4");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//8.多媒体播放:
Intent intent = new Intent(Intent.ACTION_VIEW);
Uri uri = Uri.parse("file:///sdcard/foo.mp3");
intent.setDataAndType(uri, "audio/mp3");
startActivity(intent);

//获取SD卡下所有音频文件,然后播放第一首=-=
Uri uri = Uri.withAppendedPath(MediaStore.Audio.Media.INTERNAL_CONTENT_URI, "1");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//9.打开摄像头拍照:
// 打开拍照程序
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
startActivityForResult(intent, 0);
// 取出照片数据
Bundle extras = intent.getExtras();
Bitmap bitmap = (Bitmap) extras.get("data");

//另一种:
//调用系统相机应用程序，并存储拍下来的照片
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
time = Calendar.getInstance().getTimeInMillis();
intent.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(new File(Environment
.getExternalStorageDirectory().getAbsolutePath()+"/tucue", time + ".jpg")));
startActivityForResult(intent, ACTIVITY_GET_CAMERA_IMAGE);

//10.获取并剪切图片
// 获取并剪切图片
Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
intent.setType("image/*");
intent.putExtra("crop", "true"); // 开启剪切
intent.putExtra("aspectX", 1); // 剪切的宽高比为1：2
intent.putExtra("aspectY", 2);
intent.putExtra("outputX", 20); // 保存图片的宽和高
intent.putExtra("outputY", 40);
intent.putExtra("output", Uri.fromFile(new File("/mnt/sdcard/temp"))); // 保存路径
intent.putExtra("outputFormat", "JPEG");// 返回格式
startActivityForResult(intent, 0);
// 剪切特定图片
Intent intent = new Intent("com.android.camera.action.CROP");
intent.setClassName("com.android.camera", "com.android.camera.CropImage");
intent.setData(Uri.fromFile(new File("/mnt/sdcard/temp")));
intent.putExtra("outputX", 1); // 剪切的宽高比为1：2
intent.putExtra("outputY", 2);
intent.putExtra("aspectX", 20); // 保存图片的宽和高
intent.putExtra("aspectY", 40);
intent.putExtra("scale", true);
intent.putExtra("noFaceDetection", true);
intent.putExtra("output", Uri.parse("file:///mnt/sdcard/temp"));
startActivityForResult(intent, 0);

//11.打开Google Market
// 打开Google Market直接进入该程序的详细页面
Uri uri = Uri.parse("market://details?id=" + "com.demo.app");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//12.进入手机设置界面:
// 进入无线网络设置界面（其它可以举一反三）
Intent intent = new Intent(android.provider.Settings.ACTION_WIRELESS_SETTINGS);
startActivityForResult(intent, 0);

//13.安装apk:
Uri installUri = Uri.fromParts("package", "xxx", null);
returnIt = new Intent(Intent.ACTION_PACKAGE_ADDED, installUri);

//14.卸载apk:
Uri uri = Uri.fromParts("package", strPackageName, null);
Intent it = new Intent(Intent.ACTION_DELETE, uri);
startActivity(it);

//15.发送附件:
Intent it = new Intent(Intent.ACTION_SEND);
it.putExtra(Intent.EXTRA_SUBJECT, "The email subject text");
it.putExtra(Intent.EXTRA_STREAM, "file:///sdcard/eoe.mp3");
sendIntent.setType("audio/mp3");
startActivity(Intent.createChooser(it, "Choose Email Client"));

//16.进入联系人页面:
Intent intent = new Intent();
intent.setAction(Intent.ACTION_VIEW);
intent.setData(People.CONTENT_URI);
startActivity(intent);

//17.查看指定联系人:
Uri personUri = ContentUris.withAppendedId(People.CONTENT_URI, info.id);//info.id联系人ID
Intent intent = new Intent();
intent.setAction(Intent.ACTION_VIEW);
intent.setData(personUri);
startActivity(intent);
```

## 4.1.2 Activity初窥门径

> 来源: https://www.runoob.com/w3cnote/android-tutorial-activity-start.html

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

```xml
<!-- 默认Activity跳转动画 -->
<style name="default_animation" mce_bogus="1" parent="@android:style/Animation.Activity">
    <item name="android:activityOpenEnterAnimation">@anim/default_anim_in</item>
    <item name="android:activityOpenExitAnimation">@anim/anim_stay</item>
    <item name="android:activityCloseEnterAnimation">@anim/anim_stay</item>
    <item name="android:activityCloseExitAnimation">@anim/default_anim_out</item>
</style>
```

```xml
<style name="AppTheme" mce_bogus="1" parent="@android:style/Theme.Light">
        <item name="android:windowAnimationStyle">@style/default_animation</item>
        <item name="android:windowNoTitle">true</item>
</style>
```

```xml
<application
   android:icon="@drawable/logo"
   android:label="@string/app_name"
   android:theme="@style/AppTheme" >
```

```java
android:theme="@android:style/Theme.Dialog"
```

```java
//设置左上角小图标
requestWindowFeature(Window.FEATURE_LEFT_ICON);
setContentView(R.layout.main);
getWindow().setFeatureDrawableResource(Window.FEATURE_LEFT_ICON, android.R.drawable.ic_lion_icon);
//设置文字:
setTitle(R.string.actdialog_title);  //XML代码中设置:android:label="@string/activity_dialog"
```

## 4.1.3 Activity登堂入室

> 来源: https://www.runoob.com/w3cnote/android-tutorial-activity-intro.html

```java
package net.oschina.app;

import java.util.Stack;

import android.app.Activity;
import android.app.ActivityManager;
import android.content.Context;


public class AppManager {

    private static Stack<Activity> activityStack;
    private static AppManager instance;

    private AppManager(){}
    /**
     * 单一实例
     */
    public static AppManager getAppManager(){
        if(instance==null){
            instance=new AppManager();
        }
        return instance;
    }
    /**
     * 添加Activity到堆栈
     */
    public void addActivity(Activity activity){
        if(activityStack==null){
            activityStack=new Stack<Activity>();
        }
        activityStack.add(activity);
    }
    /**
     * 获取当前Activity（堆栈中最后一个压入的）
     */
    public Activity currentActivity(){
        Activity activity=activityStack.lastElement();
        return activity;
    }
    /**
     * 结束当前Activity（堆栈中最后一个压入的）
     */
    public void finishActivity(){
        Activity activity=activityStack.lastElement();
        finishActivity(activity);
    }
    /**
     * 结束指定的Activity
     */
    public void finishActivity(Activity activity){
        if(activity!=null){
            activityStack.remove(activity);
            activity.finish();
            activity=null;
        }
    }
    /**
     * 结束指定类名的Activity
     */
    public void finishActivity(Class<?> cls){
        for (Activity activity : activityStack) {
            if(activity.getClass().equals(cls) ){
                finishActivity(activity);
            }
        }
    }
    /**
     * 结束所有Activity
     */
    public void finishAllActivity(){
        for (int i = 0, size = activityStack.size(); i < size; i++){
            if (null != activityStack.get(i)){
                activityStack.get(i).finish();
            }
        }
        activityStack.clear();
    }
    /**
     * 退出应用程序
     */
    public void AppExit(Context context) {
        try {
            finishAllActivity();
            ActivityManager activityMgr= (ActivityManager) context.getSystemService(Context.ACTIVITY_SERVICE);
            activityMgr.restartPackage(context.getPackageName());
            System.exit(0);
        } catch (Exception e) {    }
    }
}
```

## 4.5.1 Intent的基本使用

> 来源: https://www.runoob.com/w3cnote/android-tutorial-intent-base.html

```java
Intent it = new Intent();
it.setAction(Intent.ACTION_MAIN);
it.addCategory(Intent.CATEGORY_HOME);
startActivity(it);
```

```java
Intent it = new Intent();
it.setAction(Intent.ACTION_VIEW);
it.setData(Uri.parse("http://www.baidu.com"));
startActivity(it);
```

```java
Intent it = new Intent();
it.setAction(Intent.ACTION_VIEW);
startActivity(it);
```

```xml
<activity android:name=".SecondActivity"
            android:label="第二个Activity">
    <intent-filter>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
    </intent-filter>
 </activity>
```

```java
Intent it = new Intent();
it.setAction("my_action");
it.addCategory("my_category");
startActivity(it);
```

```xml
<activity android:name=".SecondActivity"
        android:label="第二个Activity">
    <intent-filter>
        <action android:name="my_action"/>
        <category android:name="my_category"/>
        <category android:name="android.intent.category.DEFAULT"/>
    </intent-filter>
</activity>
```

```xml
<category android:name="android.intent.category.DEFAULT"/>
```

```java
//===============================================================
//1.拨打电话
// 给移动客服10086拨打电话
Uri uri = Uri.parse("tel:10086");
Intent intent = new Intent(Intent.ACTION_DIAL, uri);
startActivity(intent);

//===============================================================

//2.发送短信
// 给10086发送内容为“Hello”的短信
Uri uri = Uri.parse("smsto:10086");
Intent intent = new Intent(Intent.ACTION_SENDTO, uri);
intent.putExtra("sms_body", "Hello");
startActivity(intent);

//3.发送彩信（相当于发送带附件的短信）
Intent intent = new Intent(Intent.ACTION_SEND);
intent.putExtra("sms_body", "Hello");
Uri uri = Uri.parse("content://media/external/images/media/23");
intent.putExtra(Intent.EXTRA_STREAM, uri);
intent.setType("image/png");
startActivity(intent);

//===============================================================

//4.打开浏览器:
// 打开百度主页
Uri uri = Uri.parse("http://www.baidu.com");
Intent intent  = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//===============================================================

//5.发送电子邮件:(阉割了Google服务的没戏!!!!)
// 给[email protected]发邮件
Uri uri = Uri.parse("mailto:[email protected]");
Intent intent = new Intent(Intent.ACTION_SENDTO, uri);
startActivity(intent);
// 给[email protected]发邮件发送内容为“Hello”的邮件
Intent intent = new Intent(Intent.ACTION_SEND);
intent.putExtra(Intent.EXTRA_EMAIL, "[email protected]");
intent.putExtra(Intent.EXTRA_SUBJECT, "Subject");
intent.putExtra(Intent.EXTRA_TEXT, "Hello");
intent.setType("text/plain");
startActivity(intent);
// 给多人发邮件
Intent intent=new Intent(Intent.ACTION_SEND);
String[] tos = {"[email protected]", "[email protected]"}; // 收件人
String[] ccs = {"[email protected]", "[email protected]"}; // 抄送
String[] bccs = {"[email protected]", "[email protected]"}; // 密送
intent.putExtra(Intent.EXTRA_EMAIL, tos);
intent.putExtra(Intent.EXTRA_CC, ccs);
intent.putExtra(Intent.EXTRA_BCC, bccs);
intent.putExtra(Intent.EXTRA_SUBJECT, "Subject");
intent.putExtra(Intent.EXTRA_TEXT, "Hello");
intent.setType("message/rfc822");
startActivity(intent);

//===============================================================

//6.显示地图:
// 打开Google地图中国北京位置（北纬39.9，东经116.3）
Uri uri = Uri.parse("geo:39.9,116.3");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//===============================================================

//7.路径规划
// 路径规划：从北京某地（北纬39.9，东经116.3）到上海某地（北纬31.2，东经121.4）
Uri uri = Uri.parse("http://maps.google.com/maps?f=d&saddr=39.9 116.3&daddr=31.2 121.4");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//===============================================================

//8.多媒体播放:
Intent intent = new Intent(Intent.ACTION_VIEW);
Uri uri = Uri.parse("file:///sdcard/foo.mp3");
intent.setDataAndType(uri, "audio/mp3");
startActivity(intent);

//获取SD卡下所有音频文件,然后播放第一首=-=
Uri uri = Uri.withAppendedPath(MediaStore.Audio.Media.INTERNAL_CONTENT_URI, "1");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//===============================================================

//9.打开摄像头拍照:
// 打开拍照程序
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
startActivityForResult(intent, 0);
// 取出照片数据
Bundle extras = intent.getExtras();
Bitmap bitmap = (Bitmap) extras.get("data");

//另一种:
//调用系统相机应用程序，并存储拍下来的照片
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
time = Calendar.getInstance().getTimeInMillis();
intent.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(new File(Environment
.getExternalStorageDirectory().getAbsolutePath()+"/tucue", time + ".jpg")));
startActivityForResult(intent, ACTIVITY_GET_CAMERA_IMAGE);

//===============================================================

//10.获取并剪切图片
// 获取并剪切图片
Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
intent.setType("image/*");
intent.putExtra("crop", "true"); // 开启剪切
intent.putExtra("aspectX", 1); // 剪切的宽高比为1：2
intent.putExtra("aspectY", 2);
intent.putExtra("outputX", 20); // 保存图片的宽和高
intent.putExtra("outputY", 40);
intent.putExtra("output", Uri.fromFile(new File("/mnt/sdcard/temp"))); // 保存路径
intent.putExtra("outputFormat", "JPEG");// 返回格式
startActivityForResult(intent, 0);
// 剪切特定图片
Intent intent = new Intent("com.android.camera.action.CROP");
intent.setClassName("com.android.camera", "com.android.camera.CropImage");
intent.setData(Uri.fromFile(new File("/mnt/sdcard/temp")));
intent.putExtra("outputX", 1); // 剪切的宽高比为1：2
intent.putExtra("outputY", 2);
intent.putExtra("aspectX", 20); // 保存图片的宽和高
intent.putExtra("aspectY", 40);
intent.putExtra("scale", true);
intent.putExtra("noFaceDetection", true);
intent.putExtra("output", Uri.parse("file:///mnt/sdcard/temp"));
startActivityForResult(intent, 0);

//===============================================================

//11.打开Google Market
// 打开Google Market直接进入该程序的详细页面
Uri uri = Uri.parse("market://details?id=" + "com.demo.app");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);

//===============================================================

//12.进入手机设置界面:
// 进入无线网络设置界面（其它可以举一反三）
Intent intent = new Intent(android.provider.Settings.ACTION_WIRELESS_SETTINGS);
startActivityForResult(intent, 0);

//===============================================================

//13.安装apk:
Uri installUri = Uri.fromParts("package", "xxx", null);
returnIt = new Intent(Intent.ACTION_PACKAGE_ADDED, installUri);

//===============================================================

//14.卸载apk:
Uri uri = Uri.fromParts("package", strPackageName, null);
Intent it = new Intent(Intent.ACTION_DELETE, uri);
startActivity(it);

//===============================================================

//15.发送附件:
Intent it = new Intent(Intent.ACTION_SEND);
it.putExtra(Intent.EXTRA_SUBJECT, "The email subject text");
it.putExtra(Intent.EXTRA_STREAM, "file:///sdcard/eoe.mp3");
sendIntent.setType("audio/mp3");
startActivity(Intent.createChooser(it, "Choose Email Client"));

//===============================================================

//16.进入联系人页面:
Intent intent = new Intent();
intent.setAction(Intent.ACTION_VIEW);
intent.setData(People.CONTENT_URI);
startActivity(intent);

//===============================================================


//17.查看指定联系人:
Uri personUri = ContentUris.withAppendedId(People.CONTENT_URI, info.id);//info.id联系人ID
Intent intent = new Intent();
intent.setAction(Intent.ACTION_VIEW);
intent.setData(personUri);
startActivity(intent);

//===============================================================

//18.调用系统编辑添加联系人（高版本SDK有效）：
Intent it = newIntent(Intent.ACTION_INSERT_OR_EDIT);
it.setType("vnd.android.cursor.item/contact");
//it.setType(Contacts.CONTENT_ITEM_TYPE);
it.putExtra("name","myName");
it.putExtra(android.provider.Contacts.Intents.Insert.COMPANY, "organization");
it.putExtra(android.provider.Contacts.Intents.Insert.EMAIL,"email");
it.putExtra(android.provider.Contacts.Intents.Insert.PHONE,"homePhone");
it.putExtra(android.provider.Contacts.Intents.Insert.SECONDARY_PHONE,"mobilePhone");
it.putExtra( android.provider.Contacts.Intents.Insert.TERTIARY_PHONE,"workPhone");
it.putExtra(android.provider.Contacts.Intents.Insert.JOB_TITLE,"title");
startActivity(it);

//===============================================================

//19.调用系统编辑添加联系人（全有效）：
Intent intent = newIntent(Intent.ACTION_INSERT_OR_EDIT);
intent.setType(People.CONTENT_ITEM_TYPE);
intent.putExtra(Contacts.Intents.Insert.NAME, "My Name");
intent.putExtra(Contacts.Intents.Insert.PHONE, "+1234567890");
intent.putExtra(Contacts.Intents.Insert.PHONE_TYPE,Contacts.PhonesColumns.TYPE_MOBILE);
intent.putExtra(Contacts.Intents.Insert.EMAIL, "[email protected]");
intent.putExtra(Contacts.Intents.Insert.EMAIL_TYPE, Contacts.ContactMethodsColumns.TYPE_WORK);
startActivity(intent);

//===============================================================

//20.打开另一程序
Intent i = new Intent();
ComponentName cn = new ComponentName("com.example.jay.test",
"com.example.jay.test.MainActivity");
i.setComponent(cn);
i.setAction("android.intent.action.MAIN");
startActivityForResult(i, RESULT_OK);

//===============================================================

//21.打开录音机
Intent mi = new Intent(Media.RECORD_SOUND_ACTION);
startActivity(mi);

//===============================================================

//22.从google搜索内容
Intent intent = new Intent();
intent.setAction(Intent.ACTION_WEB_SEARCH);
intent.putExtra(SearchManager.QUERY,"searchString")
startActivity(intent);

//===============================================================
```

## 4.5.2 Intent之复杂数据的传递

> 来源: https://www.runoob.com/w3cnote/android-tutorial-intent-pass-data.html

```java
bd.putStringArray("StringArray", new String[]{"呵呵","哈哈"});
//可把StringArray换成其他数据类型,比如int,float等等...
```

```java
String[] str = bd.getStringArray("StringArray")
```

```java
intent.putStringArrayListExtra(name, value)
intent.putIntegerArrayListExtra(name, value)
```

```java
intent.getStringArrayListExtra(name)
intent.getIntegerArrayListExtra(name)
```

```java
putExtras(key, (Serializable)list)
```

```java
(List<Object>) getIntent().getSerializable(key)
```

```java
//传递复杂些的参数
Map<String, Object> map1 = new HashMap<String, Object>();
map1.put("key1", "value1");
map1.put("key2", "value2");
List<Map<String, Object>> list = new ArrayList<Map<String, Object>>();
list.add(map1);

Intent intent = new Intent();
intent.setClass(MainActivity.this,ComplexActivity.class);
Bundle bundle = new Bundle();

//须定义一个list用于在budnle中传递需要传递的ArrayList<Object>,这个是必须要的
ArrayList bundlelist = new ArrayList();
bundlelist.add(list);
bundle.putParcelableArrayList("list",bundlelist);
intent.putExtras(bundle);
startActivity(intent);
```

```java
public class Book{
    private int id;
    private String title;
    //...
}

public class Author{
    private int id;
    private String name;
    //...
}
```

```java
Book book=new Book();
book.setTitle("Java编程思想");
Author author=new Author();
author.setId(1);
author.setName("Bruce Eckel");
book.setAuthor(author);
Intent intent=new Intent(this,SecondActivity.class);
intent.putExtra("book",new Gson().toJson(book));
startActivity(intent);
```

```java
String bookJson=getIntent().getStringExtra("book");
Book book=new Gson().fromJson(bookJson,Book.class);
Log.d(TAG,"book title->"+book.getTitle());
Log.d(TAG,"book author name->"+book.getAuthor().getName());
```

```java
//Internal Description Interface,You do not need to manage
@Override
public int describeContents() {
     return 0;
}


@Override
public void writeToParcel(Parcel parcel, int flags){
    parcel.writeString(bookName);
    parcel.writeString(author);
    parcel.writeInt(publishTime);
}


public static final Parcelable.Creator<Book> CREATOR = new Creator<Book>() {
    @Override
    public Book[] newArray(int size) {
        return new Book[size];
    }

    @Override
    public Book createFromParcel(Parcel source) {
        Book mBook = new Book();
        mBook.bookName = source.readString();
        mBook.author = source.readString();
        mBook.publishTime = source.readInt();
        return mBook;
    }
};
```

```java
Bitmap bitmap = null;
Intent intent = new Intent();
Bundle bundle = new Bundle();
bundle.putParcelable("bitmap", bitmap);
intent.putExtra("bundle", bundle);
```

```java
class MyApp extends Application {
    private String myState;
    public String getState(){
        return myState;
    }
    public void setState(String s){
        myState = s;
    }
}
```

```xml
<application android:name=".MyApp" android:icon="@drawable/icon"
  android:label="@string/app_name">
```

```java
class Blah extends Activity {
    @Override
    public void onCreate(Bundle b){
        ...
    MyApp appState = ((MyApp)getApplicationContext());
    String state = appState.getState();
        ...
    }
}
```

```java
class MyApp extends Application {
    private String myState;
    private static MyApp instance;

    public static MyApp getInstance(){
        return instance;
    }


    public String getState(){
        return myState;
    }
    public void setState(String s){
        myState = s;
    }

    @Override
    public void onCreate(){
        onCreate();
        instance = this;
    }

}
```

```java
public class XclSingleton
{
    //单例模式实例
    private static XclSingleton instance = null;

    //synchronized 用于线程安全，防止多线程同时创建实例
    public synchronized static XclSingleton getInstance(){
        if(instance == null){
            instance = new XclSingleton();
        }
        return instance;
    }

    final HashMap<String, Object> mMap;
    private XclSingleton()
    {
        mMap = new HashMap<String,Object>();
    }

    public void put(String key,Object value){
        mMap.put(key,value);
    }

    public Object get(String key)
    {
        return mMap.get(key);
    }

}
```

```java
XclSingleton.getInstance().put("key1", "value1");
XclSingleton.getInstance().put("key2", "value2");
```
