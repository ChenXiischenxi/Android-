# 10.6 PowerManager(电源服务)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-powermanager.html

## 代码块 1

```java
PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
PowerManager.WakeLock w1 = pm.newWakeLock(PowerManager.SCREEN_DIM_WAKE_LOCK, "MyTag");
w1.acquire();
//在这个过程,屏幕会保持光亮!
w1.release();
```

## 代码块 2

```xml
<uses-permission android:name="android.permission.WAKE_LOCK"/>
```

## 代码块 3

```xml
<uses-permission android:name="android.permission.DEVICE_POWER"/>
```
