---
layout: wiki
title: Git
categories: Git
description:
keywords: git 
---


# Syntax

## gitconfig


## Tags

```bash
git tag tagName #  添加tag
git tag -a v1.0 # 添加tag, 并打开编辑器，提示输入注释，用于注释较复杂场合
git tag -a v1.0 -m 'my commits about tag v1.0' # 直接添加带注释tag
git tag -a  v1.2 9fceb02 # refill a tag to commit 9fcebo2 , 9fxxx为提交的校验和，命令git log --pretty=oneline 查看
git tag #  list all tags
git tag -l 'v1.*' # list all tags begin with v1.
git show xxx # show the information about tag xxx
git push origin xxx # push tag xxx to servers
git push origin --tags # push all tags
git tag -d xxx # delete the local tag xxx
git push origin --delete xxx # delete tag xxx in remote server, method 1
git push origin :refs/tags/xxx # detete tag xxx in remote server, method 2
git fetch origin tag xxx # get the content of tag xxx
```

## Branch

```bash
git branch xxx # 创建分支 xxx
git checkout xxx # 切换到分支 xxx
git checkout -b xxx # 创建并切换到分支 xxx, 相当于：git brance dev && git checkout dev
git branck -a # 列出当前所有分支, 当前分支会标注*
git merge xxx # 合并分支 xxx
git branch -d xxx # 删除 xxx 分支
# 如果进行修改，新建一个分支，修改后，调试完成后 merge 到主分支上
git brance -D <name> # 强制删除分支 name，一般用于没有 merge 的其他分支上
git branch -m oldBranchName newBranchName # 重命名 branch
git merge branchName # merge the branchName to current branch
git merge --no-ff branchName # merge the branchName to current branch with non-fast-forward
```

将分支bugfix合并到master，有几种情况(图片来自[猴子都能懂的git入门](https://backlogtool.com/git-tutorial/cn/stepup/stepup1_4.html)，侵删）
- 当合并bugfix到master分支时，如果master分支没有被更改过，则合并非常简单。这种合并成为fast-forward合并
  合并前：

  ![alt](/images/git/bugfix_master.png)

  合并后：

  ![alt](/images/git/merge_fast_forward.png)    

- 如果合并时master已经有新的修改，则需要将master分支和branchName分支修改内容汇合起来。
  合并前：

  ![alt](/images/git/bugfix_edited_master.png)

  合并后:

  ![alt](/images/git/merge_bugfix_edited_master.png) 

- `no-fast-forward`选项，则即使能够fastforward合并，也会生成新的提交并合并。

  ![alt](/images/git/merge_no_fast_forward.png)

- rebase
    ```bash
    $ git rebase branchName 
    ```
    rebase前：

    ![alt](/images/git/before_rebase.png)

    rebase后：

    ![alt](/images/git/after_rebase.png)

    bugfix的历史记录会添加在master分支中，这样历史记录会形成一条直线，相对整洁。（如果出现冲突，则需要修改冲突后合并分支）

    ![alt](/images/git/rebase_bugfix_master.png)

    rebase后，master head位置不变，只是将master的head移动到bugfix的head这里。

    ![alt](/images/git/bugfixAndMaster.png)

- merge 和 rebase 区别
  - merge
    保持修改内容的历史记录，但是历史记录会很复杂。
  - rebase
    历史记录简单，是在原有提交的基础上将差异内容反映进去。因此，可能导致原本的提交内容无法正常运行。
    因此：
    - 在topic分支中更新merge分支的最新代码，请使用rebase
    - 向merge分支导入topic分支的话，先使用rebase，再使用merge（待理解）
- 删除 branch
  ```bash
  git branch -d branchName # delete the branch branchName
  git branch -D branchName # delete the branch branchName even they are still content to be committed
  # delete branch in remote server
  git push origin --delete branchName
  git push origin :branchName  #相当于推送一个空分支到远程分支，相当于删除远程分支，推荐上一种方法
  ```

# 自定义功能

## 简化提交步骤

```bash
# 输入 gac 提交更改内容， 输入 gacp 提交更改并 push 到远程目录， 如果没有 commit message, 自动提交当前时间作为 commit message
$ vi ~/.bashrc
gac(){
	if 	[ $# = 0 ]; then
		git add --all && git commit -m "$(date)"
	else
	   git add --all && git commit -m "$*"
   fi
   }
gacp(){
	if 	[ $# = 0 ]; then
		git add --all && git commit -m "$(date)" && git push origin master
    else
	   git add --all && git commit -m "$*" && git push origin master
    fi
   }
```

## Overwrite local files

```shell
# warning: git clean deletes all your untracked files/directories and can't be undone
$ git reset --hard HEAD
$ git clean -f -d
$ git pull
```

## 删除之前所有提交记录并保存当前代码

>>要求 `git version > 1.7.2 ( current 2.14.2)`

```bash
# 新建一个新的独立的 branch--lastest
git checkout --orphan lastest
# 添加提交内容
git commit -am " A brand new start"
# 删除master 
git branch -D master 
# 将当前分支（lastest）重命名为master
git branch -m master
# 提交到github
git push -f origin master
```

## 降低git仓库占用的存储空间

- 将二进制文件添加到`.gitignore`中
- `Clone`仓库时只保留最近几次提交:`git clone xxx --depth=1`

## Ignore Files

```bash
# 方法1:
$ vi .gitignore
*.o # c++ 
*.py[cod] # python
# pictures
*.png
*.jpg
*.pdf
# 方法2
$ vi .gitignore
# Ignore any files
*
# Except some files
!*.tex
!*.bib
!*.png
!*.jpg
# Except the files mentioned above in subdirectories
!*/
```

# bugFix
- git commit -a 弹出两个窗口
  具体原因未知，推测是没有设定git默认编辑器。
  ```bash
  $ git config --global core.editor vim
  $ git config --global merge.tool vimdiff
  ```
- git merge failed
  - 修改或者删除冲突文件
  - `git commit -m "remove merge conflicts"`
  - `git pull origin branchName`

# Links
- [git官网](https://git-scm.com/)
- [猴子都能懂的git入门](https://backlogtool.com/git-tutorial/cn/)
- [Git 教程--易百教程](https://www.yiibai.com/git)
- [Pro Git](http://iissnan.com/progit/)
- [remove merge conflicts](https://stackoverflow.com/questions/26376832/why-does-git-say-pull-is-not-possible-because-you-have-unmerged-files/27187110)
- [force git pull](https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files)
