# MySQL 基础

## foreword

用到啥学啥了，东西太多太乱

## 正文

### SQL 的名词

[基本名词]](https://blog.csdn.net/bushunqiu/article/details/50849872)

名词关系

- 数据库 -> 表 -> 记录
- 模式 -> 列名 -> 行

---

名词解释

- 模式（schema）：关于数据库和表的布局及特性的信息。
- 列（column）：表中的一个字段。所有表都是由一个或多个列组成的。
- 行（row）：表中的一个记录。
- 主键（primary key）：一列（或一组列），其值能够唯一标识表中每一行。(一般为ID)，在记录中是不重复的

### 基本语法

#### 数据库(DATABASE)

- 数据库的创建和删除

    使用命令:
        > CREATE DATABASE DatabaseName;

        > DROP DATABASE DatabaseName;
    CREATE 和 DROP 删库跑路标准操作

- 数据库的选择

    数据库，是我们的模型的最大单位， 后面的就是表和记录，这里先对数据库进行选择 **USE**

        > USE DatabaseName;

        > SHOW DATABASES;

        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |
        | orig               |
        | test               |
        +--------------------+
        4 rows in set (0.00 sec)

    这里可见，先对数据库进行选择。show 可以列出所有的数据库。 4个记录

#### 表

表， 作为数据库的第二大的单位， 可以类比于一个存储数据的容器。

- 创建 删除表

    创建一个表，需要这个表的参数， 参数就是列名。

        > CREATE TABLE table_name(
            column1 type,
            column2 type,
            column3 type,
            PRIMARY KEY(columnx))   # 这里指定主键
        )
    创建一个指定命名的表，其中的列名参数进行指定，前面是列名， 后面的是该参数的 类型

    实例：

        > CREATE TABLE CUSTOMERS(
        ID   INT              NOT NULL,
        NAME VARCHAR (20)     NOT NULL,
        AGE  INT              NOT NULL,
        ADDRESS  CHAR (25) ,
        SALARY   DECIMAL (18, 2),
        PRIMARY KEY (ID)
        );
    可以照上面的 结构进行对比

    使用 **DESC** 列出表的结构

        > DESC CUSTOMERS;
        +---------+---------------+------+-----+---------+-------+
        | Field   | Type          | Null | Key | Default | Extra |
        +---------+---------------+------+-----+---------+-------+
        | ID      | int(11)       | NO   | PRI |         |       |
        | NAME    | varchar(20)   | NO   |     |         |       |
        | AGE     | int(11)       | NO   |     |         |       |
        | ADDRESS | char(25)      | YES  |     | NULL    |       |
        | SALARY  | decimal(18,2) | YES  |     | NULL    |       |
        +---------+---------------+------+-----+---------+-------+
        5 rows in set (0.00 sec)

    和删除数据库一样， 对表的删除是 **DROP**

        DROP TABLE table_name

#### 字段操作

这里就是对数据表的 插入和查询， 当然只是实现最简单的语法呢

- 插入表
    对数据表进行数据的插入， 其语法如下， 使得列名和其 记录值就是一一对应 的关系，这样就可以对其进行插入
        INSERT INTO TABLE_NAME (column1, column2, column3,...columnN) 
        VALUES (value1, value2, value3,...valueN);

- 查询表
    使用 SELECT 对数据表进行查询

        > SELECT * FROM table_name (ADMIN)
        # 列出表中所有的字段记录

        > SELECT passwd FROM ADMIN
        # 列出密码这个字段

        > SELECT PASSWD, UNAME FROM ADMIN

- 条件查询
    查询满足我们的条件的 记录

        SELECT column1, column2, columnN 
        FROM table_name
        WHERE [condition]

    再例如

        SELECT PASSWD, UNAME
        FROM ADMIN
        WHERE UNAME = 'ROOT'

### 常用实例

- 列出所有 数据库

        SHOW DATABASES

- 列出所有 表

        SHOW TABELS

- 列出 表结构

        DESC table_name

- 列出 指定数据库 全部表 字段 字段类型

        select table_name from information_schema.tables where table_schema='database_name' and table_type='base table';

    这个 information_schema(模式) 就是用于保存 数据库的结构的 一个专用数据库

    这里的这条语句 查询 列名，字段类型

        select column_name,data_type from information_schema.columns where table_schema='database_name' and table_name='table_name';

- 列出时间段的 数据，前提是 在字段名中是存在 时间戳的

        SELECT * FROM table_name WHERE table_name.stattime > DATE_SUB( curdate( ), INTERVAL 1 DAY ) AND table_name.stattime <  date_sub(curdate( ), interval -17 hour);

    这个查询语句 就比较长， 一点点的 看，选择所有字段，其中时间戳需要满足条件

        DATE_SUB( curdate( ), INTERVAL 1 DAY )  // 当前时间 减去一天
        date_ADD( curdate( ), interval 17 hour);// 当前天加上 17小时
        table_name.stattime < now() // 优雅的版本

    可以变得更优雅， 学习是渐进的

        SELECT * FROM tbn WHERE tbn.stattime > DATE_SUB( now(), INTERVAL 1 hour ) AND tbn.stattime <  now();

    更更优雅， 列出一个小时的数据

        SELECT * FROM tbn WHERE tbn.stattime BETWEEN DATE_SUB( now(), INTERVAL 1 hour ) AND now();

    (实力菜鸡，巩固基础)