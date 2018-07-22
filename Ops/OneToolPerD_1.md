# 每天一个 OP_tool

## Foreword

这个系列算是自己又开的了，这个 op 系列已经乱七八糟了，这样有嵌套了其他的， 那不是更乱了。

不过也无所谓了，自己作为一个记录呢。

每天一个 工具的用处， 和其方法。慢慢的 进步！

## 正文

### crontab

这个，是相当常用的东西了，不能说是不了解，只是自己只是用到接触，没有留下太大的，太深刻的影像，所以自己的做一个系统的学习了。

- 功能
    
    功能，还是总结一下，是在linux下的实现一个周期性进行任务处理的一个工具。在系统中是以守护进程的 形式存在的。
    
    所以其命名是 **crond** 这个 D 意味着 Deamon 。

- 启动
    
        service crond start
        service crond stop

- 配置

    Crontab 的 配置语法实际是 很简单的 使用` crontab -l`可以列出当前的 配置项；类似于这样的东西

        */1 * * * * (cd /data/D/xxx-api; sh nx.sh.1) > /dev/null 2>&1
        */1 * * * * (cd /data/D/xxx-api; sh xxx_api.sh.2) > /dev/null 2>&1
        */1 * * * * (cd /data/D/xxx-api; sh xxx_api.sh.3 ) > /dev/null 2>&1
        */1 * * * * (cd /data/D/xxx-api; sh xxx_api.sh.4) > /dev/null 2>&1
        */1 * * * * (cd /data/D/xxx-api; sh nx.sh.5) > /dev/null 2>&1
    这个就是我们的配置文件，乍一看，是比较混乱的。

    在网上找到的图，可以很清楚的说明一切 图片出处 [peida](http://www.cnblogs.com/peida/archive/2013/01/08/2850483.html)

    ![tab](https://images0.cnblogs.com/blog/34483/201301/08090352-4e0aa3fe4f404b3491df384758229be1.png)

    所以我们可以看出，上面的的配置意味着是 每分钟 进行一次任务。

        00 23 * * * (cd /data/D/xxx-api; sh nx.sh.5) > /dev/null 2>&1

    进而， 这样，可以看出， 是每天的 23：00 执行指定任务

        00 0-23/2 * * * 
    
    这样表示 在 0-23 点 每 2 小时 执行一次

        crontab -e 
    
    进行 时间表编辑
    
    FIN

### netstat
