# 2.4.8 ListView之checkbox错位问题解决

> 来源: https://www.runoob.com/w3cnote/android-tutorial-listview-checkbox.html

## 代码块 1

```java
public class Person implements Serializable{
    private String name;
    private String number;
    private boolean checkStatus;

    public Person(String name, String number) {
        super();
        this.name = name;
        this.number = number;
        this.checkStatus = false;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public boolean getCheckStatus() {
        return checkStatus;
    }

    public void setCheckStatus(boolean checkStatus) {
        this.checkStatus = checkStatus;
    }

}
```

## 代码块 2

```java
public class ContactListAdapter extends BaseAdapter implements CompoundButton.OnCheckedChangeListener{

    private List<Person> mData;
    private Context mContext;

    public ContactListAdapter(List<Person> data, Context context) {
        mData = data;
        mContext = context;
    }

    // 定义一个刷新数据的方法
    public void changeData(List<Person> data) {
        mData = data;
        notifyDataSetChanged();
    }

    @Override
    public int getCount() {
        return mData.size();
    }

    @Override
    public Person getItem(int position) {
        return mData.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        final int index = position;
        ViewHolder viewHolder;
        if (convertView == null) {
            convertView = LayoutInflater.from(mContext).inflate(
                    R.layout.item_contact, parent, false);
            viewHolder = new ViewHolder();
            viewHolder.ly = (RelativeLayout) convertView
                    .findViewById(R.id.lyContactListItem);
            viewHolder.txtName = (TextView) convertView
                    .findViewById(R.id.txtName);
            viewHolder.txtNumber = (TextView) convertView
                    .findViewById(R.id.txtNumber);
            viewHolder.cbxStatus = (CheckBox) convertView
                    .findViewById(R.id.cbxStatus);
            convertView.setTag(viewHolder);
            viewHolder.cbxStatus.setTag(index);
        } else {
            viewHolder = (ViewHolder) convertView.getTag();
        }
        viewHolder.cbxStatus.setOnCheckedChangeListener(this);
        viewHolder.cbxStatus.setChecked(mData.get(position).getcheckStatus());
        viewHolder.txtName.setText(mData.get(index).getName());
        viewHolder.txtNumber.setText(mData.get(index).getNumber());
        return convertView;
    }

    @Override
    public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
        int index = (int)buttonView.getTag();
        if (isChecked)
            mData.get(index).setCheckStatus(true);
        else
            mData.get(index).setCheckStatus(false);
    }


    private class ViewHolder {
        RelativeLayout ly;
        TextView txtName;
        TextView txtNumber;
        CheckBox cbxStatus;
    }
}
```
