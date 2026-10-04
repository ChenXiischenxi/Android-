# 10.2 SmsManager(短信管理器)

> 来源: https://www.runoob.com/w3cnote/android-tutorial-smsmanager.html

## 代码块 1

```java
public void SendSMSTo(String phoneNumber,String message){
    //判断输入的phoneNumber是否为合法电话号码
    if(PhoneNumberUtils.isGlobalPhoneNumber(phoneNumber)){
        //Uri.parse("smsto") 这里是转换为指定Uri,固定写法
        Intent intent = new Intent(Intent.ACTION_SENDTO, Uri.parse("smsto:"+phoneNumber));
        intent.putExtra("sms_body", message);
        startActivity(intent);
    }
}
```

## 代码块 2

```java
public void sendSMS(String phoneNumber,String message){
    //获取短信管理器
    android.telephony.SmsManager smsManager = android.telephony.SmsManager.getDefault();
    //拆分短信内容（手机短信长度限制）,貌似长度限制为140个字符,就是
    //只能发送70个汉字,多了要拆分成多条短信发送
    //第四五个参数,如果没有需要监听发送状态与接收状态的话可以写null
    List<String> divideContents = smsManager.divideMessage(message);
    for (String text : divideContents) {
        smsManager.sendTextMessage(phoneNumber, null, text, sentPI, deliverPI);
    }
}
```

## 代码块 3

```java
//处理返回的发送状态
String SENT_SMS_ACTION = "SENT_SMS_ACTION";
Intent sentIntent = new Intent(SENT_SMS_ACTION);
PendingIntent sentPI = PendingIntent.getBroadcast(context, 0, sentIntent,  0);
//注册发送信息的广播接收者
context.registerReceiver(new BroadcastReceiver() {
    @Override
    public void onReceive(Context _context, Intent _intent) {
        switch (getResultCode()) {
        case Activity.RESULT_OK:
            Toast.makeText(context, "短信发送成功", Toast.LENGTH_SHORT).show();
            break;
        case SmsManager.RESULT_ERROR_GENERIC_FAILURE:    //普通错误
            break;
        case SmsManager.RESULT_ERROR_RADIO_OFF:         //无线广播被明确地关闭
            break;
        case SmsManager.RESULT_ERROR_NULL_PDU:          //没有提供pdu
            break;
        case SmsManager.RESULT_ERROR_NO_SERVICE:         //服务当前不可用
            break;
        }
    }
}, new IntentFilter(SENT_SMS_ACTION));
```

## 代码块 4

```java
//处理返回的接收状态
String DELIVERED_SMS_ACTION = "DELIVERED_SMS_ACTION";
//创建接收返回的接收状态的Intent
Intent deliverIntent = new Intent(DELIVERED_SMS_ACTION);
PendingIntent deliverPI = PendingIntent.getBroadcast(context, 0,deliverIntent, 0);
context.registerReceiver(new BroadcastReceiver() {
   @Override
   public void onReceive(Context _context, Intent _intent) {
       Toast.makeText(context,"收信人已经成功接收", Toast.LENGTH_SHORT).show();
   }
}, new IntentFilter(DELIVERED_SMS_ACTION));
```
