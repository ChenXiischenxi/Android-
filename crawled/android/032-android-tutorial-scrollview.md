# 2.4.1 ScrollView(滚动条)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-scrollview.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn_down;
    private Button btn_up;
    private ScrollView scrollView;
    private TextView txt_show;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bindViews();
    }


    private void bindViews() {
        btn_down = (Button) findViewById(R.id.btn_down);
        btn_up = (Button) findViewById(R.id.btn_up);
        scrollView = (ScrollView) findViewById(R.id.scrollView);
        txt_show = (TextView) findViewById(R.id.txt_show);
        btn_down.setOnClickListener(this);
        btn_up.setOnClickListener(this);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 100; i++) {
            sb.append("呵呵 * " + i + "\n");
        }
        txt_show.setText(sb.toString());

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_down:
                scrollView.fullScroll(ScrollView.FOCUS_DOWN);
                break;
            case R.id.btn_up:
                scrollView.fullScroll(ScrollView.FOCUS_UP);
                break;
        }
    }
}
```

## 代码块 2

```java
public static void scrollToBottom(final View scroll, final View inner) {
    Handler mHandler = new Handler();
    mHandler.post(new Runnable() {
        public void run() {
            if (scroll == null || inner == null) {
                return;
            }
            int offset = inner.getMeasuredHeight() - scroll.getHeight();
            if (offset < 0) {
                offset = 0;
            }
            scroll.scrollTo(0, offset);
        }
    });
}
```

## 代码块 3

```java
@Override
public void fling(int velocityY) {
    super.fling(velocityY / 2);    //速度变为原来的一半
}
```
