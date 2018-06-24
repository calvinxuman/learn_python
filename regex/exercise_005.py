#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:04 PM
# @Author  : Calvin
# @File    : exercise_005.py
import re

'''根据美国接到地址格式,匹配街道地址。美国街道地址使用如下格式:1180 Bordeaux Drive。
使你的正则表达式足够灵活,以支持多单词的街道名称,如3120 De la Cruz Boulevard'''

pa = re.compile('\d+[\w\s]+')
print(re.findall(pa,'3120 De la Cruz Boulevard'))