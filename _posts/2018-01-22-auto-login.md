---
layout: post
title: Auto Login the Internet of Fudan University
categories: Computer-Internet
description: auto login
keywords: python bash login
---

auto-login

# Syntax 
- login

```bash
$ python NetAuth.py
$ bash NetAuth.sh
```
- logout

```bash
$ python NetAuth.py --action logout
```

# Scripts

## Python

```python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import requests
import logging
import socket
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CONFIG_USER = {
    "username": "student_id",
    "password": "pass_word"
}
AUTH_URL = "https://10.108.255.249/include/auth_action.php"

logging.basicConfig(
    filename='login_record.log',
    level=logging.ERROR,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

config_login = {
    "action": "login",
    "ac_id": 1,
    # "nas_ip": "",
    # "user_mac": "",
    "save_me": 1,
    "ajax": 1
}

config_logout = {
    "action": "logout",
    "ajax": 1
}


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))  # Any IP is OK here
        my_ip = s.getsockname()[0]
    except:
        my_ip = '127.0.0.1'
    finally:
        s.close()
    return my_ip


def sign(action):
    config = None
    if "login" == action:
        config = config_login
    elif "logout" == action:
        config = config_logout
    config.update(CONFIG_USER)
    config.update({"user_ip": get_ip()})
    try:
        result = requests.post(
            AUTH_URL,
            data=config,
            timeout=5,
            verify=False
        )
        logging.info(result.text.split(",")[0])
    except Exception as e:
        logging.error(str(e))


if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, default="login", choices=['login', 'logout'])
    args = parser.parse_args()

    sign(args.action)

```

## bash

```bash
#!/bin/bash
username="YOUR_STUDENT_ID_HERE"
password="YOUR_PASSWORD_HERE"
ip="YOUR_IP_HERE"
URL="https://10.108.255.249/include/auth_action.php"
curl $URL --insecure --data "action=login&username=$username&password=$password&ac_id=1&user_ip=$ip&nas_ip=&user_mac=&save_me=1&ajax=1" > /dev/null 2>&1
```

# Auto Login

```bash
$ sudo crontab -e -uroot # add
*/30 * * * * python /path/to/NetAuth.py
*/30 * * * * bash /path/to/NetAuth.sh
```
# Links

- [gist code](https://gist.github.com/jinyu121/343f4fc91ceceea6d6adb27f10ba095e)
