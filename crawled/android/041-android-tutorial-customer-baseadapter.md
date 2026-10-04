# 2.5.0 构建一个可复用的自定义BaseAdapter

> 来源: https://www.runoob.com/w3cnote/android-tutorial-customer-baseadapter.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/9/21 0021.
 */
public class MyAdapter extends BaseAdapter {

    private Context mContext;
    private LinkedList<Data> mData;

    public MyAdapter() {
    }

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
        if (convertView == null) {
            convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list, parent, false);
            holder = new ViewHolder();
            holder.img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
            holder.txt_content = (TextView) convertView.findViewById(R.id.txt_content);
            convertView.setTag(holder);
        } else {
            holder = (ViewHolder) convertView.getTag();
        }
        holder.img_icon.setImageResource(mData.get(position).getImgId());
        holder.txt_content.setText(mData.get(position).getContent());
        return convertView;
    }

    //添加一个元素
    public void add(Data data) {
        if (mData == null) {
            mData = new LinkedList<>();
        }
        mData.add(data);
        notifyDataSetChanged();
    }

    //往特定位置，添加一个元素
    public void add(int position,Data data){
        if (mData == null) {
            mData = new LinkedList<>();
        }
        mData.add(position, data);
        notifyDataSetChanged();
    }

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

    public void clear() {
        if(mData != null) {
            mData.clear();
        }
        notifyDataSetChanged();
    }

    private class ViewHolder {
        ImageView img_icon;
        TextView txt_content;
    }

}
```

## 代码块 2

```java
public class MyAdapter<T> extends BaseAdapter {

    private Context mContext;
    private LinkedList<T> mData;

    public MyAdapter() {
    }

    public MyAdapter(LinkedList<T> mData, Context mContext) {
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
        if (convertView == null) {
            convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list, parent, false);
            holder = new ViewHolder();
            holder.img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
            holder.txt_content = (TextView) convertView.findViewById(R.id.txt_content);
            convertView.setTag(holder);
        } else {
            holder = (ViewHolder) convertView.getTag();
        }
        holder.img_icon.setImageResource(mData.get(position).getImgId());
        holder.txt_content.setText(mData.get(position).getContent());
        return convertView;
    }

    //添加一个元素
    public void add(T data) {
        if (mData == null) {
            mData = new LinkedList<>();
        }
        mData.add(data);
        notifyDataSetChanged();
    }

    //往特定位置，添加一个元素
    public void add(int position,T data){
        if (mData == null) {
            mData = new LinkedList<>();
        }
        mData.add(position, data);
        notifyDataSetChanged();
    }

    public void remove(T data) {
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

    public void clear() {
        if(mData != null) {
            mData.clear();
        }
        notifyDataSetChanged();
    }

    private class ViewHolder {
        ImageView img_icon;
        TextView txt_content;
    }

}
```

## 代码块 3

```java
public static class ViewHolder {

    private SparseArray<View> mViews;   //存储ListView 的 item中的View
    private View item;                  //存放convertView
    private int position;               //游标
    private Context context;            //Context上下文

    //构造方法，完成相关初始化
    private ViewHolder(Context context, ViewGroup parent, int layoutRes) {
        mViews = new SparseArray<>();
        this.context = context;
        View convertView = LayoutInflater.from(context).inflate(layoutRes, parent,false);
        convertView.setTag(this);
        item = convertView;
    }

    ImageView img_icon;
    TextView txt_content;
}
```

## 代码块 4

```java
//绑定ViewHolder与item
public static ViewHolder bind(Context context, View convertView, ViewGroup parent,
                              int layoutRes, int position) {
    ViewHolder holder;
    if(convertView == null) {
        holder = new ViewHolder(context, parent, layoutRes);
    } else {
        holder = (ViewHolder) convertView.getTag();
        holder.item = convertView;
    }
    holder.position = position;
    return holder;
}
```

## 代码块 5

```java
public <T extends View> T getView(int id) {
    T t = (T) mViews.get(id);
    if(t == null) {
        t = (T) item.findViewById(id);
        mViews.put(id, t);
    }
    return t;
}
```

## 代码块 6

```java
/**
 * 获取当前条目
 */
public View getItemView() {
    return item;
}

/**
 * 获取条目位置
 */
public int getItemPosition() {
    return position;
}

/**
 * 设置文字
 */
public ViewHolder setText(int id, CharSequence text) {
    View view = getView(id);
    if(view instanceof TextView) {
        ((TextView) view).setText(text);
    }
    return this;
}

/**
 * 设置图片
 */
public ViewHolder setImageResource(int id, int drawableRes) {
    View view = getView(id);
    if(view instanceof ImageView) {
        ((ImageView) view).setImageResource(drawableRes);
    } else {
        view.setBackgroundResource(drawableRes);
    }
    return this;
}


/**
 * 设置点击监听
 */
public ViewHolder setOnClickListener(int id, View.OnClickListener listener) {
    getView(id).setOnClickListener(listener);
    return this;
}

/**
 * 设置可见
 */
public ViewHolder setVisibility(int id, int visible) {
    getView(id).setVisibility(visible);
    return this;
}

/**
 * 设置标签
 */
public ViewHolder setTag(int id, Object obj) {
    getView(id).setTag(obj);
    return this;
}

//其他方法可自行扩展
```

## 代码块 7

```java
public abstract void bindView(ViewHolder holder, T obj);
```

## 代码块 8

```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
    ViewHolder holder = ViewHolder.bind(parent.getContext(), convertView, parent, mLayoutRes
            , position);
    bindView(holder,getItem(position));
    return holder.getItemView();
}
```

## 代码块 9

```java
public class MainActivity extends AppCompatActivity {

    private Context mContext;
    private ListView list_book;
    private ListView list_app;

    private MyAdapter<App> myAdapter1 = null;
    private MyAdapter<Book> myAdapter2 = null;
    private List<App> mData1 = null;
    private List<Book> mData2 = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = MainActivity.this;
        init();

    }

    private void init() {

        list_book = (ListView) findViewById(R.id.list_book);
        list_app = (ListView) findViewById(R.id.list_app);

        //数据初始化
        mData1 = new ArrayList<App>();
        mData1.add(new App(R.mipmap.iv_icon_baidu,"百度"));
        mData1.add(new App(R.mipmap.iv_icon_douban,"豆瓣"));
        mData1.add(new App(R.mipmap.iv_icon_zhifubao,"支付宝"));

        mData2 = new ArrayList<Book>();
        mData2.add(new Book("《第一行代码Android》","郭霖"));
        mData2.add(new Book("《Android群英传》","徐宜生"));
        mData2.add(new Book("《Android开发艺术探索》","任玉刚"));

        //Adapter初始化
        myAdapter1 = new MyAdapter<App>((ArrayList)mData1,R.layout.item_one) {
            @Override
            public void bindView(ViewHolder holder, App obj) {
                holder.setImageResource(R.id.img_icon,obj.getaIcon());
                holder.setText(R.id.txt_aname,obj.getaName());
            }
        };
        myAdapter2 = new MyAdapter<Book>((ArrayList)mData2,R.layout.item_two) {
            @Override
            public void bindView(ViewHolder holder, Book obj) {
                holder.setText(R.id.txt_bname,obj.getbName());
                holder.setText(R.id.txt_bauthor,obj.getbAuthor());
            }
        };

        //ListView设置下Adapter：
        list_book.setAdapter(myAdapter2);
        list_app.setAdapter(myAdapter1);

    }


}
```

## 代码块 10

```java
/**
 * Created by Jay on 2015/9/22 0022.
 */
public abstract class MyAdapter<T> extends BaseAdapter {

    private ArrayList<T> mData;
    private int mLayoutRes;           //布局id


    public MyAdapter() {
    }

    public MyAdapter(ArrayList<T> mData, int mLayoutRes) {
        this.mData = mData;
        this.mLayoutRes = mLayoutRes;
    }

    @Override
    public int getCount() {
        return mData != null ? mData.size() : 0;
    }

    @Override
    public T getItem(int position) {
        return mData.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder = ViewHolder.bind(parent.getContext(), convertView, parent, mLayoutRes
                , position);
        bindView(holder, getItem(position));
        return holder.getItemView();
    }

    public abstract void bindView(ViewHolder holder, T obj);

    //添加一个元素
    public void add(T data) {
        if (mData == null) {
            mData = new ArrayList<>();
        }
        mData.add(data);
        notifyDataSetChanged();
    }

    //往特定位置，添加一个元素
    public void add(int position, T data) {
        if (mData == null) {
            mData = new ArrayList<>();
        }
        mData.add(position, data);
        notifyDataSetChanged();
    }

    public void remove(T data) {
        if (mData != null) {
            mData.remove(data);
        }
        notifyDataSetChanged();
    }

    public void remove(int position) {
        if (mData != null) {
            mData.remove(position);
        }
        notifyDataSetChanged();
    }

    public void clear() {
        if (mData != null) {
            mData.clear();
        }
        notifyDataSetChanged();
    }


    public static class ViewHolder {

        private SparseArray<View> mViews;   //存储ListView 的 item中的View
        private View item;                  //存放convertView
        private int position;               //游标
        private Context context;            //Context上下文

        //构造方法，完成相关初始化
        private ViewHolder(Context context, ViewGroup parent, int layoutRes) {
            mViews = new SparseArray<>();
            this.context = context;
            View convertView = LayoutInflater.from(context).inflate(layoutRes, parent, false);
            convertView.setTag(this);
            item = convertView;
        }

        //绑定ViewHolder与item
        public static ViewHolder bind(Context context, View convertView, ViewGroup parent,
                                      int layoutRes, int position) {
            ViewHolder holder;
            if (convertView == null) {
                holder = new ViewHolder(context, parent, layoutRes);
            } else {
                holder = (ViewHolder) convertView.getTag();
                holder.item = convertView;
            }
            holder.position = position;
            return holder;
        }

        @SuppressWarnings("unchecked")
        public <T extends View> T getView(int id) {
            T t = (T) mViews.get(id);
            if (t == null) {
                t = (T) item.findViewById(id);
                mViews.put(id, t);
            }
            return t;
        }


        /**
         * 获取当前条目
         */
        public View getItemView() {
            return item;
        }

        /**
         * 获取条目位置
         */
        public int getItemPosition() {
            return position;
        }

        /**
         * 设置文字
         */
        public ViewHolder setText(int id, CharSequence text) {
            View view = getView(id);
            if (view instanceof TextView) {
                ((TextView) view).setText(text);
            }
            return this;
        }

        /**
         * 设置图片
         */
        public ViewHolder setImageResource(int id, int drawableRes) {
            View view = getView(id);
            if (view instanceof ImageView) {
                ((ImageView) view).setImageResource(drawableRes);
            } else {
                view.setBackgroundResource(drawableRes);
            }
            return this;
        }


        /**
         * 设置点击监听
         */
        public ViewHolder setOnClickListener(int id, View.OnClickListener listener) {
            getView(id).setOnClickListener(listener);
            return this;
        }

        /**
         * 设置可见
         */
        public ViewHolder setVisibility(int id, int visible) {
            getView(id).setVisibility(visible);
            return this;
        }

        /**
         * 设置标签
         */
        public ViewHolder setTag(int id, Object obj) {
            getView(id).setTag(obj);
            return this;
        }

        //其他方法可自行扩展

    }

}
```
