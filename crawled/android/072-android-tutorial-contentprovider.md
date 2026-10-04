# 4.4.1 ContentProvider初探

> 来源: https://www.runoob.com/w3cnote/android-tutorial-contentprovider.html

## 代码块 1

```java
private void getMsgs(){
    Uri uri = Uri.parse("content://sms/");
    ContentResolver resolver = getContentResolver();
    //获取的是哪些列的信息
    Cursor cursor = resolver.query(uri, new String[]{"address","date","type","body"}, null, null, null);
    while(cursor.moveToNext())
    {
        String address = cursor.getString(0);
        String date = cursor.getString(1);
        String type = cursor.getString(2);
        String body = cursor.getString(3);
        System.out.println("地址:" + address);
        System.out.println("时间:" + date);
        System.out.println("类型:" + type);
        System.out.println("内容:" + body);
        System.out.println("======================");
    }
    cursor.close();
}
```

## 代码块 2

```xml
<uses-permission android:name="android.permission.READ_SMS"/>
```

## 代码块 3

```java
private void insertMsg() {
    ContentResolver resolver = getContentResolver();
    Uri uri = Uri.parse("content://sms/");
    ContentValues conValues = new ContentValues();
    conValues.put("address", "123456789");
    conValues.put("type", 1);
    conValues.put("date", System.currentTimeMillis());
    conValues.put("body", "no zuo no die why you try!");
    resolver.insert(uri, conValues);
    Log.e("HeHe", "短信插入完毕~");
}
```

## 代码块 4

```java
private void getContacts(){
    //①查询raw_contacts表获得联系人的id
    ContentResolver resolver = getContentResolver();
    Uri uri = ContactsContract.CommonDataKinds.Phone.CONTENT_URI;
    //查询联系人数据
    cursor = resolver.query(uri, null, null, null, null);
    while(cursor.moveToNext())
    {
        //获取联系人姓名,手机号码
        String cName = cursor.getString(cursor.getColumnIndex(ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME));
        String cNum = cursor.getString(cursor.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER));
        System.out.println("姓名:" + cName);
        System.out.println("号码:" + cNum);
        System.out.println("======================");
    }
    cursor.close();
}
```

## 代码块 5

```xml
<uses-permission android:name="android.permission.READ_CONTACTS"/>
```

## 代码块 6

```java
private void queryContact(String number){
        Uri uri = Uri.parse("content://com.android.contacts/data/phones/filter/" + number);
        ContentResolver resolver = getContentResolver();
        Cursor cursor = resolver.query(uri, new String[]{"display_name"}, null, null, null);
        if (cursor.moveToFirst()) {
            String name = cursor.getString(0);
            System.out.println(number + "对应的联系人名称：" + name);
        }
    cursor.close();
}
```

## 代码块 7

```java
private void AddContact() throws RemoteException, OperationApplicationException {
    //使用事务添加联系人
    Uri uri = Uri.parse("content://com.android.contacts/raw_contacts");
    Uri dataUri =  Uri.parse("content://com.android.contacts/data");

    ContentResolver resolver = getContentResolver();
    ArrayList<ContentProviderOperation> operations = new ArrayList<ContentProviderOperation>();
    ContentProviderOperation op1 = ContentProviderOperation.newInsert(uri)
            .withValue("account_name", null)
            .build();
    operations.add(op1);

    //依次是姓名，号码，邮编
    ContentProviderOperation op2 = ContentProviderOperation.newInsert(dataUri)
            .withValueBackReference("raw_contact_id", 0)
            .withValue("mimetype", "vnd.android.cursor.item/name")
            .withValue("data2", "Coder-pig")
            .build();
    operations.add(op2);

    ContentProviderOperation op3 = ContentProviderOperation.newInsert(dataUri)
            .withValueBackReference("raw_contact_id", 0)
            .withValue("mimetype", "vnd.android.cursor.item/phone_v2")
            .withValue("data1", "13798988888")
            .withValue("data2", "2")
            .build();
    operations.add(op3);

    ContentProviderOperation op4 = ContentProviderOperation.newInsert(dataUri)
            .withValueBackReference("raw_contact_id", 0)
            .withValue("mimetype", "vnd.android.cursor.item/email_v2")
            .withValue("data1", "[email protected]")
            .withValue("data2", "2")
            .build();
    operations.add(op4);
    //将上述内容添加到手机联系人中~
    resolver.applyBatch("com.android.contacts", operations);
    Toast.makeText(getApplicationContext(), "添加成功", Toast.LENGTH_SHORT).show();
}
```

## 代码块 8

```xml
<uses-permission android:name="android.permission.WRITE_CONTACTS"/>
<uses-permission android:name="android.permission.WRITE_PROFILE"/>
```

## 代码块 9

```java
public class DBOpenHelper extends SQLiteOpenHelper {

    final String CREATE_SQL = "CREATE TABLE test(_id INTEGER PRIMARY KEY AUTOINCREMENT,name)";

    public DBOpenHelper(Context context, String name, CursorFactory factory,
            int version) {
        super(context, name, null, 1);
    }


    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREATE_SQL);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // TODO Auto-generated method stub

    }

}
```

## 代码块 10

```java
public class NameContentProvider extends ContentProvider {

    //初始化一些常量
     private static UriMatcher matcher = new UriMatcher(UriMatcher.NO_MATCH);
     private DBOpenHelper dbOpenHelper;

    //为了方便直接使用UriMatcher,这里addURI,下面再调用Matcher进行匹配

     static{
         matcher.addURI("com.jay.example.providers.myprovider", "test", 1);
     }

    @Override
    public boolean onCreate() {
        dbOpenHelper = new DBOpenHelper(this.getContext(), "test.db", null, 1);
        return true;
    }

    @Override
    public Cursor query(Uri uri, String[] projection, String selection,
            String[] selectionArgs, String sortOrder) {
        return null;
    }

    @Override
    public String getType(Uri uri) {
        return null;
    }

    @Override
    public Uri insert(Uri uri, ContentValues values) {

        switch(matcher.match(uri))
        {
        //把数据库打开放到里面是想证明uri匹配完成
        case 1:
            SQLiteDatabase db = dbOpenHelper.getReadableDatabase();
            long rowId = db.insert("test", null, values);
            if(rowId > 0)
            {
                //在前面已有的Uri后面追加ID
                Uri nameUri = ContentUris.withAppendedId(uri, rowId);
                //通知数据已经发生改变
                getContext().getContentResolver().notifyChange(nameUri, null);
                return nameUri;
            }
        }
        return null;
    }

    @Override
    public int delete(Uri uri, String selection, String[] selectionArgs) {
        return 0;
    }

    @Override
    public int update(Uri uri, ContentValues values, String selection,
            String[] selectionArgs) {
        return 0;
    }

}
```

## 代码块 11

```xml
<!--属性依次为：全限定类名,用于匹配的URI,是否共享数据 -->
<provider android:name="com.jay.example.bean.NameContentProvider"
            android:authorities="com.jay.example.providers.myprovider"
            android:exported="true" />
```

## 代码块 12

```java
public class MainActivity extends Activity {

    private Button btninsert;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btninsert = (Button) findViewById(R.id.btninsert);

        //读取contentprovider 数据
        final ContentResolver resolver = this.getContentResolver();


        btninsert.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                 ContentValues values = new ContentValues();
                 values.put("name", "测试");
                 Uri uri = Uri.parse("content://com.jay.example.providers.myprovider/test");
                resolver.insert(uri, values);
                Toast.makeText(getApplicationContext(), "数据插入成功", Toast.LENGTH_SHORT).show();

            }
        });

    }
}
```
