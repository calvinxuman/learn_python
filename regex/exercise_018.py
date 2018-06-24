#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 4:43 PM
# @Author  : Calvin
# @File    : exercise_018.py

import re
from time import ctime
'''通过确认整数字段中的第一个整数匹配在每个输出行起始部分的时间戳，确保在redata.txt中没有数据损坏。'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+?)::(.+?)::(\d+?)-\d+-\d+')
time_list = []
stamp_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        time_list.append(re.match(pa,i).group(1))
        stamp_list.append(re.match(pa, i).group(3))
for i in range(len(time_list)):
    if time_list[i] == ctime(int(stamp_list[i])):
        print('The %s line is correct'%i)
    else:
        print('The %s line is wrong'%i)
