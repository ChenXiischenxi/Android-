# 2.5.4 AutoCompleteTextView(自动完成文本框)的基本使用

> 来源: https://www.runoob.com/w3cnote/android-tutorial-autocompletetextview.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <AutoCompleteTextView
        android:id="@+id/atv_content"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:completionHint="请输入搜索内容"
        android:completionThreshold="1"
        android:dropDownHorizontalOffset="5dp" />

    <MultiAutoCompleteTextView
        android:id="@+id/matv_content"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:completionThreshold="1"
        android:dropDownHorizontalOffset="5dp"
        android:text="" />

</LinearLayout>
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity {

    private AutoCompleteTextView atv_content;
    private MultiAutoCompleteTextView matv_content;

    private static final String[] data = new String[]{
            "小猪猪", "小狗狗", "小鸡鸡", "小猫猫", "小咪咪"
    };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        atv_content = (AutoCompleteTextView) findViewById(R.id.atv_content);
        matv_content = (MultiAutoCompleteTextView) findViewById(R.id.matv_content);


        ArrayAdapter<String> adapter = new ArrayAdapter<String>(MainActivity.
                this, android.R.layout.simple_dropdown_item_1line, data);
        atv_content.setAdapter(adapter);

        ArrayAdapter<String> adapter2 = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_dropdown_item_1line, data);
        matv_content.setAdapter(adapter);
        matv_content.setTokenizer(new MultiAutoCompleteTextView.CommaTokenizer());
    }
}
```
