# 7.2.2 Android JSON数据解析

> 来源: https://www.runoob.com/w3cnote/android-tutorial-json.html

## 代码块 1

```java
[
    { "id":"1","name":"基神","age":"18" },
    { "id":"2","name":"B神","age":"18"  },
    { "id":"3","name":"曹神","age":"18" }
]
```

## 代码块 2

```java
/**
 * Created by Jay on 2015/9/8 0008.
 */
public class Person {
    private String id;
    private String name;
    private String age;
    public void setId(String id){
        this.id = id;
    }
    public String getId(){
        return this.id;
    }
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public void setAge(String age){
        this.age = age;
    }
    public String getAge(){
        return this.age;
    }
    @Override
    public String toString() {
        return this.name + "~年方：" + this.age;
    }
}
```

## 代码块 3

```java
private void parseEasyJson(String json){
    persons = new ArrayList<Person>();
    try{
        JSONArray jsonArray = new JSONArray(json);
        for(int i = 0;i < jsonArray.length();i++){
            JSONObject jsonObject = (JSONObject) jsonArray.get(i);
            Person person = new Person();
            person.setId(i+"");
            person.setName(jsonObject.getString("name"));
            person.setAge(jsonObject.getString("age"));
            persons.add(person);
        }
    }catch (Exception e){e.printStackTrace();}
}
```

## 代码块 4

```java
private void parseDiffJson(String json) {
    try {
        JSONObject jsonObject1 = new JSONObject(json);
        Log.e("Json", json);
        JSONArray jsonArray = jsonObject1.getJSONArray("ch");
        for (int i = 0; i < jsonArray.length(); i++) {
            JSONObject jsonObject = (JSONObject) jsonArray.get(i);
            //取出name
            String sname = jsonObject.getString("names");
            JSONArray jarray1 = jsonObject.getJSONArray("data");
            JSONArray jarray2 = jsonObject.getJSONArray("times");
            Log.e("Json", sname);
            Log.e("Json", jarray1.toString());
            Log.e("Json", jarray2.toString());
        }
    } catch (Exception e) {
        e.printStackTrace();
    }

}
```
