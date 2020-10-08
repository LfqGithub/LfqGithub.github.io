
# linux下免密码登陆

## 1. linux bash下生成密钥

***注意***：如果用户目录下已经存在.ssh文件夹并且该文件夹下已经存在`id_rsa`和`id_rsa.pub`，则跳过该步骤直接到2；

`ssh-keygen -t rsa -C "youremail@example.com"`

之后的操作一般采用默认设置（一路回车）

## 2. 将生成的公钥提交到自己的github账户
`cat  ~/.ssh/id_rsa.pub`

拷贝输出的内容，输入到github账户-`setting` -`ssh key`

## 3. 测试

`ssh -T git@github.com`

提示成功后再次提交代码就可以免密码。

第一次使用可能会提示设置用户名和邮箱，按照提示操作即可。

## 4. 设置免密码登陆可能遇到问题
a. 提示密钥已经被使用
解决方法：按照上述步骤1重新生成公钥和私钥。

b. 提示Permission denied (publickey)

```bash
rm -r ~/.ssh
ssh-keygen -t rsa -C "xxx@xxx.com"
chmod 0700 ~/.ssh
chmod 0600 ~/.ssh/id_rsa*
cat ~/.ssh/id_rsa.pub
#copy it to github.com
```
