# 8.4.4 Android动画合集之属性动画-又见

> 来源: https://www.runoob.com/w3cnote/android-tutorial-valueanimator2.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/11/18 0018.
 */
public class Point {

    private float x;
    private float y;

    public Point() {
    }

    public Point(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float getX() {
        return x;
    }

    public float getY() {
        return y;
    }

    public void setX(float x) {
        this.x = x;
    }

    public void setY(float y) {
        this.y = y;
    }
}
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/11/18 0018.
 */
public class PointEvaluator implements TypeEvaluator<Point>{
    @Override
    public Point evaluate(float fraction, Point startValue, Point endValue) {
        float x = startValue.getX() + fraction * (endValue.getX() - startValue.getX());
        float y = startValue.getY() + fraction * (endValue.getY() - startValue.getY());
        Point point = new Point(x, y);
        return point;
    }
}
```

## 代码块 3

```java
/**
 * Created by Jay on 2015/11/18 0018.
 */
public class AnimView extends View {

    public static final float RADIUS = 80.0f;
    private Point currentPoint;
    private Paint mPaint;

    public AnimView(Context context) {
        this(context, null);
    }

    public AnimView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public AnimView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void init() {
        mPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
        mPaint.setColor(Color.BLUE);
    }

    private void drawCircle(Canvas canvas){
        float x = currentPoint.getX();
        float y = currentPoint.getY();
        canvas.drawCircle(x, y, RADIUS, mPaint);
    }

    private void startAnimation() {
        Point startPoint = new Point(RADIUS, RADIUS);
        Point endPoint = new Point(getWidth() - RADIUS, getHeight() - RADIUS);
        ValueAnimator anim = ValueAnimator.ofObject(new PointEvaluator(), startPoint, endPoint);
        anim.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                currentPoint = (Point) animation.getAnimatedValue();
                invalidate();
            }
        });
        anim.setDuration(3000l);
        anim.start();
    }

    @Override
    protected void onDraw(Canvas canvas) {
        if (currentPoint == null) {
            currentPoint = new Point(RADIUS, RADIUS);
            drawCircle(canvas);
            startAnimation();
        } else {
            drawCircle(canvas);
        }
    }
}
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(new AnimView(this));
    }
}
```

## 代码块 5

```java
/**
 * Created by Jay on 2015/11/18 0018.
 */
public class ColorEvaluator implements TypeEvaluator<Integer>{
    @Override
    public Integer evaluate(float fraction, Integer startValue, Integer endValue) {
        int alpha = (int) (Color.alpha(startValue) + fraction *
                (Color.alpha(endValue) - Color.alpha(startValue)));
        int red = (int) (Color.red(startValue) + fraction *
                (Color.red(endValue) - Color.red(startValue)));
        int green = (int) (Color.green(startValue) + fraction *
                (Color.green(endValue) - Color.green(startValue)));
        int blue = (int) (Color.blue(startValue) + fraction *
                (Color.blue(endValue) - Color.blue(startValue)));
        return Color.argb(alpha, red, green, blue);
    }
}
```

## 代码块 6

```java
/**
 * Created by Jay on 2015/11/18 0018.
 */
public class AnimView2 extends View {

    public static final float RADIUS = 80.0f;
    private Point currentPoint;
    private Paint mPaint;
    private int mColor;

    public AnimView2(Context context) {
        this(context, null);
    }

    public AnimView2(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public AnimView2(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private void init() {
        mPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
        mPaint.setColor(Color.BLUE);
    }


    private void drawCircle(Canvas canvas){
        float x = currentPoint.getX();
        float y = currentPoint.getY();
        canvas.drawCircle(x, y, RADIUS, mPaint);
    }

    private void startAnimation() {
        Point startPoint = new Point(RADIUS, RADIUS);
        Point endPoint = new Point(getWidth() - RADIUS, getHeight() - RADIUS);
        ValueAnimator anim = ValueAnimator.ofObject(new PointEvaluator(), startPoint, endPoint);
        anim.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                currentPoint = (Point) animation.getAnimatedValue();
                invalidate();
            }
        });

        ObjectAnimator objectAnimator = ObjectAnimator.ofObject(this, "color", new ColorEvaluator(),
                Color.BLUE, Color.RED);
        //动画集合将前面两个动画加到一起，with同时播放
        AnimatorSet animatorSet = new AnimatorSet();
        animatorSet.play(anim).with(objectAnimator);
        animatorSet.setStartDelay(1000l);
        animatorSet.setDuration(3000l);
        animatorSet.start();
    }

    @Override
    protected void onDraw(Canvas canvas) {
        if (currentPoint == null) {
            currentPoint = new Point(RADIUS, RADIUS);
            drawCircle(canvas);
            startAnimation();
        } else {
            drawCircle(canvas);
        }
    }

    //color的get和set方法~
    public int getColor() {
        return mColor;
    }

    public void setColor(int color) {
        mColor = color;
        mPaint.setColor(color);
        invalidate();
    }
}
```

## 代码块 7

```java
private class DecelerateAccelerateInterpolator implements TimeInterpolator {
    @Override
    public float getInterpolation(float input) {
        if (input < 0.5) {
            return (float) (Math.sin(input * Math.PI) / 2);
        } else {
            return 1 - (float) (Math.sin(input * Math.PI) / 2);
        }
    }
}
```

## 代码块 8

```java
ObjectAnimator animator = ObjectAnimator.ofFloat(textview, "alpha", 0f);
animator.start();
```

## 代码块 9

```java
textview.animate().alpha(0f);
```

## 代码块 10

```java
textview.animate().x(500).y(500).setDuration(5000)
        .setInterpolator(new BounceInterpolator());
```
