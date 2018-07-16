# NoSQL

这个只是自己的学习笔记，在原文基础上。加上自己的理解

不做任何商业用途
> 原文地址出处 [RUNOOB](http://www.runoob.com/mongodb/nosql.html)

## what is NoSQL

NoSQL = Not only SQL

一般常用的类似于 MySQL 一样的数据库，称之为关系数据库。数据库事务 transaction 遵循 ACID 规则

- Atomicity
- Consistency
- Isolation
- Durability

---

> CAP原则又称CAP定理，指的是在一个分布式系统中，Consistency（一致性）、 Availability（可用性）、Partition tolerance（分区容错性），三者不可得兼 。

- 一致性(Consistency) (所有节点在同一时间具有相同的数据)
- 可用性(Availability) (保证每个请求不管成功或者失败都有响应)
- 分隔容忍(Partition tolerance) (系统中任意信息的丢失或失败不会影响系统的继续运作)

这里和区块链系统中的部分概念是一样的 CAP 定理。

在区块链系统中是可以存在分区容忍性， 和可用性保证，弱化了一致性。也就是网络的弱一致性。

---

用CAP 原理对NoSQL 进行定义 其属于 CP 型， 而传统的关系数据库属于 CA

> RDBMS即关系数据库管理系统(Relational Database Management System)

两者的差别在 可用性 和分区容忍性

NoSQL的优缺点

优点

- 高可扩展性
- 分布式计算
- 低成本
- 架构的灵活性，半结构化数据
- 没有复杂的关系

缺点:

- 没有标准化
- 有限的查询功能（到目前为止）
- 最终一致是不直观的程序

(对于这些的具体体现还是比较不清楚)

---

在 NoSQL 的设计定义不同于 经典数据库的 ACID ，这里称之为 BASE

- 基本可用(Basically Available)
- 软状态/柔性事务(Soft state)
- 最终一致性 (Eventual consistency)     // 这点看起来怎么有点区链的感觉

其基本的存储方式 ：

- 列存储
- 文档存储
- 键值存储
- 图存储
- 对象存储
- xml数据库