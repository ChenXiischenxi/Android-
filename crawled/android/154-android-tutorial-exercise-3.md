# 12.3 DrySister看妹子应用(第一版)——3.图片加载优化(写个图片缓存小框架)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-exercise-3.html

## 代码块 1

```java
public class MemoryCache {

    private static final int MAX_CACHE_COUNT = 30;  //设置最大缓存数

    /**
    Map弱引用Bitmap，内存够的情况Bitmap不会被回收，当缓存数大于阈值，会清除最早放入缓存的
     */
    private HashMap<String,SoftReference<Bitmap>> mCacheMap = new LinkedHashMap<String,SoftReference<Bitmap>>() {
        @Override
        protected boolean removeEldestEntry(Entry eldest) {
            return size() > MAX_CACHE_COUNT;
        }
    };

    /**
     * 添加图片到缓存中
     * */
    public void put(String id,Bitmap bitmap) {
        mCacheMap.put(id, new SoftReference<>(bitmap));
    }

    /**
     * 取出缓存中的图片
     * */
    public Bitmap get(String id,Bitmap bitmap) {
       if(!mCacheMap.containsKey(id))return null;
        SoftReference<Bitmap> ref = mCacheMap.get(id);
        return ref.get();
    }

    /**
     * 清除所有缓存
     * */
    public void clear() {
        try{
            for (Map.Entry<String,SoftReference<Bitmap>>entry : mCacheMap.entrySet()) {
                SoftReference<Bitmap> sr = entry.getValue();
                if(null != sr) {
                    Bitmap bitmap = sr.get();
                    if(null != bitmap) {
                        bitmap.recycle();
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
```

## 代码块 2

```java
private SisterLoader mLoader;
mLoader = SisterLoader.getInstance(MainActivity.this);
mLoader.bindBitmap(data.get(curPos).getUrl(),showImg,400,400);
```
