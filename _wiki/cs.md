---
layout: wiki
title: C#
keywords: c#, c-sharp 
categories: [code, c#,c-sharp]
description: Learn C#
---

# Config
# Compile C# on Linux
## Mono
- msc: Mono's C# command line compiler

## Install Mono on Ubuntu
Taking Ubuntu 18.04 as an example--[Install Mono on Ubuntu](https://www.mono-project.com/download/stable/#download-lin)
```bash
# On ubuntu 18.04
sudo apt install gnupg ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt update
sudo apt install mono-devel
```
```
$ vi hello_world.cs
using System;
namespace HelloWorldApplication
{
	class Helloworld
	{
		static void Main(string[] args)
		{
			/* my first c# program*/
			Console.WriteLine("Hello World");
			Console.ReadKey();
		}
	}
}
$ mcs hello_world.cs 
$ ./hello_world.exe
Hello World
```

# Topic

## 封装

- 访问修饰符(Access Specifier)范围
  - Pubilc ：任何公有成员可以被外部的类访问。
  - Private ：只有同一个类中的函数可以访问它的私有成员。
  - Protected ：该类内部和继承类中可以访问。
  - internal : 同一个程序集的对象可以访问。
  - Protected internal ：3 和 4 的并集，符合任意一条都可以访问。


# Q & A
- 类中有Main函数，不调用该类时，该类也会执行吗？
- 输出参数

# Ref
- [C#教程--w3cschool.cn](https://www.w3cschool.cn/csharp/csharp-intro.html)
