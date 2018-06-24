#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:32 PM
# @Author  : Calvin
# @File    : exercise_010.py
import re

'''表示所有能够表示Python复数的字符集'''

pa = re.compile('[-]?\d+[+-]{1}\d+j')
print(re.match(pa,'-123+12j').group())