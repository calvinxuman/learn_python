#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 7:02 PM
# @Author  : Calvin
# @File    : exercise_024.py
import re
'''仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名一起提取）'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+::)(\w+)@(.+)::(.+)')
user_list = []
domain_list = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        user_list.append(re.match(pa, i).group(2))
        domain_list.append(re.match(pa, i).group(3))
print(user_list)
print(domain_list)