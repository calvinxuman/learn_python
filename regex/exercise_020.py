#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 6:26 PM
# @Author  : Calvin
# @File    : exercise_020.py

import re
'''提取每行中完整的电子邮件地址'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+?)::(.+?)::(\d+?)-\d+-\d+')
email_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        email_list.append(re.match(pa, i).group(2))
print(email_list)