#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/18 9:10 PM
# @Author  : Calvin
# @File    : exercise_006.py
import re

'''匹配以“www”起始且以“.com”结尾的简单Web域名:例如,http://www.yahoo.com,也可以支持其他高级域名
如.edu,.net,.org,.cn等'''

pa = re.compile('www\.[\w\.]+(.com|.edu|.net|.org|.cn)')
print(re.match(pa,'www.yahoo.com').group())
print(re.match(pa,'www.yahoo.edu').group())
print(re.match(pa,'www.yahoo.net').group())
print(re.match(pa,'www.yahoo.org').group())
print(re.match(pa,'www.yahoo.net').group())