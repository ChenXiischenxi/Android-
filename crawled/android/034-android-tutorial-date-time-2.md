# 2.4.3 Date &#038; Time组件(下)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-date-time-2.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity implements DatePicker.OnDateChangedListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        DatePicker dp_test = (DatePicker) findViewById(R.id.dp_test);
        Calendar calendar = Calendar.getInstance();
        int year=calendar.get(Calendar.YEAR);
        int monthOfYear=calendar.get(Calendar.MONTH);
        int dayOfMonth=calendar.get(Calendar.DAY_OF_MONTH);
        dp_test.init(year,monthOfYear,dayOfMonth,this);
    }

    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        Toast.makeText(MainActivity.this,"您选择的日期是："+year+"年"+(monthOfYear+1)+"月"+dayOfMonth+"日!",Toast.LENGTH_SHORT).show();
    }
}
```

## 代码块 2

```java
public class MainActivity extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TimePicker tp_test = (TimePicker) findViewById(R.id.tp_test);
        tp_test.setOnTimeChangedListener(new TimePicker.OnTimeChangedListener() {
            @Override
            public void onTimeChanged(TimePicker view, int hourOfDay, int minute) {
                Toast.makeText(MainActivity.this,"您选择的时间是："+hourOfDay+"时"+minute+"分!",Toast.LENGTH_SHORT).show();
            }
        });
    }

}
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        CalendarView cv_test = (CalendarView) findViewById(R.id.cv_test);
        cv_test.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDayChange(CalendarView view, int year, int month, int dayOfMonth) {
                Toast.makeText(MainActivity.this,"您选择的时间是："+ year + "年" + month + "月" + dayOfMonth + "日",Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```
