# 12.2 DrySister看妹子应用(第一版)——2.解析后台数据

> 来源: https://www.runoob.com/w3cnote/android-tutorial-exercise-2.html

## 代码块 1

```java
/**
 * 描述：妹子业务Bean
 *
 * @author coder-pig： 2016/08/06 17:16
 */
public class Sister {

    private String _id;
    private String createAt;
    private String desc;
    private String publishedAt;
    private String source;
    private String type;
    private String url;
    private boolean used;
    private String who;

    // 一些get和set方法...

}
```

## 代码块 2

```java
/**
 * 描述：网络请求处理相关类
 *
 * @author coder-pig： 2016/08/07 14:28
 */
public class SisterApi {
    private static final String TAG = "Network";
    private static final String BASE_URL = "http://gank.io/api/data/福利/";

    /**
     * 查询妹子信息
     */
    public ArrayList<Sister> fetchSister(int count, int page) {
        String fetchUrl = BASE_URL + count + "/" + page;
        ArrayList<Sister> sisters = new ArrayList<>();
        try {
            URL url = new URL(fetchUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setConnectTimeout(5000);
            conn.setRequestMethod("GET");
            int code = conn.getResponseCode();
            Log.v(TAG, "Server response：" + code);
            if (code == 200) {
                InputStream in = conn.getInputStream();
                byte[] data = readFromStream(in);
                String result = new String(data, "UTF-8");
                sisters = parseSister(result);
            } else {
                Log.e(TAG,"请求失败：" + code);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return sisters;
    }


    /**
     * 解析返回Json数据的方法
     */
    public ArrayList<Sister> parseSister(String content) throws Exception {
        ArrayList<Sister> sisters = new ArrayList<>();
        JSONObject object = new JSONObject(content);
        JSONArray array = object.getJSONArray("results");
        for (int i = 0; i < array.length(); i++) {
            JSONObject results = (JSONObject) array.get(i);
            Sister sister = new Sister();
            sister.set_id(results.getString("_id"));
            sister.setCreateAt(results.getString("createdAt"));
            sister.setDesc(results.getString("desc"));
            sister.setPublishedAt(results.getString("publishedAt"));
            sister.setSource(results.getString("source"));
            sister.setType(results.getString("type"));
            sister.setUrl(results.getString("url"));
            sister.setUsed(results.getBoolean("used"));
            sister.setWho(results.getString("who"));
            sisters.add(sister);
        }
        return sisters;
    }

    /**
     * 读取流中数据的方法
     */
    public byte[] readFromStream(InputStream inputStream) throws Exception {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        byte[] buffer = new byte[1024];
        int len ;
        while ((len = inputStream.read(buffer)) != -1) {
            outputStream.write(buffer, 0, len);
        }
        inputStream.close();
        return outputStream.toByteArray();
    }

}
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private Button showBtn;
    private Button refreshBtn;
    private ImageView showImg;

    private ArrayList<Sister> data;
    private int curPos = 0; //当前显示的是哪一张
    private int page = 1;   //当前页数
    private PictureLoader loader;
    private SisterApi sisterApi;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sisterApi = new SisterApi();
        loader = new PictureLoader();
        initData();
        initUI();
    }

    private void initData() {
        data = new ArrayList<>();
        new SisterTask(page).execute();
    }

    private void initUI() {
        showBtn = (Button) findViewById(R.id.btn_show);
        refreshBtn = (Button) findViewById(R.id.btn_refresh);
        showImg = (ImageView) findViewById(R.id.img_show);

        showBtn.setOnClickListener(this);
        refreshBtn.setOnClickListener(this);
    }

    @Override public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_show:
                if(data != null && !data.isEmpty()) {
                    if (curPos > 9) {
                        curPos = 0;
                    }
                    loader.load(showImg, data.get(curPos).getUrl());
                    curPos++;
                }
                break;
            case R.id.btn_refresh:
                page++;
                new SisterTask(page).execute();
                curPos = 0;
                break;
        }
    }

    private class SisterTask extends AsyncTask<Void,Void,ArrayList<Sister>> {

        private int page;

        public SisterTask(int page) {
            this.page = page;
        }

        @Override
        protected ArrayList<Sister> doInBackground(Void... params) {
            return sisterApi.fetchSister(10,page);
        }

        @Override
        protected void onPostExecute(ArrayList<Sister> sisters) {
            super.onPostExecute(sisters);
            data.clear();
            data.addAll(sisters);
        }
    }

}
```

## 代码块 4

```java
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private Button showBtn;
    private Button refreshBtn;
    private ImageView showImg;

    private ArrayList<Sister> data;
    private int curPos = 0; //当前显示的是哪一张
    private int page = 1;   //当前页数
    private PictureLoader loader;
    private SisterApi sisterApi;
    private SisterTask sisterTask;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sisterApi = new SisterApi();
        loader = new PictureLoader();
        initData();
        initUI();
    }

    private void initData() {
        data = new ArrayList<>();
    }

    private void initUI() {
        showBtn = (Button) findViewById(R.id.btn_show);
        refreshBtn = (Button) findViewById(R.id.btn_refresh);
        showImg = (ImageView) findViewById(R.id.img_show);

        showBtn.setOnClickListener(this);
        refreshBtn.setOnClickListener(this);
    }

    @Override public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btn_show:
                if(data != null && !data.isEmpty()) {
                    if (curPos > 9) {
                        curPos = 0;
                    }
                    loader.load(showImg, data.get(curPos).getUrl());
                    curPos++;
                }
                break;
            case R.id.btn_refresh:
                sisterTask = new SisterTask();
                sisterTask.execute();
                curPos = 0;
                break;
        }
    }

    private class SisterTask extends AsyncTask<Void,Void,ArrayList<Sister>> {

        public SisterTask() { }

        @Override
        protected ArrayList<Sister> doInBackground(Void... params) {
            return sisterApi.fetchSister(10,page);
        }

        @Override
        protected void onPostExecute(ArrayList<Sister> sisters) {
            super.onPostExecute(sisters);
            data.clear();
            data.addAll(sisters);
            page++;
        }

        @Override
        protected void onCancelled() {
            super.onCancelled();
            sisterTask = null;
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        sisterTask.cancel(true);
    }
}
```
