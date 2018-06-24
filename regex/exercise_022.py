#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 6:49 PM
# @Author  : Calvin
# @File    : exercise_022.py
import re
'''仅仅提取时间戳中的年份'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+\s)(\d{4})(.+)')
year_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        year_list.append(re.match(pa, i).group(2))
print(year_list)