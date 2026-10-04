# 2.3.5.RadioButton(单选按钮)&#038;Checkbox(复选框)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-radiobutton-checkbox.html

## 代码块 1

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/LinearLayout1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="请选择性别"
        android:textSize="23dp"
        />

    <RadioGroup
        android:id="@+id/radioGroup"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <RadioButton
            android:id="@+id/btnMan"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="男"
            android:checked="true"/>

        <RadioButton
            android:id="@+id/btnWoman"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="女"/>
    </RadioGroup>

    <Button
        android:id="@+id/btnpost"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="提交"/>

</LinearLayout>
```

## 代码块 2

```java
RadioGroup radgroup = (RadioGroup) findViewById(R.id.radioGroup);
        //第一种获得单选按钮值的方法
        //为radioGroup设置一个监听器:setOnCheckedChanged()
        radgroup.setOnCheckedChangeListener(new OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                RadioButton radbtn = (RadioButton) findViewById(checkedId);
                Toast.makeText(getApplicationContext(), "按钮组值发生改变,你选了" + radbtn.getText(), Toast.LENGTH_LONG).show();
            }
        });
```

## 代码块 3

```java
Button btnchange = (Button) findViewById(R.id.btnpost);
        RadioGroup radgroup = (RadioGroup) findViewById(R.id.radioGroup);
        //为radioGroup设置一个监听器:setOnCheckedChanged()
        btnchange.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                for (int i = 0; i < radgroup.getChildCount(); i++) {
                    RadioButton rd = (RadioButton) radgroup.getChildAt(i);
                    if (rd.isChecked()) {
                        Toast.makeText(getApplicationContext(), "点击提交按钮,获取你选择的是:" + rd.getText(), Toast.LENGTH_LONG).show();
                        break;
                    }
                }
            }
        });
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener,CompoundButton.OnCheckedChangeListener{

    private CheckBox cb_one;
    private CheckBox cb_two;
    private CheckBox cb_three;
    private Button btn_send;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cb_one = (CheckBox) findViewById(R.id.cb_one);
        cb_two = (CheckBox) findViewById(R.id.cb_two);
        cb_three = (CheckBox) findViewById(R.id.cb_three);
        btn_send = (Button) findViewById(R.id.btn_send);

        cb_one.setOnCheckedChangeListener(this);
        cb_two.setOnCheckedChangeListener(this);
        cb_three.setOnCheckedChangeListener(this);
        btn_send.setOnClickListener(this);

    }

    @Override
    public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
       if(compoundButton.isChecked()) Toast.makeText(this,compoundButton.getText().toString(),Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onClick(View view) {
        String choose = "";
        if(cb_one.isChecked())choose += cb_one.getText().toString() + "";
        if(cb_two.isChecked())choose += cb_two.getText().toString() + "";
        if(cb_three.isChecked())choose += cb_three.getText().toString() + "";
        Toast.makeText(this,choose,Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 5

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:state_enabled="true"
        android:state_checked="true"
        android:drawable="@mipmap/ic_checkbox_checked"/>
    <item
        android:state_enabled="true"
        android:state_checked="false"
        android:drawable="@mipmap/ic_checkbox_normal" />
</selector>
```

## 代码块 6

```java
android:button="@drawable/rad_btn_selctor"
```

## 代码块 7

```xml
    <style name="MyCheckBox" parent="@android:style/Widget.CompoundButton.CheckBox">
        <item name="android:button">@drawable/rad_btn_selctor</item>
    </style>
```

## 代码块 8

```java
style="@style/MyCheckBox"
```

## 代码块 9

```java
rb.setButtonDrawable(R.drawable.rad_btn_selctor);
int rb_paddingLeft = getResources().getDrawable(R.mipmap.ic_checkbox_checked).getIntrinsicWidth()+5;
rb.setPadding(rb_paddingLeft, 0, 0, 0);
```
