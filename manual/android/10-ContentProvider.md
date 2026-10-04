# ContentProvider

> 本章归并自 2 页教程代码块，来源见各节。

## 4.4.1 ContentProvider初探

> 来源: https://www.runoob.com/w3cnote/android-tutorial-contentprovider.html

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

```xml
<uses-permission android:name="android.permission.READ_SMS"/>
```

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

```xml
<uses-permission android:name="android.permission.READ_CONTACTS"/>
```

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

```xml
<uses-permission android:name="android.permission.WRITE_CONTACTS"/>
<uses-permission android:name="android.permission.WRITE_PROFILE"/>
```

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

```xml
<!--属性依次为：全限定类名,用于匹配的URI,是否共享数据 -->
<provider android:name="com.jay.example.bean.NameContentProvider"
            android:authorities="com.jay.example.providers.myprovider"
            android:exported="true" />
```

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

## 4.4.2 ContentProvider再探——Document Provider

> 来源: https://www.runoob.com/w3cnote/android-tutorial-contentprovider-2.html

```java
 Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("image/*");
        startActivity(intent);
```

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private static final int READ_REQUEST_CODE = 42;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn_show = (Button) findViewById(R.id.btn_show);
        btn_show.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("image/*");
        startActivityForResult(intent, READ_REQUEST_CODE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == READ_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            Uri uri;
            if (data != null) {
                uri = data.getData();
                Log.e("HeHe", "Uri: " + uri.toString());
            }
        }
    }
}
```

```java
public void dumpImageMetaData(Uri uri) {
    Cursor cursor = getContentResolver()
            .query(uri, null, null, null, null, null);
    try {
        if (cursor != null && cursor.moveToFirst()) {
            String displayName = cursor.getString(
                    cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME));
            Log.e("HeHe", "Display Name: " + displayName);
            int sizeIndex = cursor.getColumnIndex(OpenableColumns.SIZE);
            String size = null;
            if (!cursor.isNull(sizeIndex)) {
                size = cursor.getString(sizeIndex);
            }else {
                size = "Unknown";
            }
            Log.e("HeHe", "Size: " + size);
        }
    }finally {
        cursor.close();
    }
}
```

```java
private Bitmap getBitmapFromUri(Uri uri) throws IOException {
        ParcelFileDescriptor parcelFileDescriptor =
        getContentResolver().openFileDescriptor(uri, "r");
        FileDescriptor fileDescriptor = parcelFileDescriptor.getFileDescriptor();
        Bitmap image = BitmapFactory.decodeFileDescriptor(fileDescriptor);
        parcelFileDescriptor.close();
        return image;
}
```

```java
private String readTextFromUri(Uri uri) throws IOException {
    InputStream inputStream = getContentResolver().openInputStream(uri);
    BufferedReader reader = new BufferedReader(new InputStreamReader(
            inputStream));
    StringBuilder stringBuilder = new StringBuilder();
    String line;
    while ((line = reader.readLine()) != null) {
        stringBuilder.append(line);
    }
    fileInputStream.close();
    parcelFileDescriptor.close();
    return stringBuilder.toString();
}
```

```java
private void createFile(String mimeType, String fileName) {
    Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);
    intent.addCategory(Intent.CATEGORY_OPENABLE);
    intent.setType(mimeType);
    intent.putExtra(Intent.EXTRA_TITLE, fileName);
    startActivityForResult(intent, WRITE_REQUEST_CODE);
}
```

```java
DocumentsContract.deleteDocument(getContentResolver(), uri);
```

```xml
<manifest... >
    ...
    <uses-sdk
        android:minSdkVersion="19"
        android:targetSdkVersion="19" />
        ....
        <provider
            android:name="com.example.android.storageprovider.MyCloudProvider"
            android:authorities="com.example.android.storageprovider.documents"
            android:grantUriPermissions="true"
            android:exported="true"
            android:permission="android.permission.MANAGE_DOCUMENTS"
            android:enabled="@bool/atLeastKitKat">
            <intent-filter>
                <action android:name="android.content.action.DOCUMENTS_PROVIDER" />
            </intent-filter>
        </provider>
    </application>

</manifest>
```

```java
@Override
public Cursor queryRoots(String[] projection) throws FileNotFoundException {

    // Create a cursor with either the requested fields, or the default
    // projection if "projection" is null.
    final MatrixCursor result =
            new MatrixCursor(resolveRootProjection(projection));

    // If user is not logged in, return an empty root cursor.  This removes our
    // provider from the list entirely.
    if (!isUserLoggedIn()) {
        return result;
    }

    // It's possible to have multiple roots (e.g. for multiple accounts in the
    // same app) -- just add multiple cursor rows.
    // Construct one row for a root called "MyCloud".
    final MatrixCursor.RowBuilder row = result.newRow();
    row.add(Root.COLUMN_ROOT_ID, ROOT);
    row.add(Root.COLUMN_SUMMARY, getContext().getString(R.string.root_summary));

    // FLAG_SUPPORTS_CREATE means at least one directory under the root supports
    // creating documents. FLAG_SUPPORTS_RECENTS means your application's most
    // recently used documents will show up in the "Recents" category.
    // FLAG_SUPPORTS_SEARCH allows users to search all documents the application
    // shares.
    row.add(Root.COLUMN_FLAGS, Root.FLAG_SUPPORTS_CREATE |
            Root.FLAG_SUPPORTS_RECENTS |
            Root.FLAG_SUPPORTS_SEARCH);

    // COLUMN_TITLE is the root title (e.g. Gallery, Drive).
    row.add(Root.COLUMN_TITLE, getContext().getString(R.string.title));

    // This document id cannot change once it's shared.
    row.add(Root.COLUMN_DOCUMENT_ID, getDocIdForFile(mBaseDir));

    // The child MIME types are used to filter the roots and only present to the
    //  user roots that contain the desired type somewhere in their file hierarchy.
    row.add(Root.COLUMN_MIME_TYPES, getChildMimeTypes(mBaseDir));
    row.add(Root.COLUMN_AVAILABLE_BYTES, mBaseDir.getFreeSpace());
    row.add(Root.COLUMN_ICON, R.drawable.ic_launcher);

    return result;
}
```

```java
public Cursor queryChildDocuments(String parentDocumentId, String[] projection,
                              String sortOrder) throws FileNotFoundException {

    final MatrixCursor result = new
            MatrixCursor(resolveDocumentProjection(projection));
    final File parent = getFileForDocId(parentDocumentId);
    for (File file : parent.listFiles()) {
        // Adds the file's display name, MIME type, size, and so on.
        includeFile(result, null, file);
    }
    return result;
}
```

```java
@Override
public Cursor queryDocument(String documentId, String[] projection) throws
        FileNotFoundException {

    // Create a cursor with the requested projection, or the default projection.
    final MatrixCursor result = new
            MatrixCursor(resolveDocumentProjection(projection));
    includeFile(result, documentId, null);
    return result;
}
```

```java
content://com.android.providers.media.documents/document/image%3A69983
```

```java
content://media/external/images/media/image%3A69983
```

```java
public static String getPath(final Context context, final Uri uri) {
    final boolean isKitKat = Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT;
    // DocumentProvider
    if (isKitKat && DocumentsContract.isDocumentUri(context, uri)) {
        // ExternalStorageProvider
        if (isExternalStorageDocument(uri)) {
            final String docId = DocumentsContract.getDocumentId(uri);
            final String[] split = docId.split(":");
            final String type = split[0];

            if ("primary".equalsIgnoreCase(type)) {
                return Environment.getExternalStorageDirectory() + "/" + split[1];
            }

            // TODO handle non-primary volumes
        }
        // DownloadsProvider
        else if (isDownloadsDocument(uri)) {

            final String id = DocumentsContract.getDocumentId(uri);
            final Uri contentUri = ContentUris.withAppendedId(
                    Uri.parse("content://downloads/public_downloads"), Long.valueOf(id));

            return getDataColumn(context, contentUri, null, null);
        }
        // MediaProvider
        else if (isMediaDocument(uri)) {
            final String docId = DocumentsContract.getDocumentId(uri);
            final String[] split = docId.split(":");
            final String type = split[0];
            Uri contentUri = null;
            if ("image".equals(type)) {
                contentUri = MediaStore.Images.Media.EXTERNAL_CONTENT_URI;
            } else if ("video".equals(type)) {
                contentUri = MediaStore.Video.Media.EXTERNAL_CONTENT_URI;
            } else if ("audio".equals(type)) {
                contentUri = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
            }
            final String selection = "_id=?";
            final String[] selectionArgs = new String[] {
                    split[1]
            };
            return getDataColumn(context, contentUri, selection, selectionArgs);
        }
    }
    // MediaStore (and general)
    else if ("content".equalsIgnoreCase(uri.getScheme())) {
        return getDataColumn(context, uri, null, null);
    }
    // File
    else if ("file".equalsIgnoreCase(uri.getScheme())) {
        return uri.getPath();
    }
    return null;
}

/**
 * Get the value of the data column for this Uri. This is useful for
 * MediaStore Uris, and other file-based ContentProviders.
 *
 * @param context The context.
 * @param uri The Uri to query.
 * @param selection (Optional) Filter used in the query.
 * @param selectionArgs (Optional) Selection arguments used in the query.
 * @return The value of the _data column, which is typically a file path.
 */
public static String getDataColumn(Context context, Uri uri, String selection,
                                   String[] selectionArgs) {

    Cursor cursor = null;
    final String column = "_data";
    final String[] projection = {
            column
    };

    try {
        cursor = context.getContentResolver().query(uri, projection, selection, selectionArgs,
                null);
        if (cursor != null && cursor.moveToFirst()) {
            final int column_index = cursor.getColumnIndexOrThrow(column);
            return cursor.getString(column_index);
        }
    } finally {
        if (cursor != null)
            cursor.close();
    }
    return null;
}


/**
 * @param uri The Uri to check.
 * @return Whether the Uri authority is ExternalStorageProvider.
 */
public static boolean isExternalStorageDocument(Uri uri) {
    return "com.android.externalstorage.documents".equals(uri.getAuthority());
}

/**
 * @param uri The Uri to check.
 * @return Whether the Uri authority is DownloadsProvider.
 */
public static boolean isDownloadsDocument(Uri uri) {
    return "com.android.providers.downloads.documents".equals(uri.getAuthority());
}

/**
 * @param uri The Uri to check.
 * @return Whether the Uri authority is MediaProvider.
 */
public static boolean isMediaDocument(Uri uri) {
    return "com.android.providers.media.documents".equals(uri.getAuthority());
}
```
