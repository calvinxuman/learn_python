#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 6:28 PM
# @Author  : Calvin
# @File    : exercise_021.py
import re
'''仅仅提取时间戳中的月份'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'([A-Za-z]{3})\s([A-Za-z]{3})(.+)')
mon_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        mon_list.append(re.match(pa, i).group(2))
print(mon_list)