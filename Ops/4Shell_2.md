# Shell Basic

## if 分支语句的实现 续

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

## for 的循环实现

test