---
layout: quant 
title: Azure Storage
---

# Install

```bash
$ sudo python3 -m pip install azure-storage
```
# Syntax

## Blob

```bash
$ vi azure-storage-example.py
from azure.storage.blob import BlockBlobService
mystoragename="yundong"
mystoragekey='xxx'
blob_service=BlockBlobService(account_name=mystoragename, account_key=mystoragekey,endpoint_suffix='core.chinacloudapi.cn')
#  国内 Azure 用户添加 endpoint_suffix='core.chinacloundapi.cn' 项

# creat new container
blob_service.create_container('test')

# creat new blob 
blob_service.create_blob_from_text("test", "test","Microsoft love linux.")

# list all containers
generator=blob_service.list_containers()
for blob in generator:
    print(blob.name)

# list all blobs 
blobs=blob_service.list_blobs("share")
for blob in blobs:
    print(blob.name)
```

# Issue

## Issue1

> 按天、按合约查询数据并且格式化

## 从Microsoft Azure 获取数据

```python
import os,sys
from azure.storage.blob import BlockBlobService

mystoragename="xxx"
mystoragekey='xxx'

blob_service=BlockBlobService(account_name=mystoragename, account_key=mystoragekey,endpoint_suffix='core.chinacloudapi.cn')

container_name='shfe'
print("listing containers...")
containers=blob_service.list_containers()
for container in containers:
    print(container.name)

# download blob from azure
blob_service.get_blob_to_path(container_name, "20180328/m1807-C-3200_20180328.gz", "testgz-0328.gz")
```
- 输出

```bash
accele
bit
bitmex
btcontainer
bttrade
czce
dceforwardtest
dcelv1
dcerem
dcexqn
decadvanced
declv1
future
jsyfuture
liufaqiang-test
shfe
shfelv2
stock
vibranium
```
## 读取并且格式化数据

## Issue2: 计算时间差

### Dependency

- 使用python包-[chinesecalendar](https://github.com/LKI/chinese-calendar)
  - `pip install chinesecalendar`

# References

- [Official Docs-azure file](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)
- [官方文档-azure file](https://docs.azure.cn/zh-cn/storage/files/storage-python-how-to-use-file-storage)
- [Official Docs-azure blob](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)
- [Microsoft Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/)
