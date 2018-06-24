#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 6:25 PM
# @Author  : Calvin
# @File    : exercise_019.py

import re
'''提取每行中完整的时间戳'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+?)::(.+?)::(\d+?)-\d+-\d+')
stamp_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        stamp_list.append(re.match(pa, i).group(3))
print(stamp_list)