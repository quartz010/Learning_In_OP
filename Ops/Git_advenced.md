# Git 高级

## Foreword

之前渣操作导致了一些问题，赶忙的查找资料解决，所以这个，就是当自己 的一点经验收集吧

## 正文

### 回滚 Rollback

万一提交了错误的代码， 要进行的必要的 回滚操作。存在情况

1. 已经 commmit 没有推送到 remote
2. 已经 push 到 remote

---

使用 `reset` 进行撤销到上次的 commit 状态

    git reset [--hard|soft|mixed|merge|keep] [commit|HEAD]

如果已经推送但远程，好像比较纯的方法，是本地执行 

    git push -f 

来强制覆盖远程分支，好像有些不妥，不过效果是差不多的。

### 用户名 username

很尴尬的是，电脑上存在两个用户名，都有对 remote 进行 push 的权限，所以，变成了其他账户的的提交，很是尴尬。

使用如下命令，设置全局的默认 git 账号

    git config --global user.name gitaccount
    git config --global user.email gitaccount@example.com

如果 不想进行全局设置，而是对单个的仓储进行设置，使用：

    git config user.name anothergitaccount
    git config user.email anothergitaccount@example.com

对当前的仓储进行配置，弱化全局设置

