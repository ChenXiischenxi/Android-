# 12.5 DrySister看妹子应用(第一版)——5.代码回顾，调整与日志类编写

> 来源: https://www.runoob.com/w3cnote/android-tutorial-exercise-5.html

## 代码块 1

```java
git add .
git commit -m "fix code in as3.0"
git checkout develop    # 切换到develop分支
git rebase fix_code_as3.0.1 # 合并分支
git push origin develop # 推送develop到远程分支
git branch -d fix_code_as3.0.1  # 删除合并后的本地分支
```

## 代码块 2

```java
git add .
git commit -m "add LogUtils and CrashHandler"
git checkout develop    # 切换到develop分支
git rebase bug_log_catch # 合并分支
git push origin develop # 推送develop到远程分支
git branch -d bug_log_catch  # 删除合并后的本地分支
```
