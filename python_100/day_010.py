#!/usr/bin/env python
# coding:utf-8
import re
'''BSA平台要求密码由数字,小写字母,大写字母和特殊字符四种构成的8至32位字符，请用正则表达式匹配'''

def rematch(str):
    pa = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_])[0-9a-zA-Z\W_]{8,32}')
    ma = re.match(pa,str)
    try:
        str_re = ma.group()
        # print(str_re)
    except Exception,e:
        return False
    if str_re == str:
        return True
    else:
        return False

print('Nsf0cus!@#:%s'%rematch('Nsf0cus!@#'))#符合要求
print('Nsfocus!@#:%s'%rematch('Nsfocus!@#'))#不包含数字
print('Nsfocus343:%s'%rematch('Nsfocus343'))#不包含特殊字符
print('12345A!@#:%s'%rematch('12345A!@#'))#不包含小写字母
print('12345a!@#:%s'%rematch('12345a!@#'))#不包含大写字母
print('Ns0!@#:%s'%rematch('Ns0!@#'))#少于8位
print('!@#1234567890123456789012345678Ao:%s'%rematch('!@#1234567890123456789012345678Ao'))#大于32位

