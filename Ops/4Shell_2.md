# Shell Basic

## foreword

接着前面的 shell 的笔记

## 正文

### if 分支语句的实现 续

使用 if 语句实现的分支语句，自己试了试发现孩还是有了不少的理解了

    if [ `ps -ef | grep -c ssh` -gt 1 ]; then echo "find ssh"; fi

    if [ $(ps -ef | grep -c ssh) -gt 1 ]; then echo "ok"; fi

这里对上面的语句进行简单的总结了。

- `grep -c` 返回的是符合条件的条目数目 count
- 时刻记住 [] 前后的空格 [ 是二进制程序
- -gt greater 参数
- 在标准格式中是用缩进代表语句结束， 在单行模式下是使用的 ; 分号 semicolon   
- then 是 if 后面的 必须关键字
- fi 表示 if 结构的结束。 有效避免了if 悬挂的问题
- 这里的通过反引号，和$() 实现了同样的功能，其具体差别在于，在其语句解释里的进行的转义。
   
    [Shell中反引号（`）与$()用法的区别](https://blog.csdn.net/apache0554/article/details/47055827)

    这里也学习到了，一回尽量使用 ` $() ` 这样的新的标准结构
- 关于 [
    
    在 man 手册里， 实际上这个elf程序 被称之为 test 。可以通过 [] 内部的返回值，设定自己的的返回值 为 true 还是 false 。

    其支持很多的形式，不过具体上讲，是需要自己 `man 1` 的。支持z字符串的直接比较， 和整数的大型的参数比较 

        - gt greater than
        - ge greater or equal than
        - eq equal
        - le less or equal
        - lt less than 
        - ne not equal

    关于 [ 的用法还是相当多的了，自己man吧

### for 的循环实现

**循环格式**

这里的是一般形式

    for var in item1 item2 ... itemN
    do
        command1
        command2
        ...
        commandN
    done

这里是在终端的单行形式

    for var in item1 item2 ... itemN; do command1; command2… done;

---

后面 前面变量 对后面 的item 进行迭代。eg:

    for var in 1 2 3 4 5 
    do
        echo "num is $var"
    done

写作单行

    for var in 1 2 3 4 5; do echo "num : $var" ; done

- 记住 分号不意味着语句结束，而是格式缩进
- item 可以是返回内容，这样自动转换为 对单个词汇(空格隔开)进行的迭代；

    例如
    
        for var in $(ps -ef); do echo "ps:$var"; done
    
    当然这里应该使用 awk 或者 xarg ，这个神奇，后面了解

- in列表可以包含替换、字符串和文件名。

### while 循环实现

**基本格式**

    while condition
    do
        command
    done

可见 while 使用在 条件循环的实现。 for 实现的是列表的迭代。

---


迭代条件是判断 condition 是真的时候 eg：

    int=10
    while(( $int > 0))
    do
        echo $int
        let "int--"
    done

这里是实现了对于 int 的自减，且连续输出。

- [let 的用法](http://www.runoob.com/linux/linux-comm-let.html) 用于执行一个或者多个表达式。

    let "int --"    在使用过程中是不需要 $ 进行变量引用。 有空格需要引号

    具体什么意思呢？ 举个例子

        > a=5+4
        > echo $a
        5+4
        > let a=5+4
        echo $a
        9
    发现了，在相识赋值语句这样的语句，只是进行赋值，对表达式本身是不进行计算的。        