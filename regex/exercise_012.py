#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:59 PM
# @Author  : Calvin
# @File    : exercise_012.py
import re

''' 匹配所有能够表示有效网址的集合(URL)'''

pa = re.compile('http://[\w\.]+(.com|.edu|.net|.org|.cn)')
print(re.match(pa,'http://www.baidu.com').group())