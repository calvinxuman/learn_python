#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/18 1:19 PM
# @Author  : Calvin
# @File    : exercise_016.py
from string import ascii_lowercase as lc
from random import randrange,choice
from time import ctime

'''为gendata.py更新代码，使数据直接输出到redata.txt而不是屏幕'''

tlds = ('edu','net','com','org','cn','gov')
with open('redata.txt','w') as f:
    for i in range(randrange(10,15)):
        dtint = randrange(2**31-1)
        dtstr = ctime(dtint)
        llen = randrange(4,8)
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen,13)
        dom = ''.join(choice(lc) for i in range(dlen))
        data ='%s::%s@%s.%s::%d-%d-%d\n'%(dtstr,login,dom,choice(tlds),dtint,llen,dlen)
        f.write(data)
