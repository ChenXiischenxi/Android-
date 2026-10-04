# 3.7 AsyncTask异步任务

> 来源: https://www.runoob.com/w3cnote/android-tutorial-ansynctask.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MyActivity">
    <TextView
        android:id="@+id/txttitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />
    <!--设置一个进度条,并且设置为水平方向-->
    <ProgressBar
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:id="@+id/pgbar"
        style="?android:attr/progressBarStyleHorizontal"/>
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/btnupdate"
        android:text="更新progressBar"/>
</LinearLayout>
```

## 代码块 2

```java
public class DelayOperator {
    //延时操作,用来模拟下载
    public void delay()
    {
        try {
            Thread.sleep(1000);
        }catch (InterruptedException e){
            e.printStackTrace();;
        }
    }
}
```

## 代码块 3

```java
public class MyAsyncTask extends AsyncTask<Integer,Integer,String>
{
    private TextView txt;
    private ProgressBar pgbar;

    public MyAsyncTask(TextView txt,ProgressBar pgbar)
    {
        super();
        this.txt = txt;
        this.pgbar = pgbar;
    }


    //该方法不运行在UI线程中,主要用于异步操作,通过调用publishProgress()方法
    //触发onProgressUpdate对UI进行操作
    @Override
    protected String doInBackground(Integer... params) {
        DelayOperator dop = new DelayOperator();
        int i = 0;
        for (i = 10;i <= 100;i+=10)
        {
            dop.delay();
            publishProgress(i);
        }
        return  i + params[0].intValue() + "";
    }

    //该方法运行在UI线程中,可对UI控件进行设置
    @Override
    protected void onPreExecute() {
        txt.setText("开始执行异步线程~");
    }


    //在doBackground方法中,每次调用publishProgress方法都会触发该方法
    //运行在UI线程中,可对UI控件进行操作


    @Override
    protected void onProgressUpdate(Integer... values) {
        int value = values[0];
        pgbar.setProgress(value);
    }
}
```

## 代码块 4

```java
public class MyActivity extends ActionBarActivity {

    private TextView txttitle;
    private ProgressBar pgbar;
    private Button btnupdate;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txttitle = (TextView)findViewById(R.id.txttitle);
        pgbar = (ProgressBar)findViewById(R.id.pgbar);
        btnupdate = (Button)findViewById(R.id.btnupdate);
        btnupdate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                MyAsyncTask myTask = new MyAsyncTask(txttitle,pgbar);
                myTask.execute(1000);
            }
        });
    }
}
```
