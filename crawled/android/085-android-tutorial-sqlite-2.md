# 6.3.2 数据存储与访问之——又见SQLite数据库

> 来源: https://www.runoob.com/w3cnote/android-tutorial-sqlite-2.html

## 代码块 1

```java
public void onUpgrade(SQLiteDatabase db, ConnectionSource connectionSource,
            int arg2, int arg3) {
    switch(arg2){
        case 1:
            db.execSQL(第一个版本的建表语句);
        case 2:
            db.execSQL(第二个版本的建表语句);
        case 3:
            db.execSQL(第三个版本的建表语句);
    }
}
```
