# Python Package概念
一个package中包含多个[module](python_module.md)
package是包含多个module的目录。解决了引用某个目录中的模块问题。为了说明该目录是一个package,需要在该目录中放一个`__init__.py`文件。
## 举例

```bash
mkdir package_test
# add a.py and b.py to package_test
touch __init__.py  
python
>>> import package_test.a
>>>package_test.a.lang.function_in_a()
```

