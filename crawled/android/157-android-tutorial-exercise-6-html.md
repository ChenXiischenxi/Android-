# 12.6 DrySister看妹子应用(第一版)——6.图标制作，混淆，签名打包，APK瘦身，应用发布

> 来源: https://www.runoob.com/w3cnote/android-tutorial-exercise-6-html.html

## 代码块 1

```java
#指定压缩级别
-optimizationpasses 5

#不跳过非公共的库的类成员
-dontskipnonpubliclibraryclassmembers

#混淆时采用的算法
-optimizations !code/simplification/arithmetic,!field/*,!class/merging/*

#把混淆类中的方法名也混淆了
-useuniqueclassmembernames

#优化时允许访问并修改有修饰符的类和类的成员
-allowaccessmodification

#将文件来源重命名为“SourceFile”字符串
-renamesourcefileattribute SourceFile
#保留行号
-keepattributes SourceFile,LineNumberTable
#保持泛型
-keepattributes Signature

#保持所有实现 Serializable 接口的类成员
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}

#Fragment不需要在AndroidManifest.xml中注册，需要额外保护下
-keep public class * extends android.support.v4.app.Fragment
-keep public class * extends android.app.Fragment

# 保持测试相关的代码
-dontnote junit.framework.**
-dontnote junit.runner.**
-dontwarn android.test.**
-dontwarn android.support.test.**
-dontwarn org.junit.**
```

## 代码块 2

```java
git checkout master # 切换到master分支
git rebase develop  # 合并develop分支
git push origin master # 推送到远程master分支
git tag v1.0.0  # 为当前commit打上TAG
git push origin v1.0.0 # 把TAG推送到远程仓库
```
