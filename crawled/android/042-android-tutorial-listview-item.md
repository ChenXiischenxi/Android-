# 2.5.1 ListView Item多布局的实现

> 来源: https://www.runoob.com/w3cnote/android-tutorial-listview-item.html

## 代码块 1

```java
/**
 * Created by Jay on 2015/9/23 0023.
 */
public class MutiLayoutAdapter extends BaseAdapter{

    //定义两个类别标志
    private static final int TYPE_BOOK = 0;
    private static final int TYPE_APP = 1;
    private Context mContext;
    private ArrayList<Object> mData = null;


    public MutiLayoutAdapter(Context mContext,ArrayList<Object> mData) {
        this.mContext = mContext;
        this.mData = mData;
    }

    @Override
    public int getCount() {
        return mData.size();
    }

    @Override
    public Object getItem(int position) {
        return mData.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    //多布局的核心，通过这个判断类别
    @Override
    public int getItemViewType(int position) {
        if (mData.get(position) instanceof App) {
            return TYPE_APP;
        } else if (mData.get(position) instanceof Book) {
            return TYPE_BOOK;
        } else {
            return super.getItemViewType(position);
        }
    }

    //类别数目
    @Override
    public int getViewTypeCount() {
        return 2;
    }


    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        int type = getItemViewType(position);
        ViewHolder1 holder1 = null;
        ViewHolder2 holder2 = null;
        if(convertView == null){
           switch (type){
               case TYPE_APP:
                   holder1 = new ViewHolder1();
                   convertView = LayoutInflater.from(mContext).inflate(R.layout.item_one, parent, false);
                   holder1.img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
                   holder1.txt_aname = (TextView) convertView.findViewById(R.id.txt_aname);
                   convertView.setTag(R.id.Tag_APP,holder1);
                   break;
               case TYPE_BOOK:
                   holder2 = new ViewHolder2();
                   convertView = LayoutInflater.from(mContext).inflate(R.layout.item_two, parent, false);
                   holder2.txt_bname = (TextView) convertView.findViewById(R.id.txt_bname);
                   holder2.txt_bauthor = (TextView) convertView.findViewById(R.id.txt_bauthor);
                   convertView.setTag(R.id.Tag_Book,holder2);
                   break;
           }
        }else{
            switch (type){
                case TYPE_APP:
                    holder1 = (ViewHolder1) convertView.getTag(R.id.Tag_APP);
                    break;
                case TYPE_BOOK:
                    holder2 = (ViewHolder2) convertView.getTag(R.id.Tag_Book);
                    break;
            }
        }

        Object obj = mData.get(position);
        //设置下控件的值
        switch (type){
            case TYPE_APP:
                App app = (App) obj;
                if(app != null){
                    holder1.img_icon.setImageResource(app.getaIcon());
                    holder1.txt_aname.setText(app.getaName());
                }
                break;
            case TYPE_BOOK:
                Book book = (Book) obj;
                if(book != null){
                    holder2.txt_bname.setText(book.getbName());
                    holder2.txt_bauthor.setText(book.getbAuthor());
                }
                break;
        }
        return convertView;
    }


    //两个不同的ViewHolder
    private static class ViewHolder1{
        ImageView img_icon;
        TextView txt_aname;
    }

    private static class ViewHolder2{
        TextView txt_bname;
        TextView txt_bauthor;
    }
}
```

## 代码块 2

```xml
<item name="Tag_APP" type="id"></item>
<item name="Tag_Book" type="id"></item>
```

## 代码块 3

```java
public class MainActivity extends AppCompatActivity {

    private static final int TYPE_BOOK = 0;
    private static final int TYPE_APP = 1;
    private ListView list_content;
    private ArrayList<Object> mData = null;
    private MutiLayoutAdapter myAdapter = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //数据准备：
        mData = new ArrayList<Object>();
        for(int i = 0;i < 20;i++){
            switch ((int)(Math.random() * 2)){
                case TYPE_BOOK:
                    mData.add(new Book("《第一行代码》","郭霖"));
                    break;
                case TYPE_APP:
                    mData.add(new App(R.mipmap.iv_icon_baidu,"百度"));
                    break;
            }
        }

        list_content = (ListView) findViewById(R.id.list_content);
        myAdapter = new MutiLayoutAdapter(MainActivity.this,mData);
        list_content.setAdapter(myAdapter);
    }
}
```
