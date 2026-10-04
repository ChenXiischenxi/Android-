# 8.3.16 Canvas API详解(Part 1)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-canvas-api1.html

## 代码块 1

```java
for(int i=0; i < 5; i++) {
    canvas.drawCircle(50, 50, 50, mPaint);
    canvas.translate(100, 100);
}
```

## 代码块 2

```java
Rect rect = new Rect(50,0,150,50);
canvas.translate(200, 200);
for(int i = 0; i < 36;i++){
    canvas.rotate(10);
    canvas.drawRect(rect, mPaint);
}
```

## 代码块 3

```java
canvas.drawBitmap(bmp,0,0,mPaint);
canvas.scale(0.8f, 0.8f);
canvas.drawBitmap(bmp, 0, 0, mPaint);
canvas.scale(0.8f, 0.8f);
canvas.drawBitmap(bmp,0,0,mPaint);
```

## 代码块 4

```java
canvas.drawBitmap(bmp,0,0,mPaint);
canvas.translate(200, 200);
canvas.skew(0.2f,-0.8f);
canvas.drawBitmap(bmp,0,0,mPaint);
```

## 代码块 5

```java
canvas.save();  //保存当前canvas的状态

canvas.translate(100, 100);
canvas.drawCircle(50, 50, 50, mPaint);

canvas.restore();  //恢复保存的Canvas的状态
canvas.drawCircle(50, 50, 50, mPaint);
```

## 代码块 6

```java
canvas.save();

canvas.translate(300, 300);
canvas.drawBitmap(bmp, 0, 0, mPaint);
canvas.save();

canvas.rotate(45);
canvas.drawBitmap(bmp, 0, 0, mPaint);
canvas.save();

canvas.rotate(45);
canvas.drawBitmap(bmp, 0, 0, mPaint);
canvas.save();

canvas.translate(0, 200);
canvas.drawBitmap(bmp, 0, 0, mPaint);
```

## 代码块 7

```java
canvas.restore();
canvas.restore();
canvas.translate(0, 200);
canvas.drawBitmap(bmp, 0, 0, mPaint);
```

## 代码块 8

```java
RectF bounds = new RectF(0, 0, 400, 400);
canvas.saveLayer(bounds, mPaint, Canvas.CLIP_TO_LAYER_SAVE_FLAG);
canvas.drawColor(getResources().getColor(R.color.moss_tide));
canvas.drawBitmap(bmp, 200, 200, mPaint);
canvas.restoreToCount(1);
canvas.drawBitmap(bmp, 300, 200, mPaint);
```
