#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 10:08 PM
# @Author  : Calvin
# @File    : exercise_027.py
import re
'''从时间戳中提取月、日和年，然后以“年,日，月”的格式，每一行仅仅迭代一次。'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(\w{3})\s(\w{3})(\s+)(\d+)\s(.+)\s(\d{4})(.+)')
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        print(re.sub(pa,r'\6 \2 \4 \5 \1 \7', i.strip()))