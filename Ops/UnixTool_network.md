# Linux Tool FOR Network AND Performance

## Network

### Ping

这个不用多说，使用 ICMP 检查网络连通性。

切记 Ping 是没有做端口指定的，ICMP 协议在网络层的东西，实现的是网络控制。 这层是没有端口的概念的。

端口检测使用 Telnet 

![](https://upload-images.jianshu.io/upload_images/3130736-a459d885684f4c00?imageMogr2/auto-orient/strip%7CimageView2/2/w/351)

    > ping -c 2 -I eth0 -W 2 baidu.com

通过interface eth0 发送 2 个capture Wait 2 second

> 在ping过程中按下ctrl+|会打印出当前的summary信息，统计当前发送包数量、接收数量、丢包率等。

### netstat

netstat 顾名思义 网络状态， 这个经常常用的 功能。 女生用起来只记得 ano / aunto， 这里做个记录。系统的学习一下

> Netstat 命令用于显示各种网络相关信息，如网络连接，路由表，接口状态 (Interface Statistics)，masquerade 连接，多播成员 (Multicast Memberships) 等等。

#### 使用

键入 netstat 命令后，得到输出分两部分

    Active Internet connections (w/o servers)
    Proto Recv-Q Send-Q Local Address               Foreign Address         State      
    tcp        0      0 192.168.1.*:345*           10.*.*.142:mysql         TIME_WAIT   
    tcp        0      0 192.168.1.*:345*           10.*.*.142:mysql         ESTABLISHED 
    tcp        0      0 192.168.1.*:348*           10.*.*.42:mysql          TIME_WAIT   
    tcp        0      0 192.168.1.*:348*           10.*.*.42:mysql          ESTABLISHED 
    tcp        0      0 192.168.1.*:345*           10.*.*.142:mysql         TIME_WAIT   
    tcp        0      0 192.168.1.*:345*           10.*.*.142:mysql         TIME_WAIT   

    Active UNIX domain sockets (w/o servers)
    Proto RefCnt Flags       Type       State         I-Node    Path
    unix  2      [ ]         DGRAM                    4*8173 /usr/local/sa/agent/log/ssh_notify.sock
    unix  2      [ ]         DGRAM                    1*5       /tmp/agent_cmd.sock
    unix  2      [ ]         DGRAM                    1*7  /usr/local/sa/agent/log/agent_cmd.sock
    unix  2      [ ]         DGRAM                    1*        @/org/kernel/udev/udevd
    unix  3      [ ]         STREAM     CONNECTED     9*9   
    unix  3      [ ]         STREAM     CONNECTED     9*0   
    unix  3      [ ]         STREAM     CONNECTED     9*9   

上面 的说明，可以出，分别是 **活动有源TCP连接** 和 **有源Unix域套套接字**

- 活动有源TCP连接 

    这个指的是 一个本地和远程主机建立的 **TCP连接** 。Recv-Q 指的是 Queue。

    常规情况，Q值应为0，否则说明，连接堵塞，存在数据包缓冲积压

- 有源Unix域套套接字

    UNIX域，就是指的是本机内部。套接字属于网络内容，同样的套接字是属于进程间通信的东西，所以这里展示的，就是系统的进程所创建的套接字。



- -a (all)显示所有选项，默认不显示LISTEN相关
- -t (tcp)仅显示tcp相关选项
- -u (udp)仅显示udp相关选项
- -n 拒绝显示别名，能显示数字的全部转化成数字。
- -l 仅列出有在 Listen (监听) 的服務状态
- -p 显示建立相关链接的程序名
- -r 显示路由信息，路由表
- -e 显示扩展信息，例如uid等
- -s 按各个协议进行统计
- -c 每隔一个固定时间，执行该netstat命令


### ss

### traceroute

### telnet

### ifconfig

### tcpdump

### wireshark

## Performance

### top

### iostat

### vmstat

### free

### prstat

### mpstat

### sar