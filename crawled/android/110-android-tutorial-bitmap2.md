# 8.2.2 Bitmap引起的OOM问题

> 来源: https://www.runoob.com/w3cnote/android-tutorial-bitmap2.html

## 代码块 1

```java
ActivityManager activityManager = (ActivityManager)context.getSystemService(Context.ACTIVITY_SERVICE);
Log.e("HEHE","最大内存：" + activityManager.getMemoryClass());
```

## 代码块 2

```java
adb shell getprop | grep dalvik.vm.heapgrowthlimit
```

## 代码块 3

```java
dalvik.vm.heapstartsize=8m
dalvik.vm.heapgrowthlimit=192m
dalvik.vm.heapsize=512m
dalvik.vm.heaptargetutilization=0.75
dalvik.vm.heapminfree=2m
dalvik.vm.heapmaxfree=8m
```

## 代码块 4

```java
public static int caculateInSampleSize(BitmapFactory.Options options, int reqWidth, int reqHeight) {
    int width = options.outWidth;
    int height = options.outHeight;
    int inSampleSize = 1;
    if (width > reqWidth || height > reqHeight) {
        int widthRadio = Math.round(width * 1.0f / reqWidth);
        int heightRadio = Math.round(height * 1.0f / reqHeight);
        inSampleSize = Math.max(widthRadio, heightRadio);
    }
    return inSampleSize;
}
```

## 代码块 5

```java
BitmapFactory.Options options = new BitmapFactory.Options();
options.inJustDecodeBounds = true; // 设置了此属性一定要记得将值设置为false
Bitmap bitmap = null;
bitmap = BitmapFactory.decodeFile(url, options);
options.inSampleSize = computeSampleSize(options,128,128);
options.inPreferredConfig = Bitmap.Config.ARGB_4444;
/* 下面两个字段需要组合使用 */
options.inPurgeable = true;
options.inInputShareable = true;
options.inJustDecodeBounds = false;
try {
    bitmap = BitmapFactory.decodeFile(url, options);
} catch (OutOfMemoryError e) {
        Log.e(TAG, "OutOfMemoryError");
}
```

## 代码块 6

```java
private Map<String, SoftReference<Bitmap>> imageMap
                                           = new HashMap<String, SoftReference<Bitmap>>();

public Bitmap loadBitmap(final String imageUrl,final ImageCallBack imageCallBack) {
    SoftReference<Bitmap> reference = imageMap.get(imageUrl);
    if(reference != null) {
        if(reference.get() != null) {
            return reference.get();
        }
    }
    final Handler handler = new Handler() {
        public void handleMessage(final android.os.Message msg) {
            //加入到缓存中
            Bitmap bitmap = (Bitmap)msg.obj;
            imageMap.put(imageUrl, new SoftReference<Bitmap>(bitmap));
            if(imageCallBack != null) {
                imageCallBack.getBitmap(bitmap);
            }
        }
    };
    new Thread(){
        public void run() {
            Message message = handler.obtainMessage();
            message.obj = downloadBitmap(imageUrl);
            handler.sendMessage(message);
        }
    }.start();
    return null ;
}

// 从网上下载图片
private Bitmap downloadBitmap (String imageUrl) {
    Bitmap bitmap = null;
    try {
        bitmap = BitmapFactory.decodeStream(new URL(imageUrl).openStream());
        return bitmap ;
    } catch (Exception e) {
        e.printStackTrace();
        return null;
    }
}
public interface ImageCallBack{
    void getBitmap(Bitmap bitmap);
}
```

## 代码块 7

```java
private LruCache<String, Bitmap> mMemoryCache;
private LruCacheUtils() {
    if (mMemoryCache == null)
        mMemoryCache = new LruCache<String, Bitmap>(
                MAXMEMONRY / 8) {
            @Override
            protected int sizeOf(String key, Bitmap bitmap) {
                // 重写此方法来衡量每张图片的大小，默认返回图片数量。
                return bitmap.getRowBytes() * bitmap.getHeight() / 1024;
            }

            @Override
            protected void entryRemoved(boolean evicted, String key,
                    Bitmap oldValue, Bitmap newValue) {
                Log.v("tag", "hard cache is full , push to soft cache");

            }
        };
}
```

## 代码块 8

```java
public void clearCache() {
    if (mMemoryCache != null) {
        if (mMemoryCache.size() > 0) {
            Log.d("CacheUtils",
                    "mMemoryCache.size() " + mMemoryCache.size());
            mMemoryCache.evictAll();
            Log.d("CacheUtils", "mMemoryCache.size()" + mMemoryCache.size());
        }
        mMemoryCache = null;
    }
}

public synchronized void addBitmapToMemoryCache(String key, Bitmap bitmap) {
    if (mMemoryCache.get(key) == null) {
        if (key != null && bitmap != null)
            mMemoryCache.put(key, bitmap);
    } else
        Log.w(TAG, "the res is aready exits");
}

public synchronized Bitmap getBitmapFromMemCache(String key) {
    Bitmap bm = mMemoryCache.get(key);
    if (key != null) {
        return bm;
    }
    return null;
}

/**
 * 移除缓存
 *
 * @param key
 */
public synchronized void removeImageCache(String key) {
    if (key != null) {
        if (mMemoryCache != null) {
            Bitmap bm = mMemoryCache.remove(key);
            if (bm != null)
                bm.recycle();
        }
    }
}
```
