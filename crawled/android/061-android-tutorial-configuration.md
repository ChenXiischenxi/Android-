# 3.6 响应系统设置的事件(Configuration类)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-configuration.html

## 代码块 1

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView txtResult = (TextView) findViewById(R.id.txtResult);
        StringBuffer status = new StringBuffer();
        //①获取系统的Configuration对象
        Configuration cfg = getResources().getConfiguration();
        //②想查什么查什么
        status.append("densityDpi:" + cfg.densityDpi + "\n");
        status.append("fontScale:" + cfg.fontScale + "\n");
        status.append("hardKeyboardHidden:" + cfg.hardKeyboardHidden + "\n");
        status.append("keyboard:" + cfg.keyboard + "\n");
        status.append("keyboardHidden:" + cfg.keyboardHidden + "\n");
        status.append("locale:" + cfg.locale + "\n");
        status.append("mcc:" + cfg.mcc + "\n");
        status.append("mnc:" + cfg.mnc + "\n");
        status.append("navigation:" + cfg.navigation + "\n");
        status.append("navigationHidden:" + cfg.navigationHidden + "\n");
        status.append("orientation:" + cfg.orientation + "\n");
        status.append("screenHeightDp:" + cfg.screenHeightDp + "\n");
        status.append("screenWidthDp:" + cfg.screenWidthDp + "\n");
        status.append("screenLayout:" + cfg.screenLayout + "\n");
        status.append("smallestScreenWidthDp:" + cfg.densityDpi + "\n");
        status.append("touchscreen:" + cfg.densityDpi + "\n");
        status.append("uiMode:" + cfg.densityDpi + "\n");
        txtResult.setText(status.toString());
    }
}
```

## 代码块 2

```java
public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btn = (Button) findViewById(R.id.btncahange);
        btn.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                Configuration config = getResources().getConfiguration();
                //如果是横屏的话切换成竖屏
                if(config.orientation == Configuration.ORIENTATION_LANDSCAPE)
                {
                    MainActivity.this.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
                }
                //如果竖屏的话切换成横屏
                if(config.orientation == Configuration.ORIENTATION_PORTRAIT)
                {
                    MainActivity.this.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
                }
            }
        });
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        String screen = newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE?"横屏":"竖屏";
        Toast.makeText(MainActivity.this, "系统屏幕方向发生改变 \n 修改后的方向为" + screen, Toast.LENGTH_SHORT).show();
    }
}
```
