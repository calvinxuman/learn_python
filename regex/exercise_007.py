#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:21 PM
# @Author  : Calvin
# @File    : exercise_007.py
import re

'''匹配所有能够表示Python整数的字符串集'''

pa = re.compile('[+-]?\d+')
print(re.match(pa,'+11').group())