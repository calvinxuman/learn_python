#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 8:25 PM
# @Author  : Calvin
# @File    : exercise_002.py
import re

'''匹配由单个空格分隔的任意单词对，也就是姓和名'''

pa = re.compile('(\w)+\s(\w)+')
print (re.match(pa,'calvin smith').group())
