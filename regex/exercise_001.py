#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 8:20 PM
# @Author  : Calvin
# @File    : exercise_001.py
import re

'''写出能够匹配“bat”，“bit”，“but”，“hat”，“hit”或者“hut”的正则表达式'''

pa = re.compile('[bh][aiu]t')
print (re.match(pa,'hut').group())