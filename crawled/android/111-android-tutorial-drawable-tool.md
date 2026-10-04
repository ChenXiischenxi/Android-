# 8.3.1 三个绘图工具类详解

> 来源: https://www.runoob.com/w3cnote/android-tutorial-drawable-tool.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/10/15 0015.
 */
public class MyView extends View{

    private Paint mPaint;


    public MyView(Context context) {
        super(context);
        init();
    }

    public MyView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public MyView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }

    private void init(){
        mPaint = new Paint();
        mPaint.setAntiAlias(true);          //抗锯齿
        mPaint.setColor(getResources().getColor(R.color.puple));//画笔颜色
        mPaint.setStyle(Paint.Style.FILL);  //画笔风格
        mPaint.setTextSize(36);             //绘制文字大小，单位px
        mPaint.setStrokeWidth(5);           //画笔粗细
    }

    //重写该方法，在这里绘图
    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
    }

}
```

## 代码块 2

```java
canvas.drawColor(getResources().getColor(R.color.yellow));   //设置画布背景颜色
```

## 代码块 3

```java
canvas.drawCircle(200, 200, 100, mPaint);           //画实心圆
```

## 代码块 4

```java
canvas.drawRect(0, 0, 200, 100, mPaint);            //画矩形
```

## 代码块 5

```java
canvas.drawBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.ic_launcher), 0, 0, mPaint);
```

## 代码块 6

```java
canvas.drawArc(new RectF(0, 0, 100, 100),0,90,true,mPaint);  //绘制弧形区域
```

## 代码块 7

```java
canvas.drawRoundRect(new RectF(10,10,210,110),15,15,mPaint); //画圆角矩形
```

## 代码块 8

```java
canvas.drawOval(new RectF(0,0,200,300),mPaint); //画椭圆
```

## 代码块 9

```java
Path path = new Path();
path.moveTo(10, 10); //移动到 坐标10,10
path.lineTo(100, 50);
path.lineTo(200,40);
path.lineTo(300, 20);
path.lineTo(200, 10);
path.lineTo(100, 70);
path.lineTo(50, 40);
path.close();
canvas.drawPath(path,mPaint);
```

## 代码块 10

```java
canvas.drawText("最喜欢看曹神日狗了~",50,50,mPaint);    //绘制文字
```

## 代码块 11

```java
Path path = new Path();
path.moveTo(50,50);
path.lineTo(100, 100);
path.lineTo(200, 200);
path.lineTo(300, 300);
path.close();
canvas.drawTextOnPath("最喜欢看曹神日狗了~", path, 50, 50, mPaint);    //绘制文字
```

## 代码块 12

```java
protected void onDraw(Canvas canvas) {
    super.onDraw(canvas);
    canvas.translate(canvas.getWidth()/2, 200); //将位置移动画纸的坐标点:150,150
    canvas.drawCircle(0, 0, 100, mPaint); //画圆圈

    //使用path绘制路径文字
    canvas.save();
    canvas.translate(-75, -75);
    Path path = new Path();
    path.addArc(new RectF(0,0,150,150), -180, 180);
    Paint citePaint = new Paint(mPaint);
    citePaint.setTextSize(14);
    citePaint.setStrokeWidth(1);
    canvas.drawTextOnPath("绘制表盘~", path, 28, 0, citePaint);
    canvas.restore();

    Paint tmpPaint = new Paint(mPaint); //小刻度画笔对象
    tmpPaint.setStrokeWidth(1);

    float  y=100;
    int count = 60; //总刻度数

    for(int i=0 ; i <count ; i++){
        if(i%5 == 0){
            canvas.drawLine(0f, y, 0, y+12f, mPaint);
            canvas.drawText(String.valueOf(i/5+1), -4f, y+25f, tmpPaint);

        }else{
            canvas.drawLine(0f, y, 0f, y +5f, tmpPaint);
        }
        canvas.rotate(360/count,0f,0f); //旋转画纸
    }

    //绘制指针
    tmpPaint.setColor(Color.GRAY);
    tmpPaint.setStrokeWidth(4);
    canvas.drawCircle(0, 0, 7, tmpPaint);
    tmpPaint.setStyle(Paint.Style.FILL);
    tmpPaint.setColor(Color.YELLOW);
    canvas.drawCircle(0, 0, 5, tmpPaint);
    canvas.drawLine(0, 10, 0, -65, mPaint);
}
```
