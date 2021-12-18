---
layout: wiki
title: SQL
categories: [SQL]
keywords: sql, mysql
---

updating...

# 基本概念

- Database: 数据库
- SQL: Structured Query Language，结构化查询语言
- RDBMS: Relational Database Management System, 关系数据库管理系统 

## 基本语法
```mysql
mysql> source  db_name.sql 
mysql> select lastnam,firstname,jobtitle from employees;
mysql> select * from employees where office >5;
mysql> select * from employees where office between 3 and 5;
mysql> desc/asc products;
mysql> select orderNumber,requireddate,status from orders where requireddate between cast('2013-01-01' as date) and cast('2013-01-31' as date);
mysql> select employeeNumber, lastName,firstName from employees where firstName like 'a%';
mysql> select employeeNumber, lastName,firstName from employees where firstName not like 'B%';

```
# 使用mysql
```bash
$ mysql -u root -p # 以root身份登录mysql
$ show databases 
$ create database database_name
$ use database_name
$ show tables
$ show columns from table_name
```

# WSL运行mysql
- 安装: `$ sudo apt install mysql-server mysql-client mysql-dev libmysqlclient-dev`
- 启动mysql: `sudo service mysql start`

# Bugfix
## No directory
- 问题描述：启动mysql(`sudo service mysql start`)时,提示`No directory, logging in with HOME=/`
- [解决方法](https://askubuntu.com/questions/737903/mysql-5-7-no-directory-logging-in-with-home)
  ```bash
  $ sudo service mysql stop
  $ sudo usermod -d /var/lib/mysql/ mysql
  ```

# 参考
- [MySQL教程-w3cschool](https://m.w3cschool.cn/mysql/mysql-tutorial.html)
