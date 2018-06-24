#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 10:07 PM
# @Author  : Calvin
# @File    : exercise_013.py
import re

''' 创建一个能从字符串中提取实际类型名称的正则表达式。函数将对于<type ‘int‘>字符串返回int'''

pa = re.compile('<type\s\‘(\w+)\‘>')
print(re.match(pa,'<type ‘int‘>').group(1))