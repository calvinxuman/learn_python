#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 8:41 PM
# @Author  : Calvin
# @File    : exercise_003.py
import re

'''匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母'''

pa = re.compile('(\w)+,\s(\w)+')
print (re.match(pa,'calvin, smith').group())