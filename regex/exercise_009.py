#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:27 PM
# @Author  : Calvin
# @File    : exercise_009.py
import re

'''匹配所有能够表示Python浮点数的字符串集'''

pa = re.compile('[-]?\d+\.[\d]*')
print(re.match(pa,'0.1').group())