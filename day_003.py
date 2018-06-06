#!/usr/bin/env python
#coding:utf-8
'''一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''
'''设这个数为x，m,n为整数，
则x+100=n²，x+268=m²
所以(m+n)*(m-n)=168,
又因为m>n,所以m-n>1
则m+n<168,所以m,n均小于168
可以遍历m,n即可求出x'''

list_x = []
for m in xrange(168):
    for n in xrange(m):
        if m*m - n*n == 168:
            x = n*n -100
            list_x.append(x)
print('满足条件的数有：%s'%list_x)