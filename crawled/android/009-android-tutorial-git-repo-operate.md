# 1.5.1 Git使用教程之本地仓库的基本操作

> 来源: https://www.runoob.com/w3cnote/android-tutorial-git-repo-operate.html

## 代码块 1

```java
sudo apt-get install git
```

## 代码块 2

```java
git config --global user.name "coder-pig"
git config --global user.email "[email protected]"
```

## 代码块 3

```java
git init
```

## 代码块 4

```java
 git add readme.txt
 git commit -m "Wrote a readme file"
```

## 代码块 5

```java
git log
```

## 代码块 6

```java
commit defd8af52be5183dfceb3e5cf23f78ea47d013b0
Author: coder-pig <[email protected]>
Date:   Fri Jun 19 17:00:36 2015 +0800
MainActivity Delete Menu
```

## 代码块 7

```java
git checkout src/com/jay/example/testforgit/MainActivity.java
```

## 代码块 8

```java
git reset HEAD src/com/jay/example/testforgit/MainActivity.java
git checkout src/com/jay/example/testforgit/MainActivity.java
```

## 代码块 9

```java
 git reset --hard HEAD
 git reset --hard HEAD^
 git log
```

## 代码块 10

```java
git reset --hard ad2080c
```

## 代码块 11

```java
git reflog
```

## 代码块 12

```java
git reset --hard ad2080c
```
