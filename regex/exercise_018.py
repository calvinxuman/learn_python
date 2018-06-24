#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 4:43 PM
# @Author  : Calvin
# @File    : exercise_018.py

import re
'''通过确认整数字段中的第一个整数匹配在每个输出行起始部分的时间戳，确保在redata.txt中没有数据损坏。'''

week_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        week_list.append(re.split('\s+',i.strip('\n'))[0])
week_set = set(week_list)
for i in week_set:
    print(i,week_list.count(i))