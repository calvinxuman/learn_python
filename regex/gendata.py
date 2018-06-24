#!/usr/bin/env python
from string import ascii_lowercase as lc
from random import randrange,choice
from sys import maxint
from time import ctime

tlds = ('edu','net','com','org','cn','gov')

for i in xrange(randrange(5,11)):
    dtint = randrange(2**31-1)
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in xrange(llen))
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc) for i in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d'%(dtstr,login,dom,choice(tlds),dtint,llen,dlen)

