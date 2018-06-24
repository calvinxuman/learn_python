#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 7:14 PM
# @Author  : Calvin
# @File    : exercise_025.py
import re
'''仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名分开提取）'''

#Wed Mar 12 19:55:01 1986::rwhjipw@qdiyzgk.org::511012501-7-7
pa = re.compile(r'(.+::)(\w+)@(\w+)\.(\w+)::(.+)')
user_list = []
domain_list1 = []
domain_list2 = []
with open('redata.txt','r') as f:
    data = f.readlines()
    for i in data:
        user_list.append(re.match(pa, i).group(2))
        domain_list1.append(re.match(pa, i).group(3))
        domain_list2.append(re.match(pa, i).group(4))
print(user_list)
print(domain_list1)
print(domain_list2)