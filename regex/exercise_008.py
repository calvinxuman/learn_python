#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:25 PM
# @Author  : Calvin
# @File    : exercise_008.py
import re

'''匹配所有能够表示Python长整数的字符串集'''

pa = re.compile('[+-]?\d+[lL]')
print(re.match(pa,'+11l').group())