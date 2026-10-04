# 8.1.1 Android中的13种Drawable小结 Part 1

> 来源: https://www.runoob.com/w3cnote/android-tutorial-drawable1.html

## 代码块 1

```java
ColorDrawable drawable = new ColorDrawable(0xffff2200);
txtShow.setBackground(drawable);
```

## 代码块 2

```xml
<?xml version="1.0" encoding="utf-8"?>
<color
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:color="#FF0000"/>
```

## 代码块 3

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="material_grey_100">#fff5f5f5</color>
    <color name="material_grey_300">#ffe0e0e0</color>
    <color name="material_grey_50">#fffafafa</color>
    <color name="material_grey_600">#ff757575</color>
    <color name="material_grey_800">#ff424242</color>
    <color name="material_grey_850">#ff303030</color>
    <color name="material_grey_900">#ff212121</color>
</resources>
```

## 代码块 4

```java
int mycolor = getResources().getColor(R.color.mycolor);
btn.setBackgroundColor(mycolor);
```

## 代码块 5

```java
int mycolor = 0xff123456;
btn.setBackgroundColor(mycolor);
```

## 代码块 6

```java
int getcolor = Resources.getSystem().getColor(android.R.color.holo_green_light);
btn.setBackgroundColor(getcolor);
```

## 代码块 7

```xml
<!--pic9.xml-->
<!--参数依次为:引用的.9图片,是否对位图进行抖动处理-->
<?xml version="1.0" encoding="utf-8"?>
<nine-patch
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:src="@drawable/dule_pic"
    android:dither="true"/>
```

## 代码块 8

```xml
<!--pic9.xml-->
<!--参数依次为:引用的.9图片,是否对位图进行抖动处理-->
<?xml version="1.0" encoding="utf-8"?>
<bitmap
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:src="@drawable/dule_pic"
    android:dither="true"/>
```

## 代码块 9

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval" >
    <gradient
        android:angle="90"
        android:centerColor="#FFEB82"
        android:endColor="#35B2DE"
        android:startColor="#DEACAB" />

    <stroke
        android:dashGap="5dip"
        android:dashWidth="4dip"
        android:width="3dip"
        android:color="#fff" />
</shape>
```

## 代码块 10

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:innerRadius="0dip"
    android:shape="ring"
    android:thickness="70dip"
    android:useLevel="false" >

    <gradient
        android:centerColor="#FFEB82"
        android:endColor="#35B2DE"
        android:gradientRadius="70"
        android:startColor="#DEACAB"
        android:type="radial"
        android:useLevel="false" />

</shape>
```

## 代码块 11

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:innerRadiusRatio="8"
    android:shape="ring"
    android:thicknessRatio="3"
    android:useLevel="false" >

    <gradient
        android:centerColor="#FFEB82"
        android:endColor="#35B2DE"
        android:startColor="#DEACAB"
        android:type="sweep"
        android:useLevel="false" />

</shape>
```

## 代码块 12

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/txtShow1"
        android:layout_width="200dp"
        android:layout_height="100dp"
        android:background="@drawable/gradient_linear" />

    <TextView
        android:id="@+id/txtShow2"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:background="@drawable/gradient_radial" />

    <TextView
        android:id="@+id/txtShow3"
        android:layout_width="100dp"
        android:layout_height="100dp"
        android:background="@drawable/gradient_sweep" />

</LinearLayout>
```

## 代码块 13

```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(new SampleView(this));
    }

    private static class SampleView extends View {
        private ShapeDrawable[] mDrawables;

        private static Shader makeSweep() {
            return new SweepGradient(150, 25,
                    new int[] { 0xFFFF0000, 0xFF00FF00, 0xFF0000FF, 0xFFFF0000 },
                    null);
        }

        private static Shader makeLinear() {
            return new LinearGradient(0, 0, 50, 50,
                    new int[] { 0xFFFF0000, 0xFF00FF00, 0xFF0000FF },
                    null, Shader.TileMode.MIRROR);
        }

        private static Shader makeTiling() {
            int[] pixels = new int[] { 0xFFFF0000, 0xFF00FF00, 0xFF0000FF, 0};
            Bitmap bm = Bitmap.createBitmap(pixels, 2, 2,
                    Bitmap.Config.ARGB_8888);

            return new BitmapShader(bm, Shader.TileMode.REPEAT,
                    Shader.TileMode.REPEAT);
        }

        private static class MyShapeDrawable extends ShapeDrawable {
            private Paint mStrokePaint = new Paint(Paint.ANTI_ALIAS_FLAG);

            public MyShapeDrawable(Shape s) {
                super(s);
                mStrokePaint.setStyle(Paint.Style.STROKE);
            }

            public Paint getStrokePaint() {
                return mStrokePaint;
            }

            @Override protected void onDraw(Shape s, Canvas c, Paint p) {
                s.draw(c, p);
                s.draw(c, mStrokePaint);
            }
        }

        public SampleView(Context context) {
            super(context);
            setFocusable(true);

            float[] outerR = new float[] { 12, 12, 12, 12, 0, 0, 0, 0 };
            RectF inset = new RectF(6, 6, 6, 6);
            float[] innerR = new float[] { 12, 12, 0, 0, 12, 12, 0, 0 };

            Path path = new Path();
            path.moveTo(50, 0);
            path.lineTo(0, 50);
            path.lineTo(50, 100);
            path.lineTo(100, 50);
            path.close();

            mDrawables = new ShapeDrawable[7];
            mDrawables[0] = new ShapeDrawable(new RectShape());
            mDrawables[1] = new ShapeDrawable(new OvalShape());
            mDrawables[2] = new ShapeDrawable(new RoundRectShape(outerR, null,
                    null));
            mDrawables[3] = new ShapeDrawable(new RoundRectShape(outerR, inset,
                    null));
            mDrawables[4] = new ShapeDrawable(new RoundRectShape(outerR, inset,
                    innerR));
            mDrawables[5] = new ShapeDrawable(new PathShape(path, 100, 100));
            mDrawables[6] = new MyShapeDrawable(new ArcShape(45, -270));

            mDrawables[0].getPaint().setColor(0xFFFF0000);
            mDrawables[1].getPaint().setColor(0xFF00FF00);
            mDrawables[2].getPaint().setColor(0xFF0000FF);
            mDrawables[3].getPaint().setShader(makeSweep());
            mDrawables[4].getPaint().setShader(makeLinear());
            mDrawables[5].getPaint().setShader(makeTiling());
            mDrawables[6].getPaint().setColor(0x88FF8844);

            PathEffect pe = new DiscretePathEffect(10, 4);
            PathEffect pe2 = new CornerPathEffect(4);
            mDrawables[3].getPaint().setPathEffect(
                    new ComposePathEffect(pe2, pe));

            MyShapeDrawable msd = (MyShapeDrawable)mDrawables[6];
            msd.getStrokePaint().setStrokeWidth(4);
        }

        @Override protected void onDraw(Canvas canvas) {

            int x = 10;
            int y = 10;
            int width = 400;
            int height = 100;

            for (Drawable dr : mDrawables) {
                dr.setBounds(x, y, x + width, y + height);
                dr.draw(canvas);
                y += height + 5;
            }
        }
    }
}
```
