# 2.4.9 ListView的数据更新问题

> 来源: https://www.runoob.com/w3cnote/android-tutorial-listview-update.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/9/21 0021.
 */
public class Data {
    private int imgId;
    private String content;

    public Data() {}

    public Data(int imgId, String content) {
        this.imgId = imgId;
        this.content = content;
    }

    public int getImgId() {
        return imgId;
    }

    public String getContent() {
        return content;
    }

    public void setImgId(int imgId) {
        this.imgId = imgId;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
```

## 代码块 2

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <ListView
        android:id="@+id/list_one"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

## 代码块 3

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal">

    <ImageView
        android:id="@+id/img_icon"
        android:layout_width="56dp"
        android:layout_height="56dp"/>

    <TextView
        android:id="@+id/txt_content"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="20dp"
        android:layout_marginLeft="10dp"
        android:textSize="18sp" />

</LinearLayout>
```

## 代码块 4

```java
/**
 * Created by Jay on 2015/9/21 0021.
 */
public class MyAdapter extends BaseAdapter {

    private Context mContext;
    private LinkedList<Data> mData;

    public MyAdapter() {}

    public MyAdapter(LinkedList<Data> mData, Context mContext) {
        this.mData = mData;
        this.mContext = mContext;
    }

    @Override
    public int getCount() {
        return mData.size();
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder = null;
        if(convertView == null){
            convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list,parent,false);
            holder = new ViewHolder();
            holder.img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
            holder.txt_content = (TextView) convertView.findViewById(R.id.txt_content);
            convertView.setTag(holder);
        }else{
            holder = (ViewHolder) convertView.getTag();
        }
        holder.img_icon.setImageResource(mData.get(position).getImgId());
        holder.txt_content.setText(mData.get(position).getContent());
        return convertView;
    }

    private class ViewHolder{
        ImageView img_icon;
        TextView txt_content;
    }

}
```

## 代码块 5

```java
public class MainActivity extends AppCompatActivity {

    private ListView list_one;
    private MyAdapter mAdapter = null;
    private List<Data> mData = null;
    private Context mContext = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        bindViews();
        mData = new LinkedList<Data>();
        mAdapter = new MyAdapter((LinkedList<Data>) mData,mContext);
        list_one.setAdapter(mAdapter);
    }

    private void bindViews(){
        list_one = (ListView) findViewById(R.id.list_one);
    }

}
```

## 代码块 6

```xml
<TextView
        android:id="@+id/txt_empty"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:textSize="15pt"
        android:textColor="#000000"/>

txt_empty = (TextView) findViewById(R.id.txt_empty);
txt_empty.setText("暂无数据~");
list_one.setEmptyView(txt_empty);
```

## 代码块 7

```java
public void add(Data data) {
    if (mData == null) {
        mData = new LinkedList<>();
    }
    mData.add(data);
    notifyDataSetChanged();
}
```

## 代码块 8

```java
private Button btn_add;
btn_add = (Button) findViewById(R.id.btn_add);
btn_add.setOnClickListener(this);

@Override
public void onClick(View v) {
    switch (v.getId()){
        case R.id.btn_add:
            mAdapter.add(new Data(R.mipmap.ic_icon_qitao,"给猪哥跪了~~~ x " + flag));
            flag++;
            break;
    }
}
```

## 代码块 9

```java
//往特定位置，添加一个元素
public void add(int position,Data data){
    if (mData == null) {
        mData = new LinkedList<>();
    }
    mData.add(position,data);
    notifyDataSetChanged();
}
```

## 代码块 10

```java
private Button btn_add2;
btn_add2 = (Button) findViewById(R.id.btn_add2);
btn_add2.setOnClickListener(this);

case R.id.btn_add2:
//position从0开始算的
mAdapter.add(4,new Data(R.mipmap.ic_icon_qitao,"给猪哥跪了~~~ x " + flag));
break;
```

## 代码块 11

```java
public void remove(Data data) {
    if(mData != null) {
        mData.remove(data);
    }
    notifyDataSetChanged();
}

public void remove(int position) {
    if(mData != null) {
        mData.remove(position);
    }
    notifyDataSetChanged();
}
```

## 代码块 12

```java
case R.id.btn_remove:
    mAdapter.remove(mData_5);
    break;
case R.id.btn_remove2:
    mAdapter.remove(2);
    break;
```

## 代码块 13

```java
public void clear() {
    if(mData != null) {
        mData.clear();
    }
    notifyDataSetChanged();
}
```

## 代码块 14

```java
private void updateListItem(int postion,Data mData){
    int visiblePosition = list_one.getFirstVisiblePosition();
    View v = list_one.getChildAt(postion - visiblePosition);
    ImageView img = (ImageView) v.findViewById(R.id.img_icon);
    TextView tv = (TextView) v.findViewById(R.id.txt_content);
    img.setImageResource(mData.getImgId());
    tv.setText(mData.getContent());
}
```
