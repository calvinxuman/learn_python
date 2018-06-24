#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:37 PM
# @Author  : Calvin
# @File    : exercise_011.py
import re

'''匹配所有能够表示有效电子邮件的集合'''

pa = re.compile('\w+@[\w\.]+.com')
print(re.match(pa,'calvin1102@xuman.aliyun.com').group())