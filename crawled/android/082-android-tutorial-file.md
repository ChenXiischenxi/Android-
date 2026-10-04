# 6.1 数据存储与访问之——文件存储读写

> 来源: https://www.runoob.com/w3cnote/android-tutorial-file.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="com.jay.example.filedemo1.MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/nametitle" />

    <EditText
        android:id="@+id/editname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/detailtitle" />

    <EditText
        android:id="@+id/editdetail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:minLines="2" />

    <LinearLayout
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <Button
            android:id="@+id/btnsave"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/btnwrite" />

        <Button
            android:id="@+id/btnclean"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/btnclean" />
    </LinearLayout>

    <Button
        android:id="@+id/btnread"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/btnread" />

</LinearLayout>
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/9/1 0001.
 */
public class FileHelper {

    private Context mContext;

    public FileHelper() {
    }

    public FileHelper(Context mContext) {
        super();
        this.mContext = mContext;
    }

    /*
    * 这里定义的是一个文件保存的方法，写入到文件中，所以是输出流
    * */
    public void save(String filename, String filecontent) throws Exception {
        //这里我们使用私有模式,创建出来的文件只能被本应用访问,还会覆盖原文件哦
        FileOutputStream output = mContext.openFileOutput(filename, Context.MODE_PRIVATE);
        output.write(filecontent.getBytes());  //将String字符串以字节流的形式写入到输出流中
        output.close();         //关闭输出流
    }


    /*
    * 这里定义的是文件读取的方法
    * */
    public String read(String filename) throws IOException {
        //打开文件输入流
        FileInputStream input = mContext.openFileInput(filename);
        byte[] temp = new byte[1024];
        StringBuilder sb = new StringBuilder("");
        int len = 0;
        //读取文件内容:
        while ((len = input.read(temp)) > 0) {
            sb.append(new String(temp, 0, len));
        }
        //关闭输入流
        input.close();
        return sb.toString();
    }

}
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private EditText editname;
    private EditText editdetail;
    private Button btnsave;
    private Button btnclean;
    private Button btnread;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = getApplicationContext();
        bindViews();
    }


    private void bindViews() {
        editdetail = (EditText) findViewById(R.id.editdetail);
        editname = (EditText) findViewById(R.id.editname);
        btnclean = (Button) findViewById(R.id.btnclean);
        btnsave = (Button) findViewById(R.id.btnsave);
        btnread = (Button) findViewById(R.id.btnread);

        btnclean.setOnClickListener(this);
        btnsave.setOnClickListener(this);
        btnread.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btnclean:
                editdetail.setText("");
                editname.setText("");
                break;
            case R.id.btnsave:
                FileHelper fHelper = new FileHelper(mContext);
                String filename = editname.getText().toString();
                String filedetail = editdetail.getText().toString();
                try {
                    fHelper.save(filename, filedetail);
                    Toast.makeText(getApplicationContext(), "数据写入成功", Toast.LENGTH_SHORT).show();
                } catch (Exception e) {
                    e.printStackTrace();
                    Toast.makeText(getApplicationContext(), "数据写入失败", Toast.LENGTH_SHORT).show();
                }
                break;
            case R.id.btnread:
                String detail = "";
                FileHelper fHelper2 = new FileHelper(getApplicationContext());
                try {
                    String fname = editname.getText().toString();
                    detail = fHelper2.read(fname);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                Toast.makeText(getApplicationContext(), detail, Toast.LENGTH_SHORT).show();
                break;
        }
    }
}
```

## 代码块 4

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="com.jay.example.filedemo2.MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="清输入文件名" />

    <EditText
        android:id="@+id/edittitle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="文件名" />


    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="清输入文件内容" />

    <EditText
        android:id="@+id/editdetail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="文件内容" />

    <Button
        android:id="@+id/btnsave"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="保存到SD卡" />

    <Button
        android:id="@+id/btnclean"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="清空" />

    <Button
        android:id="@+id/btnread"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="读取sd卡中的文件" />

</LinearLayout>
```

## 代码块 5

```java
/**
 * Created by Jay on 2015/9/1 0001.
 */
public class SDFileHelper {

    private Context context;

    public SDFileHelper() {
    }

    public SDFileHelper(Context context) {
        super();
        this.context = context;
    }

    //往SD卡写入文件的方法
    public void savaFileToSD(String filename, String filecontent) throws Exception {
        //如果手机已插入sd卡,且app具有读写sd卡的权限
        if (Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
            filename = Environment.getExternalStorageDirectory().getCanonicalPath() + "/" + filename;
            //这里就不要用openFileOutput了,那个是往手机内存中写数据的
            FileOutputStream output = new FileOutputStream(filename);
            output.write(filecontent.getBytes());
            //将String字符串以字节流的形式写入到输出流中
            output.close();
            //关闭输出流
        } else Toast.makeText(context, "SD卡不存在或者不可读写", Toast.LENGTH_SHORT).show();
    }

    //读取SD卡中文件的方法
    //定义读取文件的方法:
    public String readFromSD(String filename) throws IOException {
        StringBuilder sb = new StringBuilder("");
        if (Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
            filename = Environment.getExternalStorageDirectory().getCanonicalPath() + "/" + filename;
            //打开文件输入流
            FileInputStream input = new FileInputStream(filename);
            byte[] temp = new byte[1024];

            int len = 0;
            //读取文件内容:
            while ((len = input.read(temp)) > 0) {
                sb.append(new String(temp, 0, len));
            }
            //关闭输入流
            input.close();
        }
        return sb.toString();
    }


}
```

## 代码块 6

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private EditText editname;
    private EditText editdetail;
    private Button btnsave;
    private Button btnclean;
    private Button btnread;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = getApplicationContext();
        bindViews();
    }

    private void bindViews() {
        editname = (EditText) findViewById(R.id.edittitle);
        editdetail = (EditText) findViewById(R.id.editdetail);
        btnsave = (Button) findViewById(R.id.btnsave);
        btnclean = (Button) findViewById(R.id.btnclean);
        btnread = (Button) findViewById(R.id.btnread);

        btnsave.setOnClickListener(this);
        btnclean.setOnClickListener(this);
        btnread.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btnclean:
                editdetail.setText("");
                editname.setText("");
                break;
            case R.id.btnsave:
                String filename = editname.getText().toString();
                String filedetail = editdetail.getText().toString();
                SDFileHelper sdHelper = new SDFileHelper(mContext);
                try
                {
                    sdHelper.savaFileToSD(filename, filedetail);
                    Toast.makeText(getApplicationContext(), "数据写入成功", Toast.LENGTH_SHORT).show();
                }
                catch(Exception e){
                    e.printStackTrace();
                    Toast.makeText(getApplicationContext(), "数据写入失败", Toast.LENGTH_SHORT).show();
                }
                break;
            case R.id.btnread:
                String detail = "";
                SDFileHelper sdHelper2 = new SDFileHelper(mContext);
                try
                {
                    String filename2 = editname.getText().toString();
                    detail = sdHelper2.readFromSD(filename2);
                }
                catch(IOException e){e.printStackTrace();}
                Toast.makeText(getApplicationContext(), detail, Toast.LENGTH_SHORT).show();
                break;
        }
    }
}
```

## 代码块 7

```xml
<!-- 在SDCard中创建与删除文件权限 -->
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
<!-- 往SDCard写入数据权限 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

## 代码块 8

```java
InputStream is =getResources().openRawResource(R.raw.filename);
```

## 代码块 9

```java
AssetManager am =  getAssets();
InputStream is = am.open("filename");
```
