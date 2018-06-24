#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 1:11 PM
# @Author  : Calvin
# @File    : exercise_014.py

import re

''' 处理日期。1.2节提供了来匹配单个或者两个数字字符串的正则表达式模式，来表示1～9的月份(0?[1-9])。
创建一个正则表达式来表示标准日历中剩余三个月的数字'''

pa = re.compile('1[0-2]')
print(re.match(pa,'13').group())