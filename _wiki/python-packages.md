---
layout: wiki
title: Python Packages
---

# 绘图

## [mpltex](https://github.com/liuyxpp/mpltex)

- Installation

```bash
python -m pip install mpltex
# needed 
sudo apt install texlive texlive-science texlive-latex-extra texlive-fonts-recommended dvipng
```

## [pycairo](git://git.cairographics.org/git/pycairo)

> for tilings

- Installation
  ```bash
  git clone git://git.cairographics.org/git/pycairo
  sudo apt-get install libcairo2-dev libjpeg-dev  libgif-dev
  cd pycairo
  sudo python3 setup.py install
  ```
- possible errors 
  - `error: command 'x86_64-linux-gnu-gcc' failed with exit status 1`
    - 解决方法
      ```bash
      sudo apt install python3-dev
      sudo apt-get build-dep python-lxml
      ```
  - `ImportError: libGL.so.1: cannot open shared object file: No such file or directory`
    ```bash
    sudo apt install libgl1-mesa-glx
    ```
