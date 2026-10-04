# 2.3.2 EditText(输入框)详解

> 来源: https://www.runoob.com/w3cnote/android-tutorial-edittext.html

## 代码块 1

```java
android:hint="默认提示文本"
android:textColorHint="#95A1AA"
```

## 代码块 2

```java
android:selectAllOnFocus="true"
```

## 代码块 3

```xml
<EditText
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:inputType="phone" />
```

## 代码块 4

```java
android:inputType="none"
android:inputType="text"
android:inputType="textCapCharacters"
android:inputType="textCapWords"
android:inputType="textCapSentences"
android:inputType="textAutoCorrect"
android:inputType="textAutoComplete"
android:inputType="textMultiLine"
android:inputType="textImeMultiLine"
android:inputType="textNoSuggestions"
android:inputType="textUri"
android:inputType="textEmailAddress"
android:inputType="textEmailSubject"
android:inputType="textShortMessage"
android:inputType="textLongMessage"
android:inputType="textPersonName"
android:inputType="textPostalAddress"
android:inputType="textPassword"
android:inputType="textVisiblePassword"
android:inputType="textWebEditText"
android:inputType="textFilter"
android:inputType="textPhonetic"
```

## 代码块 5

```java
android:inputType="number"
android:inputType="numberSigned"
android:inputType="numberDecimal"
android:inputType="phone"//拨号键盘
android:inputType="datetime"
android:inputType="date"//日期键盘
android:inputType="time"//时间键盘
```

## 代码块 6

```java
android:singleLine="true"
```

## 代码块 7

```java
android:textScaleX="1.5"    //设置字与字的水平间隔
android:textScaleY="1.5"    //设置字与字的垂直间隔
```

## 代码块 8

```java
InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
imm.toggleSoftInput(0, InputMethodManager.HIDE_NOT_ALWAYS);
```

## 代码块 9

```java
InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);     imm.showSoftInput(view,InputMethodManager.SHOW_FORCED);
imm.hideSoftInputFromWindow(view.getWindowToken(), 0); //强制隐藏键盘
```

## 代码块 10

```java
public class MainActivity extends Activity {
    private Button btn_add;
    private EditText edit_one;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn_add = (Button) findViewById(R.id.btn_add);
        edit_one = (EditText) findViewById(R.id.edit_one);
        btn_add.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                SpannableString spanStr = new SpannableString("imge");
                Drawable drawable = MainActivity.this.getResources().getDrawable(R.drawable.f045);
                drawable.setBounds(0,0,drawable.getIntrinsicWidth(),drawable.getIntrinsicHeight());
                ImageSpan span = new ImageSpan(drawable,ImageSpan.ALIGN_BASELINE);
                spanStr.setSpan(span,0,4,Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
                int cursor = edit_one.getSelectionStart();
                edit_one.getText().insert(cursor, spanStr);
            }
        });
    }
}
```

## 代码块 11

```java
public class EditTextWithDel extends EditText {

    private final static String TAG = "EditTextWithDel";
    private Drawable imgInable;
    private Drawable imgAble;
    private Context mContext;

    public EditTextWithDel(Context context) {
        super(context);
        mContext = context;
        init();
    }

    public EditTextWithDel(Context context, AttributeSet attrs) {
        super(context, attrs);
        mContext = context;
        init();
    }

    public EditTextWithDel(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        mContext = context;
        init();
    }

    private void init() {
        imgInable = mContext.getResources().getDrawable(R.drawable.delete_gray);
        addTextChangedListener(new TextWatcher() {
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }

            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void afterTextChanged(Editable s) {
                setDrawable();
            }
        });
        setDrawable();
    }

    // 设置删除图片
    private void setDrawable() {
        if (length() < 1)
            setCompoundDrawablesWithIntrinsicBounds(null, null, null, null);
        else
            setCompoundDrawablesWithIntrinsicBounds(null, null, imgInable, null);
    }

    // 处理删除事件
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        if (imgInable != null && event.getAction() == MotionEvent.ACTION_UP) {
            int eventX = (int) event.getRawX();
            int eventY = (int) event.getRawY();
            Log.e(TAG, "eventX = " + eventX + "; eventY = " + eventY);
            Rect rect = new Rect();
            getGlobalVisibleRect(rect);
            rect.left = rect.right - 100;
            if (rect.contains(eventX, eventY))
                setText("");
        }
        return super.onTouchEvent(event);
    }
    @Override
    protected void finalize() throws Throwable {
        super.finalize();
    }
}
```
