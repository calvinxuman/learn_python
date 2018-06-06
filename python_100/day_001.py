#!/usr/bin/env python
# coding:utf-8

'''有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
n=1
num = [4,2,3,1]
list_num = [i*100+j*10+k for i in num for j in num for k in num if (i!=j) and (j!=k) and (i!=k)]
print('能组成%s个相互不同且无重复的数字的三位数'%len(list_num))
print('它们分别是%s'%list_num)

#按照从小到大排序
for i in xrange(len(list_num)):
    for j in xrange(len(list_num)):
        if list_num[i] < list_num[j]:
            list_num[i],list_num[j] = list_num[j],list_num[i]
print('它们从小到大的顺序是%s'%list_num)

#求所有满足要求的三位数之和
sum = 0
for i in list_num:
    sum = sum + i
print('它们的累计求和是%s'%sum)


sum_0 = 0
sum_1 = 0
#求所有偶数和
for i in list_num:
    if i%2 == 0:
        sum_0 = sum_0 + i
print('所有偶数求和是%s'%sum_0)

#求所有奇数和
for i in list_num:
    if i%2 != 0:
        sum_1 = sum_1 + i
print('所有偶数求和是%s'%sum_1)