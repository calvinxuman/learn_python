#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 7:20 PM
# @Author  : Calvin
# @File    : exercise_026.py
import re
'''仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名分开提取）'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+::)(\w+@\w+\.\w+)(::.+)')
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        print(re.sub(pa,r'\1calvin1102@ailiyun.com\3', i.strip()))