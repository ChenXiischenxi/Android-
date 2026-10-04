# 2.4.6 BaseAdapter优化

> 来源: https://www.runoob.com/w3cnote/android-tutorial-baseadapter.html

## 代码块 1

```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
    convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list_animal,parent,false);
    ImageView img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
    TextView txt_aName = (TextView) convertView.findViewById(R.id.txt_aName);
    TextView txt_aSpeak = (TextView) convertView.findViewById(R.id.txt_aSpeak);

    img_icon.setBackgroundResource(mData.get(position).getaIcon());
    txt_aName.setText(mData.get(position).getaName());
    txt_aSpeak.setText(mData.get(position).getaSpeak());
    return convertView;
}
```

## 代码块 2

```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {

    if(convertView == null){
        convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list_animal,parent,false);
    }

    ImageView img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
    TextView txt_aName = (TextView) convertView.findViewById(R.id.txt_aName);
    TextView txt_aSpeak = (TextView) convertView.findViewById(R.id.txt_aSpeak);

    img_icon.setBackgroundResource(mData.get(position).getaIcon());
    txt_aName.setText(mData.get(position).getaName());
    txt_aSpeak.setText(mData.get(position).getaSpeak());
    return convertView;
}
```

## 代码块 3

```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
    ViewHolder holder = null;
    if(convertView == null){
        convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list_animal,parent,false);
        holder = new ViewHolder();
        holder.img_icon = (ImageView) convertView.findViewById(R.id.img_icon);
        holder.txt_aName = (TextView) convertView.findViewById(R.id.txt_aName);
        holder.txt_aSpeak = (TextView) convertView.findViewById(R.id.txt_aSpeak);
        convertView.setTag(holder);   //将Holder存储到convertView中
    }else{
        holder = (ViewHolder) convertView.getTag();
    }
    holder.img_icon.setBackgroundResource(mData.get(position).getaIcon());
    holder.txt_aName.setText(mData.get(position).getaName());
    holder.txt_aSpeak.setText(mData.get(position).getaSpeak());
    return convertView;
}

static class ViewHolder{
    ImageView img_icon;
    TextView txt_aName;
    TextView txt_aSpeak;
}
```
