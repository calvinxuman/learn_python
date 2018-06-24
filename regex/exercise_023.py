#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 6:57 PM
# @Author  : Calvin
# @File    : exercise_023.py
import re
'''仅仅提取时间戳中的时间（HH:MM:SS）'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+\s)(\d{2}:\d{2}:\d{2})(.+)')
time_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        time_list.append(re.match(pa, i).group(2))
print(time_list)