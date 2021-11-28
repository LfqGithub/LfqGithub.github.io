# 再学 Git

### 恢复 `git rm `的文件

```bash
$: git status # 显示工作区和暂存区的状态
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    apt-dpkg.md
$: git reset HEAD apt-dpkg.md # 取消暂存的变更
$: git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  use "git restore <file>..." to discard changes in working directory)
        deleted:    apt-dpkg.md
$: git checkout -- apt-dpkg.md # 用版本库里的版本代替工作区的版本

```

