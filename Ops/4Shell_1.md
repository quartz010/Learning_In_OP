# Shell Basic

## 简介

### What is Shell

系统交互的桥梁，shell 实际上是一个工具

在这里取其泛指，是包含语法的东西了

[shell 在线模拟器](http://www.runoob.com/try/runcode.php?filename=helloworld&type=bash)

上面的👆原理差不多是，后端直接给开一个docker。

shell 脚本 script 是这里重点学习的东西了。

### Shell 种类

好多种：

- sh
- bash
- zsh
- fish

`#!/bin/bash` 来指定默认的解释器

### 执行

    chmod +x ./xxx.sh
    ./xxx.sh

    /bin/sh test.sh

### shell 之于其他的脚本语言
- 它的函数只能返回字串，无法返回数组
- 它不支持面向对象，你无法实现一些优雅的设计模式
- 它是解释型的，一边解释一边执行，连PHP那种预编译都不是，如果你的脚本包含错误(例如调用了不存在的函数)，只要没执行到这一行，就不会报错

## 快速入门

### 文件格式

示例代码 [ss1](./shells/ss_1.sh)

这里是一个很简单的 脚本编写

    #!/bin/sh   # 指定解释器
    cd ~
    mkdir test
    cd test

    for ((i=0; i<10; i++)); do    # 这里的语法可是是比较奇怪的
        touch test_$i.txt
    done

第一行 灰指定这个脚本文件所指定的解释器，这里使用的的是 bash。当然我们可以联系到，python的解释器指定

实际上，这里的 #! 是什么意思呢？？我们在 shell 里面执行这个脚本文件，shell 靠这条命令去找到我们的解释器！所以拓展开来，如果我们把这个解释器选项缺省，**那么默认的是指定 bash 对该脚本文件进行解释**


注意，这里的变量赋值语句， 其等号的前面是不能有 空格的 space

把 i 变量进行循环迭代，使用 $ 对变量进行引用。

### 变量 

在定义变量时后，不加美元符号,且记住 在 **等号两边不允许出现空格**， 之前经常出现这样的问题

    dba=123
    adm="ad"

**变量迭代**

这个语句就是可以对 home 目录中的所有的文件名进行迭代
   
    for file in `ls /home`

注意后面的反引号 \` \` 意味这里的内容是反引号中命令的 shell 进行执行后的输出

**变量引用**

变量的引用 直接使用变量名和 `$` 符号，就可以直接对变量名进行引用。

    echo $dba
    echo $adm

也可以使用 `${}` 的形式对变量进行引用，这样可以对连续的 内容进行区分

    echo ${adm}in

变量赋值可以直接被覆盖，值得注意的 是：

只是在对变量进行引用的时候才会需要加上 $ 符号， 对其进行赋值的时候是不需要添加 $ 的

---

变量在shell是很底层的存在，shell 不把他作为一个变量之类的对待，比如

    > ab=123
    > echo $ab    # 显然这里是可以直接打印ab 变量的 值 
    123
    > $ab         # 这里，就是直接把123的值给进 shell 
    bash : command '123' not found



### 注释

大量注释的激技巧，[出处](https://github.com/qinjx/30min_guides/blob/master/shell.md)

> 把这一段要注释的代码用一对花括号括起来，定义成一个函数，没有地方调用这个函数，这块代码就不会执行，达到了和注释一样的效果。


### 字符串

#### 类型

字符串是 shell里面最重要的数据类型了，没有之一。在shell 里面字符串是有两种的：单引号，双引号。

- 单引号
    - 在单引号中的任意 的字符都将原文输出。意味着 不会出现转义字符，和变量
    - 不可出现 匹配 单引号之外的另一个单引号，同上单引号也是无法进行转义的。

- 双引号
    - 在双引号中可以出现 $ 符号， 这个是直接意外这变量的值。
    - 可以出现转义字符，\n \t \r \d...

#### 操作

**拼接**

    > srt1="hello"
    > str2="$strworld"
    > echo $str2
    helloworld
    > echo "sds" "sdsd"
    sds sdsd



**字符串长度**

    string="abcd"
    echo ${#string}     #输出：4

注意： 这里是 $#str 的形式， 这样的是字符串的长度。标准写法 ${#str} 。切记，不可写成 #$str 这样会直接解析成一个注释，导致直接不进行执行。


**子串提取**

    > str="admin"
    > echo ${admin:3:5}
    in

这种对字符串切片的语法，之前是在python 中遇到的。 在这里也算是找到了类似的影子


**查找字符串**

    echo `expr index "$string" is`



### 控制语句

##### 条件控制

这个是 在ss里面的if的语法结构

**if**

if condition
then
	command1 
	command2
	...
	commandN 
fi

**if else**

    if condition
    then
        command1 
        command2
        ...
        commandN
    else
        command
    fi


**if elsif**

    if condition1
    then
        command1
    elif condition2
        command2
    else
        commandN
    fi

**IF的实现**

上面写道 这里的if 后面是 condition， condition 是使用 [] 进行包括，这里真正厉害的是，[] 并不是shell 语法中有的东西。而是 一个内建的 二进制程序。之前装 busybox 中是有见到过这个

    > which [
    /usr/bin/[

这里还有这样的格式

    if [ `ps -ef | grep -c ssh` -gt 1];  then echo hello; fi    # 分号由于同行输入

看见，后者是没有使用 [] 的，反引号命令是执行，返回内容，这个就是通过 grep 返回的内容判断，十分存在某个进程， 决定是否打印，这个 hello。

[] 在 shell里主要是实现来 条件判断 例如 :
    
    if [ $a == $b ]
    if [ $a -gt $b ]

可见使用 [] 可以实现变量之间的条件判断。


