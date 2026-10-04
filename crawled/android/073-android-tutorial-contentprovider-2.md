# 4.4.2 ContentProvider再探——Document Provider

> 来源: https://www.runoob.com/w3cnote/android-tutorial-contentprovider-2.html

## 代码块 1

```java
 Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("image/*");
        startActivity(intent);
```

## 代码块 2

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

## 代码块 3

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

## 代码块 4

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

## 代码块 5

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

## 代码块 6

```java
private void createFile(String mimeType, String fileName) {
    Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);
    intent.addCategory(Intent.CATEGORY_OPENABLE);
    intent.setType(mimeType);
    intent.putExtra(Intent.EXTRA_TITLE, fileName);
    startActivityForResult(intent, WRITE_REQUEST_CODE);
}
```

## 代码块 7

```java
DocumentsContract.deleteDocument(getContentResolver(), uri);
```

## 代码块 8

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

## 代码块 9

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

## 代码块 10

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

## 代码块 11

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

## 代码块 12

```java
content://com.android.providers.media.documents/document/image%3A69983
```

## 代码块 13

```java
content://media/external/images/media/image%3A69983
```

## 代码块 14

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
