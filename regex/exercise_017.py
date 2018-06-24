#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 1:28 PM
# @Author  : Calvin
# @File    : exercise_017.py
import re
'''判断在redata.txt中一周的每一天出现的次数（换句话说，读者也可以计算所选择的年份中每个月中出现的次数）。'''

week_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        week_list.append(re.split('\s+',i.strip('\n'))[0])
week_set = set(week_list)
for i in week_set:
    print(i,week_list.count(i))
