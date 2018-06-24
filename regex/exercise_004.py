#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 8:57 PM
# @Author  : Calvin
# @File    : exercise_004.py
import re

'''匹配所有的有效的Python标识符集合'''

pa = re.compile('[A-Za-z_]\w*')
print(re.findall(pa,'A'))