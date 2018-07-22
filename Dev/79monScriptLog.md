# 项目总结

## foreword

作为一个简单项目的总结，通过这个，对自己的能力的提升，还是很大的

## Context

**行读取源文件**
	
	# cat ${CONF} | grep -v "^#" | while read line
	# 循环读取不匹配行
	# ^# 表示 # 注释行

按行读取一个 log 文件，使用正则表达式，可以忽略注释行

    for line in open('log.out', 'rb')：
        if re.match(r'^#', line):
			continue    # to skip the comment

[Python 文件读取技巧](https://www.cnblogs.com/sysuoyj/archive/2012/03/14/2395789.html)


**Shell中的通配符**
[通配符](https://www.jianshu.com/p/49d5ee46de47)


**awk用法**
IP=`echo ${line} | awk -F'|' '{print $1}'`

使用 -F 把得到的文本行按 | 分解成参数组 (A B C D) ,

print $1 指的是第一个参数

-F <value> - tells awk what field separator to use. In your case, -F: means that the separator is : (colon).

**SHELL 的重定向语法**
[重定向](http://www.runoob.com/linux/linux-shell-io-redirections.html)

**list 查找元素**
[LIST中元素存在](https://blog.csdn.net/lachesis999/article/details/53185299)

**所谓的并发**

操作还是有问题
[连接池]
(https://www.cnblogs.com/Xjng/p/3437694.html)

[线程池]
(https://www.cnblogs.com/xiaozi/p/6182990.html)

[PIP换源]
(https://blog.csdn.net/lambert310/article/details/52412059)

**析构**

    __del__

