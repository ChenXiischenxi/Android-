# 6.3.1 数据存储与访问之——初见SQLite数据库

> 来源: https://www.runoob.com/w3cnote/android-tutorial-sqlite-intro.html

## 代码块 1

```java
public class MyDBOpenHelper extends SQLiteOpenHelper {
    public MyDBOpenHelper(Context context, String name, CursorFactory factory,
            int version) {super(context, "my.db", null, 1); }
    @Override
    //数据库第一次创建时被调用
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE person(personid INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(20))");

    }
    //软件版本号发生改变时调用
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("ALTER TABLE person ADD phone VARCHAR(12) NULL");
    }
}
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Context mContext;
    private Button btn_insert;
    private Button btn_query;
    private Button btn_update;
    private Button btn_delete;
    private SQLiteDatabase db;
    private MyDBOpenHelper myDBHelper;
    private StringBuilder sb;
    private int i = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        myDBHelper = new MyDBOpenHelper(mContext, "my.db", null, 1);
        bindViews();
    }

    private void bindViews() {
        btn_insert = (Button) findViewById(R.id.btn_insert);
        btn_query = (Button) findViewById(R.id.btn_query);
        btn_update = (Button) findViewById(R.id.btn_update);
        btn_delete = (Button) findViewById(R.id.btn_delete);

        btn_query.setOnClickListener(this);
        btn_insert.setOnClickListener(this);
        btn_update.setOnClickListener(this);
        btn_delete.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        db = myDBHelper.getWritableDatabase();
        switch (v.getId()) {
            case R.id.btn_insert:
                ContentValues values1 = new ContentValues();
                values1.put("name", "呵呵~" + i);
                i++;
                //参数依次是：表名，强行插入null值得数据列的列名，一行记录的数据
                db.insert("person", null, values1);
                Toast.makeText(mContext, "插入完毕~", Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_query:
                sb = new StringBuilder();
                //参数依次是:表名，列名，where约束条件，where中占位符提供具体的值，指定group by的列，进一步约束
                //指定查询结果的排序方式
                Cursor cursor = db.query("person", null, null, null, null, null, null);
                if (cursor.moveToFirst()) {
                    do {
                        int pid = cursor.getInt(cursor.getColumnIndex("personid"));
                        String name = cursor.getString(cursor.getColumnIndex("name"));
                        sb.append("id：" + pid + "：" + name + "\n");
                    } while (cursor.moveToNext());
                }
                cursor.close();
                Toast.makeText(mContext, sb.toString(), Toast.LENGTH_SHORT).show();
                break;
            case R.id.btn_update:
                ContentValues values2 = new ContentValues();
                values2.put("name", "嘻嘻~");
                //参数依次是表名，修改后的值，where条件，以及约束，如果不指定三四两个参数，会更改所有行
                db.update("person", values2, "name = ?", new String[]{"呵呵~2"});
                break;
            case R.id.btn_delete:
                //参数依次是表名，以及where条件与约束
                db.delete("person", "personid = ?", new String[]{"3"});
                break;
        }
    }
}
```

## 代码块 3

```java
public void save(Person p)
{
    SQLiteDatabase db = dbOpenHelper.getWritableDatabase();
    db.execSQL("INSERT INTO person(name,phone) values(?,?)",
                new String[]{p.getName(),p.getPhone()});
}
```

## 代码块 4

```java
public void delete(Integer id)
{
    SQLiteDatabase db = dbOpenHelper.getWritableDatabase();
    db.execSQL("DELETE FROM person WHERE personid = ?",
                new String[]{id});
}
```

## 代码块 5

```java
public void update(Person p)
{
    SQLiteDatabase db = dbOpenHelper.getWritableDatabase();
    db.execSQL("UPDATE person SET name = ?,phone = ? WHERE personid = ?",
        new String[]{p.getName(),p.getPhone(),p.getId()});
}
```

## 代码块 6

```java
public Person find(Integer id)
{
    SQLiteDatabase db = dbOpenHelper.getReadableDatabase();
    Cursor cursor =  db.rawQuery("SELECT * FROM person WHERE personid = ?",
            new String[]{id.toString()});
    //存在数据才返回true
    if(cursor.moveToFirst())
    {
        int personid = cursor.getInt(cursor.getColumnIndex("personid"));
        String name = cursor.getString(cursor.getColumnIndex("name"));
        String phone = cursor.getString(cursor.getColumnIndex("phone"));
        return new Person(personid,name,phone);
    }
    cursor.close();
    return null;
}
```

## 代码块 7

```java
public List<Person> getScrollData(int offset,int maxResult)
{
    List<Person> person = new ArrayList<Person>();
    SQLiteDatabase db = dbOpenHelper.getReadableDatabase();
    Cursor cursor =  db.rawQuery("SELECT * FROM person ORDER BY personid ASC LIMIT= ?,?",
        new String[]{String.valueOf(offset),String.valueOf(maxResult)});
    while(cursor.moveToNext())
    {
        int personid = cursor.getInt(cursor.getColumnIndex("personid"));
        String name = cursor.getString(cursor.getColumnIndex("name"));
        String phone = cursor.getString(cursor.getColumnIndex("phone"));
        person.add(new Person(personid,name,phone)) ;
    }
    cursor.close();
    return person;
}
```

## 代码块 8

```java
public long getCount()
{
    SQLiteDatabase db = dbOpenHelper.getReadableDatabase();
    Cursor cursor =  db.rawQuery("SELECT COUNT (*) FROM person",null);
    cursor.moveToFirst();
    long result = cursor.getLong(0);
    cursor.close();
    return result;
}
```
